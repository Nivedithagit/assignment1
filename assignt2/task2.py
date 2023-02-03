##2. Write a program in Python to perform the following operator based task:

choice=int(input("Press 1 for addition,\n Press 2 for subtraction, \n Press 3 for division,\n Press 4 for multiplication.\n Press 5 for average)"))

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))


result = 0
if choice == 1:
    result = num1 + num2
elif choice == 2:
    result = num1 - num2
elif choice == 3:
    result = num1 * num2
elif choice == 4:
    result = num1 / num2
elif choice == 5:
    result = (num1+num2)/2
else:
    print("choose correct option")

print(num1, choice , num2, ":", result)
if result<0:
 print("negative result")
