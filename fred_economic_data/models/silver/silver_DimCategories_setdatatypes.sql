SELECT 
CAST(SeriesID AS NVARCHAR(60)) AS SeriesID,
CAST(Category AS NVARCHAR(60)) AS Category
FROM {{ ref('bronze_DimCategories') }}