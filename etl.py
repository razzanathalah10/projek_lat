import pandas as pd
from sqlalchemy import create_engine

# Konfigurasi Server
engine = create_engine(
    "mssql+pyodbc://@localhost/wc2026?driver=ODBC+Driver+18+for+SQL+Server&trusted_connection=yes"
)
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

#transformation
def transformation(df):
    df = df.drop(columns=["photo", "flag", "club_logo"])
    return df




def loads(df):
    try:
        if df is None:
            print("No data to load.")
            return None
        else:
            df.to_sql(name="stat_pemain", con=engine, if_exists="replace", index=False)
    except Exception as e:
        print(f"Error loading data: {e}")

data = extract("C:\\Users\\razzan\\Downloads\\players.csv")
if data is not None:
    data = transformation(data)
    loads(data)