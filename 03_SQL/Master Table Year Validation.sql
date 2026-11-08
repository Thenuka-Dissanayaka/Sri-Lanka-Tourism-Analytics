SELECT
    Year,
    COUNT(*) AS Total_Records,
    SUM(Arrivals) AS Total_Arrivals
FROM dbo.TourismArrivals_Cleaned
GROUP BY Year
ORDER BY Year;