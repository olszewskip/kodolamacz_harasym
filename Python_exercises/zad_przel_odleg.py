def przelicz_metry(metry: int) -> dict:
    kilometry = int(metry / 1_000)
    mile = float(metry / 1608)
    mile_morskie = float(metry / 1852)

    return {
        'kilometers': kilometry,
        'miles': mile,
        'nautical miles': mile_morskie,
        'all': [kilometry, mile, mile_morskie]
            }

print(przelicz_metry(1234))