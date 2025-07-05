import json
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

def generate_pdf(input_json="summarized_articles.json", output_pdf="daily_newsletter.pdf"):
    # Load summarized articles
    with open(input_json, "r", encoding="utf-8") as f:
        articles = json.load(f)

    # Create a PDF
    doc = SimpleDocTemplate(output_pdf, pagesize=A4)
    styles = getSampleStyleSheet()

    # Custom Styles
    title_style = ParagraphStyle("Title", parent=styles["Heading1"], alignment=TA_CENTER, fontSize=20, spaceAfter=20)
    source_style = styles["Heading4"]
    content_style = styles["BodyText"]

    story = []

    # Newsletter Header
    story.append(Paragraph("📰 Web3 Daily Digest", title_style))
    story.append(Spacer(1, 12))

    for idx, article in enumerate(articles, start=1):
        story.append(Paragraph(f"{idx}. {article['title']}", styles["Heading2"]))
        story.append(Paragraph(f"Source: {article.get('url', 'Unknown')}", source_style))
        story.append(Paragraph(f"Published: {article.get('published', 'N/A')}", source_style))
        story.append(Spacer(1, 6))

        summary = article.get("summary", "Summary not available.")
        story.append(Paragraph(summary, content_style))
        story.append(Spacer(1, 12))

        story.append(Paragraph(f"🔗 <a href='{article['url']}'>{article['url']}</a>", styles["BodyText"]))
        story.append(PageBreak())

    doc.build(story)
    print(f"✅ PDF generated: {output_pdf}")

if __name__ == "__main__":
    generate_pdf()
