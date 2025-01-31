from ast import comprehension


def fizzy(number):
    numbers = [x for x in range(1,number +1)]
    fizz=[x for x in numbers if x%3==0]
    buzz=[x for x in numbers if x%5==0]
    fizzbuzz= [x for x in numbers if x%3==0 and x%5==0]
    print(f"Numbers that are divisible by 3: {fizz}. \n Numbers that are divisible by 5: {buzz}. \n Numbers that are divisible by BOTH 3 and 5: {fizzbuzz}.")
fizzy(100)
if given list of numbers just take out the numbers list comprehension

#if given a range to work through 
#  def fizz_buzz(number):
    numbers =[x for x in range(1, number+1)]
    for num in numbers:
        if num %3 ==0 and num %5 ==0:
            print(num, "fizzbuzz")
        elif num %3 == 0:
            print(num, "fizz")
        elif num % 5 ==0:
           print(num, "buzz")
        else:
            print(num)

fizz_buzz(100)
#number=100
#numbers =[x for x in range(1, number+1)]
#print(numbers)

# 
# # USE RANGE
# def fizz_buzz(numbers):
#     # I think that you need to use range and len here so that when it iterates through it keeps the list. if you just use for i in numbers, it will return the values as individuals
#     for i in range(len(numbers)):
#         num=numbers[i]
#         if num %3 ==0:
#             numbers[i]="fizz"
#         if num %5 ==0:
#             numbers[i]="buzz"
#         if num %3 ==0 and num % 5==0:
#             numbers[i]="fizzbuzz"

# numbers=[45,22,14,65,97,72]
# fizz_buzz(numbers)
# numbers
# #USE ENUMERATE enumerate allows you to iterate through a list AND its indicies returning a tuple
# def fizz_buzz(numbers):
#     # I think that you need to use range and len here so that when it iterates through it keeps the list. if you just use for i in numbers, it will return the values as individuals
#     breakpoint()
#     for i, num in enumerate(numbers):
#         num=numbers[i]
#         if num %3 ==0:
#             numbers[i]="fizz"
#         if num %5 ==0:
#             numbers[i]="buzz"
#         if num %3 ==0 and num % 5==0:
#             numbers[i]="fizzbuzz"

# fizz_buzz(numbers)

numbers = [x for x in range(0,51)]
fizz=[x for x in numbers if x%3==0]
buzz=[x for x in numbers if x%5==0]
fizzbuzz= [x for x in numbers if x%3==0 and x%5==0]
fizzy(numbers)
print(f"Numbers that are divisible by 3: {fizz}. \n Numbers that are divisible by 5: {buzz}. \n Numbers that are divisible by BOTH 3 and 5: {fizzbuzz}.")

def fizzy(number):
    numbers = [x for x in range(1,number +1)]
    fizz=[x for x in numbers if x%3==0]
    buzz=[x for x in numbers if x%5==0]
    fizzbuzz= [x for x in numbers if x%3==0 and x%5==0]
    print(f"Numbers that are divisible by 3: {fizz}. \n Numbers that are divisible by 5: {buzz}. \n Numbers that are divisible by BOTH 3 and 5: {fizzbuzz}.")