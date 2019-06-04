import csv, json, yaml

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


def r_w_csv():
    with open('data/example_csv.csv', 'w') as file:
        writer = csv.writer(file)
        for row in raw:
            writer.writerow(row)


r_w_csv()