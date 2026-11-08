SELECT
    Country,
    Month,
    SUM(Arrivals) AS Arrivals,
    Year
FROM dbo.TourismArrivals_Cleaned
WHERE Year = 2020
GROUP BY Country, Month, Year
ORDER BY Country, Month;