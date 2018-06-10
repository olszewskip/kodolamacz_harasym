from statistics import mean

grade_book = []
ALLOWED = (2, 3, 3.5, 4, 4.5, 5)

while True:
    try:
        grade = float(input('Wprowadź ocenę: '))
        if grade in ALLOWED:
            grade_book.append(grade)
        else:
            print('Bledna wartosc. Dopuszczalne:', ALLOWED)
            break
    except ValueError:
        break

if grade_book:
    print('Srednia: ', mean(grade_book))