SELECT 
CAST(Date AS DATETIME(7)) AS Date,
CAST(Series AS FLOAT) AS Series,
CAST(Name AS NVARCHAR(60)) AS Name,
CAST(Units AS NVARCHAR(60)) AS Units,
CAST(AdjSeas AS BOOLEAN) AS AdjSeas,
CAST(Freq AS NVARCHAR(60)) AS Freq,
CAST(LastUpdatedDate AS DATETIME(7)) AS LastUpdatedDate,
CAST(Category AS NVARCHAR(60)) AS Category,
CAST(FetchDate AS DATETIME(7)) AS FetchDate
FROM {{ref('silver_cpi_ppi_sentiment_addcategory')}}