SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate             
FROM {{ref('bronze_cpiaucsl')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate             
FROM {{ref('bronze_ppiaco')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate             
FROM {{ref('bronze_pce')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate             
FROM {{ref('bronze_cpilfesl')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate             
FROM {{ref('bronze_umcsent')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate             
FROM {{ref('bronze_pcepilfe')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate             
FROM {{ref('bronze_mich')}}