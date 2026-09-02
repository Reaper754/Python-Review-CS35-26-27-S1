from unittest import result


#def square(number):
    #return number * number


#result=int(input("What number do you want squared: "))
#result=square(result)

#print(result)

def larger_number(a, b):
    if a>b:
        return a
    else:
        return b

a=int(input("What is your first number: "))
b=int(input("What is your second number: "))
result=larger_number(a,b)
print(result)