#4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
#in a hyphen-separated sequence after sorting them alphabetically.

print("Enter words separated by Hyphens : ")
newlist = [wrd for wrd in input().split("-")]
newlist.sort()
print('-'.join(newlist))
