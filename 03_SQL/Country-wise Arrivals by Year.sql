SELECT
    Country,
    Year,
    SUM(Arrivals) AS Total_Arrivals
FROM dbo.TourismismArrivals
GROUP BY Country, Year
ORDER BY Country, Year;