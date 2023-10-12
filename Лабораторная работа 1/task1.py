numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_None = numbers.index(None)

sum_of_numbers = sum(numbers[:index_None]) + sum(numbers[index_None+1:])
count_of_numbers = len(numbers)
mean = sum_of_numbers / count_of_numbers

numbers[index_None] = mean
print('Измененный список:', numbers)
# TODO заменить значение пропущенного элемента средним арифметическим
