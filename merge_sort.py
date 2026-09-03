def merge(left, right):
    result = []

    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result


def merge_sort(values):
    if len(values) <= 1:
        return values

    middle = len(values) // 2

    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])

    return merge(left, right)


numbers = [12, 4, 9, 2, 15, 7, 1, 10]

numbers = merge_sort(numbers)

print(numbers)