#5. Write a program that accepts a sequence of lines as input and prints the lines after making all
#characters in the sentence capitalized.

lines = []
while True:
    s = input("Enter Lines :")
    if s:
        lines.append(s.upper())
    elif s=='':
        print("input is blank so ending the input")
        break
        
for sentence in lines:
    print(sentence)
	