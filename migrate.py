import os
import pyodbc
import psycopg2
import pandas as pd

# ==============================
# MS SQL SERVER
# ==============================

SERVER = r"localhost\SQLEXPRESS"
DATABASE = "ShopSmartDB"

SQL_CONNECTION = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"
)

print("Connecting to MS SQL Server...")
sql_connection = pyodbc.connect(SQL_CONNECTION)
print("MS SQL Server connected!")

# ==============================
# RENDER POSTGRESQL
# ==============================

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    print("ERROR: DATABASE_URL is not set.")
    exit()

print("Connecting to Render PostgreSQL...")
pg_connection = psycopg2.connect(DATABASE_URL)
print("PostgreSQL connected!")

# ==============================
# READ TABLES FROM SQL SERVER
# ==============================

tables = [
    "Categories",
    "Customers",
    "Products",
    "Orders",
    "OrderDetails"
]

for table in tables:

    print(f"\nReading {table}...")

    df = pd.read_sql(
        f"SELECT * FROM {table}",
        sql_connection
    )

    print(f"{len(df)} rows found.")

    # Create PostgreSQL table automatically
    columns = []

    for column, dtype in zip(df.columns, df.dtypes):

        if "int" in str(dtype):
            sql_type = "INTEGER"
        elif "float" in str(dtype):
            sql_type = "DOUBLE PRECISION"
        elif "datetime" in str(dtype):
            sql_type = "TIMESTAMP"
        else:
            sql_type = "TEXT"

        columns.append(f'"{column}" {sql_type}')

    create_query = f'''
        CREATE TABLE IF NOT EXISTS "{table}" (
            {", ".join(columns)}
        )
    '''

    cursor = pg_connection.cursor()

    cursor.execute(create_query)

    # Clear existing data
    cursor.execute(f'DELETE FROM "{table}"')

    # Insert data
    column_names = ", ".join(
        f'"{column}"'
        for column in df.columns
    )

    placeholders = ", ".join(
        ["%s"] * len(df.columns)
    )

    insert_query = f'''
        INSERT INTO "{table}" ({column_names})
        VALUES ({placeholders})
    '''

    for _, row in df.iterrows():

        values = []

        for value in row:

            if pd.isna(value):
                values.append(None)
            else:
                values.append(value)

        cursor.execute(
            insert_query,
            tuple(values)
        )

    pg_connection.commit()
    cursor.close()

    print(f"{table} migrated successfully!")

# ==============================
# CLOSE CONNECTIONS
# ==============================

sql_connection.close()
pg_connection.close()

print("\n================================")
print("MIGRATION COMPLETED SUCCESSFULLY")
print("================================")