
def f(x):
    return x ** 3 + 4 * x ** 2 - 10



def bisection_method(a, b, tolerans):
    if f(a) * f(b) > 0:
        print("Bu aralıkta bir kök yok.")
        return None

    iterasyon = 0

    while (b - a) / 2 > tolerans:
        c = (a + b) / 2
        fc = f(c)

        print(f"Iterasyon {iterasyon + 1}: a = {a}, b = {b}, c = {c}, f(c) = {fc}")

        if fc == 0:
            return c 
        elif f(a) * fc < 0:
            b = c
        else:
            a = c

        iterasyon += 1

    return (a + b) / 2  



a = 1
b = 2
tolerans = 1e-6


root = bisection_method(a, b, tolerans)


if root is not None:
    print(f"Bulunan kök: {root}")
else:
    print("Belirtilen toleransa ulaşılamadı.")
