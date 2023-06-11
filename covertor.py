from flask import   jsonify
import csv
from io import TextIOWrapper

def convert_csv_to_json(file):
    # Check if the file has a valid name and extension
    if file.filename == '':
        return jsonify({'error': 'Empty file name'})

    if not file.filename.lower().endswith(('.csv')):
        return jsonify({'error': 'Invalid file extension. Only CSV files are allowed.'})

    # Read the CSV data
    csv_file = TextIOWrapper(file, encoding='utf-8')
    csv_reader = csv.DictReader(csv_file)

    # Convert CSV data to a list of dictionaries
    data = []
    for row in csv_reader:
        data.append(row)
    # # Read the CSV file
    # with open(csv_file_path, 'r') as csv_file:
    #     csv_data = csv.DictReader(csv_file)
        
    #     # Convert CSV data to a list of dictionaries
    #     data = []
    #     for row in csv_data:
    #         data.append(row)
    # print(data)
    return data
    # Write the JSON data to a file
    # with open(json_file_path, 'w') as json_file:
    #     json.dump(data, json_file, indent=4)

# Specify the paths of the CSV and JSON files
# csv_file_path = 'sample.csv'


# # Call the function to convert CSV to JSON
# convert_csv_to_json(csv_file_path)