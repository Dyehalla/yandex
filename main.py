'''print('bruh')
print(' ноу факинг вей, оно воркинг') # вместо Hello World
print('фор рил мен')
'''


def partial_sums(*numbers):
    result = [0]
    Oleg = list([*numbers])
    for i in range(len(Oleg)):
        result.append(sum(Oleg[:i + 1]))
    return (result)


# partial_sums() - это лишнее, просто для проверки
