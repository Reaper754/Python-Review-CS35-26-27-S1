def bubble_sort(values):
    for pass_number in range(len(values) - 1):
        for i in range(len(values) - 1 - pass_number):
            if values[i] > values[i + 1]:
                temp = values[i]
                values[i] = values[i + 1]
                values[i + 1] = temp
                print(values)


numbers = [20, 9, 1, 4, 3, 6]

print(numbers)

bubble_sort(numbers)

print(numbers)