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
    WHEN SeasAdjAbbr = 'NSA' THEN FALSE 
    WHEN SeasAdjAbbr = 'SA' THEN TRUE 
    ELSE NULL 
END AS SeasAdjBool
FROM {{ ref('bronze_DimSeries') }}