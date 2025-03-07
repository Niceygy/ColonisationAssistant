# import json, csv

# # Define the output JSON file path
# json_file_path = '/root/code/ED/colony/server/tmp.json'
# file_path = '/root/code/ED/colony/server/tmp.tsv'
# # Read the TSV file and write to JSON
# with open(file_path, newline='') as tsvfile:
#     reader = csv.DictReader(tsvfile, delimiter='\t')
#     data = list(reader)

# with open(json_file_path, 'w') as jsonfile:
#     json.dump(data, jsonfile, indent=4)
import json

def extract_commodities(data):
    commodities = {}
    for station in data:
        station_type = station.get("Type (Listed as/under)", "Unknown")
        station_commodities = {k: v for k, v in station.items() if k not in ["Tier", "Location", "Category", "Type (Listed as/under)", "Building Type", "Facility Layouts", "Required Facility In System", "Construction Points Cost", "Construction Points Reward", "Pad", "Facility Economy", "Initial Population Increase", "Max Population Increase", "System Economy Influence", "Security", "Tech Level", "Wealth", "Standard of Living", "Development Level", "Total amount of Commodities", "# Trips with 784 cargo space (L)", "# Trips with 400 cargo space (M)"]}
        commodities[station_type] = station_commodities
    return commodities

def main():
    with open('/root/code/ED/colony/server/tmp.json', 'r') as file:
        data = json.load(file)
    commodities = extract_commodities(data)
    print(json.dumps(commodities, indent=4))

if __name__ == "__main__":
    main()