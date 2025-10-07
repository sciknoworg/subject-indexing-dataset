import json

# Path to your JSON file
json_file = "../subjects-taxonomy/GND-subjects.json"

# Read the JSON file
with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract all "Code" values
codes = [item.get("Code") for item in data if "Code" in item]

# Count unique codes
unique_codes = set(codes)

print(f"Total records: {len(codes)}")
print(f"Unique 'Code' values: {len(unique_codes)}")
