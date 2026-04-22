f = open("demo.txt" , 'r')

data = f.read()
print(data)
print(type(data ))
f.close()                       # a good programmer must close the file 

##########  IMPORTANT   ##########
# WE CAN OPEN A TEXT OR BINARY FILE FROM A DIFFERENT FOLDER , WE WILL HAVE TO USE \\ OR / INSTEAD OF \ 

with open("C:\\Users\\ompra\\OneDrive\\Desktop\\coding and stuffs\\apna_college_python\\basic to advance question practice\\practices.txt" , 'r') as prac:
    print(prac.readline())
with open("sample.txt", "r") as f :
    print(f.read())

# with open("sample.txt" , "a") as f:
#     print(f.write(" \n this is going to get added at the last of the line"))   # with syntax we donot need to close the file .
     

with open("demo.txt" , "r+") as ra:    # r+ mode is used to get mouse pointer at the beginning
    print(ra.write("123"))


with open("sample.txt", "a+") as f :  #moves pointer to the end of the file you can read but it won't show anything in the terminal because the pointer is at the end 
    print(f.read())
    print(f.write("this is a great news"))



#MODULES = moddules (like a code library) is a file written by another programmer that generally has a function that we can use.


# os is a module that helps us in deleting file from our computer . IT is also used for many other works that i don't know as of now.

import os
os.remove("demo.txt")

# "r+" pointer is at the beginning of the txt file
