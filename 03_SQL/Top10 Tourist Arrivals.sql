SELECT TOP 10
    Country,
    SUM(Arrivals) AS Total_Arrivals
FROM dbo.TourismismArrivals
GROUP BY Country
ORDER BY Total_Arrivals DESC;