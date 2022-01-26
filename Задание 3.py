st = int(input("Введите количество строк: "))
result = []
for s in range(st):
    lett = input("Введите строку: ").split()
    for ss in lett:
        result.append(ss)
print(len(list(set(result))))

