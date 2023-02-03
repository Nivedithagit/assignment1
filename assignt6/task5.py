#5. Write an example on decorators.
def Upperstring(ref):
    def process():
        data=ref()
        return data.upper()
    return process

def Split(ref):
    def process():
        data=ref()
        return data.split()
    return process

@Split
@Upperstring
def MyFunction():
    return "welcome to python"

print(MyFunction())
