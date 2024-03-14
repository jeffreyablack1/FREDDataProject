SELECT Date, Series, Name, Units, AdjSeas, Freq, Category FROM {{ref('silver_energy_restrictdate')}} 
UNION ALL 
SELECT Date, Series, Name, Units, AdjSeas, Freq, Category FROM {{ref('silver_cpi_ppi_sentiment_restrictdate')}} 
UNION ALL 
SELECT Date, Series, Name, Units, AdjSeas, Freq, Category FROM {{ref('silver_employment_restrictdate')}} 
UNION ALL 
SELECT Date, Series, Name, Units, AdjSeas, Freq, Category FROM {{ref('silver_federal_funds_restrictdate')}} 
UNION ALL 
SELECT Date, Series, Name, Units, AdjSeas, Freq, Category FROM {{ref('silver_housing_restrictdate')}}