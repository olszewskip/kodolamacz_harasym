def is_even() -> (int, bool):
    liczba_str = input('Podaj liczbę z conjwyzej jedna kropka jako znakiem decymalnym: ').strip()
    if "." in liczba_str:
        liczba = round(float(liczba_str))
    elif "," in liczba_str:
        idx = liczba_str.find(",")
        liczba =round(float(liczba_str[:idx] + "." + liczba_str[idx + 1:]))
    else:
        liczba = int(liczba_str)
    return liczba, liczba % 2 == 0


print(is_even())
