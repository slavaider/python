import csv
import pprint
import datetime


def convert2ampm(time24: str):
    return datetime.datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


if __name__ == '__main__':
    file_path = '../files/buzzdata.csv'
    print('List')
    with open(file_path, encoding='utf-8') as file:
        for line in csv.reader(file):
            print(line)
    print('Dict')
    with open(file_path, encoding='utf-8') as file:
        for line in csv.DictReader(file):
            print(line)
    print('For')
    with open(file_path) as file:
        ignore = file.readline()
        flights = {}
        for line in file:
            k, v = line.strip().split(',')
            flights[k] = v
        pprint.pprint(flights)

    dist = [i.title() for i in flights.values()]
    print(dist)
    fts = {convert2ampm(k): v.title() for k, v in flights.items()}

    result = {}
    for item in set(fts.values()):
        result[item] = [i for i in fts.keys() if item == fts[i]]
    # same as upper
    result1 = {item: [i for i in fts.keys() if item == fts[i]] for item in set(fts.values())}
    pprint.pprint(result)
