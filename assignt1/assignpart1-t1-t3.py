## 1.Create three variables in a single line and assign values to them in such a manner that each one of
##them belongs to a different data type.

thisdict = {
  "a": 1,
  "b": 2.01,
  "c": "test",
}
##2. Create a variable of type complex and swap it with another variable of type integer.
x=3+5j
y=5
x, y=y, x

print("after swapping")
print(x,y)

##3.Swap two numbers using a third variable and do the same task without using any third variable.
#with third variable:
x = 20
y = 25
temp = x
x = y
y = temp

print(x,y)



#without third variable
x = 10
y = 17
 
# code to swap 
x, y = y, x
 
print ("After swapping: ")
print(x, y)

##4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
##Version.

##Python version 2:

x = raw_input("Enter a string: ") #String input
x = int(raw_input("Enter a number: ")) #integer input
x = float(raw_input("Enter a float : ")) #float input

print x,y,z
#python version 3:
x=int(input("enter a number"))
y=input("enter a string")
z=float(input("enter a float"))

print(x,y,z)

##5 Write a program to complete the task given below:
##Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
##another variable called z. Add 30 to z and store the output in variable result and print result as the
##final output.
x=input("enter a number between 1 and 10")
y=input("enter a number between 1 and 10")
z=x+y
a=z+30
print("output is" +a)

##6. Write a program to check the data type of the entered values.
##HINT: Printed output should say - The data type of the input value is : int/float/string/etc
x=input("enter a value")
print("the data type of the input value is :" type(x))

##7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
##UPPERCASE.
x=helloWorld - lowerCamel
y=Hello World - UpperCamel (Pascal Case)
z=hello_world - snake case

##8 If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
##again. Will it change the value? If Yes then Why?

##yes it will change the value because the variable is like a box contains old value when new value is assigned
##it will empty the previous and add the new one.Variable can hold anytype of variable int, string,float.

