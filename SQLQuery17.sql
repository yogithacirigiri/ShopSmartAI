SELECT
    Categories.CategoryName,
    SUM(OrderDetails.Quantity * OrderDetails.Price) AS TotalRevenue
FROM OrderDetails
INNER JOIN Products
    ON OrderDetails.ProductID = Products.ProductID
INNER JOIN Categories
    ON Products.CategoryID = Categories.CategoryID
GROUP BY Categories.CategoryName
ORDER BY TotalRevenue DESC;