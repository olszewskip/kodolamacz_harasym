from random import shuffle

DATA = [
    ("Sepal length", "Sepal width", "Petal length", "Petal width", "Species"),
    (5.1, 3.5, 1.4, 0.2, "I. setosa"),
    (4.9, 3.0, 1.4, 0.2, "I. setosa"),
    (4.7, 3.2, 1.3, 0.2, "I. setosa"),
    (4.6, 3.1, 1.5, 0.2, "I. setosa"),
    (5.0, 3.6, 1.4, 0.3, "I. setosa"),
    (5.4, 3.9, 1.7, 0.4, "I. setosa"),
    (4.6, 3.4, 1.4, 0.3, "I. setosa"),
    (7.0, 3.2, 4.7, 1.4, "I. versicolor"),
    (6.4, 3.2, 4.5, 1.5, "I. versicolor"),
    (6.9, 3.1, 4.9, 1.5, "I. versicolor"),
    (5.5, 2.3, 4.0, 1.3, "I. versicolor"),
    (6.5, 2.8, 4.6, 1.5, "I. versicolor"),
    (5.7, 2.8, 4.5, 1.3, "I. versicolor"),
    (5.7, 2.8, 4.1, 1.3, "I. versicolor"),
    (6.3, 3.3, 6.0, 2.5, "I. virginica"),
    (5.8, 2.7, 5.1, 1.9, "I. virginica"),
    (7.1, 3.0, 5.9, 2.1, "I. virginica"),
    (6.3, 2.9, 5.6, 1.8, "I. virginica"),
    (6.5, 3.0, 5.8, 2.2, "I. virginica"),
    (7.6, 3.0, 6.6, 2.1, "I. virginica"),
    (4.9, 2.5, 4.5, 1.7, "I. virginica"),
]

header = DATA[0]
data = DATA[1:]
shuffle(data)

#features = {
#    "I. setosa": 1,
#    "I. versicolor": 2,
#    "I. virginica": 3
#        }


FRACTION = 0.8
div_idx = int(len(data) * FRACTION)
learn_data, test_data = data[:div_idx], data[div_idx:]

print([raw[0] for raw in learn_data[:5]])
print(len(learn_data))
print([raw[0] for raw in test_data[:5]])
print(len(test_data))
print(len(learn_data) / len(a))
