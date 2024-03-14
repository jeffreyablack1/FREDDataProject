SELECT 
Date,
Series,
Name,
Units,
AdjSeas,
Freq,
LastUpdatedDate,
'employment' AS Category,
FetchDate
FROM {{ref('silver_employment_binaryconversion')}}