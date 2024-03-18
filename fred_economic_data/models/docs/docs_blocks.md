
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
    
            {% docs bronze_dcoilwtico %}
            Crude Oil Prices: West Texas Intermediate (WTI) - Cushing, Oklahoma

            ...
            For more information, visit: https://fred.stlouisfed.org/series/dcoilwtico.
            {% enddocs %}
            
            {% docs bronze_gasregw %}
            US Regular All Formulations Gas Price

            ...
            For more information, visit: https://fred.stlouisfed.org/series/gasregw.
            {% enddocs %}
            
            {% docs bronze_dpropanembtx %}
            Propane Prices: Mont Belvieu, Texas

            ...
            For more information, visit: https://fred.stlouisfed.org/series/dpropanembtx.
            {% enddocs %}
            
            {% docs bronze_cpiaucsl %}
            Consumer Price Index for All Urban Consumers: All Items in U.S. City Average

            ...
            For more information, visit: https://fred.stlouisfed.org/series/cpiaucsl.
            {% enddocs %}
            
            {% docs bronze_ppiaco %}
            Producer Price Index by Commodity: All Commodities

            ...
            For more information, visit: https://fred.stlouisfed.org/series/ppiaco.
            {% enddocs %}
            
            {% docs bronze_pce %}
            Personal Consumption Expenditures

            ...
            For more information, visit: https://fred.stlouisfed.org/series/pce.
            {% enddocs %}
            
            {% docs bronze_cpilfesl %}
            Consumer Price Index for All Urban Consumers: All Items Less Food and Energy in U.S. City Average

            ...
            For more information, visit: https://fred.stlouisfed.org/series/cpilfesl.
            {% enddocs %}
            
            {% docs bronze_umcsent %}
            University of Michigan: Consumer Sentiment

            ...
            For more information, visit: https://fred.stlouisfed.org/series/umcsent.
            {% enddocs %}
            
            {% docs bronze_pcepilfe %}
            Personal Consumption Expenditures Excluding Food and Energy (Chain-Type Price Index)

            ...
            For more information, visit: https://fred.stlouisfed.org/series/pcepilfe.
            {% enddocs %}
            
            {% docs bronze_mich %}
            University of Michigan: Inflation Expectation

            ...
            For more information, visit: https://fred.stlouisfed.org/series/mich.
            {% enddocs %}
            
            {% docs bronze_payems %}
            All Employees, Total Nonfarm

            ...
            For more information, visit: https://fred.stlouisfed.org/series/payems.
            {% enddocs %}
            
            {% docs bronze_unrate %}
            Unemployment Rate

            ...
            For more information, visit: https://fred.stlouisfed.org/series/unrate.
            {% enddocs %}
            
            {% docs bronze_ces0500000003 %}
            Average Hourly Earnings of All Employees, Total Private

            ...
            For more information, visit: https://fred.stlouisfed.org/series/ces0500000003.
            {% enddocs %}
            
            {% docs bronze_civpart %}
            Labor Force Participation Rate

            ...
            For more information, visit: https://fred.stlouisfed.org/series/civpart.
            {% enddocs %}
            
            {% docs bronze_jtsjol %}
            Job Openings: Total Nonfarm

            ...
            For more information, visit: https://fred.stlouisfed.org/series/jtsjol.
            {% enddocs %}
            
            {% docs bronze_icsa %}
            Initial Claims

            ...
            For more information, visit: https://fred.stlouisfed.org/series/icsa.
            {% enddocs %}
            
            {% docs bronze_adpwnusnersa %}
            Total Nonfarm Private Payroll Employment

            ...
            For more information, visit: https://fred.stlouisfed.org/series/adpwnusnersa.
            {% enddocs %}
            
            {% docs bronze_u6rate %}
            Total Unemployed, Plus All Persons Marginally Attached to the Labor Force, Plus Total Employed Part Time for Economic Reasons, as a Percent of the Civilian Labor Force Plus All Persons Marginally Attached to the Labor Force (U-6)

            ...
            For more information, visit: https://fred.stlouisfed.org/series/u6rate.
            {% enddocs %}
            
            {% docs bronze_awhnonag %}
            Average Weekly Hours of Production and Nonsupervisory Employees, Total Private

            ...
            For more information, visit: https://fred.stlouisfed.org/series/awhnonag.
            {% enddocs %}
            
            {% docs bronze_fedfunds %}
            Federal Funds Effective Rate

            ...
            For more information, visit: https://fred.stlouisfed.org/series/fedfunds.
            {% enddocs %}
            
            {% docs bronze_dfedtar %}
            Federal Funds Target Rate (DISCONTINUED)

            ...
            For more information, visit: https://fred.stlouisfed.org/series/dfedtar.
            {% enddocs %}
            
            {% docs bronze_ioer %}
            Interest Rate on Excess Reserves (DISCONTINUED)

            ...
            For more information, visit: https://fred.stlouisfed.org/series/ioer.
            {% enddocs %}
            
            {% docs bronze_discount %}
            Discount Rate Changes: Historical Dates of Changes and Rates (DISCONTINUED)

            ...
            For more information, visit: https://fred.stlouisfed.org/series/discount.
            {% enddocs %}
            
            {% docs bronze_dgs10 %}
            Market Yield on U.S. Treasury Securities at 10-Year Constant Maturity, Quoted on an Investment Basis

            ...
            For more information, visit: https://fred.stlouisfed.org/series/dgs10.
            {% enddocs %}
            
            {% docs bronze_sofr %}
            Secured Overnight Financing Rate

            ...
            For more information, visit: https://fred.stlouisfed.org/series/sofr.
            {% enddocs %}
            
            {% docs bronze_prime %}
            Bank Prime Loan Rate Changes: Historical Dates of Changes and Rates

            ...
            For more information, visit: https://fred.stlouisfed.org/series/prime.
            {% enddocs %}
            
            {% docs bronze_tb3ms %}
            3-Month Treasury Bill Secondary Market Rate, Discount Basis

            ...
            For more information, visit: https://fred.stlouisfed.org/series/tb3ms.
            {% enddocs %}
            
            {% docs bronze_cpff %}
            3-Month Commercial Paper Minus Federal Funds Rate

            ...
            For more information, visit: https://fred.stlouisfed.org/series/cpff.
            {% enddocs %}
            
            {% docs bronze_csushpinsa %}
            S&P CoreLogic Case-Shiller U.S. National Home Price Index

            ...
            For more information, visit: https://fred.stlouisfed.org/series/csushpinsa.
            {% enddocs %}
            
            {% docs bronze_hsn1f %}
            New One Family Houses Sold: United States

            ...
            For more information, visit: https://fred.stlouisfed.org/series/hsn1f.
            {% enddocs %}
            
            {% docs bronze_permit %}
            New Privately-Owned Housing Units Authorized in Permit-Issuing Places: Total Units

            ...
            For more information, visit: https://fred.stlouisfed.org/series/permit.
            {% enddocs %}
            
            {% docs bronze_houst %}
            New Privately-Owned Housing Units Started: Total Units

            ...
            For more information, visit: https://fred.stlouisfed.org/series/houst.
            {% enddocs %}
            
            {% docs bronze_ussthpi %}
            All-Transactions House Price Index for the United States

            ...
            For more information, visit: https://fred.stlouisfed.org/series/ussthpi.
            {% enddocs %}
            
            {% docs bronze_exhoslusm495s %}
            Existing Home Sales

            ...
            For more information, visit: https://fred.stlouisfed.org/series/exhoslusm495s.
            {% enddocs %}
            
            {% docs bronze_mortgage30us %}
            30-Year Fixed Rate Mortgage Average in the United States

            ...
            For more information, visit: https://fred.stlouisfed.org/series/mortgage30us.
            {% enddocs %}
            
            {% docs bronze_rrvrusq156n %}
            Rental Vacancy Rate in the United States

            ...
            For more information, visit: https://fred.stlouisfed.org/series/rrvrusq156n.
            {% enddocs %}
            
            {% docs bronze_rhorusq156n %}
            Homeownership Rate in the United States

            ...
            For more information, visit: https://fred.stlouisfed.org/series/rhorusq156n.
            {% enddocs %}
            
            {% docs bronze_hosinvusm495n %}
            Existing Home Sales: Housing Inventory

            ...
            For more information, visit: https://fred.stlouisfed.org/series/hosinvusm495n.
            {% enddocs %}
            
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
    
    {% docs gold_freddata %}
    This is all of the data series appended/unioned together into one vertical unified table of 
    analytics and modeling. 
    {% enddocs %}
    