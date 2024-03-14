SELECT 
Date,
Series,
Name,
Units,
AdjSeas,
Freq
FROM {{ref('silver_employment_setdatatypes')}}
WHERE Date <= CURRENT_DATE AND Date > CURRENT_DATE - INTERVAL '10' YEAR