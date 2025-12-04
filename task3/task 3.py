import sys
import json

path_tests, path_values = sys.argv[1:]

with open(path_tests, 'r') as f:
    string = f.read()
    tests = json.loads(string)

with open(path_values, 'r') as f:
    string = f.read()
    values = json.loads(string)

def mark_level(tests, values):
    for value in values['values']:
        Id = value['id']
        Value = value['value']
        for i in range(len(tests)):
            if tests[i]['id'] == Id:
                tests[i]['value'] = Value
                break
            if 'values' in tests[i].keys():
                tests[i]['values'] = mark_level(tests[i]['values'], values)
    return tests



with open('report.json', 'w+') as f:
    json.dump(mark_level(tests['tests'], values), f, indent=1)
    
# print(tests['tests'])
# print(values['values'])

