SELECT 
Date,
Series,
Name,
Units,
CASE 
    WHEN AdjSeas = 'Not Seasonally Adjusted' THEN 0 
    WHEN AdjSeas = 'Seasonally Adjusted' THEN 1 
    ELSE NULL 
END AS AdjSeas,
Freq,
LastUpdatedDate,
FetchDate
FROM {{ref('silver_energy_unionall')}}