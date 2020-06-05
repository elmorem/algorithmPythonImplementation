# USE RANGE
def fizz_buzz(numbers):
    # I think that you need to use range and len here so that when it iterates through it keeps the list. if you just use for i in numbers, it will return the values as individuals
    for i in range(len(numbers)):
        breakpoint()
        num=numbers[i]
        if num %3 ==0:
            numbers[i]="fizz"
        if num %5 ==0:
            numbers[i]="buzz"
        if num %3 ==0 and num % 5==0:
            numbers[i]="fizzbuzz"

numbers=[45,22,14,65,97,72]
fizz_buzz(numbers)
numbers
#USE ENUMERATE enumerate allows you to iterate through a list AND its indicies returning a tuple
def fizz_buzz(numbers):
    # I think that you need to use range and len here so that when it iterates through it keeps the list. if you just use for i in numbers, it will return the values as individuals
    for i, num in enumerate(numbers):
        num=numbers[i]
        if num %3 ==0:
            numbers[i]="fizz"
        if num %5 ==0:
            numbers[i]="buzz"
        if num %3 ==0 and num % 5==0:
            numbers[i]="fizzbuzz"

numbers=[45,22,14,65,97,72]
fizz_buzz(numbers)
numbers