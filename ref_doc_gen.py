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
Represents a calendar date using the ISO 8601 format, where YYYY is the four-digit year, MM is the two-digit month, and DD is the two-digit day. 
Example: 2023-03-16.
{% enddocs %}

{% docs Series %}
The value of a specific economic index at each point in time denoted by 'Date'. It reflects the quantitative measure of the economic index, capturing its fluctuations and trends over time.
{% enddocs %}

{% docs SeriesID %}
A unique identifier for the economic index.
{% enddocs %}

{% docs Name %}
The name or title of the economic index, identifying the specific market, sector, or economic indicator being measured and tracked over time.
{% enddocs %}

{% docs Units %}
The standard of measurement used for the economic index, indicating the scale or type of data represented, such as dollars, billions of dollars, percent, persons, etc.
{% enddocs %}

{% docs SeasAdj %}
Indicates whether the Series has been adjusted for seasonality. A true value means the data has been seasonally adjusted.
{% enddocs %}

{% docs Frequency %}
The frequency at which the economic index is measured and reported, such as monthly, weekly, daily, etc. Defines the intervals at which data points are displayed.
{% enddocs %}

{% docs LastUpdatedDate %}
The date when the series was last updated, reflecting the most current data point or revision available.
{% enddocs %}

{% docs Category %}
The classification or sector to which the economic index belongs, aiding in the analysis and comparison of trends within specific economic areas.
{% enddocs %}

{% docs FetchDate %}
The date when the data was retrieved from the source, indicating when the information was extracted or downloaded for analysis.
{% enddocs %}

{% docs RealTimeStart %}
Represents the timestamp when the data was first accessed or available from the API, marking the beginning of the real-time data availability window.
{% enddocs %}

{% docs RealTimeEnd %}
Indicates the timestamp when the data was last accessed or available from the API, marking the end of the real-time data availability window.
{% enddocs %}

{% docs FrequencyAbbr %}
The abbreviated form of the frequency at which the economic index is measured and reported, such as M for monthly, W for weekly, D for daily, etc.
{% enddocs %}

{% docs UnitsAbbr %}
The abbreviated form of the units used for the economic index, such as $ for dollars, % for percent, etc.
{% enddocs %}

{% docs SeasAdjAbbr %}
The abbreviated indicator of whether the series is seasonally adjusted, such as NSA for not seasonally adjusted or SA for seasonally adjusted.
{% enddocs %}

{% docs SeasAdjBool %}
A Boolean value indicating whether the series is seasonally adjusted, where true represents seasonally adjusted data.
{% enddocs %}

{% docs ObservationStart %}
The earliest date for which data is available in the series.
{% enddocs %}

{% docs ObservationEnd %}
The most recent date for which data is available in the series.
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
            seriesid = x.iloc[0] if len(x) > 0 else i.upper()
            last_fetch_date = x.iloc[1] if len(x) > 1 else 'Unknown'
            name = x.iloc[3] if len(x) > 3 else ''
            first_observation_date = x.iloc[4] if len(x) > 4 else 'Unknown'
            last_observation_date = x.iloc[5] if len(x) > 5 else 'Unknown'
            frequency = x.iloc[6] if len(x) > 6 else 'Not Available'
            frequency_short = x.iloc[7] if len(x) > 7 else ''
            units = x.iloc[8] if len(x) > 8 else 'Not Available'
            units_short = x.iloc[9] if len(x) > 9 else ''
            seas_adj = x.iloc[10] if len(x) > 10 else 'Not Available'
            seas_adj_short = x.iloc[11] if len(x) > 11 else ''
            last_updated = x.iloc[12] if len(x) > 12 else 'Not Available'
            popularity = x.iloc[13] if len(x) > 13 else 'Not Available'
            note = x.iloc[14] if len(x) > 14 else 'None'
            id = i.lower()
            series_markdown_content = f"""
{{% docs bronze_Fact{seriesid} %}}
{name}\n
\nFrequency: {frequency} ({frequency_short})
\nUnits: {units} ({units_short})
\nSeasonality: {seas_adj} ({seas_adj_short})
\n\nLast Fetch Date: {last_fetch_date}
\nEarliest Observation Date Available: {first_observation_date}
\nLatest Observation Date Available: {last_observation_date}
\nLast FRED Update Date: {last_updated}
\nFRED Popularity Ranking: {popularity}
\n\nNOTE: {note}
For more information, visit: https://fred.stlouisfed.org/series/{id}.
{{% enddocs %}}
            """
            file.write(series_markdown_content)
        print("Markdown File Created: {}".format(target_path))

