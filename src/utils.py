import sqlite3
import pandas as pd

def read_sqlite_table_to_df(db_path, table_name):
    conn = sqlite3.connect(db_path)
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def create_sqlite_db_from_df(df, db_path, table_name):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, index=False, if_exists='replace')
    conn.close()


class AbcXyzAnalysis:
    pass