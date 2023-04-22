import json
import csv

with open('data.json') as js:
    data = json.load(js)

with open('table.csv', 'w') as cs:
    writer = csv.writer(cs, delimiter=',')
    headers = [''] + [f'person {i}' for i in range(1, len(data)+1)]
    writer.writerow(headers)
    ids = ['id'] + [f'{j}' for j in data]
    writer.writerow(ids)
    names = ['name'] + [f'{k[1][0]}' for k in data.items()]
    writer.writerow(names)
    ages = ['age'] + [f'{n[1][1]}' for n in data.items()]
    writer.writerow(ages)
    phones = ['phone', '999-22-33', '876-54-32', '123-45-67', '950-56-16', '232-23-23', '879-56-34']
    writer.writerow(phones)
