import csv, json, yaml
import pprint

raw = '''
data1,data2,data3,data4,data5
data1,data2,data3,data4,data5
data1,data2,data3,data4,data5
data1,data2,data3,data4,data5
data1,data2,data3,data4,data5
data1,data2,data3,data4,data5
data1,data2,data3,data4,data5
data1,data2,data3,data4,data5
data1,data2,data3,data4,data5
data1,data2,data3,data4,data5
data1,data2,data3,data4,data5
'''
data = [   
    ['data1', 'data2', 'data3', 'data4', 'data5'],
    ['data1', 'data2', 'data3', 'data4', 'data5'],
    ['data1', 'data2', 'data3', 'data4', 'data5'],
    ['data1', 'data2', 'data3', 'data4', 'data5'],
    ['data1', 'data2', 'data3', 'data4', 'data5'],
    ['data1', 'data2', 'data3', 'data4', 'data5'],
    ['data1', 'data2', 'data3', 'data4', 'data5'],
    ['data1', 'data2', 'data3', 'data4', 'data5'],
    ['data1', 'data2', 'data3', 'data4', 'data5'],
    ['data1', 'data2', 'data3', 'data4', 'data5'],
    ['data1', 'data2', 'data3', 'data4', 'data5']
    ]

data_json = {   'age': 35,
    'children': [   {'age': 6, 'firstName': 'Alice'},
                    {'age': 8, 'firstName': 'Cooper'}],
    'firstName': 'Max',
    'hobbies': ['running', 'extreme', 'singing'],
    'lastName': 'Mad'}

data_yaml = {   'attr1': 'valye',
    'attr2': 123,
    'attr3': 0.89,
    'attr4': ['value1', 'value2', 'value3']}


def read_csv():
    with open('data/hw_csv.csv') as file:
        reader = csv.reader(file)
        data = []
        printer = pprint.PrettyPrinter(indent=4)
        for row in reader:
            data.append(row)
        printer.pprint(data)


def write_csv():
    with open('data/hw_csv.csv', 'w') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)


def read_json():
    with open('data/hw_json.json') as file:
        data = json.load(file)
        printer = pprint.PrettyPrinter(indent=4)
        printer.pprint(data)


def write_json():
    with open('data/hw_json.json', 'w') as file:
        json.dump(data_json, file)


def read_yaml():
    with open('data/hw_yaml.yml') as file:
        data = yaml.load(file, Loader=yaml.Loader)
        printer = pprint.PrettyPrinter(indent=4)
        printer.pprint(data)

def write_yaml():
    with open('data/hw_yaml.yml', 'w') as file:
        yaml.dump(data_yaml, file, Dumper=yaml.Dumper)



write_yaml()
read_yaml()
write_json()
read_json()
write_csv()
read_csv()