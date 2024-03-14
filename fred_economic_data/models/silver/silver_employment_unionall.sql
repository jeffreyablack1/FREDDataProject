SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_payems')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_unrate')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_ces0500000003')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_civpart')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_jtsjol')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_icsa')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_adpwnusnersa')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_u6rate')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_awhnonag')}}