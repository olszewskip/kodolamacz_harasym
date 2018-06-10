def int_to_str(nums: int) -> str:
    """
    >>> int_to_str(1969)
    'one nine six nine'

    >>> int_to_str(31337)
    'three one three three seven'
    """
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
    words = [spelling[digit] for digit in digits]
    return " ".join(words)


int_to_str(973)
