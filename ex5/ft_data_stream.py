#!/usr/bin/python3

def count_to(n):
    count = 1
    while count <= n:
        yield count
        count+=1

numbers = int(input("Enter a Number: "))

for n in count_to(numbers):
    print(n)