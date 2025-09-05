import configparser
import os
import pandas as pd
from pgdb import PGDatabase


config = configparser.ConfigParser()
config.read(os.path.join("config.ini"))

DATABASE_CREDS = config["Database"]
SALES_PATH = config["Files"]["SALES_PATH"]

database = PGDatabase(
    host=DATABASE_CREDS["HOST"],
    database=DATABASE_CREDS["DATABASE"],
    user=DATABASE_CREDS["USER"],
    password=DATABASE_CREDS["PASSWORD"],
)

sales_df = []
for file in os.listdir('data'):
    file_path = os.path.join('data', file)
    df = pd.read_csv(file_path)
    sales_df.append(df)
    sales = pd.concat(sales_df, ignore_index=True)


for i, row in sales.iterrows():
        query = f"insert into checks values ('{row['doc_id']}', '{row['item']}', '{row['category']}', '{row['amount']}', '{row['price']}', '{row['discount']}')"
        database.post(query)

