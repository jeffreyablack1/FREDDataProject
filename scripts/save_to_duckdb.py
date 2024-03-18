import duckdb

def create_duckdb_connection(db_path='data/fred.db'):
    """
    Establishes a connection to a DuckDB database.

    Parameters:
    - db_path (str): Path to the DuckDB database file.

    Returns:
    - Connection object to the DuckDB database.
    """
    return duckdb.connect(db_path)


def save_dataframe_to_table(conn, table_name, dataframe):
    """
    Saves a DataFrame to a DuckDB table, replacing it if it already exists.

    Parameters:
    - conn: The DuckDB connection object.
    - table_name (str): Name of the table where the DataFrame will be saved.
    - dataframe (pd.DataFrame): The DataFrame to be saved.
    """
    temp_table_name = f"{table_name}_temp"
    conn.register(temp_table_name, dataframe)
    conn.execute(f'''
        CREATE OR REPLACE TABLE {table_name} AS 
        SELECT * FROM {temp_table_name}
    ''')
    conn.unregister(temp_table_name)


def main(fred_series_ids, dataframes, metadata_df, category_df):
    """
    Main function to save dataframes to DuckDB.

    Parameters:
    - fred_series_ids (list): List of FRED series IDs.
    - dataframes (list of pd.DataFrame): List of dataframes corresponding to each series ID.
    - metadata_df (pd.DataFrame): The metadata dataframe.
    - category_df (pd.DataFrame): The category dataframe.
    """
    conn = create_duckdb_connection()

    # Save each series dataframe to its table
    for series_id, dataframe in zip(fred_series_ids, dataframes):
        table_name = series_id.lower()
        save_dataframe_to_table(conn, table_name, dataframe)

    # Save metadata and categories dataframes
    if not metadata_df.empty:
        save_dataframe_to_table(conn, 'metadata', metadata_df)

    if not category_df.empty:
        save_dataframe_to_table(conn, 'categories', category_df)

    conn.close()




# conn = duckdb.connect('data/fred.db')
# for series_id, dataframe in zip(fred_series_ids, dataframes):
#     # Convert series ID to lowercase for the table name
#     table_name = series_id.lower()
    
#     # Register the DataFrame as a virtual table
#     conn.register(table_name + "_temp", dataframe)
    
#     # Create or replace the physical table from the virtual table
#     conn.execute(f'''
#     CREATE OR REPLACE TABLE {table_name} AS 
#     SELECT * FROM {table_name}_temp
#     ''')

#     # Optionally, unregister the virtual table to clean up
#     conn.unregister(table_name + "_temp")

# # Inserting metadata
# if not metadata_df.empty:
#     # Register the metadata DataFrame as a virtual table
#     conn.register("metadata_temp", metadata_df)

#     # Create or replace the physical table for metadata from the virtual table
#     conn.execute('''
#     CREATE OR REPLACE TABLE metadata AS 
#     SELECT * FROM metadata_temp
#     ''')

#     # Optionally, unregister the virtual table to clean up
#     conn.unregister("metadata_temp")

# # Inserting categories
# if not category_df.empty:
#     # Register the categories DataFrame as a virtual table
#     conn.register("categories_temp", category_df)

#     # Create or replace the physical table for categories from the virtual table
#     conn.execute('''
#     CREATE OR REPLACE TABLE categories AS 
#     SELECT * FROM categories_temp
#     ''')

#     # Optionally, unregister the virtual table to clean up
#     conn.unregister("categories_temp")

# conn.close()