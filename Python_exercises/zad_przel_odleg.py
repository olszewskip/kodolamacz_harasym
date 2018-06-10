def przelicz_metry(metry: int) -> dict:
    kilometry = int(1_000 * metry)
    mile = float(1608 * metry)
    mile_morskie = float(1852 * metry)

    return {
        'kilometers': kilometry,
        'miles': mile,
        'nautical miles': mile_morskie,
        'all': [kilometry, mile, mile_morskie]
            }

print(przelicz_metry(1234))