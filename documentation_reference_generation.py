import subprocess
import time
import os
from fredapi import Fred
import certifi
from config import FRED_API_KEY

os.environ['SSL_CERT_FILE'] = certifi.where()
fred = Fred(api_key=FRED_API_KEY)

def write_metadata_markdown(target_path):
    """
    Write metadata documentation to a Markdown file.

    Parameters:
    - target_path (str): The path to the Markdown file.
    """
    metadata_markdown_content = """
    {% docs Date %}
    Represents a calendar date using the ISO 8601 format, where YYYY is the four-digit year, MM is the 
    two-digit month, and DD is the two-digit day. 
    Example: 2023-03-16.
    {% enddocs %}

    {% docs Series %}
    Represents the value of a specific economic index, identified under 'Name', at each point in time denoted 
    by 'Date'. This series reflects the quantitative measure of the economic index, capturing its fluctuations 
    and trends over time.
    {% enddocs %}

    {% docs Name %}
    The identifier or title of the economic index, which signifies the specific market, sector, or economic 
    indicator being measured and tracked over time in the series.
    {% enddocs %}

    {% docs Units %}
    The measurement standard used for the economic index, indicating the scale or type of data represented, 
    such as dollars, billions of dollars, percent, persons, etc. This specifies the quantitative terms in which 
    the index values are expressed.
    {% enddocs %}

    {% docs AdjSeas %}
    A boolean value indicating whether the Series has been adjusted for seasonality. When true, it 
    signifies that the values have already been adjusted for seasonality in the data.
    {% enddocs %}

    {% docs Freq %}
    The frequency at which the economic index is measured and reported, such as monthly, weekly, daily, etc. 
    This defines the intervals at which data points are displayed.
    {% enddocs %}

    {% docs LastUpdatedDate %}
    The date on which the series was most recently updated by the data source, reflecting the latest available 
    data point or revision in the economic index series. This ensures the timeliness and relevance of the data 
    being analyzed.
    {% enddocs %}

    {% docs Category %}
    The classification or sector to which the economic index series belongs, such as energy, food, housing, etc. 
    This categorization helps in analyzing and comparing trends within specific areas of the economy.
    {% enddocs %}

    {% docs FetchDate %}
    The date on which the data was retrieved from the data source, indicating when the information was extracted 
    or downloaded for analysis or reporting purposes.
    {% enddocs %}
    """

    with open(target_path, 'w') as file:
        file.write(metadata_markdown_content)


def write_series_markdown(target_path, fred_series_ids):
    """
    Write series documentation for each FRED series ID to a Markdown file.

    Parameters:
    - target_path (str): The path to the Markdown file.
    - fred_series_ids (list of str): List of FRED series IDs.
    """
    with open(target_path, 'a') as file:  # Append to the existing file
        for i in fred_series_ids:
            x = fred.get_series_info(i)
            seriesid = x['id']
            name = x['title']

            series_markdown_content = f"""
            {{% docs bronze_{seriesid.lower()} %}}
            {name}\n
            ...
            For more information, visit: https://fred.stlouisfed.org/series/{seriesid.lower()}.
            {{% enddocs %}}
            """
            file.write(series_markdown_content)


def write_layer_markdown(target_path):
    """
    Write documentation for silver and gold layers to a Markdown file.

    Parameters:
    - target_path (str): The path to the Markdown file.
    """
    silver_markdown_content = """
    {% docs silver_addcategory %}
    This silver layer adds the category label to this data. 
    {% enddocs %}

    {% docs silver_binaryconversion %}
    This silver layer converts the AdjSeas (Seasonally Adjusted) to a binary label for this data. 
    {% enddocs %}

    {% docs silver_restrictdate %}
    This silver layer sets parameters to only show the most recent years of data. 
    {% enddocs %}

    {% docs silver_setdatatypes %}
    This silver layer explicitly sets the datatypes for each column in this data. 
    {% enddocs %}

    {% docs silver_unionall %}
    This silver layer combines/appends all the bronze series data together. 
    {% enddocs %}
    """

    gold_markdown_content = """
    {% docs gold_freddata %}
    This is all of the data series appended/unioned together into one vertical unified table of 
    analytics and modeling. 
    {% enddocs %}
    """

    with open(target_path, 'a') as file:  # Append to the existing file
        file.write(silver_markdown_content)
        file.write(gold_markdown_content)


def write_schema_yaml(target_path, fred_series_ids):
    """
    Write the schema YAML for each FRED series ID.

    Parameters:
    - target_path (str): The path to the YAML file.
    - fred_series_ids (list of str): List of FRED series IDs.
    """
    yaml_start_content = """models:
    """

    with open(target_path, 'w') as file:
        file.write(yaml_start_content)
        for i in fred_series_ids:
            id = i.lower()
            yaml_bronze_content = f"""  - name: bronze_{id}
    description: '{{{{ doc("bronze_{id}")}}}}'
    columns: 
      - name: Date
        description: '{{{{ doc("Date")}}}}'
      - name: Series
        description: '{{{{ doc("Series")}}}}'
      - name: Name
        description: '{{{{ doc("Name")}}}}'
      - name: Units
        description: '{{{{ doc("Units")}}}}'
      - name: AdjSeas
        description: '{{{{ doc("AdjSeas")}}}}'
      - name: Freq
        description: '{{{{ doc("Freq")}}}}'
      - name: LastUpdatedDate
        description: '{{{{ doc("LastUpdatedDate")}}}}'
      - name: FetchDate
        description: '{{{{ doc("FetchDate")}}}}'
    """
            file.write(yaml_bronze_content)

