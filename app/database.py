import os
import pyodbc
import pandas as pd
import psycopg2


SERVER = r"localhost\SQLEXPRESS"
DATABASE = "ShopSmartDB"

SQL_SERVER_CONNECTION = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"
)


def get_connection():
    # Render
    if os.getenv("DATABASE_URL"):
        return psycopg2.connect(os.getenv("DATABASE_URL"))

    # Local computer
    return pyodbc.connect(SQL_SERVER_CONNECTION)


def get_products():
    connection = get_connection()

    query = """
    SELECT
        p.ProductID,
        p.ProductName,
        p.CategoryID,
        c.CategoryName
    FROM Products p
    JOIN Categories c
        ON p.CategoryID = c.CategoryID
    """

    df = pd.read_sql(query, connection)
    connection.close()

    return df