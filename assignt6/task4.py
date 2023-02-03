#4. Write a program in Python using generators to reverse the string.
#Input String = “Consultadd Training”

def rev_string_generator(string):
    rev_str = string[::-1]
    yield rev_str
for c in rev_string_generator("Consultadd Training"):
    print(c)




'''''
def reverse_string(my_str):
    length = len(my_str)
    for i in range(length-1, -1, -1):
        yield my_str[i]

for char in reverse_string("Consultadd Training"):
    print(char)
'''''
