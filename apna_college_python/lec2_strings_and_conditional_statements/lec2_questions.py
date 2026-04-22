#WAP take a number from the user and check if the number is odd or even.

num = int(input("Please enter a number of your choice:"))

if (num%2==0):
    print('EVEN')
else:
    print('ODD')



#--------------------------------------------------------------------------
#WAP to find the greatest of the 3 numbers entered by the user.
num_1 = int(input("Enter the first of the 3 numbers:"))
num_2 = int(input("Enter the second of the 3 numbers:"))
num_3 = int(input("Enter the third of the 3 numbers:"))


if(num_1>num_2):
    if(num_1>num_3):
        print(num_1)
    else:
        print(num_3)
elif(num_2>num_3):
    if(num_2>num_1):
        print(num_2)
    else:
        print(num_3)     
elif(num_3>num_1):
    if(num_3>num_2):
        print(num_3)
    else:
        print(num_2)
# 
# Alternate way
        
if (num_1>=num_2 and num_1>=num_3):
    print(num_1)
elif(num_2>num_3):
    print(num_2)
else:
    print(num_3)
    


#---------------------------------------------------------------------------------------------
#WAP check whether the given number is a multiple of 7 or not.
numb = int(input("Please type your name here:"))
if (numb%7== 0):
    print("Multiple of 7")
else:
    print("Not a multiple of 7")
