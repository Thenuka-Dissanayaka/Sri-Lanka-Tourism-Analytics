SELECT
    Country,
    Month,
    Arrivals,
    Year
INTO dbo.TourismArrivals_Cleaned
FROM dbo.TourismismArrivals
WHERE Year <> 2020

UNION ALL

SELECT
    Country,
    Month,
    Arrivals,
    Year
FROM dbo.Tourism_2020_Cleaned1;