#!/usr/bin/python3
"""converts a csv file to a json file"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """function reads the CSV file, converts its contents to
    a list of dictionaries, and writes the data to a JSON file"""
    try:
        with open(csv_filename, mode='r', newline='', encoding='utf-8'
                  )as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception:
        return False
