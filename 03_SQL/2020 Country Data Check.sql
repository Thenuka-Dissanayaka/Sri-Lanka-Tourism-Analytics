USE SriLankaTourismDB;
GO

SELECT
    Country,
    Month,
    Arrivals,
    Year
FROM dbo.TourismArrivals_Cleaned
WHERE Country LIKE 'SAINT VINCENT%'
AND Year = 2020
ORDER BY Month, Arrivals;