import os
from flask import jsonify
import csv
import io
from io import TextIOWrapper , StringIO

import pandas as pd

def clean_csv(file_path):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)
    
    # Remove null values
    df = df.dropna()

    # Trim leading and trailing white spaces from all columns
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Save the cleaned DataFrame to a new CSV file
    csv_data = df.to_csv(index=False).encode()

# Create IO[bytes] object from in-memory CSV data
    io_bytes = io.BytesIO(csv_data)
    return io_bytes
   



def convert_csv_to_json(file):
    # Check if the file has a valid name and extension
    if file.filename == '':
        return jsonify({'error': 'Empty file name'})

    if not file.filename.lower().endswith(('.csv')):
        return jsonify({'error': 'Invalid file extension. Only CSV files are allowed.'})
    
    textdata = clean_csv(file)
 
    # Read the CSV data
    csv_file = TextIOWrapper(textdata, encoding='utf-8')
    # csv_file = textdata;
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
    # os.remove("output.csv")
    return data
    # Write the JSON data to a file
    # with open(json_file_path, 'w') as json_file:
    #     json.dump(data, json_file, indent=4)
# Specify the paths of the CSV and JSON files
# csv_file_path = 'sample.csv'


# # Call the function to convert CSV to JSON
# convert_csv_to_json(csv_file_path)