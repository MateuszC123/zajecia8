def potega(a, b):
    c = []
    if len(a) != len(b):
        return c

    for i in range(len(a)):
        c.append(a[i] ** b[i])
    return c
print(potega([2, 4, 6], [6, 4, 2]))
