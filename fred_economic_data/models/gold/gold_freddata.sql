
    SELECT 
    fs.Date,
    fs.Series,
    ds.Name,
    ds.Frequency,
    ds.Units,
    ds.SeasAdjBool AS SeasonallyAdjusted,
    dc.Category
    FROM {{ ref('silver_FactSeries_setdatatypes') }} fs
    LEFT JOIN {{ ref('silver_DimSeries_setdatatypes') }} ds ON ds.SeriesID = fs.SeriesID 
    LEFT JOIN {{ ref('silver_DimCategories_setdatatypes') }} dc ON dc.SeriesID = fs.SeriesID
    