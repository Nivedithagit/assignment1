#15. Write a program in Python to multiply the elements of a list by itself using a traditional function
#and pass the function to map() to complete the operation.
def multiply(n):
    return n*n
my_list = [2,3,4,5,6,7,8,9]
updated_list = map(multiply, my_list)
print(updated_list)
print(list(updated_list))
