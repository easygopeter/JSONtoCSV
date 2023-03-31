import json
import csv
import sys

if len(sys.argv) < 4:
    print("Usage: python adv_json_to_csv.py <input_json_file> <output_csv_file> <field1> [<field2> ...]")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
fieldnames = sys.argv[3:]

# Load the JSON data from the file
with open(input_file, "r") as json_file:
    data = json.load(json_file)

# Extract the results array from the JSON data
results = data["result"]

# Write the CSV file
with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for item in results:
        row = {}
        for field in fieldnames:
            if "." in field:
                keys = field.split(".")
                value = item
                for key in keys:
                    value = value.get(key)
                    if value is None:
                        break
                row[field] = value
            else:
                row[field] = item.get(field, "")
        writer.writerow(row)
