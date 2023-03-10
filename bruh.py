def sumdig(n):
    if len(str(n)) == 1:
        return n
    return n % 10 + sumdig(n // 10)
