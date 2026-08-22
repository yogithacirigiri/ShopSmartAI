import pyodbc
import pandas as pd

# SQL Server connection
server = r"localhost\SQLEXPRESS"
database = "ShopSmartDB"

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
)

connection = pyodbc.connect(connection_string)

# =========================================================
# 1. MONTHLY REVENUE
# =========================================================

query = "SELECT * FROM Orders"

orders_df = pd.read_sql(query, connection)

orders_df["OrderDate"] = pd.to_datetime(orders_df["OrderDate"])
orders_df["Month"] = orders_df["OrderDate"].dt.month_name()

monthly_revenue = orders_df.groupby("Month")["TotalAmount"].sum()

print("\nMonthly Revenue:")
print(monthly_revenue)

best_month = monthly_revenue.idxmax()
best_revenue = monthly_revenue.max()

print("\nBest Performing Month:")
print(best_month, "₹", best_revenue)


# =========================================================
# 2. TOP CUSTOMER
# =========================================================

customer_revenue = orders_df.groupby("CustomerID")["TotalAmount"].sum()

top_customer = customer_revenue.idxmax()
top_customer_revenue = customer_revenue.max()

print("\nTop Customer:")
print("Customer ID:", top_customer)
print("Revenue: ₹", top_customer_revenue)


# =========================================================
# 3. TOP PRODUCT
# =========================================================

query = """
SELECT
    p.ProductID,
    p.ProductName,
    SUM(od.Quantity) AS TotalQuantity,
    SUM(od.Quantity * od.Price) AS Revenue
FROM OrderDetails od
JOIN Products p
    ON od.ProductID = p.ProductID
GROUP BY
    p.ProductID,
    p.ProductName
ORDER BY Revenue DESC
"""

product_df = pd.read_sql(query, connection)

print("\nProduct Revenue:")
print(product_df)

top_product = product_df.iloc[0]

print("\nTop Product:")
print("Product:", top_product["ProductName"])
print("Quantity Sold:", top_product["TotalQuantity"])
print("Revenue: ₹", top_product["Revenue"])


# =========================================================
# 4. TOP CATEGORY
# =========================================================

query = """
SELECT
    c.CategoryID,
    c.CategoryName,
    SUM(od.Quantity * od.Price) AS Revenue
FROM OrderDetails od
JOIN Products p
    ON od.ProductID = p.ProductID
JOIN Categories c
    ON p.CategoryID = c.CategoryID
GROUP BY
    c.CategoryID,
    c.CategoryName
ORDER BY Revenue DESC
"""

category_df = pd.read_sql(query, connection)

print("\nCategory Revenue:")
print(category_df)

top_category = category_df.iloc[0]

print("\nTop Category:")
print("Category:", top_category["CategoryName"])
print("Revenue: ₹", top_category["Revenue"])


# =========================================================
# 5. DATASET INFORMATION
# =========================================================

print("\nDataset Information:")
print(orders_df.info())


# =========================================================
# 6. BASIC STATISTICS
# =========================================================

print("\nBasic Statistics:")
print(orders_df.describe())


# =========================================================
# 7. DATA TYPES
# =========================================================

print("\nData Types:")
print(orders_df.dtypes)


# Close connection
connection.close()