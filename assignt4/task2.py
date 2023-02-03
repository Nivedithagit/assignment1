#2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
#letters.
def upper_lower(string):
    lowercase_count = 0
    uppercase_count = 0

    for letter in string:
        if letter.isupper():
            uppercase_count += 1
        elif letter.islower():
            lowercase_count += 1

    print("no of uppercasecount:\n"+str(uppercase_count))
    print("no of lowercasecount\n"+str(lowercase_count))
  

upper_lower("abcSdefPghijQkl")
