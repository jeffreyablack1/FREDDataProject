SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_dcoilwtico')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_gasregw')}} 
UNION ALL 
SELECT Date,             
Series,             
Name,             
Units,             
AdjSeas,             
Freq,             
LastUpdatedDate,             
FetchDate FROM {{ref('bronze_dpropanembtx')}}