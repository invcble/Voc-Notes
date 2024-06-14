from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import pandas as pd
from tableauhyperapi import HyperProcess, Connection, Telemetry, TableDefinition, SqlType, Inserter, TableName, CreateMode

def create_hyper(path):
    with open(path, 'r') as file:
        text = file.read()

    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words and word.isalpha()]
    word_counts = Counter(filtered_words)

    df = pd.DataFrame(word_counts.items(), columns=['Word', 'Frequency'])

    
    hyper_file_path = 'word_frequencies.hyper'
    table_definition = TableDefinition(
        table_name=TableName('Extract', 'Extract')
    )
    table_definition.add_column('Word', SqlType.text())
    table_definition.add_column('Frequency', SqlType.big_int())

    # Hyper file creation
    with HyperProcess(telemetry=Telemetry.SEND_USAGE_DATA_TO_TABLEAU) as hyper:
        with Connection(endpoint=hyper.endpoint, database=hyper_file_path, create_mode=CreateMode.CREATE_AND_REPLACE) as connection:

            connection.catalog.create_schema('Extract')
            connection.catalog.create_table(table_definition)
            
            with Inserter(connection, table_definition) as inserter:
                inserter.add_rows(df.itertuples(index=False, name=None))
                inserter.execute()
