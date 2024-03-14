SELECT 
Date,
Series,
Name,
Units,
AdjSeas,
Freq,
LastUpdatedDate,
'energy' AS Category,
FetchDate
FROM {{ref('silver_energy_binaryconversion')}}