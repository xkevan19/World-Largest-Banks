# Bank Data Extraction and Transformation
This Python script extracts data from a Wikipedia page listing the largest banks and performs data transformation, saving the processed data to both CSV and SQLite database formats.

## Requirements
- Python 3.x
### Libraries:
- requests
- BeautifulSoup (bs4)
- pandas
- sqlite3
## Usage
Clone the repository or download the script.
Install the required libraries if not already installed: pip install -r requirements.txt.
Run the script.

```python bank_data_extraction.py```

## Description
### Functions
log_progress(message)
Logs progress messages to a log file with timestamps.

extract(url, table_attribs)
Extracts data from the provided URL using BeautifulSoup and returns a Pandas DataFrame.

transform(df, csv_path)
Transforms the DataFrame by converting Market Cap values to GBP, EUR, and INR based on exchange rates from a provided CSV file.

load_to_csv(df, output_path)
Saves the DataFrame to a CSV file.

load_to_db(df, sql_connection, table_name)
Saves the DataFrame to an SQLite database table.

run_query(query_statement, sql_connection)
Executes a query on the SQLite database table and prints the result.

## Tasks
1. Extracting data: Scrapes data from the Wikipedia page listing the largest banks.
2. Transforming data: Converts Market Cap values to GBP, EUR, and INR.
3. Saving to CSV: Saves the processed data to a CSV file.
4. Loading to Database: Loads the processed data into an SQLite database.
5. Running Queries on Database: Executes a sample query on the database.

## Acknowledgments
Data source: [Wikipedia - List of largest banks](https://en.wikipedia.org/wiki/List_of_largest_banks)
Exchange rate data: [IBMSkillsNetwork-PY0221EN-Coursera](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv)

## Developer
- [Github](https://github.com/xkevan19)
- [LinkedIn](https://www.linkedin.com/in/kevansuchit/)

With over 2 years of industry experience, I've refined the full cycle of web application development, from planning to deployment. Proficient in SQL, web development, data analytics, UI/UX design, and product management, I deliver tailored solutions that blend technical expertise with client-centricity. I excel in pre-sale engineering and customer service, driving innovation and inspiring others in the evolving IT landscape.
