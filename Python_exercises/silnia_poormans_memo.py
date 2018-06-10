factorial_memo_table = {0: 1}

def factorial_memo(n: int):
    if n < 0:
        return None

    if n in factorial_memo_table:
        return factorial_memo_table[n]
    else:
        result = factorial_memo(n-1) * n
        factorial_memo_table[n] = result
        return result

print(factorial_memo_table)
print(factorial_memo(6))
print(factorial_memo_table)
print(factorial_memo(5))
print(factorial_memo_table)