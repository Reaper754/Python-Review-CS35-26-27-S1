scores = [72, 91, 64, 85, 78, 95, 68, 88]
def calculate_average(scores):
    first = 0
    for i in range(len(scores)):
        if i == 0:
            first = scores[i]
        else:
            first = first + scores[i]

    first=first/8
    return first

def linear_search(values, target):
    for i in range(len(scores)):
        if scores[i] == target:
            return i

    return -1

print(calculate_average(scores))