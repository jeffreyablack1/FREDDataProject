import os 
import subprocess

def create_gold_sql_union_all_file(target_directory):
    """
    Create a single .sql file in the 'gold' directory that joins all tables into an analytics view.

    Parameters:
    - target_directory (str): The target directory to store the .sql file.
    """
    # Define the target directory for the gold SQL file
    gold_directory = os.path.join(target_directory, "gold")
    os.makedirs(gold_directory, exist_ok=True)

    sql_query = """
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
    """

    # Final SQL file path
    file_name = "gold_freddata.sql"
    file_path = os.path.join(gold_directory, file_name)
    
    # Write the combined SQL query to the file
    with open(file_path, 'w') as sql_file:
        sql_file.write(sql_query)
        
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
    create_gold_sql_union_all_file(target_directory)
    #execute_dbt_commands()