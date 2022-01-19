list1 = list(map(int, input("Введите первый список чисел\n").split(" ")))
list2 = list(map(int, input("Введите второй список чисел\n").split(" ")))
print(set(list1) & set(list2))