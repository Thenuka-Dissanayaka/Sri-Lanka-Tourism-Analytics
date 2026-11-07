SELECT TOP 10
    Country,
    SUM(Arrivals) AS Total_Arrivals
FROM dbo.TourismismArrivals
WHERE Year = 2025
GROUP BY Country
ORDER BY Total_Arrivals DESC;