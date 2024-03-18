ECONOMIC DATA ENABLEMENT PROJECT
================================

PROJECT OVERVIEW
----------------
This project is in the development phase, focusing on establishing a robust data engineering workflow. Currently, it primarily involves dbt-core for data transformations within a medallion architecture framework. The ultimate goal is to create a comprehensive pipeline handling economic data from extraction to insight, incorporating data quality assurance, workflow orchestration, and data visualization.

CURRENT STATUS
--------------
- DBT Tasks: Completed initial setup and configuration of dbt-core for data transformation tasks.
- The subsequent phases of the project, including the implementation of Soda Core for data quality, Apache Airflow for workflow orchestration, and data visualization, are in the planning and design stages.

TECHNOLOGIES USED
-----------------
- DuckDB
- dbt-core (Currently in use)
- Soda-core (Planned)
- Apache Spark (Planned)
- Apache Airflow (Planned)
- Data Visualization (Tableau) (Planned)
- Docker (Planned for containerized setup)

GETTING STARTED
---------------
Prerequisites:
- Python 3.9.0
- Access to a REST API for economic data (e.g., FRED API)
- See requirements.txt

Installation and Setup:
1. Clone the Repository:
   - git clone https://github.com/jeffreyablack1/FREDDataProject.git
   - cd FREDDataProject

2. Environment Setup:
   - Create and activate a virtual environment:
     - Windows: fred_venv\Scripts\activate
     - Unix/MacOS: source fred_venv/bin/activate
   - Install dependencies: pip install -r requirements.txt

USAGE
-----
Currently, the project supports data transformation tasks using dbt-core. Detailed steps for these tasks are provided in the dbt section of the project documentation.

CONTRIBUTING
------------
Contribution guidelines will be developed as the project matures.

LICENSE
-------
MIT License

Copyright (c) 2024 JB

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

ACKNOWLEDGMENTS
---------------
Acknowledgments will be added to recognize contributions and resources that have been instrumental in the project development.

