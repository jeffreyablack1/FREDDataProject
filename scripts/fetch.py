import pandas as pd
from fredapi import Fred
import certifi
import os
import sys
from scripts.config import FRED_API_KEY
from datetime import datetime, timedelta, date
today_date = date.today().strftime('%Y-%m-%d') #Fetch Date

os.environ['SSL_CERT_FILE'] = certifi.where()
fred = Fred(api_key=FRED_API_KEY)


def fetch_series_data(series_id):
    """
    Fetch series data for a given series ID.
    
    Parameters:
    - series_id (str): The FRED series ID.
    
    Returns:
    - pd.Series: The time series data.
    """
    try:
        series_data = fred.get_series(series_id)
        return series_data
    except Exception as e:
        print(f"Error fetching series data for {series_id}: {e}")
        return pd.Series([])

def fetch_metadata(series_id):
    """
    Fetch metadata for a given series ID.
    
    Parameters:
    - series_id (str): The FRED series ID.
    
    Returns:
    - series: The metadata for the series.
    """
    try:
        metadata = fred.get_series_info(series_id)
        return metadata
    except Exception as e:
        print(f"Error fetching metadata for {series_id}: {e}")
        return {}

def construct_dataframe(series_data, series_id, fetch_date):
    """
    Construct a DataFrame from series data and metadata.
    
    Parameters:
    - series_data (pd.Series): The time series data.
    - series_id (str): The FRED series ID.
    - fetch_date (str): The date when the data was fetched.
    
    Returns:
    - pd.DataFrame: The constructed DataFrame with data and metadata.
    """
    try:
        df = pd.DataFrame(series_data, columns=['series_index'])
        df.reset_index(inplace=True)
        df.rename(columns={'index': 'date'}, inplace=True)
        df['seriesid'] = series_id
        df['fetch_date'] = fetch_date
        return df
    except Exception as e:
        print(f"Error constructing dataframe for {series_id}: {e}")
        return pd.DataFrame()

def fetch_fred_data(series_ids):
    """
    Fetch data and metadata for a list of FRED series IDs.
    
    Parameters:
    - series_ids (list of str): The FRED series IDs.
    - today_date (str): The date when the data is fetched.
    
    Returns:
    - tuple: A list of DataFrames with data for each series, and a DataFrame with metadata for all series.
    """
    dataframes = []
    metadata_records = []

    for series_id in series_ids:
        series_data = fetch_series_data(series_id)
        metadata = fetch_metadata(series_id)
        if not series_data.empty:
            df = construct_dataframe(series_data, series_id, today_date)
            dataframes.append(df)
        if not metadata.empty:
            metadata_records.append(metadata)

    metadata_df = pd.DataFrame(metadata_records)
    return dataframes, metadata_df

def prepare_category_data(index_categories):
    """
    Prepare category data for given index categories.
    
    Parameters:
    - index_categories (dict): Dictionary of categories and their associated series IDs.
    
    Returns:
    - pd.DataFrame: A DataFrame mapping series IDs to categories.
    """
    data = []
    for category, series_ids in index_categories.items():
        for series_id in series_ids:
            data.append((series_id, category))
    return pd.DataFrame(data, columns=['SeriesID', 'Category'])

def main(fred_series_ids, index_categories):
    """
    Main function to fetch and return data and metadata.
    
    Parameters:
    - fred_series_ids (list): List of FRED series IDs.
    - today_date (str): The current date.
    - index_categories (dict): Categories and their associated series IDs.
    
    Returns:
    - tuple: Dataframes for series data, metadata, and category mapping.
    """
    dataframes, metadata_df = fetch_fred_data(fred_series_ids)
    category_df = prepare_category_data(index_categories)
    return dataframes, metadata_df, category_df

if __name__ == "__main__":
    # Convert string arguments back to appropriate data types
    fred_series_ids = eval(sys.argv[1])
    today_date = sys.argv[2]
    index_categories = eval(sys.argv[3])



# def fetch_series_data(series_id):
#     """
#     Fetch series data for a given series ID between start_date and end_date.
    
#     Parameters:
#     - series_id (str): The FRED series ID.
    
#     Returns:
#     - pd.Series: The time series data.
#     """
#     try:
#         series_data = fred.get_series(series_id)
#         return series_data
#     except Exception as e:
#         print(f"Error fetching series data for {series_id}: {e}")
#         return pd.Series([])

# def fetch_metadata(series_id):
#     """
#     Fetch metadata for a given series ID.
    
#     Parameters:
#     - series_id (str): The FRED series ID.
    
#     Returns:
#     - dict: The metadata for the series.
#     """
#     try:
#         metadata = fred.get_series_info(series_id)
#         return metadata
#     except Exception as e:
#         print(f"Error fetching metadata for {series_id}: {e}")
#         return {}

# def construct_dataframe(series_data, series_id, fetch_date):
#     """
#     Construct a DataFrame from series data and metadata.
    
#     Parameters:
#     - series_data (pd.Series): The time series data.
#     - series_id (str): The FRED series ID.
#     - fetch_date (str): The date when the data was fetched.
    
#     Returns:
#     - pd.DataFrame: The constructed DataFrame with data and metadata.
#     """
#     try:
#         df = pd.DataFrame(series_data, columns=['series_index']).reset_index().rename(columns={'index': 'date'})
#         df['seriesid'] = series_id
#         df['fetch_date'] = fetch_date
#         return df
#     except Exception as e:
#         print(f"Error constructing dataframe for {series_id}: {e}")
#         return pd.DataFrame()

# def fetch_fred_data(series_ids, today_date):
#     """
#     Fetch data and metadata for a list of FRED series IDs.
    
#     Parameters:
#     - series_ids (list of str): The FRED series IDs.
    
#     Returns:
#     - list of pd.DataFrame: A list of DataFrames with data and metadata for each series.
#     """
#     dataframes = []
#     metadata_records = []

#     for series_id in series_ids:
#         series_data = fetch_series_data(series_id)
#         metadata = fetch_metadata(series_id)
#         if not series_data.empty:
#             df = construct_dataframe(series_data, series_id, today_date)
#             dataframes.append(df)

#         if isinstance(metadata, pd.Series) and not metadata.empty:
#             metadata_dict = metadata.to_dict()
#             metadata_records.append(metadata_dict)
#     metadata_df = pd.DataFrame(metadata_records)
#     return dataframes, metadata_df

# def prepare_category_data(index_categories):
#     data = []
#     for category, series_ids in index_categories.items():
#         for series_id in series_ids:
#             data.append((series_id, category))
#     return pd.DataFrame(data, columns=['SeriesID', 'Category'])
    


#     import duckdb
# import pandas as pd
# from fredapi import Fred
# import certifi
# import os
# from datetime import datetime, timedelta, date
# from config import FRED_API_KEY
# os.environ['SSL_CERT_FILE'] = certifi.where() #API Key security requirements
# fred = Fred(api_key=FRED_API_KEY)
# today_date = date.today().strftime('%Y-%m-%d') #Fetch Date