# def execute_dbt_commands():
#     """
#     Execute dbt commands in sequence.
#     """
#     project_path = "/Users/jeffreyblack/Projects/FREDDataProject/fred_economic_data"
    
#     commands = [
#         f"dbt debug",
#         f"dbt compile",
#         f"dbt run",
#         f"dbt docs generate",
#         f"dbt docs serve"
#     ]
    
#     for command in commands:
#         full_command = f"cd {project_path} && {command}"
#         subprocess.run(full_command, shell=True, capture_output=False)
#         print(f"Executed command: {full_command}")



def execute_dbt_commands():
    """
    Execute dbt commands in sequence and terminate the last command after a short duration.
    """
    project_path = "/Users/jeffreyblack/Projects/FREDDataProject/fred_economic_data"
    
    commands = [
        "dbt debug",
        "dbt compile",
        "dbt run",
        "dbt docs generate"
    ]

    for command in commands:
        full_command = f"cd {project_path} && {command}"
        print(f"Executing command: {full_command}")
        subprocess.run(full_command, shell=True)
        print(f"Executed command: {full_command}")

    # Assuming 'dbt docs serve' is the command you want to automatically terminate
    serve_command = "dbt docs serve"
    full_serve_command = f"cd {project_path} && {serve_command}"
    print(f"Executing command: {full_serve_command}")
    serve_process = subprocess.Popen(full_serve_command, shell=True)
    
    # Wait for some time and then terminate the process
    try:
        time.sleep(10)  # Adjust the sleep time as needed
        serve_process.terminate()
        print(f"Terminated command: {serve_command}")
    except KeyboardInterrupt:
        print('Execution interrupted by user.')
        serve_process.terminate()

def main(fred_series_ids, target_directory):
    """
    Main function to orchestrate the documentation and schema generation.

    Parameters:
    - target_directory (str): The base directory where documentation will be stored.
    - fred_series_ids (list of str): List of FRED series IDs for which documentation is generated.
    """
    docs_path = os.path.join(target_directory, 'docs', 'docs_blocks.md')
    yaml_path = os.path.join(target_directory, 'docs', 'schema.yml')

    write_metadata_markdown(docs_path)
    write_series_markdown(docs_path, fred_series_ids)
    write_layer_markdown(docs_path)
    write_schema_yaml(yaml_path, fred_series_ids)
    execute_dbt_commands()


# with open('/Users/jeffreyblack/Projects/FREDDataProject/fred_economic_data/models/docs/docs_blocks.md', 'w') as file:
#     metadata_markdown_content = """
# {% docs Date %}
# Represents a calendar date using the ISO 8601 format, where YYYY is the four-digit year, MM is the 
# two-digit month, and DD is the two-digit day. 
# Example: 2023-03-16.
# {% enddocs %}

# {% docs Series %}
# Represents the value of a specific economic index, identified under 'Name', at each point in time denoted 
# by 'Date'. This series reflects the quantitative measure of the economic index, capturing its fluctuations 
# and trends over time.
# {% enddocs %}

# {% docs Name %}
# The identifier or title of the economic index, which signifies the specific market, sector, or economic 
# indicator being measured and tracked over time in the series.
# {% enddocs %}

# {% docs Units %}
# The measurement standard used for the economic index, indicating the scale or type of data represented, 
# such as dollars, billions of dollars, percent, persons, etc. This specifies the quantitative terms in which 
# the index values are expressed.
# {% enddocs %}

# {% docs AdjSeas %}
# A boolean value indicating whether the Series has been adjusted for seasonality. When true, it 
# signifies that the values have already been adjusted for seasonality in the data.
# {% enddocs %}

# {% docs Freq %}
# The frequency at which the economic index is measured and reported, such as monthly, weekly, daily, etc. 
# This defines the intervals at which data points are displayed.
# {% enddocs %}

# {% docs LastUpdatedDate %}
# The date on which the series was most recently updated by the data source, reflecting the latest available 
# data point or revision in the economic index series. This ensures the timeliness and relevance of the data 
# being analyzed.
# {% enddocs %}

# {% docs Category %}
# The classification or sector to which the economic index series belongs, such as energy, food, housing, etc. 
# This categorization helps in analyzing and comparing trends within specific areas of the economy.
# {% enddocs %}

