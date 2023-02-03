#10. Write a program which uses filter() to make a list whose elements are even numbers between 1
#and 20 (both included)

def check_even(numbers):
    if numbers % 2 == 0:
          return True  

    return False
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20]

even = filter(check_even, numbers)
even_numbers = list(even)

print(even_numbers)

