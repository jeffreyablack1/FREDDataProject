SELECT 
CAST(SeriesID AS NVARCHAR(60)) AS SeriesID,
CAST(RealTimeStart AS DATETIME) AS RealTimeStart,
CAST(RealTimeEnd AS DATETIME) AS RealTimeEnd,
CAST(Name AS NVARCHAR(255)) AS Name,
CAST(ObservationStart AS DATETIME) AS ObservationStart,
CAST(ObservationEnd AS DATETIME) AS ObservationEnd,
CAST(Frequency AS NVARCHAR(60)) AS Frequency,
CAST(FrequencyAbbr AS NVARCHAR(60)) AS FrequencyAbbr,
CAST(Units AS NVARCHAR(60)) AS Units,
CAST(UnitsAbbr AS NVARCHAR(60)) AS UnitsAbbr,
CAST(SeasAdj AS NVARCHAR(60)) AS SeasAdj,
CAST(SeasAdjAbbr AS NVARCHAR(60)) AS SeasAdjAbbr,
CAST(SeasAdjBool AS BOOLEAN) AS SeasAdjBool
FROM {{ ref('silver_DimSeries_binaryconversion') }}