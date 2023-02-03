#3. Write a program to handle an error if the user entered a number more than four digits it should
#return “The length is too short/long !!! Please provide only four digits”

number=input("please enter a number")
if(len(number)==4):
  print("length of the number is correct")
elif(len(number)<4):
 print("the length is too short please provide only four digit") 
elif(len(number)>4): 
 print("number is too long please provide only four digit")

