import os
import subprocess

def create_sql_files(series_ids, target_directory):
    """
    Create .sql files in the target directory for a list of series IDs.

    Parameters:
    - series_ids (list of str): The FRED series IDs.
    - target_directory (str): The target directory to store .sql files.
    """
    # Ensure the target directory exists, create if not
    bronze_directory = os.path.join(target_directory, "bronze")
    os.makedirs(bronze_directory, exist_ok=True)
    
    # SQL template for each series
    sql_template = """SELECT 
date AS Date,
series_index AS Series,
seriesid AS SeriesID,
fetch_date AS FetchDate
FROM {}
"""
    # SQL template for metadata
    metadata_sql_template = """SELECT 
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
"""
    # SQL template for categories
    categories_sql_template = """SELECT 
SeriesID,
Category
FROM categories
"""
    
    # Iterate over series IDs and create SQL files
    for series_id in series_ids:
        file_name = f"bronze_Fact{series_id}.sql"
        file_path = os.path.join(bronze_directory, file_name)
        
        # Format the SQL query for the current series ID
        sql_query = sql_template.format(series_id.lower())
        
        # Write the SQL query to a file
        with open(file_path, 'w') as sql_file:
            sql_file.write(sql_query)
        print(f"SQL file created: {file_path}")
    
    # Create SQL file for metadata
    metadata_file_name = "bronze_DimSeries.sql"
    metadata_file_path = os.path.join(bronze_directory, metadata_file_name)
    with open(metadata_file_path, 'w') as metadata_sql_file:
        metadata_sql_file.write(metadata_sql_template)
    print(f"SQL file created: {metadata_file_path}")

    # Create SQL file for categories
    categories_file_name = "bronze_DimCategories.sql"
    categories_file_path = os.path.join(bronze_directory, categories_file_name)
    with open(categories_file_path, 'w') as categories_sql_file:
        categories_sql_file.write(categories_sql_template)
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

def main(series_ids, target_directory):
    create_sql_files(series_ids, target_directory)
    #execute_dbt_commands()





# def create_bronze_sql_files(series_ids, target_directory):
#     """
#     Create .sql files in the target directory for a list of series IDs.
    
#     Parameters:
#     - series_ids (list of str): The FRED series IDs.
#     - target_directory (str): The target directory to store .sql files.
#     """
#     # Ensure the target directory exists, create if not
#     bronze_directory = os.path.join(target_directory, "bronze")
#     os.makedirs(bronze_directory, exist_ok=True)
    
#     # SQL template for each series
#     sql_template = """SELECT 
# date AS Date,
# series_index AS Series,
# seriesid AS SeriesID,
# fetch_date AS FetchDate
# FROM {}
# """
#     # SQL template for metadata
#     metadata_sql_template = """SELECT 
# id AS SeriesID,
# realtime_start AS RealTimeStart, 
# realtime_end AS RealTimeEnd,
# title AS Name, 
# observation_start AS ObservationStart,
# observation_end AS ObservationEnd, 
# frequency AS Frequency, 
# frequency_short AS FrequencyAbbr, 
# units AS Units,
# units_short AS UnitsAbbr, 
# seasonal_adjustment AS SeasAdj, 
# seasonal_adjustment_short AS SeasAdjAbbr
# FROM metadata
# """
#     # SQL template for metadata
#     categories_sql_template = """SELECT 
# SeriesID,
# Category
# FROM categories
# """
    
#     # Iterate over series IDs and create SQL files
#     for series_id in series_ids:
#         file_name = f"bronze_Fact{series_id}.sql"
#         file_path = os.path.join(bronze_directory, file_name)
        
#         # Format the SQL query for the current series ID
#         sql_query = sql_template.format(series_id.lower())
        
#         # Write the SQL query to a file
#         with open(file_path, 'w') as sql_file:
#             sql_file.write(sql_query)
            
#         print(f"SQL file created: {file_path}")
    
#     # Create SQL file for metadata
#     metadata_file_name = "bronze_DimSeries.sql"
#     metadata_file_path = os.path.join(bronze_directory, metadata_file_name)

#     # Write the SQL query for metadata to a file
#     with open(metadata_file_path, 'w') as metadata_sql_file:
#         metadata_sql_file.write(metadata_sql_template)
#     print(f"SQL file created: {metadata_file_path}")

#     # Create SQL file for categories
#     categories_file_name = "bronze_DimCategories.sql"
#     categories_file_path = os.path.join(bronze_directory, categories_file_name)

#     # Write the SQL query for metadata to a file
#     with open(categories_file_path, 'w') as categories_sql_file:
#         categories_sql_file.write(categories_sql_template)
#     print(f"SQL file created: {categories_file_path}")
    
# create_bronze_sql_files(fred_series_ids, target_directory)