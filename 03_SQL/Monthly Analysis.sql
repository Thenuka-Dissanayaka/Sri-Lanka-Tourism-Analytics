SELECT
    CASE
        WHEN Month IN ('Jan','January') THEN 'January'
        WHEN Month IN ('Feb','February') THEN 'February'
        WHEN Month IN ('Mar','March') THEN 'March'
        WHEN Month IN ('Apr','April') THEN 'April'
        WHEN Month IN ('May') THEN 'May'
        WHEN Month IN ('Jun','June') THEN 'June'
        WHEN Month IN ('Jul','July') THEN 'July'
        WHEN Month IN ('Aug','August') THEN 'August'
        WHEN Month IN ('Sep','September') THEN 'September'
        WHEN Month IN ('Oct','October') THEN 'October'
        WHEN Month IN ('Nov','November') THEN 'November'
        WHEN Month IN ('Dec','December') THEN 'December'
    END AS Month_Name,
    SUM(Arrivals) AS Total_Arrivals
FROM dbo.TourismismArrivals
WHERE Month IN (
    'Jan','January','Feb','February','Mar','March',
    'Apr','April','May','Jun','June','Jul','July',
    'Aug','August','Sep','September','Oct','October',
    'Nov','November','Dec','December'
)
GROUP BY
    CASE
        WHEN Month IN ('Jan','January') THEN 'January'
        WHEN Month IN ('Feb','February') THEN 'February'
        WHEN Month IN ('Mar','March') THEN 'March'
        WHEN Month IN ('Apr','April') THEN 'April'
        WHEN Month = 'May' THEN 'May'
        WHEN Month IN ('Jun','June') THEN 'June'
        WHEN Month IN ('Jul','July') THEN 'July'
        WHEN Month IN ('Aug','August') THEN 'August'
        WHEN Month IN ('Sep','September') THEN 'September'
        WHEN Month IN ('Oct','October') THEN 'October'
        WHEN Month IN ('Nov','November') THEN 'November'
        WHEN Month IN ('Dec','December') THEN 'December'
    END
ORDER BY MIN(
    CASE
        WHEN Month IN ('Jan','January') THEN 1
        WHEN Month IN ('Feb','February') THEN 2
        WHEN Month IN ('Mar','March') THEN 3
        WHEN Month IN ('Apr','April') THEN 4
        WHEN Month = 'May' THEN 5
        WHEN Month IN ('Jun','June') THEN 6
        WHEN Month IN ('Jul','July') THEN 7
        WHEN Month IN ('Aug','August') THEN 8
        WHEN Month IN ('Sep','September') THEN 9
        WHEN Month IN ('Oct','October') THEN 10
        WHEN Month IN ('Nov','November') THEN 11
        WHEN Month IN ('Dec','December') THEN 12
    END
);