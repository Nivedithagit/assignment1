#6. Read doc.txt file using Python File handling concept and return only the even length string from
#the file. Consider the content of doc.txt as given below:
#Hello I am a file
#Where you need to return the data string
#Which is of even length
#Make sure you return the content in The same link as it is present.

f=open("doc.txt",'r')
try:
    readfile=f.read()
    print("content of file is: ", readfile)
    s=readfile.split("\n")
    print("\n",s)
    for i in range(0,4):
        print(len(s[i]))
        l=len(s[i])
        i=i+1
        string=s[i]
        if l%2 ==0:
            print(string)
finally:
    f.close()
