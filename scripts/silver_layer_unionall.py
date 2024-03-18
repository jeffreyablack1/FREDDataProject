import os
import subprocess


def create_union_sql_file(series_ids, target_directory):
    """
    Create a single .sql file that contains a UNION ALL query for each series ID.

    Parameters:
    - series_ids (list of str): The FRED series IDs.
    - target_directory (str): The target directory to store the .sql file.
    """
    sql_directory = os.path.join(target_directory, "silver")
    os.makedirs(sql_directory, exist_ok=True)

    sql_template = """SELECT 
Date,
Series,
SeriesID,
FetchDate
FROM {{{{ref('bronze_Fact{0}')}}}}
"""

    union_all_query = ""

    for series_id in series_ids:
        if union_all_query:
            union_all_query += "\nUNION ALL\n"
        union_all_query += sql_template.format(series_id)

    file_path = os.path.join(sql_directory, "silver_FactSeries_unionall.sql")
    
    with open(file_path, 'w') as sql_file:
        sql_file.write(union_all_query)
    
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

def main(series_ids, target_directory):
    create_union_sql_file(series_ids, target_directory)