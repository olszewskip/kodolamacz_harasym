import csv

FILENAME = r'csv-dictwriter-output'

DATABASE = [
    {'last_name': 'Jiménez'},
    {'first_name': 'Max', 'last_name': 'Peck'},
    {'first_name': 'Ivan'},
    {'first_name': 'Max', 'last_name': 'Peck', 'born': 1961},
    {'first_name': 'Jose', 'born': 1961, 'first_step': 1969},
]

fieldnames = set()
for dict_ in DATABASE:
    fieldnames.update(set(dict_.keys()))
fieldnames = list(fieldnames)


with open(FILENAME, mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(
        file,
        fieldnames = fieldnames,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n'
    )

    writer.writeheader()

    for row in DATABASE:
        writer.writerow(row)
