import os
import subprocess

def create_sql_set_datatypes_files(target_directory):
    """
    Create .sql files for setting data types for the silver and bronze tables.

    Parameters:
    - target_directory (str): The target directory to store .sql files.
    """
    # Define the target subdirectory for these SQL files
    set_datatypes_directory = os.path.join(target_directory, 'silver')
    os.makedirs(set_datatypes_directory, exist_ok=True)

    # SQL template for casting data types in the series dimension table
    dim_series_sql = """SELECT 
CAST(SeriesID AS NVARCHAR(60)) AS SeriesID,
CAST(RealTimeStart AS DATETIME) AS RealTimeStart,
CAST(RealTimeEnd AS DATETIME) AS RealTimeEnd,
CAST(Name AS NVARCHAR(255)) AS Name,
CAST(ObservationStart AS DATETIME) AS ObservationStart,
CAST(ObservationEnd AS DATETIME) AS ObservationEnd,
CAST(Frequency AS NVARCHAR(60)) AS Frequency,
CAST(FrequencyAbbr AS NVARCHAR(60)) AS FrequencyAbbr,
CAST(Units AS NVARCHAR(60)) AS Units,
CAST(UnitsAbbr AS NVARCHAR(60)) AS UnitsAbbr,
CAST(SeasAdj AS NVARCHAR(60)) AS SeasAdj,
CAST(SeasAdjAbbr AS NVARCHAR(60)) AS SeasAdjAbbr,
CAST(SeasAdjBool AS BOOLEAN) AS SeasAdjBool
FROM {{ ref('silver_DimSeries_binaryconversion') }}"""

    # SQL template for casting data types in the fact table
    fact_series_sql = """SELECT 
CAST(Date AS DATETIME) AS Date,
CAST(Series AS FLOAT) AS Series,
CAST(SeriesID AS NVARCHAR(60)) AS SeriesID,
CAST(FetchDate AS DATETIME) AS FetchDate
FROM {{ ref('silver_FactSeries_unionall') }}"""

    # SQL template for casting data types in the categories table
    categories_sql = """SELECT 
CAST(SeriesID AS NVARCHAR(60)) AS SeriesID,
CAST(Category AS NVARCHAR(60)) AS Category
FROM {{ ref('bronze_DimCategories') }}"""

    # Write the SQL query for the dimension table to a file
    dim_series_file_path = os.path.join(set_datatypes_directory, "silver_DimSeries_setdatatypes.sql")
    with open(dim_series_file_path, 'w') as sql_file:
        sql_file.write(dim_series_sql)
    print(f"SQL file created: {dim_series_file_path}")

    # Write the SQL query for the fact table to a file
    fact_series_file_path = os.path.join(set_datatypes_directory, "silver_FactSeries_setdatatypes.sql")
    with open(fact_series_file_path, 'w') as sql_file:
        sql_file.write(fact_series_sql)
    print(f"SQL file created: {fact_series_file_path}")

    # Write the SQL query for the categories table to a file
    categories_file_path = os.path.join(set_datatypes_directory, "silver_DimCategories_setdatatypes.sql")
    with open(categories_file_path, 'w') as sql_file:
        sql_file.write(categories_sql)
    print(f"SQL file created: {categories_file_path}")

def execute_dbt_commands():
    """
    Execute dbt commands in sequence.
    """
    project_path = "/Users/jeffreyblack/Projects/FREDDataProject/fred_economic_data"
    
    commands = [
        f"dbt debug",
        f"dbt compile",
        f"dbt run"
    ]
    
    for command in commands:
        full_command = f"cd {project_path} && {command}"
        subprocess.run(full_command, shell=True, capture_output=False)
        print(f"Executed command: {full_command}")

def main(target_directory):
    create_sql_set_datatypes_files(target_directory)
    #execute_dbt_commands()