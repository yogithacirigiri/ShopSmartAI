SELECT
    DATENAME(MONTH, OrderDate) AS MonthName,
    SUM(TotalAmount) AS MonthlyRevenue
FROM Orders
GROUP BY
    DATENAME(MONTH, OrderDate),
    MONTH(OrderDate)
ORDER BY
    MONTH(OrderDate);