from pyspark.sql import SparkSession
from pyspark.ml.feature import Tokenizer, StopWordsRemover
from pyspark.sql.functions import concat_ws, col

spark = SparkSession.builder.appName("TextPreprocessing").getOrCreate()
transcript_df = spark.read.text("CS615_lecture_transcript.txt")


tokenizer = Tokenizer(inputCol="value", outputCol="words")
tokenized_df = tokenizer.transform(transcript_df)

remover = StopWordsRemover(inputCol="words", outputCol="filtered_words")
filtered_df = remover.transform(tokenized_df)


sentences_df = filtered_df.withColumn("sentence", concat_ws(" ", col("filtered_words")))
sentences_df.select("sentence").write.text("processed_transcript.txt")

spark.stop()
