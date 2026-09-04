#from linear_search import linear_search

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

def linear_score_search(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i

    return -1

def bubble_sort(values):
    for number in range(len(values)-1):
        for i in range(len(values)-1-number):
            if values[i] > values[i+1]:
                temp=values[i]
                values[i]=values[i+1]
                values[i+1]=temp


print("Scores:", scores)

print("Average:", calculate_average(scores))

write = int(input("Enter a score to search for: "))
search = linear_score_search(scores, write)
print(scores[search], f"was found at index {search}")

bubble_sort(scores)
print("Sorted scores:", scores)