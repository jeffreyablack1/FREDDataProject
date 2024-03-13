ECONOMIC DATA ENABLEMENT PROJECT
==============================

PROJECT OVERVIEW
----------------
This project demonstrates a sophisticated data engineering workflow that incorporates a medallion architecture within DuckDB, dbt-core for data transformations, Soda Core for data quality assurance, Apache Airflow for workflow orchestration, and leverages Google Sheets and Tableau Public for data visualization. The aim is to provide a comprehensive example of handling and visualizing economic data from extraction to insight.

KEY FEATURES
------------
- Medallion Architecture: Implements bronze, silver, and gold layers in DuckDB.
- Data Quality with Soda Core: Ensures data integrity throughout the pipeline.
- Automated Workflow with Apache Airflow: Orchestrates the pipeline for seamless data updates and transformations.
- Visualization: Uses Google Sheets for data storage and Tableau Public for creating dashboards.

TECHNOLOGIES USED
-----------------
- DuckDB
- dbt-core
- Soda Core
- Apache Airflow
- Google Sheets
- Tableau Public
- Docker (optional)

GETTING STARTED
---------------
Prerequisites:
- Docker (if using a containerized setup)
- Python 3.x
- Access to a REST API for economic data (e.g., FRED API)

Installation and Setup:
1. Clone the Repository:
   - git clone https://github.com/your-username/economic-data-analysis-project.git
   - cd economic-data-analysis-project

2. Environment Setup (skip if using Docker):
   - Create and activate a virtual environment:
     - Windows: fred_venv\Scripts\activate
     - Unix/MacOS: source fred_venv/bin/activate
   - Install dependencies: pip install -r requirements.txt

3. Docker Setup (if applicable):
   - Build and run the Docker container:
     - docker build -t economic-data-analysis-project .
     - docker run economic-data-analysis-project

Configuration:
- Configure DuckDB in config/db_config.json.
- Set up Apache Airflow DAGs in airflow/dags.
- Configure Soda Core checks in soda_checks/.

USAGE
-----
Detail steps to execute the pipeline, including data extraction, transformation, quality checks, and data export to Google Sheets.

CONTRIBUTING
------------
Provide guidelines for how others can contribute to the project.

LICENSE
-------
Specify the license under which the project is available.

ACKNOWLEDGMENTS
---------------
Acknowledge any individuals, organizations, or resources that were helpful in the creation of this project.
