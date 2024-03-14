SELECT 
date AS Date,
series_index AS Series,
name AS Name,
units AS Units,
seasonal_adjustment AS AdjSeas,
frequency AS Freq,
fred_last_updated_date AS LastUpdatedDate,
fetch_date AS FetchDate
FROM tb3ms
