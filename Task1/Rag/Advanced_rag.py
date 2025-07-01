import os
from dotenv import load_dotenv
from typing import List

from PyPDF2 import PdfReader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

class RAGPipeline:
    def __init__(self, embedding_model_name: str = "all-MiniLM-L6-v2", faiss_path: str = "faiss_index"):
        load_dotenv()
        self.api_key = os.getenv("groq_api")
        if not self.api_key:
            raise ValueError("GROQ API key not found in environment variables.")
        
        self.embedding_model = HuggingFaceEmbeddings(model_name=embedding_model_name)
        self.faiss_path = faiss_path
        self.db = None

    def load_pdf(self, file_path: str) -> str:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text

    def chunk_text(self, text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
        chunks = []
        for i in range(0, len(text), chunk_size - overlap):
            chunks.append(text[i:i + chunk_size])
        return chunks

    def build_vector_store(self, pdf_path: str):
        text = self.load_pdf(pdf_path)
        chunks = self.chunk_text(text)
        self.db = FAISS.from_texts(texts=chunks, embedding=self.embedding_model)
        self.db.save_local(self.faiss_path)
        print("✅ Vector store created and saved.")

    def load_vector_store(self):
        self.db = FAISS.load_local(self.faiss_path, self.embedding_model, allow_dangerous_deserialization=True)
        print("✅ Vector store loaded from disk.")

    def ask_question(self, query: str) -> str:
        if self.db is None:
            raise ValueError("Vector store not loaded or built. Call load_vector_store() or build_vector_store().")
        
        results = self.db.similarity_search_with_relevance_scores(query, k=3)
        if not results or results[0][1] < 0.3:
            return "No relevant context found to answer the question."

        context = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
        prompt_template = """
Answer the question based only on the following context:
{context}
you have to elaborate the answer very well. Do not hallucinate. Give just on-to-the-point answers.
The answer can be of one or two paragraphs, not more than that, and should contain at least 5 lines in a paragraph.

answer the question on the above context: {question}

Note: just give the answer at the end; don’t mention “according to the context” or similar phrases.
"""
        prompt = ChatPromptTemplate.from_template(prompt_template).format(context=context, question=query)
        model = ChatGroq(model="llama-3.1-8b-instant", api_key=self.api_key)
        response = model.invoke(prompt)
        sources = [doc.metadata.get("source", None) for doc, _ in results]
        return f"📜 **Response**:\n{response.content}\n\n🔗 **Sources:** {sources[0]}"

# ---------------------------- USAGE ----------------------------

if __name__ == "__main__":
    rag = RAGPipeline(faiss_path="faiss_store")
    try:
        # Step 1: Build once, then reuse `load_vector_store` in future
        rag.build_vector_store("ds_pdf_data.pdf")
        # rag.load_vector_store()  # Use if FAISS store already built

        queries = [
            "What is the main topic of this document?",
            "Summarize the key findings."
        ]

        for query in queries:
            print("\n🔍 Query:", query)
            answer = rag.ask_question(query)
            print(answer)

    except Exception as e:
        print(f"❌ Error: {e}")
