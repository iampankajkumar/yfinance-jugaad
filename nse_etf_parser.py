import csv
import json

# File path (update this to your actual file location)
file_path = "etf.csv"

# Function to convert CSV to JSON
def csv_to_json(file_path):
    data = {}
    ignore_keywords = ['EBB', 'BBE', 'LIQ', 'GILT', 'SEC']
    
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            symbol = row['SYMBOL'].strip()
            
            # Skip if symbol contains any of the ignored keywords
            if any(keyword in symbol for keyword in ignore_keywords):
                continue
            
            symbol_ns = symbol + '.NS'
            underlying_asset = row['UNDERLYING ASSET'].strip()
            
            # Add to JSON structure
            data[symbol_ns] = underlying_asset
    
    return data

# Convert and print the JSON
stock_json = csv_to_json(file_path)

# Pretty print the JSON
print(json.dumps(stock_json, indent=4))

# Optional: Save to a JSON file
with open("stock_data.json", "w") as json_file:
    json.dump(stock_json, json_file, indent=4)

print("JSON file created successfully!")