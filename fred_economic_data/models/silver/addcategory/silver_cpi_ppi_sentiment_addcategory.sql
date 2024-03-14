SELECT 
Date,
Series,
Name,
Units,
AdjSeas,
Freq,
LastUpdatedDate,
'cpi_ppi_sentiment' AS Category,
FetchDate
FROM {{ref('silver_cpi_ppi_sentiment_binaryconversion')}}