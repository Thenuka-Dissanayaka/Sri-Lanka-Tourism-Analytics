SELECT
    Year,
    Month,
    SUM(Arrivals) AS Monthly_Arrivals
FROM dbo.TourismismArrivals
GROUP BY Year, Month
ORDER BY Year, Month;