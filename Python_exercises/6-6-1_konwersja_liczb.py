def spell_nums(nums):
    spelling = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }
    digits = [int(d) for d in str(nums)]
    print(" ".join([spelling[digit] for digit in digits]))

spell_nums(973)