import math


def f(x):
    return 4 * math.exp(-0.5 * x) - x


def df(x):
    return -2 * math.exp(-0.5 * x) - 1


def sonuc(x0, itersyon):
    x = x0
    for i in range(itersyon):
        fx = f(x)
        dfx = df(x)
        x = x - fx / dfx
        print(f"Iterasyon {i + 1}: x = {x}, f(x) = {fx}")
    return x


x0 = 2
iterasyon = 4


root = sonuc(x0, iterasyon)


print(f"Bulunan kök: {root}")
