import json


with open('budget_app\intents.json', encoding='utf-8') as data_file:
    data = json.load(data_file)
    
print(json.dumps(data, indent=2))