# {% docs FetchDate %}
# The date on which the data was retrieved from the data source, indicating when the information was extracted 
# or downloaded for analysis or reporting purposes.
# {% enddocs %}
# """
#     file.write(metadata_markdown_content)
#     for i in fred_series_ids:
#         x = fred.get_series_info(i)
#         seriesid = x.iloc[0] if len(x) > 0 else i.upper()
#         last_fetch_date = x.iloc[1] if len(x) > 1 else 'Unknown'
#         name = x.iloc[3] if len(x) > 3 else ''
#         first_observation_date = x.iloc[4] if len(x) > 4 else 'Unknown'
#         last_observation_date = x.iloc[5] if len(x) > 5 else 'Unknown'
#         frequency = x.iloc[6] if len(x) > 6 else 'Not Available'
#         frequency_short = x.iloc[7] if len(x) > 7 else ''
#         units = x.iloc[8] if len(x) > 8 else 'Not Available'
#         units_short = x.iloc[9] if len(x) > 9 else ''
#         seas_adj = x.iloc[10] if len(x) > 10 else 'Not Available'
#         seas_adj_short = x.iloc[11] if len(x) > 11 else ''
#         last_updated = x.iloc[12] if len(x) > 12 else 'Not Available'
#         popularity = x.iloc[13] if len(x) > 13 else 'Not Available'
#         note = x.iloc[14] if len(x) > 14 else 'None'
#         id = i.lower()

#         # Double the curly braces where you want them to appear literally
#         series_markdown_content = """
# {{% docs bronze_{id} %}}
# {name}\n
# Series ID: {seriesid}
# \nFrequency: {frequency} ({frequency_short})
# \nUnits: {units} ({units_short})
# \nSeasonality: {seas_adj} ({seas_adj_short})
# \n\nLast Fetch Date: {last_fetch_date}
# \nEarliest Observation Date Available: {first_observation_date}
# \nLatest Observation Date Available: {last_observation_date}
# \nLast FRED Update Date: {last_updated}
# \nFRED Popularity Ranking: {popularity}
# \n\nNOTE: {note}
# \nFor more information, visit: https://fred.stlouisfed.org/series/{id}.
# {{% enddocs %}}
# """.format(id=id, 
#            name=name.upper(), 
#            seriesid=seriesid, 
#            frequency=frequency, 
#            frequency_short=frequency_short,
#            units=units, 
#            units_short=units_short, 
#            seas_adj=seas_adj, 
#            seas_adj_short=seas_adj_short, 
#            note=note,
#            last_fetch_date=last_fetch_date, 
#            first_observation_date=first_observation_date, 
#            last_observation_date=last_observation_date,
#            last_updated=last_updated, 
#            popularity=popularity)

#         # Write the formatted markdown content to the file
#         file.write(series_markdown_content)

#     silver_markdown_content = """
# {% docs silver_addcategory %}
# This silver layer adds the category label to this data. 
# {% enddocs %}

# {% docs silver_binaryconversion %}
# This silver layer converts the AdjSeas (Seasonally Adjusted) to a binary label for this data. 
# {% enddocs %}

# {% docs silver_restrictdate %}
# This silver layer sets parameters to only show the most recent years of data. 
# {% enddocs %}

# {% docs silver_setdatatypes %}
# This silver layer explicitly sets the datatypes for each column in this data. 
# {% enddocs %}

# {% docs silver_unionall %}
# This silver layer combines/appends all the bronze series data together. 
# {% enddocs %}
# """
#     file.write(silver_markdown_content)

#     gold_markdown_content = """
# {% docs gold_freddata %}
# This is all of the data series appended/unioned together into one vertical unified table of 
# analytics and modeling. 
# {% enddocs %}
# """
#     file.write(gold_markdown_content)

# with open('/Users/jeffreyblack/Projects/FREDDataProject/fred_economic_data/models/docs/schema.yml', 'w') as file:
#     yaml_start_content = """models:
# """
#     file.write(yaml_start_content)
#     for i in fred_series_ids:
#         x = fred.get_series_info(i)
#         name = x.iloc[3]  # Using .iloc for positional indexing
#         id = i.lower()

#         # Use the format method with named placeholders
#         yaml_bronze_content = """  - name: bronze_{id}
#     description: '{{{{ doc("bronze_{id}")}}}}'
#     columns: 
#       - name: Date
#         description: '{{{{ doc("Date")}}}}'
#       - name: Series
#         description: '{{{{ doc("Series")}}}}'
#       - name: Name
#         description: '{{{{ doc("Name")}}}}'
#       - name: Units
#         description: '{{{{ doc("Units")}}}}'
#       - name: AdjSeas
#         description: '{{{{ doc("AdjSeas")}}}}'
#       - name: Freq
#         description: '{{{{ doc("Freq")}}}}'
#       - name: LastUpdatedDate
#         description: '{{{{ doc("LastUpdatedDate")}}}}'
#       - name: FetchDate
#         description: '{{{{ doc("FetchDate")}}}}'
# """.format(id=id)  # Pass id as a named argument to format
#         file.write(yaml_bronze_content)
