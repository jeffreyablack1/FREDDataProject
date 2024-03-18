SELECT 
id AS SeriesID,
realtime_start AS RealTimeStart, 
realtime_end AS RealTimeEnd,
title AS Name, 
observation_start AS ObservationStart,
observation_end AS ObservationEnd, 
frequency AS Frequency, 
frequency_short AS FrequencyAbbr, 
units AS Units,
units_short AS UnitsAbbr, 
seasonal_adjustment AS SeasAdj, 
seasonal_adjustment_short AS SeasAdjAbbr
FROM metadata
