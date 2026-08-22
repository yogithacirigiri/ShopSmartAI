SELECT
  Customers.FirstName,
    Customers.LastName,
    Orders.OrderID,
    Orders.OrderDate,
    Products.ProductName,
    OrderDetails.Quantity,
    OrderDetails.Price
FROM Orders
INNER JOIN Customers
    ON Orders.CustomerID = Customers.CustomerID
    INNER JOIN OrderDetails
    ON Orders.OrderID = OrderDetails.OrderID
    INNER JOIN Products
    ON OrderDetails.ProductID = Products.ProductID