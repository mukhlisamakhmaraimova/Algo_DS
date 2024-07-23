from random import randint

def linear_search(a, num):
    for i in range(len(a)):
        if a[i] == num:
            return f"Index: {i}"
    return f"{num} not found in list"


x = [randint(10,99) for i in range(int(input('n = ')))]

print(x)

y = int(input('Insert searched value:'))

print(linear_search(x,y))