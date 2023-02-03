#3Create a function that takes a list and returns a new list with unique elements of the first list.
def unique(numbers):
    listnew = []
    for x in numbers :
        if x not in listnew:
            listnew.append(x)
    return listnew

print(unique([1, 2, 3, 1, 2,3]))
print(unique([3,4,5,5,5,5]))
