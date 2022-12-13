
def dodawanie(a, b):
    return a + b
def odejmowanie(a, b):
    return a - b
def mnozenie(a, b):
    return a * b
def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return

kalkulator = {"+": dodawanie, "-": odejmowanie, "*": mnozenie,"/": dzielenie}
u1 = float(input("wprowadz liczbe a: "))
u2 = float(input("prosze podac liczbe b: "))

dzialnie = input('podaj dzialanie ')

print(kalkulator[dzialnie](u1, u2))