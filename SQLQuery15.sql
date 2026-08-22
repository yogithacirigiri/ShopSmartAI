SELECT
    Customers.FirstName,
    Customers.LastName,
    SUM(Orders.TotalAmount) AS TotalRevenue
FROM Orders
INNER JOIN Customers
    ON Orders.CustomerID = Customers.CustomerID
GROUP BY
    Customers.FirstName,
    Customers.LastName
ORDER BY TotalRevenue DESC;