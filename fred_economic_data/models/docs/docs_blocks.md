
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

{% docs bronze_FactDCOILWTICO %}
Crude Oil Prices: West Texas Intermediate (WTI) - Cushing, Oklahoma


Frequency: Daily (D)

Units: Dollars per Barrel ($ per Barrel)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1986-01-02

Latest Observation Date Available: 2024-03-11

Last FRED Update Date: 2024-03-13 12:11:01-05

FRED Popularity Ranking: 77


NOTE: Definitions, Sources and Explanatory Notes (http://www.eia.doe.gov/dnav/pet/TblDefs/pet_pri_spt_tbldef2.asp)
For more information, visit: https://fred.stlouisfed.org/series/dcoilwtico.
{% enddocs %}
            
{% docs bronze_FactGASREGW %}
US Regular All Formulations Gas Price


Frequency: Weekly, Ending Monday (W)

Units: Dollars per Gallon ($ per Gallon)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1990-08-20

Latest Observation Date Available: 2024-03-11

Last FRED Update Date: 2024-03-11 17:14:02-05

FRED Popularity Ranking: 69


NOTE: Weighted average based on sampling of approximately 900 retail outlets, 8:00AM Monday. The price represents self-service unless only full-service is available and includes all taxes. See (http://www.eia.doe.gov/oil_gas/petroleum/data_publications/wrgp/mogas_home_page.html) for further definitions. Regular Gasoline has an antiknock index (average of the research octane rating and the motor octane number) greater than or equal to 85 and less than 88. Octane requirements may vary by altitude.
For more information, visit: https://fred.stlouisfed.org/series/gasregw.
{% enddocs %}
            
{% docs bronze_FactDPROPANEMBTX %}
Propane Prices: Mont Belvieu, Texas


Frequency: Daily (D)

Units: Dollars per Gallon ($ per Gallon)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1992-07-09

Latest Observation Date Available: 2024-03-11

Last FRED Update Date: 2024-03-13 12:11:03-05

FRED Popularity Ranking: 42


NOTE: Definitions, Sources and Explanatory Notes: http://www.eia.doe.gov/dnav/pet/TblDefs/pet_pri_spt_tbldef2.asp
For more information, visit: https://fred.stlouisfed.org/series/dpropanembtx.
{% enddocs %}
            
{% docs bronze_FactCPIAUCSL %}
Consumer Price Index for All Urban Consumers: All Items in U.S. City Average


Frequency: Monthly (M)

Units: Index 1982-1984=100 (Index 1982-1984=100)

Seasonality: Seasonally Adjusted (SA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1947-01-01

Latest Observation Date Available: 2024-02-01

Last FRED Update Date: 2024-03-12 07:42:02-05

FRED Popularity Ranking: 95


NOTE: The Consumer Price Index for All Urban Consumers: All Items (CPIAUCSL) is a price index of a basket of goods and services paid by urban consumers. Percent changes in the price index measure the inflation rate between any two time periods. The most common inflation metric is the percent change from one year ago. It can also represent the buying habits of urban consumers. This particular index includes roughly 88 percent of the total population, accounting for wage earners, clerical workers, technical workers, self-employed, short-term workers, unemployed, retirees, and those not in the labor force.  The CPIs are based on prices for food, clothing, shelter, and fuels; transportation fares; service fees (e.g., water and sewer service); and sales taxes. Prices are collected monthly from about 4,000 housing units and approximately 26,000 retail establishments across 87 urban areas. To calculate the index, price changes are averaged with weights representing their importance in the spending of the particular group. The index measures price changes (as a percent change) from a predetermined reference date. In addition to the original unadjusted index distributed, the Bureau of Labor Statistics also releases a seasonally adjusted index. The unadjusted series reflects all factors that may influence a change in prices. However, it can be very useful to look at the seasonally adjusted CPI, which removes the effects of seasonal changes, such as weather, school year, production cycles, and holidays.  The CPI can be used to recognize periods of inflation and deflation. Significant increases in the CPI within a short time frame might indicate a period of inflation, and significant decreases in CPI within a short time frame might indicate a period of deflation. However, because the CPI includes volatile food and oil prices, it might not be a reliable measure of inflationary and deflationary periods. For a more accurate detection, the core CPI (CPILFESL (https://fred.stlouisfed.org/series/CPILFESL)) is often used. When using the CPI, please note that it is not applicable to all consumers and should not be used to determine relative living costs. Additionally, the CPI is a statistical measure vulnerable to sampling error since it is based on a sample of prices and not the complete average.  For more information on the consumer price indexes, see:   Bureau of Economic Analysis. "CPI Detailed Report." (https://www.bls.gov/cpi/) 2013.   Handbook of Methods (https://www.bls.gov/opub/hom/pdf/cpihom.pdf)   Understanding the CPI: Frequently Asked Questions (https://www.bls.gov/cpi/questions-and-answers.htm)
For more information, visit: https://fred.stlouisfed.org/series/cpiaucsl.
{% enddocs %}
            
{% docs bronze_FactPPIACO %}
Producer Price Index by Commodity: All Commodities


Frequency: Monthly (M)

Units: Index 1982=100 (Index 1982=100)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1913-01-01

Latest Observation Date Available: 2024-02-01

Last FRED Update Date: 2024-03-14 07:53:02-05

FRED Popularity Ranking: 78


NOTE: None
For more information, visit: https://fred.stlouisfed.org/series/ppiaco.
{% enddocs %}
            
{% docs bronze_FactPCE %}
Personal Consumption Expenditures


Frequency: Monthly (M)

Units: Billions of Dollars (Bil. of $)

Seasonality: Seasonally Adjusted Annual Rate (SAAR)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1959-01-01

Latest Observation Date Available: 2024-01-01

Last FRED Update Date: 2024-02-29 07:44:01-06

FRED Popularity Ranking: 83


NOTE: BEA Account Code: DPCERC A Guide to the National Income and Product Accounts of the United States (http://www.bea.gov/national/pdf/nipaguid.pdf) (NIPA).
For more information, visit: https://fred.stlouisfed.org/series/pce.
{% enddocs %}
            
{% docs bronze_FactCPILFESL %}
Consumer Price Index for All Urban Consumers: All Items Less Food and Energy in U.S. City Average


Frequency: Monthly (M)

Units: Index 1982-1984=100 (Index 1982-1984=100)

Seasonality: Seasonally Adjusted (SA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1957-01-01

Latest Observation Date Available: 2024-02-01

Last FRED Update Date: 2024-03-12 07:42:02-05

FRED Popularity Ranking: 82


NOTE: The "Consumer Price Index for All Urban Consumers: All Items Less Food & Energy" is an aggregate of prices paid by urban consumers for a typical basket of goods, excluding food and energy. This measurement, known as "Core CPI," is widely used by economists because food and energy have very volatile prices. The Bureau of Labor Statistics defines and measures the official CPI, and more information can be found in the FAQ (https://www.bls.gov/cpi/questions-and-answers.htm) or in this article (https://www.bls.gov/opub/hom/pdf/cpihom.pdf).
For more information, visit: https://fred.stlouisfed.org/series/cpilfesl.
{% enddocs %}
            
{% docs bronze_FactUMCSENT %}
University of Michigan: Consumer Sentiment


Frequency: Monthly (M)

Units: Index 1966:Q1=100 (Index 1966:Q1=100)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1952-11-01

Latest Observation Date Available: 2024-01-01

Last FRED Update Date: 2024-03-01 10:01:02-06

FRED Popularity Ranking: 80


NOTE: At the request of the source, the data is delayed by 1 month. To obtain historical data prior to January 1978, please see FRED data series UMCSENT1.  This data should be cited as follows: "Surveys of Consumers, University of Michigan, University of Michigan: Consumer Sentiment © [UMCSENT], retrieved from FRED, Federal Reserve Bank of St. Louis (https://fred.stlouisfed.org/series/UMCSENT/), (Accessed on date)"  Copyright, 2016, Surveys of Consumers, University of Michigan. Reprinted with permission.
For more information, visit: https://fred.stlouisfed.org/series/umcsent.
{% enddocs %}
            
{% docs bronze_FactPCEPILFE %}
Personal Consumption Expenditures Excluding Food and Energy (Chain-Type Price Index)


Frequency: Monthly (M)

Units: Index 2017=100 (Index 2017=100)

Seasonality: Seasonally Adjusted (SA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1959-01-01

Latest Observation Date Available: 2024-01-01

Last FRED Update Date: 2024-02-29 07:44:07-06

FRED Popularity Ranking: 77


NOTE: BEA Account Code: DPCCRG  The Personal Consumption Expenditures Price Index is a measure of the prices that people living in the United States, or those buying on their behalf, pay for goods and services. The change in the PCE price index is known for capturing inflation (or deflation) across a wide range of consumer expenses and reflecting changes in consumer behavior. For example, if car prices rise, car sales may decline while bicycle sales increase.   The PCE Price Index is produced by the Bureau of Economic Analysis (BEA), which revises previously published PCE data to reflect updated information or new methodology, providing consistency across decades of data that's valuable for researchers. They also offer the series as a Chain-Type index and excluding food and energy products, as above. The PCE price index less food excluding food and energy is used primarily for macroeconomic analysis and forecasting future values of the PCE price index.  The PCE Price Index is similar to the Bureau of Labor Statistics' consumer price index for urban consumers. The two indexes, which have their own purposes and uses, are constructed differently, resulting in different inflation rates.  For more information on the PCE price index, see: U.S. Bureau of Economic Analysis, Guide to the National Income and Product Accounts of the United States (NIPA) (https://www.bea.gov/national/pdf/nipaguid.pdf)  U.S. Bureau of Economic Analysis, Personal Consumption Expenditures Price Index (https://www.bea.gov/data/personal-consumption-expenditures-price-index) U.S. Bureau of Economic Analysis, Prices & Inflation (https://www.bea.gov/resources/learning-center/what-to-know-prices-inflation) U.S. Bureau of Labor Statistics, Differences between the Consumer Price Index and the Personal Consumption Expenditure Price Index (https://www.bls.gov/opub/btn/archive/differences-between-the-consumer-price-index-and-the-personal-consumption-expenditures-price-index.pdf)
For more information, visit: https://fred.stlouisfed.org/series/pcepilfe.
{% enddocs %}
            
{% docs bronze_FactMICH %}
University of Michigan: Inflation Expectation


Frequency: Monthly (M)

Units: Percent (%)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1978-01-01

Latest Observation Date Available: 2024-01-01

Last FRED Update Date: 2024-03-01 10:01:03-06

FRED Popularity Ranking: 69


NOTE: Median expected price change next 12 months, Surveys of Consumers. The most recent value is not shown due to an agreement with the source.  This data should be cited as follows: "Surveys of Consumers, University of Michigan, University of Michigan: Inflation Expectation© [MICH], retrieved from FRED, Federal Reserve Bank of St. Louis https://fred.stlouisfed.org/series/MICH/, (Accessed on date)"  Copyright, 2016, Surveys of Consumers, University of Michigan. Reprinted with permission.
For more information, visit: https://fred.stlouisfed.org/series/mich.
{% enddocs %}
            
{% docs bronze_FactPAYEMS %}
All Employees, Total Nonfarm


Frequency: Monthly (M)

Units: Thousands of Persons (Thous. of Persons)

Seasonality: Seasonally Adjusted (SA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1939-01-01

Latest Observation Date Available: 2024-02-01

Last FRED Update Date: 2024-03-08 08:05:02-06

FRED Popularity Ranking: 83


NOTE: All Employees: Total Nonfarm, commonly known as Total Nonfarm Payroll, is a measure of the number of U.S. workers in the economy that excludes proprietors, private household employees, unpaid volunteers, farm employees, and the unincorporated self-employed. This measure accounts for approximately 80 percent of the workers who contribute to Gross Domestic Product (GDP).  This measure provides useful insights into the current economic situation because it can represent the number of jobs added or lost in an economy. Increases in employment might indicate that businesses are hiring which might also suggest that businesses are growing. Additionally, those who are newly employed have increased their personal incomes, which means (all else constant) their disposable incomes have also increased, thus fostering further economic expansion.  Generally, the U.S. labor force and levels of employment and unemployment are subject to fluctuations due to seasonal changes in weather, major holidays, and the opening and closing of schools. The Bureau of Labor Statistics (BLS) adjusts the data to offset the seasonal effects to show non-seasonal changes: for example, women's participation in the labor force; or a general decline in the number of employees, a possible indication of a downturn in the economy. To closely examine seasonal and non-seasonal changes, the BLS releases two monthly statistical measures: the seasonally adjusted All Employees: Total Nonfarm (PAYEMS) and All Employees: Total Nonfarm (PAYNSA), which is not seasonally adjusted.  The series comes from the 'Current Employment Statistics (Establishment Survey).'  The source code is: CES0000000001
For more information, visit: https://fred.stlouisfed.org/series/payems.
{% enddocs %}
            
{% docs bronze_FactUNRATE %}
Unemployment Rate


Frequency: Monthly (M)

Units: Percent (%)

Seasonality: Seasonally Adjusted (SA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1948-01-01

Latest Observation Date Available: 2024-02-01

Last FRED Update Date: 2024-03-08 08:03:02-06

FRED Popularity Ranking: 95


NOTE: The unemployment rate represents the number of unemployed as a percentage of the labor force. Labor force data are restricted to people 16 years of age and older, who currently reside in 1 of the 50 states or the District of Columbia, who do not reside in institutions (e.g., penal and mental facilities, homes for the aged), and who are not on active duty in the Armed Forces.  This rate is also defined as the U-3 measure of labor underutilization.  The series comes from the 'Current Population Survey (Household Survey)'  The source code is: LNS14000000
For more information, visit: https://fred.stlouisfed.org/series/unrate.
{% enddocs %}
            
{% docs bronze_FactCES0500000003 %}
Average Hourly Earnings of All Employees, Total Private


Frequency: Monthly (M)

Units: Dollars per Hour ($ per Hour)

Seasonality: Seasonally Adjusted (SA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 2006-03-01

Latest Observation Date Available: 2024-02-01

Last FRED Update Date: 2024-03-08 08:05:02-06

FRED Popularity Ranking: 78


NOTE: The series comes from the 'Current Employment Statistics (Establishment Survey).' The source code is: CES0500000003  The Average Hourly Earnings of All Private Employees is a measure of the average hourly earnings of all private employees on a “gross” basis, including premium pay for overtime and late-shift work. These differ from wage rates in that average hourly earnings measure the actual return to a worker for a set period of time, rather than the amount contracted for a unit of work, the wage rate. This measure excludes benefits, irregular bonuses, retroactive pay, and payroll taxes paid by the employer.   Average Hourly Earnings are collected in the Current Employment Statistics (CES) program and published by the BLS. It is provided on a monthly basis, so this data is used in part by macroeconomists as an initial economic indicator of current trends. Progressions in earnings specifically help policy makers understand some of the pressures driving inflation.  It is important to note that this series measures the average hourly earnings of the pool of workers in each period. Thus, changes in average hourly earnings can be due to either changes in the set of workers observed in a given period, or due to changes in earnings. For instance, in recessions that lead to the disproportionate increase of unemployment in lower-wage jobs, average hourly earnings can increase due to changes in the pool of workers rather than due to the widespread increase of hourly earnings at the worker-level.  For more information, see: U.S. Bureau of Labor Statistics, CES Overview (https://www.bls.gov/web/empsit/cesprog.htm) U.S. Bureau of Labor Statistics, BLS Handbook of Methods: Chapter 2. Employment, Hours, and Earnings from the Establishment Survey (https://www.bls.gov/opub/hom/pdf/ces-20110307.pdf)
For more information, visit: https://fred.stlouisfed.org/series/ces0500000003.
{% enddocs %}
            
{% docs bronze_FactCIVPART %}
Labor Force Participation Rate


Frequency: Monthly (M)

Units: Percent (%)

Seasonality: Seasonally Adjusted (SA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1948-01-01

Latest Observation Date Available: 2024-02-01

Last FRED Update Date: 2024-03-08 08:03:02-06

FRED Popularity Ranking: 84


NOTE: The series comes from the 'Current Population Survey (Household Survey)' The source code is: LNS11300000  The Labor Force Participation Rate is defined by the Current Population Survey (CPS) as “the number of people in the labor force as a percentage of the civilian noninstitutional population […] the participation rate is the percentage of the population that is either working or actively looking for work.”   The Labor Force Participation Rate is collected in the CPS and published by the BLS. It is provided on a monthly basis, so this data is used in part by macroeconomists as an initial economic indicator of current labor market trends. The labor force participation rate helps government agencies, financial markets, and researchers gauge the overall health of the economy.   Note that long-run changes in labor force participation may reflect secular economic trends that are unrelated to the overall health of the economy. For instance, demographic changes such as the aging of population can lead to a secular increase of exits from the labor force, shrinking the labor force and decreasing the labor force participation rate.   For more information, see: U.S. Bureau of Labor Statistics, CES Overview (https://www.bls.gov/web/empsit/cesprog.htm) U.S. Bureau of Labor Statistics, Concepts and Definitions (CPS) (https://www.bls.gov/cps/definitions.htm#lfpr)
For more information, visit: https://fred.stlouisfed.org/series/civpart.
{% enddocs %}
            
{% docs bronze_FactJTSJOL %}
Job Openings: Total Nonfarm


Frequency: Monthly (M)

Units: Level in Thousands (Level in Thous.)

Seasonality: Seasonally Adjusted (SA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 2000-12-01

Latest Observation Date Available: 2024-01-01

Last FRED Update Date: 2024-03-06 09:07:01-06

FRED Popularity Ranking: 77


NOTE: Total Nonfarm Job Openings are a measure of all jobs that are not filled on the last business day of the month. A job is considered open if a specific position exists and there is work available for it, the job can be started within 30 days, and there is active recruiting for the position.   Total Nonfarm Job Openings are measured by the Job Openings and Labor Turnover Survey (JOLTS) and published by the Bureau of Labor Statistics (BLS). These data are a unique economic indicator of unmet demand for labor and labor shortages. Economists, government officials, and researchers use Job Openings as a measure of tightness within job markets.   Note that the set of available job openings may decline because openings become filled, or because previous openings are removed without filling positions.  For more information, see: U.S. Bureau of Labor Statistics, Job Openings and Labor Turnover Survey Overview Page (https://www.bls.gov/jlt/jltover.htm#purpose) U.S. Bureau of Labor Statistics, Data Definitions (https://www.bls.gov/jlt/jltdef.htm#2)
For more information, visit: https://fred.stlouisfed.org/series/jtsjol.
{% enddocs %}
            
{% docs bronze_FactICSA %}
Initial Claims


Frequency: Weekly, Ending Saturday (W)

Units: Number (Number)

Seasonality: Seasonally Adjusted (SA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1967-01-07

Latest Observation Date Available: 2024-03-09

Last FRED Update Date: 2024-03-14 07:33:01-05

FRED Popularity Ranking: 81


NOTE: An initial claim is a claim filed by an unemployed individual after a separation from an employer. The claim requests a determination of basic eligibility for the Unemployment Insurance program.
For more information, visit: https://fred.stlouisfed.org/series/icsa.
{% enddocs %}
            
{% docs bronze_FactADPWNUSNERSA %}
Total Nonfarm Private Payroll Employment


Frequency: Weekly (W)

Units: Persons (Persons)

Seasonality: Seasonally Adjusted (SA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 2010-01-02

Latest Observation Date Available: 2024-01-13

Last FRED Update Date: 2024-03-06 07:26:02-06

FRED Popularity Ranking: 56


NOTE: The January 2023 report presents the scheduled annual revision of the ADP National Employment Report (NER), which updates the data series to be consistent with the annual Quarterly Census of Employment and Wages (QCEW) benchmark data through March 2022. This is a recurring process that happens every year, and is a common practice for reports of this nature.  In addition to this regular, annual update, the NER weighting methodology was revised to facilitate an easier comparison of total employment estimates between the NER and QCEW; monthly aggregates now leverage weekly seasonal adjustments rather than a separate monthly seasonal adjustment; and the national aggregate is now constructed from industry aggregates. There was also a refinement in the labeling methodology which is used to determine how various employment sources fall into a particular industry and geography definitions. These changes were applied retroactively to the 13-year history of the NER.
For more information, visit: https://fred.stlouisfed.org/series/adpwnusnersa.
{% enddocs %}
            
{% docs bronze_FactU6RATE %}
Total Unemployed, Plus All Persons Marginally Attached to the Labor Force, Plus Total Employed Part Time for Economic Reasons, as a Percent of the Civilian Labor Force Plus All Persons Marginally Attached to the Labor Force (U-6)


Frequency: Monthly (M)

Units: Percent (%)

Seasonality: Seasonally Adjusted (SA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1994-01-01

Latest Observation Date Available: 2024-02-01

Last FRED Update Date: 2024-03-08 08:03:08-06

FRED Popularity Ranking: 67


NOTE: The series comes from the 'Current Population Survey (Household Survey)'  The source code is: LNS13327709
For more information, visit: https://fred.stlouisfed.org/series/u6rate.
{% enddocs %}
            
{% docs bronze_FactAWHNONAG %}
Average Weekly Hours of Production and Nonsupervisory Employees, Total Private


Frequency: Monthly (M)

Units: Hours (Hours)

Seasonality: Seasonally Adjusted (SA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1964-01-01

Latest Observation Date Available: 2024-02-01

Last FRED Update Date: 2024-03-08 08:05:07-06

FRED Popularity Ranking: 37


NOTE: Average weekly hours relate to the average hours per worker for which pay was received and is different from standard or scheduled hours. Factors such as unpaid absenteeism, labor turnover, part-time work, and stoppages cause average weekly hours to be lower than scheduled hours of work for an establishment. Group averages further reflect changes in the workweek of component industries. Average weekly hours are the total weekly hours divided by the employees paid for those hours.  Production and related employees include working supervisors and all nonsupervisory employees (including group leaders and trainees) engaged in fabricating, processing, assembling, inspecting, receiving, storing, handling, packing, warehousing, shipping, trucking, hauling, maintenance, repair, janitorial, guard services, product development, auxiliary production for plant's own use (for example, power plant), recordkeeping, and other services closely associated with the above production operations.  Nonsupervisory employees include those individuals in private, service-providing industries who are not above the working-supervisor level. This group includes individuals such as office and clerical workers, repairers, salespersons, operators, drivers, physicians, lawyers, accountants, nurses, social workers, research aides, teachers, drafters, photographers, beauticians, musicians, restaurant workers, custodial workers, attendants, line installers and repairers, laborers, janitors, guards, and other employees at similar occupational levels whose services are closely associated with those of the employees listed.  The series comes from the 'Current Employment Statistics (Establishment Survey).'  The source code is: CES0500000007
For more information, visit: https://fred.stlouisfed.org/series/awhnonag.
{% enddocs %}
            
{% docs bronze_FactFEDFUNDS %}
Federal Funds Effective Rate


Frequency: Monthly (M)

Units: Percent (%)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1954-07-01

Latest Observation Date Available: 2024-02-01

Last FRED Update Date: 2024-03-01 15:18:02-06

FRED Popularity Ranking: 98


NOTE: Averages of daily figures.   For additional historical federal funds rate data, please see  Daily Federal Funds Rate from 1928-1954 (https://fred.stlouisfed.org/categories/33951).  The federal funds rate is the interest rate at which depository institutions trade federal funds (balances held at Federal Reserve Banks) with each other overnight. When a depository institution has surplus balances in its reserve account, it lends to other banks in need of larger balances. In simpler terms, a bank with excess cash, which is often referred to as liquidity, will lend to another bank that needs to quickly raise liquidity. (1) The rate that the borrowing institution pays to the lending institution is determined between the two banks; the weighted average rate for all of these types of negotiations is called the effective federal funds rate.(2) The effective federal funds rate is essentially determined by the market but is influenced by the Federal Reserve through open market operations to reach the federal funds rate target.(2) The Federal Open Market Committee (FOMC) meets eight times a year to determine the federal funds target rate. As previously stated, this rate influences the effective federal funds rate through open market operations or by buying and selling of government bonds (government debt).(2) More specifically, the Federal Reserve decreases liquidity by selling government bonds, thereby raising the federal funds rate because banks have less liquidity to trade with other banks. Similarly, the Federal Reserve can increase liquidity by buying government bonds, decreasing the federal funds rate because banks have excess liquidity for trade. Whether the Federal Reserve wants to buy or sell bonds depends on the state of the economy. If the FOMC believes the economy is growing too fast and inflation pressures are inconsistent with the dual mandate of the Federal Reserve, the Committee may set a higher federal funds rate target to temper economic activity. In the opposing scenario, the FOMC may set a lower federal funds rate target to spur greater economic activity. Therefore, the FOMC must observe the current state of the economy to determine the best course of monetary policy that will maximize economic growth while adhering to the dual mandate set forth by Congress. In making its monetary policy decisions, the FOMC considers a wealth of economic data, such as: trends in prices and wages, employment, consumer spending and income, business investments, and foreign exchange markets. The federal funds rate is the central interest rate in the U.S. financial market. It influences other interest rates such as the prime rate, which is the rate banks charge their customers with higher credit ratings. Additionally, the federal funds rate indirectly influences longer- term interest rates such as mortgages, loans, and savings, all of which are very important to consumer wealth and confidence.(2) References (1) Federal Reserve Bank of New York. "Federal funds." Fedpoints, August 2007. (2) Board of Governors of the Federal Reserve System. "Monetary Policy (https://www.federalreserve.gov/monetarypolicy.htm)".
For more information, visit: https://fred.stlouisfed.org/series/fedfunds.
{% enddocs %}
            
{% docs bronze_FactDFEDTAR %}
Federal Funds Target Rate (DISCONTINUED)


Frequency: Daily, 7-Day (D)

Units: Percent (%)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1982-09-27

Latest Observation Date Available: 2008-12-15

Last FRED Update Date: 2015-05-04 14:10:26-05

FRED Popularity Ranking: 59


NOTE: Data for the period prior to 1994 come from the working paper "A New Federal Funds Rate Target Series: September 27, 1982 - December 31, 1993" (Thornton, Federal Reserve Bank of St. Louis, 2005, http://research.stlouisfed.org/wp/2005/2005-032.pdf). Due to an error in the paper values from April 2, 1986 - April 20, 1986 were adjusted manually to 7.3125%. Data from 1994 to the present are derived from FOMC meeting transcripts and FOMC meeting statements, http://www.federalreserve.gov/fomc/.  Effective December 16, 2008, target rate is reported as a range. Current data at https://fred.stlouisfed.org/series/DFEDTARU and https://fred.stlouisfed.org/series/DFEDTARL
For more information, visit: https://fred.stlouisfed.org/series/dfedtar.
{% enddocs %}
            
{% docs bronze_FactIOER %}
Interest Rate on Excess Reserves (DISCONTINUED)


Frequency: Daily, 7-Day (D)

Units: Percent (%)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 2008-10-09

Latest Observation Date Available: 2021-07-28

Last FRED Update Date: 2021-07-27 15:32:02-05

FRED Popularity Ranking: 58


NOTE: Starting July 29, 2021, the interest rate on excess reserves (IOER (https://fred.stlouisfed.org/series/IOER)) and the interest rate on required reserves (IORR (https://fred.stlouisfed.org/series/IORR)) were replaced with a single rate, the interest rate on reserve balances (IORB (https://fred.stlouisfed.org/series/IORB)). See the source's announcement (https://www.federalreserve.gov/newsevents/pressreleases/bcreg20210602a.htm) for more details.  The interest rate on excess reserves (IOER rate) is determined by the Board of Governors and gives the Federal Reserve an additional tool to conduct monetary policy.  See Policy Tools (https://www.federalreserve.gov/monetarypolicy/reqresbalances.htm) for more information.
For more information, visit: https://fred.stlouisfed.org/series/ioer.
{% enddocs %}
            
{% docs bronze_FactDISCOUNT %}
Discount Rate Changes: Historical Dates of Changes and Rates (DISCONTINUED)


Frequency: Not Applicable (NA)

Units: Percent (%)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1934-02-02

Latest Observation Date Available: 2002-11-06

Last FRED Update Date: 2003-07-23 12:37:44-05

FRED Popularity Ranking: 33


NOTE: Effective Date Data before 1975 represent the date of the New York Fed discount rate change, data after 1975 represent the date of the first Federal Reserve bank discount rate change. Source: Board of Governors: Banking and Monetary Statistics, 1914-1941, and 1941-1970; the Annual Statistical Digest, 1970-1979; and the Federal Reserve Bulletin, 1978 - January 8, 2003.  Please refer to http://www.federalreserve.gov/boarddocs/press/monetary/2003/20030106/default.htm for further information on the discontinuation of this series effective January 9, 2003.
For more information, visit: https://fred.stlouisfed.org/series/discount.
{% enddocs %}
            
{% docs bronze_FactDGS10 %}
Market Yield on U.S. Treasury Securities at 10-Year Constant Maturity, Quoted on an Investment Basis


Frequency: Daily (D)

Units: Percent (%)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1962-01-02

Latest Observation Date Available: 2024-03-14

Last FRED Update Date: 2024-03-15 15:18:02-05

FRED Popularity Ranking: 92


NOTE: For further information regarding treasury constant maturity data, please refer to the H.15 Statistical Release (https://www.federalreserve.gov/releases/h15/current/h15.pdf) notes and Treasury Yield Curve Methodology (https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/yieldmethod.aspx).
For more information, visit: https://fred.stlouisfed.org/series/dgs10.
{% enddocs %}
            
{% docs bronze_FactSOFR %}
Secured Overnight Financing Rate


Frequency: Daily (D)

Units: Percent (%)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 2018-04-03

Latest Observation Date Available: 2024-03-15

Last FRED Update Date: 2024-03-18 07:02:01-05

FRED Popularity Ranking: 83


NOTE: None
For more information, visit: https://fred.stlouisfed.org/series/sofr.
{% enddocs %}
            
{% docs bronze_FactPRIME %}
Bank Prime Loan Rate Changes: Historical Dates of Changes and Rates


Frequency: Not Applicable (NA)

Units: Percent (%)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1955-08-04

Latest Observation Date Available: 2023-07-27

Last FRED Update Date: 2023-07-28 15:37:30-05

FRED Popularity Ranking: 75


NOTE: Effective Date.  Early historical data for this series include the following:  1929 range of 5.5 to 6 1930 range of 3.5 to 6 1931 range of 2.75 to 5 1932 range of 3.25 to 4 1933 range of 1.5 to 4 1934 (date uncertain) value of 1.5 1935 (date uncertain) value of 1.5 1947-12 (specific date uncertain) value of 1.75 1948-08 (specific date uncertain) value of 2 1950-09-22: 2.25 1951-01-08: 2.5 1951-10-17: 2.75 1951-12-19: 3 1953-04-27: 3.25 1954-03-17: 3  EFFECTIVE 4/16/73 DUAL PRIME RATE
For more information, visit: https://fred.stlouisfed.org/series/prime.
{% enddocs %}
            
{% docs bronze_FactTB3MS %}
3-Month Treasury Bill Secondary Market Rate, Discount Basis


Frequency: Monthly (M)

Units: Percent (%)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1934-01-01

Latest Observation Date Available: 2024-02-01

Last FRED Update Date: 2024-03-01 15:18:15-06

FRED Popularity Ranking: 79


NOTE: Averages of Business Days, Discount Basis
For more information, visit: https://fred.stlouisfed.org/series/tb3ms.
{% enddocs %}
            
{% docs bronze_FactCPFF %}
3-Month Commercial Paper Minus Federal Funds Rate


Frequency: Daily (D)

Units: Percent (%)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1997-01-02

Latest Observation Date Available: 2024-03-13

Last FRED Update Date: 2024-03-14 16:02:09-05

FRED Popularity Ranking: 41


NOTE: Series is calculated as the spread between 3-Month AA Financial Commercial Paper (RIFSPPFAAD90NB) and Effective Federal Funds Rate (https://fred.stlouisfed.org/series/DFF). Starting with the update on June 21, 2019, the Treasury bond data used in calculating interest rate spreads is obtained directly from the U.S. Treasury Department (https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield).
For more information, visit: https://fred.stlouisfed.org/series/cpff.
{% enddocs %}
            
{% docs bronze_FactCSUSHPINSA %}
S&P CoreLogic Case-Shiller U.S. National Home Price Index


Frequency: Monthly (M)

Units: Index Jan 2000=100 (Index Jan 2000=100)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1987-01-01

Latest Observation Date Available: 2023-12-01

Last FRED Update Date: 2024-02-27 08:14:02-06

FRED Popularity Ranking: 88


NOTE: For more information regarding the index, please visit Standard & Poor's (https://www.spglobal.com/spdji/en/documents/methodologies/methodology-sp-corelogic-cs-home-price-indices.pdf). There is more information about home price sales pairs in the Methodology section. Copyright, 2016, Standard & Poor's Financial Services LLC. Reprinted with permission.
For more information, visit: https://fred.stlouisfed.org/series/csushpinsa.
{% enddocs %}
            
{% docs bronze_FactHSN1F %}
New One Family Houses Sold: United States


Frequency: Monthly (M)

Units: Thousands (Thous.)

Seasonality: Seasonally Adjusted Annual Rate (SAAR)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1963-01-01

Latest Observation Date Available: 2024-01-01

Last FRED Update Date: 2024-02-26 09:01:04-06

FRED Popularity Ranking: 71


NOTE: None
For more information, visit: https://fred.stlouisfed.org/series/hsn1f.
{% enddocs %}
            
{% docs bronze_FactPERMIT %}
New Privately-Owned Housing Units Authorized in Permit-Issuing Places: Total Units


Frequency: Monthly (M)

Units: Thousands of Units (Thous. of Units)

Seasonality: Seasonally Adjusted Annual Rate (SAAR)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1960-01-01

Latest Observation Date Available: 2024-01-01

Last FRED Update Date: 2024-02-26 07:23:01-06

FRED Popularity Ranking: 71


NOTE: Starting with the 2005-02-16 release, the series reflects an increase in the universe of permit-issuing places from 19,000 to 20,000 places.
For more information, visit: https://fred.stlouisfed.org/series/permit.
{% enddocs %}
            
{% docs bronze_FactHOUST %}
New Privately-Owned Housing Units Started: Total Units


Frequency: Monthly (M)

Units: Thousands of Units (Thous. of Units)

Seasonality: Seasonally Adjusted Annual Rate (SAAR)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1959-01-01

Latest Observation Date Available: 2024-01-01

Last FRED Update Date: 2024-02-16 07:32:02-06

FRED Popularity Ranking: 79


NOTE: As provided by the Census, start occurs when excavation begins for the footings or foundation of a building. All housing units in a multifamily building are defined as being started when this excavation begins. Beginning with data for September 1992, estimates of housing starts include units in structures being totally rebuilt on an existing foundation.
For more information, visit: https://fred.stlouisfed.org/series/houst.
{% enddocs %}
            
{% docs bronze_FactUSSTHPI %}
All-Transactions House Price Index for the United States


Frequency: Quarterly (Q)

Units: Index 1980:Q1=100 (Index 1980 Q1=100)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1975-01-01

Latest Observation Date Available: 2023-10-01

Last FRED Update Date: 2024-02-27 09:02:03-06

FRED Popularity Ranking: 75


NOTE: Estimated using sales prices and appraisal data.
For more information, visit: https://fred.stlouisfed.org/series/ussthpi.
{% enddocs %}
            
{% docs bronze_FactEXHOSLUSM495S %}
Existing Home Sales


Frequency: Monthly (M)

Units: Number of Units (Number of Units)

Seasonality: Seasonally Adjusted Annual Rate (SAAR)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 2023-01-01

Latest Observation Date Available: 2024-01-01

Last FRED Update Date: 2024-02-22 13:44:01-06

FRED Popularity Ranking: 75


NOTE: The National Association of Realtors monthly housing indicators are based on a representative sample of local boards and multiple listing services. Sales volume, inventory, and price levels for existing homes are measured for the US in aggregate and by census region. Existing homes, unlike new homes, are homes that are owned and occupied before coming onto the market.  Existing-home sales measures the transaction volume of existing single-family homes, condos, and co-ops.  For more information, see Methodology: Existing-Home Sales (https://www.nar.realtor/research-and-statistics/housing-statistics/existing-home-sales/methodology).  Copyright, 2016, National Association of Realtors. Reprinted with permission.
For more information, visit: https://fred.stlouisfed.org/series/exhoslusm495s.
{% enddocs %}
            
{% docs bronze_FactMORTGAGE30US %}
30-Year Fixed Rate Mortgage Average in the United States


Frequency: Weekly, Ending Thursday (W)

Units: Percent (%)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1971-04-02

Latest Observation Date Available: 2024-03-14

Last FRED Update Date: 2024-03-14 11:06:02-05

FRED Popularity Ranking: 99


NOTE: On November 17, 2022, Freddie Mac changed the methodology of the Primary Mortgage Market Survey® (PMMS®). The weekly mortgage rate is now based on applications submitted to Freddie Mac from lenders across the country. For more information regarding Freddie Mac’s enhancement, see their research note (https://www.freddiemac.com/research/insight/20221103-freddie-macs-newly-enhanced-mortgage-rate-survey).  Data are provided “as is” by Freddie Mac®, with no warranties of any kind, express or implied, including but not limited to warranties of accuracy or implied warranties of merchantability or fitness for a particular purpose. Use of the data is at the user’s sole risk. In no event will Freddie Mac be liable for any damages arising out of or related to the data, including but not limited to direct, indirect, incidental, special, consequential, or punitive damages, whether under a contract, tort, or any other theory of liability, even if Freddie Mac is aware of the possibility of such damages.  Copyright, 2016, Freddie Mac. Reprinted with permission.
For more information, visit: https://fred.stlouisfed.org/series/mortgage30us.
{% enddocs %}
            
{% docs bronze_FactRRVRUSQ156N %}
Rental Vacancy Rate in the United States


Frequency: Quarterly (Q)

Units: Percent (%)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1956-01-01

Latest Observation Date Available: 2023-10-01

Last FRED Update Date: 2024-01-30 09:46:02-06

FRED Popularity Ranking: 67


NOTE: The rental vacancy rate is the proportion of the rental inventory that is vacant for rent.
For more information, visit: https://fred.stlouisfed.org/series/rrvrusq156n.
{% enddocs %}
            
{% docs bronze_FactRHORUSQ156N %}
Homeownership Rate in the United States


Frequency: Quarterly (Q)

Units: Percent (%)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 1965-01-01

Latest Observation Date Available: 2023-10-01

Last FRED Update Date: 2024-01-30 09:46:01-06

FRED Popularity Ranking: 71


NOTE: The homeownership rate is the proportion of households that is owner-occupied.
For more information, visit: https://fred.stlouisfed.org/series/rhorusq156n.
{% enddocs %}
            
{% docs bronze_FactHOSINVUSM495N %}
Existing Home Sales: Housing Inventory


Frequency: Monthly (M)

Units: Number of Units (Number of Units)

Seasonality: Not Seasonally Adjusted (NSA)


Last Fetch Date: 2024-03-18

Earliest Observation Date Available: 2023-01-01

Latest Observation Date Available: 2024-01-01

Last FRED Update Date: 2024-02-22 13:44:03-06

FRED Popularity Ranking: 69


NOTE: The National Association of Realtors monthly housing indicators are based on a representative sample of local boards and multiple listing services. Sales volume, inventory, and price levels for existing homes are measured for the US in aggregate and by census region. Existing homes, unlike new homes, are homes that are owned and occupied before coming onto the market.  Inventory indicates the number of properties marked as "active" on the market or those pending sales. When a seller lists a property, it becomes counted as inventory.  For more information, see Methodology: Existing-Home Sales (https://www.nar.realtor/research-and-statistics/housing-statistics/existing-home-sales/methodology).  Copyright, 2016, National Association of Realtors. Reprinted with permission.
For more information, visit: https://fred.stlouisfed.org/series/hosinvusm495n.
{% enddocs %}
            