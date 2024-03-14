SELECT 
Date,
Series,
Name,
Units,
AdjSeas,
Freq,
LastUpdatedDate,
Category,
FetchDate
FROM {{ref('silver_employment_setdatatypes')}}
WHERE Date <= CURRENT_DATE AND Date > CURRENT_DATE - INTERVAL '10' YEAR