n = 60
counter=1
while counter<=5:   
   guess = int(input("Enter number:"))
   if n!= guess:
       while counter!=6:
           if guess < n:
             print("Too low")
             guess = int(input("Enter number again: "))
             counter=counter+1
           elif guess > n:
             print("Too high!")
             guess = int(input("Enter number again: "))
             counter=counter+1
           else:
             print("good guess")
             break
             
   else:
      print("guessed it right")
print("sorry that was not very successful")

