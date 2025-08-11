import csv
import json
import os

csv_file = r'C:\Users\sabri\Desktop\dataengineer-aws-f1-project\data\trusted\trusted_circuits.csv'
json_file = os.path.splitext(csv_file)[0] + '_example.json'

with open(csv_file, mode='r', encoding='utf-8') as f_csv:
    reader = csv.DictReader(f_csv)
    data = list(reader)

with open(json_file, mode='w', encoding='utf-8') as f_json:
    json.dump(data, f_json, indent=2)

print(f'Arquivo JSON de exemplo criado: {json_file}')

