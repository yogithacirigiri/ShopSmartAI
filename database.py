import os
import pandas as pd
import psycopg2


def get_connection():
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise Exception("DATABASE_URL is not configured")

    return psycopg2.connect(database_url)


def get_products():
    connection = get_connection()

    query = """
        SELECT
            p."ProductID",
            p."ProductName",
            p."CategoryID",
            c."CategoryName"
        FROM "Products" p
        JOIN "Categories" c
            ON p."CategoryID" = c."CategoryID"
    """

    df = pd.read_sql_query(query, connection)

    connection.close()

    return df


def get_sales():
    connection = get_connection()

    query = """
        SELECT
            "OrderID",
            "CustomerID",
            "OrderDate",
            "TotalAmount"
        FROM "Orders"
    """

    df = pd.read_sql_query(query, connection)

    connection.close()

    return df


def get_customer_orders(customer_id):
    connection = get_connection()

    query = """
        SELECT
            "OrderID",
            "CustomerID",
            "OrderDate",
            "TotalAmount"
        FROM "Orders"
        WHERE "CustomerID" = %s
    """

    df = pd.read_sql_query(
        query,
        connection,
        params=(customer_id,)
    )

    connection.close()

    return df