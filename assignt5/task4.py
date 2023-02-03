#4. Create a login page backend to ask users to enter the username and password. Make sure to
#ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
#should not be more than 3 times.

print('Enter correct username and password combo to continue')
count=1

while count<4:
    username=input('Enter username: ')
    password=input('Enter password: ')
    if password=='Password' and username=='Nive':
        print('Access granted')
        count=5
    else:
        print('Access denied. Try again.')
        count+=1
