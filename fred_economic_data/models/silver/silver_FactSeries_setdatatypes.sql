SELECT 
CAST(Date AS DATETIME) AS Date,
CAST(Series AS FLOAT) AS Series,
CAST(SeriesID AS NVARCHAR(60)) AS SeriesID,
CAST(FetchDate AS DATETIME) AS FetchDate
FROM {{ ref('silver_FactSeries_unionall') }}