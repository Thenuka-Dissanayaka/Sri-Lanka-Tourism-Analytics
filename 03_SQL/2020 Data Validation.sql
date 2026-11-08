SELECT
    COUNT(*) AS Total_Records,
    SUM(Arrivals) AS Total_2020_Arrivals,
    COUNT(DISTINCT Country) AS Unique_Countries
FROM dbo.Tourism_2020_Cleaned1;