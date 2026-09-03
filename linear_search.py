def linear_search(values, target):
    for i in range(len(values)):
        if values[i] == target:
            print(f"At index {i} is ", names[i])
            return i
        elif values[i] != target:
            print(f"At index {i} is ", names[i])

    return -1

names = ["Alex", "Jordan", "Sam", "Taylor", "Morgan"]
written = input("Enter a name: ")
result = linear_search(names, written)


if result == -1:
    print(f"{written} was not found")
else:
    print(names[result], f"found at index {result}")