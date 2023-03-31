import json
import csv
import sys

if len(sys.argv) != 3:
    print("Usage: python json_to_csv.py <input_json_file> <output_csv_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Load the JSON data from the file
with open(input_file, "r") as json_file:
    data = json.load(json_file)

# Extract the results array from the JSON data
results = data["result"]

# Define the CSV fieldnames (column headers)
fieldnames = ["title", "description", "slug", "id"]

# Write the CSV file
with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for item in results:
        # Write each item in the results array as a row in the CSV
        writer.writerow({
            "title": item.get("title", ""),
            "description": item.get("description", ""),
            "slug": item["slug"]["current"] if item.get("slug") else "",
            "id": item.get("id", "")
        })
