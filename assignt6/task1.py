#1. Write a program in Python to find out the character in a string which is uppercase using list
#comprehension.

# initializing string
str = input("enter the string ")
lst =[i for i in str if i.isupper()]          ##list comprehension
print(lst)
