numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers_1 = numbers[0:4]
numbers_2 = numbers[5:]
sum_n = sum(numbers_1 + numbers_2)
coll = len(numbers)
sr = sum_n/coll
numbers[4] = sr
# TODO заменить значение пропущенного элемента средним арифметическим
print("Измененный список:", numbers)