#grid = [
    #["A", "B", "C"],
    #["D", "E", "F"],
    #["G", "H", "I"]
#]

#for row in range(len(grid)):
    #for column in range(len(grid[row])):
        #print(f"Row {row}, Column {column}: {grid[row][column]}")

#print(grid[1][2])

numbers = [
    [5, 8, 2],
    [10, 3, 7],
    [4, 9, 6]
]
result = 0

for row in range(len(numbers)):
    for column in range(len(numbers)):
        if row == 0 and column == 0:
            result = numbers[row][column]
        else:
            result = result + numbers[row][column]
            print(result)