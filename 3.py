def prostoye(n, div=None):
    if div is None:
        div = n - 1
    while div >= 2:
        if n % div == 0:

            return print("Число не является простым")
        else:
            return prostoye(n, div - 1)
    else:

        return print("Число является простым")


n = int(input("Введите число: "))
prostoye(n)

