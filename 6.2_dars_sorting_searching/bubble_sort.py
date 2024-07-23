from random import randint

def bubble_sort(a):
    steps = 0
    for i in range(len(a)):
       for j in range(i+1, len(a)):
           steps += 1
           # if a[i] > a[j]:
           if a[i] < a[j]:
               a[i], a[j] = a[j],a[i]
    print(f"{steps=}")
    return a



x = [randint(10,99) for i in range(int(input('n = ')))]

print(x)

print(bubble_sort(x))