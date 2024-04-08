import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
from datetime import datetime


def log_progress(message):
    """ This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('code_log.txt', 'a') as f:
        f.write(f'{timestamp} - {message}\n')


def extract(url, table_attribs):
    """ This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. """
    log_progress("Starting data extraction")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', table_attribs)
    df = pd.read_html(str(table))[0]
    log_progress("Data extraction completed")
    return df


def transform(df, csv_path):
    """ This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies"""
    log_progress("Starting data transformation")
    exchange_rates = pd.read_csv(csv_path)
    df['MC_GBP_Billion'] = df['Market cap (US$ billion)'] * exchange_rates.loc[exchange_rates['Currency'] == 'GBP', 'Rate'].values[0]
    df['MC_EUR_Billion'] = df['Market cap (US$ billion)'] * exchange_rates.loc[exchange_rates['Currency'] == 'EUR', 'Rate'].values[0]
    df['MC_INR_Billion'] = df['Market cap (US$ billion)'] * exchange_rates.loc[exchange_rates['Currency'] == 'INR', 'Rate'].values[0]
    df = df.round({'MC_GBP_Billion': 2, 'MC_EUR_Billion': 2, 'MC_INR_Billion': 2})
    log_progress("Data transformation completed")
    return df


def load_to_csv(df, output_path):
    """ This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing."""
    log_progress("Saving data to CSV")
    df.to_csv(output_path, index=False)
    log_progress("Data saved to CSV successfully")


def load_to_db(df, sql_connection, table_name):
    """ This function saves the final data frame to a database
    table with the provided name. Function returns nothing."""
    log_progress("Loading data to database")
    conn = sqlite3.connect(sql_connection)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    log_progress("Data loaded to database successfully")


def run_query(query_statement, sql_connection):
    """ This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. """
    log_progress("Executing query on database")
    conn = sqlite3.connect(sql_connection)
    result = pd.read_sql_query(query_statement, conn)
    conn.close()
    log_progress("Query execution completed")
    print(result)


# Extracting data
url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
table_attribs = {'class': 'wikitable'}
df = extract(url, table_attribs)

# Transforming data
csv_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv"
df = transform(df, csv_path)


# Task 4: Saving to CSV
output_path = "./Largest_banks_data.csv"
load_to_csv(df, output_path)

# Task 5: Loading to Database
sql_connection = "Banks.db"
table_name = "Largest_banks"
load_to_db(df, sql_connection, table_name)

# Task 6: Running Queries on Database
query_statement = "SELECT * FROM Largest_banks LIMIT 5;"
run_query(query_statement, sql_connection)
