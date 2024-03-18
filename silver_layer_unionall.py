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
    #execute_dbt_commands()




# import os

# def create_union_sql_file(series_ids, target_directory):
#     """
#     Create a single .sql file that contains a UNION ALL query for each series ID.

#     Parameters:
#     - series_ids (list of str): The FRED series IDs.
#     - target_directory (str): The target directory to store the .sql file.
#     """
#     # Ensure the target directory exists, create if not
#     sql_directory = os.path.join(target_directory, "silver", "unionall")
#     os.makedirs(sql_directory, exist_ok=True)

#     # SQL template for each series
#     sql_template = """SELECT 
# date AS Date,
# series_index AS Series,
# seriesid AS SeriesID,
# fetch_date AS FetchDate
# FROM {0}
# """

#     # Start building the UNION ALL query
#     union_all_query = ""

#     for series_id in series_ids:
#         table_name = series_id.lower()
#         if union_all_query:  # Add UNION ALL after the first query
#             union_all_query += "\nUNION ALL\n"
#         union_all_query += sql_template.format(table_name)

#     # Complete SQL file content
#     sql_file_content = union_all_query

#     # File path for the SQL file
#     file_path = os.path.join(sql_directory, "series_unionall.sql")
    
#     # Write the combined SQL query to a file
#     with open(file_path, 'w') as sql_file:
#         sql_file.write(sql_file_content)
    
#     print(f"SQL file created: {file_path}")

# create_union_sql_file(fred_series_ids, target_directory)


# def create_silver_sql_union_all_files(index_categories, target_directory):
#     """
#     Create .sql files in the 'silver' subdirectory for unioning tables related to each category.

#     Parameters:
#     - index_categories (dict of list): A dictionary where each key is a category name and each value is a list of series IDs.
#     - target_directory (str): The target directory to store .sql files.
#     """
#     # Ensure the target directory exists, create if not
#     silver_directory = os.path.join(target_directory, "silver", "unionall")
#     os.makedirs(silver_directory, exist_ok=True)

#     # Iterate over each category and create SQL files
#     for category_name, series_ids in index_categories.items():
#         file_name = f"silver_{category_name}_unionall.sql"
#         file_path = os.path.join(silver_directory, file_name)
        
#         # Start the SQL query for UNION ALL
#         sql_queries = []
#         for series_id in series_ids:
#             table_name = series_id.lower()
#             sql_query = f"SELECT Date, \
#             \nSeries, \
#             \nSeriesID, \
#             \nFetchDate \
#             \nFROM {{{{ref('bronze_%s')}}}}" % table_name
#             sql_queries.append(sql_query)
#         union_sql = " \nUNION ALL \n".join(sql_queries)
        
#         # Write the SQL query to a file
#         with open(file_path, 'w') as sql_file:
#             sql_file.write(union_sql)
            
#         print(f"SQL file created: {file_path}")