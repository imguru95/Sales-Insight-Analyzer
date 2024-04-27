from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

# Create a SparkSession
spark = SparkSession.builder \
    .appName("SalesAnalysis") \
    .getOrCreate()

# Read the CSV file into a DataFrame
sales_df = spark.read.csv("data/data.csv", header=True, inferSchema=True)

# Group by ProductCategory and calculate total revenue for each category
category_revenue = sales_df.groupBy("ProductCategory").agg(sum("Revenue").alias("TotalRevenue"))

# Show the result
category_revenue.show()

# Stop the SparkSession
spark.stop()
