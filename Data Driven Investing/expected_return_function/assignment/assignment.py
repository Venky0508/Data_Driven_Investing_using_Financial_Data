import requests
import csv
from datetime import datetime

def download_weekly_stock_data(symbol, output_file, api_key):
    # Base URL for Alpha Vantage API
    base_url = "https://www.alphavantage.co/query"

    # API parameters
    params = {
        "function": "TIME_SERIES_WEEKLY",  # Weekly stock prices
        "symbol": symbol,
        "datatype": "csv",  # Request data in CSV format
        "apikey": api_key
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        # Save the full CSV data to a temporary file
        temp_file = "temp_stock_data.csv"
        with open(temp_file, "wb") as file:
            file.write(response.content)

        # Filter the data to keep only rows within the desired date range
        start_date = datetime(2000, 1, 1)
        end_date = datetime(2017, 12, 31)

        with open(temp_file, "r") as infile, open(output_file, "w", newline="") as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            # Write headers
            headers = next(reader)
            writer.writerow(headers)

            # Filter rows based on timestamp
            for row in reader:
                try:
                    date = datetime.strptime(row[0], "%Y-%m-%d")
                    if start_date <= date <= end_date:
                        writer.writerow(row)
                except ValueError:
                    print(f"Skipping invalid row: {row}")

        print(f"Data from {start_date.date()} to {end_date.date()} saved to {output_file}")
    else:
        print(f"Failed to fetch data. Error: {response.status_code}, {response.text}")


# Usage
API_KEY = "RRZY7W9Z0SJ0JWM5"  # Replace with your Alpha Vantage API key
SYMBOL = "AAPL"  # Replace with the desired stock symbol
OUTPUT_FILE = "AAPL_weekly_data.csv"  # Desired output file name

# Call the function
download_weekly_stock_data(SYMBOL, OUTPUT_FILE, API_KEY)
