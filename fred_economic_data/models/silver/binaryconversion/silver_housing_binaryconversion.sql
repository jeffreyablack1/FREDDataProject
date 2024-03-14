SELECT 
Date,
Series,
Name,
Units,
CASE 
    WHEN AdjSeas = 'Not Seasonally Adjusted' THEN FALSE 
    WHEN AdjSeas = 'Seasonally Adjusted' THEN TRUE 
    ELSE NULL 
END AS AdjSeas,
Freq,
LastUpdatedDate,
FetchDate
FROM {{ref('silver_housing_unionall')}}