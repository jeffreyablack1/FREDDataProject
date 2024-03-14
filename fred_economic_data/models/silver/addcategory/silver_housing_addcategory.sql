SELECT 
Date,
Series,
Name,
Units,
AdjSeas,
Freq,
LastUpdatedDate,
'housing' AS Category,
FetchDate
FROM {{ref('silver_housing_binaryconversion')}}