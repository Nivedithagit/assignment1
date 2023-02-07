#8. Write a program in Python to complete the following task:
even_list = []
odd_list = []
# ask user to enter the number in between 1and50
number = int(input("Enter the number between 1 and 50"))
for number in range(1,50):
    if number%2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)
print("even list are ", even_list)
print("odd lists are ", odd_list)