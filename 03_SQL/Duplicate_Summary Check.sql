SELECT
    Country,
    LEN(Country) AS Country_Length,
    Month,
    COUNT(*) AS Record_Count,
    SUM(Arrivals) AS Total_Arrivals,
    MIN(Arrivals) AS Min_Arrivals,
    MAX(Arrivals) AS Max_Arrivals
FROM dbo.TourismArrivals_Cleaned
WHERE Country LIKE 'SAINT VINCENT%'
AND Year = 2020
GROUP BY Country, LEN(Country), Month
ORDER BY Month;