def write_schema_yaml(target_path, fred_series_ids):
    """
    Write the schema YAML for each FRED series ID.

    Parameters:
    - target_path (str): The path to the YAML file.
    - fred_series_ids (list of str): List of FRED series IDs.
    """
    yaml_start_content = "models:\n"

    with open(target_path, 'w') as file:
        file.write(yaml_start_content)
        for i in fred_series_ids:
            yaml_bronze_content = f"""  - name: bronze_Fact{i}
    description: '{{{{ doc("bronze_Fact{i}") }}}}'
    columns:
      - name: Date
        description: '{{{{ doc("Date") }}}}'
      - name: Series
        description: '{{{{ doc("Series") }}}}'
      - name: SeriesID
        description: '{{{{ doc("SeriesID") }}}}'
      - name: FetchDate
        description: '{{{{ doc("FetchDate") }}}}'
"""
            file.write(yaml_bronze_content)
        yaml_bronze_DimCategories_content = f"""  - name: bronze_DimCategories
    description: This dimension table is the metadata that categorizes each series into binned groups determined at user input of data pipeline start. 
    columns:
      - name: SeriesID
        description: '{{{{ doc("SeriesID") }}}}'
      - name: Category
        description: '{{{{ doc("Category") }}}}'
"""
        file.write(yaml_bronze_DimCategories_content)


        yaml_bronze_DimSeries_content = f"""  - name: bronze_DimSeries
    description: This dimension table is the metadata for each series and is defined by the FRED. 
    columns:
      - name: SeriesID
        description: '{{{{ doc("SeriesID") }}}}'
      - name: RealTimeStart
        description: '{{{{ doc("RealTimeStart") }}}}'
      - name: RealTimeEnd
        description: '{{{{ doc("RealTimeEnd") }}}}'
      - name: Name
        description: '{{{{ doc("Name") }}}}'
      - name: ObservationStart
        description: '{{{{ doc("ObservationStart") }}}}'
      - name: ObservationEnd
        description: '{{{{ doc("ObservationEnd") }}}}'
      - name: Frequency
        description: '{{{{ doc("Frequency") }}}}'
      - name: FrequencyAbbr
        description: '{{{{ doc("FrequencyAbbr") }}}}'
      - name: Units
        description: '{{{{ doc("Units") }}}}'
      - name: UnitsAbbr
        description: '{{{{ doc("UnitsAbbr") }}}}'
      - name: SeasAdj
        description: '{{{{ doc("SeasAdj") }}}}'
      - name: SeasAdjAbbr
        description: '{{{{ doc("SeasAdjAbbr") }}}}'
      - name: SeasAdjBool
        description: '{{{{ doc("SeasAdjBool") }}}}'
"""
        file.write(yaml_bronze_DimSeries_content)
        

        yaml_silver_FactSeries_unionall_content = f"""  - name: silver_FactSeries_unionall
    description: This table unions all bronze Fact tables into one vertical table.
    columns:
      - name: Date
        description: '{{{{ doc("Date") }}}}'
      - name: Series
        description: '{{{{ doc("Series") }}}}'
      - name: SeriesID
        description: '{{{{ doc("SeriesID") }}}}'
      - name: FetchDate
        description: '{{{{ doc("FetchDate") }}}}'
"""
        file.write(yaml_silver_FactSeries_unionall_content)
        yaml_silver_FactSeries_setdatatypes_content = f"""  - name: silver_FactSeries_setdatatypes
    description: This table explicitly assigns datatypes to each column. 
    columns:
      - name: Date
        description: '{{{{ doc("Date") }}}}'
      - name: Series
        description: '{{{{ doc("Series") }}}}'
      - name: SeriesID
        description: '{{{{ doc("SeriesID") }}}}'
      - name: FetchDate
        description: '{{{{ doc("FetchDate") }}}}'
"""
        file.write(yaml_silver_FactSeries_setdatatypes_content)
        yaml_silver_DimSeries_setdatatypes_content = f"""  - name: silver_DimSeries_setdatatypes
    description: This table explicitly assigns datatypes to each column. 
    columns:
      - name: SeriesID
        description: '{{{{ doc("SeriesID") }}}}'
      - name: RealTimeStart
        description: '{{{{ doc("RealTimeStart") }}}}'
      - name: RealTimeEnd
        description: '{{{{ doc("RealTimeEnd") }}}}'
      - name: Name
        description: '{{{{ doc("Name") }}}}'
      - name: ObservationStart
        description: '{{{{ doc("ObservationStart") }}}}'
      - name: ObservationEnd
        description: '{{{{ doc("ObservationEnd") }}}}'
      - name: Frequency
        description: '{{{{ doc("Frequency") }}}}'
      - name: FrequencyAbbr
        description: '{{{{ doc("FrequencyAbbr") }}}}'
      - name: Units
        description: '{{{{ doc("Units") }}}}'
      - name: UnitsAbbr
        description: '{{{{ doc("UnitsAbbr") }}}}'
      - name: SeasAdj
        description: '{{{{ doc("SeasAdj") }}}}'
      - name: SeasAdjAbbr
        description: '{{{{ doc("SeasAdjAbbr") }}}}'
      - name: SeasAdjBool
        description: '{{{{ doc("SeasAdjBool") }}}}'
"""
        file.write(yaml_silver_DimSeries_setdatatypes_content)
        yaml_silver_DimSeries_binaryconversion_content = f"""  - name: silver_DimSeries_binaryconversion
    description: This table adds a column of data for Seasonality Adjustment (True/False). 
    columns:
      - name: SeriesID
        description: '{{{{ doc("SeriesID") }}}}'
      - name: RealTimeStart
        description: '{{{{ doc("RealTimeStart") }}}}'
      - name: RealTimeEnd
        description: '{{{{ doc("RealTimeEnd") }}}}'
      - name: Name
        description: '{{{{ doc("Name") }}}}'
      - name: ObservationStart
        description: '{{{{ doc("ObservationStart") }}}}'
      - name: ObservationEnd
        description: '{{{{ doc("ObservationEnd") }}}}'
      - name: Frequency
        description: '{{{{ doc("Frequency") }}}}'
      - name: FrequencyAbbr
        description: '{{{{ doc("FrequencyAbbr") }}}}'
      - name: Units
        description: '{{{{ doc("Units") }}}}'
      - name: UnitsAbbr
        description: '{{{{ doc("UnitsAbbr") }}}}'
      - name: SeasAdj
        description: '{{{{ doc("SeasAdj") }}}}'
      - name: SeasAdjAbbr
        description: '{{{{ doc("SeasAdjAbbr") }}}}'
      - name: SeasAdjBool
        description: '{{{{ doc("SeasAdjBool") }}}}'
"""
        file.write(yaml_silver_DimSeries_binaryconversion_content)
        yaml_silver_DimCategories_setdatatypes_content = f"""  - name: silver_DimCategories_setdatatypes
    description: This table explicitly assigns datatypes to each column. 
    columns:
      - name: SeriesID
        description: '{{{{ doc("SeriesID") }}}}'
      - name: Category
        description: '{{{{ doc("Category") }}}}'
"""
        file.write(yaml_silver_DimCategories_setdatatypes_content)
        
        yaml_gold_freddata_content = f"""  - name: gold_freddata
    description: This is the final table of all series and is ready for analytics ingestion. 
    columns:
      - name: Date
        description: '{{{{ doc("Date") }}}}'
      - name: Series
        description: '{{{{ doc("Series") }}}}'
      - name: Name
        description: '{{{{ doc("Name") }}}}'
      - name: Frequency
        description: '{{{{ doc("Frequency") }}}}'
      - name: Units
        description: '{{{{ doc("Units") }}}}'
      - name: SeasonallyAdjusted
        description: '{{{{ doc("SeasAdj") }}}}'
      - name: Category
        description: '{{{{ doc("Category") }}}}'
"""
        file.write(yaml_gold_freddata_content)
        print("YAML File Created: {}".format(target_path))


def execute_dbt_commands():
    """
    Execute dbt commands in sequence.
    """
    project_path = "/Users/jeffreyblack/Projects/FREDDataProject/fred_economic_data"
    
    commands = [
        "dbt debug",
        "dbt compile",
        "dbt run"
    ]

    for command in commands:
        full_command = f"cd {project_path} && {command}"
        print(f"Executing command: {full_command}")
        subprocess.run(full_command, shell=True)
        print(f"Executed command: {full_command}")

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
    write_schema_yaml(yaml_path, fred_series_ids)
    execute_dbt_commands()
