import pandas as pd
from sqlalchemy import create_engine

# extracttt

def extract(raw_data):
    try:
        data = pd.read_csv(raw_data)
        print(data.shape)
        print(data.head(10))
        return data
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None

extract("C:\\Users\\razzan\\Downloads\\players.csv")