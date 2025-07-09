from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col

# 1. Initialize Spark session
spark = SparkSession.builder \
    .appName("Heart Disease Preprocessing") \
    .getOrCreate()

# 2. Load raw CSV
df = spark.read.csv("heart.csv", header=True, inferSchema=True)
print("✅ Raw data loaded")

# 3. Drop rows with nulls
df = df.dropna()

# 4. Encode categorical columns manually
df = df.withColumn("Sex_F", when(col("Sex") == "F", 1).otherwise(0))
df = df.withColumn("ChestPainType_ATA", when(col("ChestPainType") == "ATA", 1).otherwise(0))
df = df.withColumn("ChestPainType_NAP", when(col("ChestPainType") == "NAP", 1).otherwise(0))
df = df.withColumn("ChestPainType_TA", when(col("ChestPainType") == "TA", 1).otherwise(0))
df = df.withColumn("RestingECG_Normal", when(col("RestingECG") == "Normal", 1).otherwise(0))
df = df.withColumn("RestingECG_ST", when(col("RestingECG") == "ST", 1).otherwise(0))
df = df.withColumn("ExerciseAngina_Y", when(col("ExerciseAngina") == "Y", 1).otherwise(0))
df = df.withColumn("ST_Slope_Flat", when(col("ST_Slope") == "Flat", 1).otherwise(0))
df = df.withColumn("ST_Slope_Up", when(col("ST_Slope") == "Up", 1).otherwise(0))

# 5. Drop original categorical columns
df = df.drop("Sex", "ChestPainType", "RestingECG", "ExerciseAngina", "ST_Slope")

# 6. Save processed data
df.write.csv("processed_heart.csv", header=True, mode="overwrite")
print("✅ Processed data saved to 'processed_heart.csv'")

# 7. Stop Spark session
spark.stop()
