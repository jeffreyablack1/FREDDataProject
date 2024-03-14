SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_fedfunds')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_dfedtar')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_ioer')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_discount')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_dgs10')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_sofr')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_prime')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_tb3ms')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_cpff')}}