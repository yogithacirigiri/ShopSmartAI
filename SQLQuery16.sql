SELECT
    Products.ProductName,
    OrderDetails.Quantity,
    OrderDetails.Price,
    OrderDetails.Quantity * OrderDetails.Price AS Revenue
FROM OrderDetails
INNER JOIN Products
    ON OrderDetails.ProductID = Products.ProductID;