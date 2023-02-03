#1. Write a program in Python to allow the error of syntax to be handled using exception handling.
#HINT: Use SyntaxError
try:
    if 5>1               
except SyntaxError:
    print('Hi')
try:
    eval("hello =")        
except SyntaxError:
    print("Hey")


try:
    print("x+1")
except ex
