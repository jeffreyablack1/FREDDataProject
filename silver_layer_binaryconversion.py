import os
import subprocess

def create_silver_sql_binaryconversion_file(target_directory):
    """
    Create an SQL file for transforming the AdjSeas column in the 'silver' subdirectory.

    Parameters:
    - target_directory (str): The target directory to store the SQL file.
    """
    # Define the target subdirectory for these transformation SQL files
    silver_directory = os.path.join(target_directory, "silver")
    os.makedirs(silver_directory, exist_ok=True)

    # SQL template for transforming AdjSeas
    sql_template = """SELECT 
SeriesID,
RealTimeStart, 
RealTimeEnd,
Name, 
ObservationStart,
ObservationEnd, 
Frequency, 
FrequencyAbbr, 
Units,
UnitsAbbr, 
SeasAdj,
SeasAdjAbbr,
CASE 
    WHEN SeasAdjAbbr = 'NSA' THEN FALSE 
    WHEN SeasAdjAbbr = 'SA' THEN TRUE 
    ELSE NULL 
END AS SeasAdjBool
FROM {{ ref('bronze_DimSeries') }}"""

    # Format file name and path
    file_name = "silver_DimSeries_binaryconversion.sql"
    file_path = os.path.join(silver_directory, file_name)
    
    # Write the formatted SQL query to a file
    with open(file_path, 'w') as sql_file:
        sql_file.write(sql_template)
        
    print(f"SQL file created: {file_path}")

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
    create_silver_sql_binaryconversion_file(target_directory)
    #execute_dbt_commands()