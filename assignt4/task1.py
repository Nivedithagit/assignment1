#1. Write a program to reverse a string.
#Sample input: “1234abcd”
#Expected output: “dcba4321”
def reverse_string(str):
    reversed_string=str[::-1]
    print("actual string: ", str)
    print("reversed string: ", reversed_string)
    
reverse_string("1234abcd")
