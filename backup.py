import sqlite3
import pandas as pd
from datetime import datetime

def create_backup():
    # Connect to the original database
    conn_orig = sqlite3.connect('stock.db')
    c_orig = conn_orig.cursor()

    # Connect to the backup database
    conn_backup = sqlite3.connect('stock_backup.db')
    c_backup = conn_backup.cursor()

    # Fetch all table names in the database
    table_query = "SELECT name FROM sqlite_master WHERE type='table';"
    c_orig.execute(table_query)
    tables = c_orig.fetchall()

    # For each table in the database, fetch the last column and append
    for table in tables:
        table = table[0]  # extract table name from tuple
        query = f"PRAGMA table_info({table});"
        c_orig.execute(query)
        columns = c_orig.fetchall()

        # Get the last column name
        last_col_name = columns[-1][1]

        # Fetch the entire table from the original database
        df_orig = pd.read_sql_query(f"SELECT * FROM {table}", conn_orig)

        # Fetch the entire table from the backup database
        df_backup = pd.read_sql_query(f"SELECT * FROM {table}", conn_backup)

        # Append the last column of the original table to the backup table with a new name (current datetime)
        df_backup[str(datetime.now())] = df_orig[last_col_name]

        # Write the updated dataframe back to the backup database
        df_backup.to_sql(table, conn_backup, if_exists='replace', index=False)

    # Close the connections to the databases
    conn_orig.close()
    conn_backup.close()

