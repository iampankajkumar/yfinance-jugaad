import requests
import pandas as pd

# Define the URL and headers
url = "https://www.nseindia.com/api/etf?csv=true&selectValFormat=crores"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
}

try:
    # Send the HTTP GET request
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an HTTPError for bad responses

    # Save the raw data to a local CSV file for debugging (optional)
    with open("raw_etf_data.csv", "w", encoding="utf-8") as raw_file:
        raw_file.write(response.text)

    # Read the CSV data into a pandas DataFrame
    from io import StringIO
    data = StringIO(response.text)  # Convert response text to a file-like object
    df = pd.read_csv(data)

    # Filter out rows containing substrings
    substrings_to_exclude = ["LIQ", "GILT"]
    df_filtered = df[~df.apply(lambda row: row.astype(str).str.contains('|'.join(substrings_to_exclude)).any(), axis=1)]

    # Save the filtered data to a new CSV file
    output_file = "filtered_etf_data.csv"
    df_filtered.to_csv(output_file, index=False)

    print(f"Filtered data saved to {output_file}")

except requests.exceptions.RequestException as e:
    print(f"HTTP Request failed: {e}")
except pd.errors.ParserError as e:
    print(f"Error parsing CSV: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
