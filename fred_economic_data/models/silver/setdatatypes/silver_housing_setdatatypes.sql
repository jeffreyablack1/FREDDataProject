SELECT 
CAST(Date AS DATETIME(7)) AS Date,
CAST(Series AS FLOAT) AS Series,
CAST(Name AS NVARCHAR(60)) AS Name,
CAST(Units AS NVARCHAR(60)) AS Units,
CAST(AdjSeas AS BIT) AS AdjSeas,
CAST(Freq AS NVARCHAR(60)) AS Freq,
CAST(LastUpdatedDate AS DATETIME(7)) AS LastUpdatedDate,
CAST(FetchDate AS DATETIME(7)) AS FetchDate
FROM {{ref('silver_housing_addcategory')}}