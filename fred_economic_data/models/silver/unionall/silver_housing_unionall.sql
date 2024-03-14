SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate             
FROM {{ref('bronze_csushpinsa')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate             
FROM {{ref('bronze_hsn1f')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate             
FROM {{ref('bronze_permit')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate             
FROM {{ref('bronze_houst')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate             
FROM {{ref('bronze_ussthpi')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate             
FROM {{ref('bronze_exhoslusm495s')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate             
FROM {{ref('bronze_mortgage30us')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate             
FROM {{ref('bronze_rrvrusq156n')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate             
FROM {{ref('bronze_rhorusq156n')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate             
FROM {{ref('bronze_hosinvusm495n')}}