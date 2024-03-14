SELECT 
Date,
Series,
Name,
Units,
AdjSeas,
Freq,
LastUpdatedDate,
'federal_funds' AS Category,
FetchDate
FROM {{ref('silver_federal_funds_binaryconversion')}}