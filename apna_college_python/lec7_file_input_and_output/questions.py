# #create a new file "practice.txt" using python. Add the following data in the same manner :
# with open("practice.txt" , "w") as prac:
#     print(prac.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java."))



# prac = open("practice.txt" , 'r')
# data = prac.read()
# print(data)
# prac.close()
# # -----------------------------------------------------------------
# # waf that replace all occurances of "java" with "python" in above file.

# with open("practice.txt" , 'r') as f:
#     data = f.read()

# new_data = data.replace("Java" , "Python")    # STRING is immutable and replace method creates an entirely different string

# with open("practice.txt" , 'w') as f:
#     f.write(new_data)


# # --------------------------------------
# # Search if the word "learning" exists in the ile or not.

# # with open("practice.txt" , "r") as ds:
# #     data1 = ds.read()
# #     if (data1.find("learning") != -1):
# #         print("found")
# #     else:
# #         print("not found")


# ## if we want to make it into a function without parameter we can do that too
# ## we can call this function anytime in the code

# def check_for_word():
#     with open("practice.txt" ,  "r") as tryd:
#         if (tryd.read().find("learning") !=  -1):
#             print("found")
#         else:
#             print("not found")

    
# check_for_word()

# -----------------------------------------------------------------
# waf to find in which line of the file does the word "learning" occurs firs. print -1 if word not found.

# def check_for_line():
#     word = "programming"
#     data = True
#     line_num = 1

#     with open("practice.txt" , "r") as ds:
        
#         while data:
#             data = ds.readline()
#             if (word in  data):
#                 print(line_num)
#                 return
#             line_num += 1
#     return -1

# print(check_for_line())

#--------------------------------------------------------------------------------------
# from a file containg numbers separated by comma, print the count of even numbers.

with open("num.txt" , "r") as x:
    data = x.read()
    print(data)
    fdata = data.split(",")
    print(fdata)
    print(type(fdata))   
