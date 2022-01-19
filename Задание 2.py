posl = list(map(int, input("Введите последовательность чисел\n").split(" ")))
a = set()
for p in posl:
    if p in a:
        print('YES')
    else:
        print('NO')
        a.add(p)