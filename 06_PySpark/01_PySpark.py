from pyspark.sql import SparkSession

def create_spark_dataframe():
    # Create a Spark session
    spark = SparkSession.builder \
        .appName("Spark DataFrame Demo") \
        .getOrCreate()

    # Sample data
    data = [
        ("Alice", 34),
        ("Bob", 45),
        ("Catherine", 29)
    ]

    # Define schema for the DataFrame
    columns = ["Name", "Age"]

    # Create a DataFrame
    df = spark.createDataFrame(data, schema=columns)

    # Show the DataFrame
    df.show()

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    create_spark_dataframe()


