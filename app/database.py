import os
import pyodbc
import psycopg2
import pandas as pd

SERVER = r"localhost\SQLEXPRESS"
DATABASE = "ShopSmartDB"

SQL_SERVER_CONNECTION = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"
)


def get_connection():
    # Render PostgreSQL
    database_url = os.getenv("DATABASE_URL")

    if database_url:
        return psycopg2.connect(database_url)

    # Local MS SQL Server
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


def get_sales():
    connection = get_connection()

    query = """
    SELECT
        OrderID,
        CustomerID,
        OrderDate,
        TotalAmount
    FROM Orders
    """

    df = pd.read_sql(query, connection)
    connection.close()

    return df


def get_customer_orders(customer_id):
    connection = get_connection()

    query = """
    SELECT
        o.OrderID,
        o.CustomerID,
        od.ProductID,
        p.ProductName,
        od.Quantity,
        od.Price
    FROM Orders o
    JOIN OrderDetails od
        ON o.OrderID = od.OrderID
    JOIN Products p
        ON od.ProductID = p.ProductID
    WHERE o.CustomerID = %s
    """

    df = pd.read_sql(query, connection, params=[customer_id])
    connection.close()

    return df