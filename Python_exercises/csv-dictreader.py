import csv

FILENAME = r'./csv-iris.csv'

with open(FILENAME, encoding='utf-8') as file:
    data = csv.DictReader(
        file,
        fieldnames = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'],
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n'
    )

    next(data)
    for row in data:
        print(row)