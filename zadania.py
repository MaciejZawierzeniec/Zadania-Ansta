from decimal import Decimal


def zadanie1(string1, string2):
    for postal_code in range(int(string1[:2] + string1[3:]) + 1, int(string2[:2] + string2[3:])):
        print(str(postal_code)[:2] + "-" + str(postal_code)[2:])


def zadanie2(numbers, n):
    print(list(set(range(1, n + 1)) - set(numbers)))


def zadanie3(n, m, jmp):
    for i in range(0, int((m-n)/jmp) + 1):
        print(Decimal(n + i*jmp))


zadanie1("79-900", "80-155")
zadanie2([2, 3, 7, 4, 9], 10)
zadanie3(2, 5.5, 0.5)
