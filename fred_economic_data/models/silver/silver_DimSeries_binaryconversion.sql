SELECT 
SeriesID,
RealTimeStart, 
RealTimeEnd,
Name, 
ObservationStart,
ObservationEnd, 
Frequency, 
FrequencyAbbr, 
Units,
UnitsAbbr, 
SeasAdj,
SeasAdjAbbr,
CASE 
    WHEN SeasAdjAbbr = 'NSA' THEN False 
    WHEN SeasAdjAbbr = 'SA' THEN True 
    WHEN SeasAdjAbbr = 'SAAR' THEN True 
    ELSE NULL 
END AS SeasAdjBool
FROM {{ ref('bronze_DimSeries') }}