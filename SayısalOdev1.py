git
def f(x):
    return x ** 3 - 2 * x ** 2 - 5



def bisection_method(a, b, iterasyon):
    if f(a) * f(b) > 0:
        print("Bu aralıkta bir kök yok.")
        return None

    for i in range(iterasyon):
        c = (a + b) / 2
        fc = f(c)

        print(f"Iterasyon {i + 1}: a = {a}, b = {b}, c = {c}, f(c) = {fc}")

        if fc == 0:
            return c
        elif f(a) * fc < 0:
            b = c
        else:
            a = c

    return (a + b) / 2



a = 2
b = 4
iterasyon = 4


root = bisection_method(a, b, iterasyon)


if root is not None:
    print(f"Bulunan kök: {root}")
else:
    print("Belirtilen iterasyon sayısına ulaşılamadı.")
