#this is a duplicate of the read_csv.py module

import sys
import csv
from pprint import pprint


def read_csv(csv_path):
    with open(csv_path) as f:
        csv_reader = csv.reader(f)
        rows = [row for row in csv_reader]

    print('Printing Row 5 using csv.reader')
    pprint(rows[5])


def read_csv_dict(csv_path):
    with open(csv_path) as f:
        csv_reader = csv.DictReader(f)
        fieldnames = csv_reader.fieldnames
        records = [row for row in csv_reader]

    print('Printing record 4 using csv.DictReader')
    pprint(records[4])
    print('Printing fieldnames')
    pprint(fieldnames)

    for name in fieldnames:
        nice_name = name.lower().replace(' ', '_').replace('(', '').replace(')', '').replace('?', '').replace(',', '_')
        print("'{}', ".format(nice_name))


def main():
    args = sys.argv

    if len(args) < 2:
        print('usage: read_csv <input_csv>')
    else:
        read_csv(args[1])
        read_csv_dict(args[1])


if __name__ == '__main__':
    main()
