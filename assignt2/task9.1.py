
n = 60
var=""
cont=input("do you want to guess type yes or no"+var)
if cont=="yes":
  guess = int(input("Enter any number: "))
  while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
      break
    print("you guessed it right!!")
elif cont=="no":
    print("game ended")
