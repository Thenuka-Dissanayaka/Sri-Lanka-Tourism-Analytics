WITH Yearly AS (
    SELECT Year, SUM(Arrivals) AS Total_Arrivals
    FROM dbo.TourismismArrivals
    GROUP BY Year
)
SELECT
    Year,
    Total_Arrivals,
    LAG(Total_Arrivals) OVER (ORDER BY Year) AS Previous_Year,
    ROUND(
        100.0 * (Total_Arrivals - LAG(Total_Arrivals) OVER (ORDER BY Year))
        / NULLIF(LAG(Total_Arrivals) OVER (ORDER BY Year), 0), 2
    ) AS Growth_Percentage
FROM Yearly
ORDER BY Year;