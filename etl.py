import pandas as pd
from sqlalchemy import create_engine

display =pd.options.display.max_rows = 99999
# Konfigurasi Server
engine = create_engine(
    "mssql+pyodbc://@localhost/wc2026?driver=ODBC+Driver+18+for+SQL+Server&trusted_connection=yes"
)
# extracttt

def extract(raw_data):
    try:
        data = pd.read_csv(raw_data)
        # #print(data.shape)
        print(data.isnull().sum())
        # print(data.info())
        return data
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None

# transformation
def transformation(df):
    try:
        if df is None:
            print("No data to transform.")
            return None
        else:
            df = df.drop(columns=["pens_conceded","team", "pens_won","gk_pens_save_pct","plus_minus_wowy","minutes_per_sub"])
            df["club"] = df["club"].fillna("unknown")
            df["age"] = df["age"].str[2:].astype(int)
            int_cols = [
            "games_starts",
            "goals",
            "assists",
            "goals_assists",
            "goals_pens",
            "pens_made",
            "pens_att",
            "cards_yellow",
            "cards_red",
            "games_complete",
            "games_subs",
            "unused_subs",
            "on_goals_for",
            "on_goals_against",
            "cards_yellow_red",
            "fouls",
            "fouled",
            "offsides",
            "crosses",
            "interceptions",
            "tackles_won"
            
        ]

            df[int_cols] = df[int_cols].astype("Int64")
            return df
    except Exception as e:
            print(f"Error transforming data: {e}")
            return None


def loads(df):
    try:
        if df is None:
            print("No data to load.")
            return None
        else:
            df.to_sql(name="stat_pemain", con=engine, if_exists="replace", index=False)
    except Exception as e:
        print(f"Error loading data: {e}")

extract("C:\\Users\\razzan\\Downloads\\players.csv")
