import pyodbc
import pandas as pd

SERVER = r"localhost\SQLEXPRESS"
DATABASE = "ShopSmartDB"

CONNECTION_STRING = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"
)


def get_connection():
    return pyodbc.connect(CONNECTION_STRING)


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
        o.OrderID,
        o.CustomerID,
        o.OrderDate,
        o.TotalAmount
    FROM Orders o
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
    WHERE o.CustomerID = ?
    """

    df = pd.read_sql(query, connection, params=[customer_id])
    connection.close()

    return df