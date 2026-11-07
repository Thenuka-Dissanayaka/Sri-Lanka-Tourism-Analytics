SELECT
    Year,
    SUM(Arrivals) AS Total_Arrivals
FROM dbo.TourismismArrivals
GROUP BY Year
ORDER BY Year;