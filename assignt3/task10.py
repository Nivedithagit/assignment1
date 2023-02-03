#10. Write a program which accepts a sequence of comma-separated numbers from console and
#generates a list and a tuple which contains every number in the form of string.
#Sample input: 34,67,55,33,12,98
#Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)
numbers = input("Type in numbers seperated only by a comma :")
lst = numbers.split(',')

number_tuple = tuple(lst)

print(number_tuple)
print(lst)
