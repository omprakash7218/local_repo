# with open("C:\\Users\\ompra\\OneDrive\\Desktop\\coding and stuffs\\apna_college_python\\lec7_file_input_and_output\\practice.txt", "r") as file:
#     line1 = file.readline()
#     line2 = file.readline()
#     line3 = file.readline()
#     line4 = file.readline()

# print(line1,line2,line3,line4)

# with open("demo.docx" , "a") as demo:
#     demo.write("let's go then!!")
# with open("demo.txt","w+") as xyx:
#     xyx.write("hello world")
#     xyx.seek(0)
#     print(xyx.read())
# with open("understandingfileIO.txt", "r+") as understandingbasicfileIO:
#     print(understandingbasicfileIO.read())
#     understandingbasicfileIO.seek(0)
#     understandingbasicfileIO.write("r+ mode in python , pointer is at the beginning of the file  but if we have already read the file before the pointer will be at the last of the file  ")


# Deleting a file using OS module
# import os
# os.remove("demo.txt")


# # WAP that replaces alll occurrences of is with with in the above file(new.txt)
# with open("new.txt" , "r") as nw:
#     line = nw.read()

# new_line = line.replace("is" , "with")

# with open("new.txt","w") as nw2:
#     nw2.write(new_line)
#WAF that finds out whether a file consist a certain word or not
# def checker():
#     with open("new.txt", "r") as f:
#         data = f.read()
#         if data.find("withi") != -1:
#             print("yes")
#         else:
#             print("no")


#WAF to find in which line of the file does the word "withi" occur first.
# print -1 if word not found.
# def checkforline ():
#     with open("new.txt","r") as f:
#         c = 1
#         data = f.readlines()
#         word = "with"
#         for x in data:
#             if x.find("withi646") != -1:
#                 print("line in which it was found is: " ,c)
#                 c+=1
#             c +=1
#         if x.find("withi646") == -1:
#             print(-1)

# checkforline()
# there is a another more better way that shradha mam has taught in her lec 7 


# from a file containing numbers separated by comma, print the count of even numbers.

with open("numbers.txt" , "r") as x:
    data = x.read()
    print(data)
    fdata = data.split(",")
    print(fdata)
    print(type(fdata))
    new_list =[]
    for i in fdata:
        new_list.append(int(i)) 
    for i in new_list:
        if i%2 ==0:
            print(i , "even")
        else:
            continue  
    
