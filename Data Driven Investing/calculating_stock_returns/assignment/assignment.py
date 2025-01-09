import requests
import csv
from datetime import datetime, timedelta

def download_stock_data_csv_for_5_years(symbol, output_file, api_key):
    # Base URL for Alpha Vantage API
    base_url = "https://www.alphavantage.co/query"

    # API parameters
    params = {
        "function": "TIME_SERIES_DAILY",  # Daily adjusted stock prices
        "symbol": symbol,
        "outputsize": "full",  # Fetch full historical data
        "datatype": "csv",    # Request data in CSV format
        "apikey": api_key
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        # Save the full CSV data to a temporary file
        temp_file = "temp_stock_data.csv"
        with open(temp_file, "wb") as file:
            file.write(response.content)

        # Filter the data to keep only 5 years' worth
        five_years_ago = datetime.now() - timedelta(days=5 * 365)
        with open(temp_file, "r") as infile, open(output_file, "w", newline="") as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            # Write headers
            headers = next(reader)
            writer.writerow(headers)

            # Filter rows based on timestamp
            for row in reader:
                date = datetime.strptime(row[0], "%Y-%m-%d")
                if date >= five_years_ago:
                    writer.writerow(row)

        print(f"Data for the past 5 years saved to {output_file}")
    else:
        print(f"Failed to fetch data. Error: {response.status_code}, {response.text}")


# Usage
API_KEY = "RRZY7W9Z0SJ0JWM5"  # Replace with your Alpha Vantage API key
SYMBOL = "AAPL"  # Replace with the desired stock symbol
OUTPUT_FILE = "AAPL_stock_data.csv"  # Desired output file name

# Call the function
download_stock_data_csv_for_5_years(SYMBOL, OUTPUT_FILE, API_KEY)
