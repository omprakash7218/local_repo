# Conditional statement
age = 23
if (age <=12):
    print("Can go outside the house but will have to be back before 6:00 PM")
elif(age<=18):
    print("Can go outside the house but will have to be back before 9:00 PM")
elif(age<=23):
    print('Can go outside and come back any time.')




#--------------------------------------------------------------------------------------------------
    #calculator
    print("What operation do you want to perform: * for multiply, \ for divide , + for sum and - for substract.")
    z = input()
    a = int(input("First number:"))
    b= int(input("Second number:"))

if (z=="*") :
    print(a*b)
elif(z=="-"):
    print(a-b)
elif(z=="/"):
    print(a/b)
elif(z=="+"):
    print(a+b)
else:
    print("You have entered a not valid operator, Please check and try again.")




#-----------------------------------------------------------------------------------------------
#Traffic light

color = input("What is the colour of the traffic light:")
if(color=='green'):
    print("GO")
elif(color=='red'):
    print('STOP')
elif(color=='yellow'):
    print('WAIT')
else:
    print("Please type a valid color:red, green, yellow")
print("End of code")



#----------------------------------------------------------------------------------------------
#STUDENT MARKS TO GRADE SYSTEM
marks = int(input("What is the marks obtained by the student?"))
if (100>=marks>=90):
    print("A")
elif(90>marks>=80):
    print("B")
elif(80>marks>=70):
    print("C")
elif(70>marks>=60):
    print("D")
elif(60>marks>=50):
    print("E")
elif(500>marks>=40):
    print("F")
elif(40>marks>=0):
    print("FAIL")
else:
    print("Print a number between 100 to 0")





#----------------------------------------------------------------------------------------------
#NESTING{statement ke andar me statement likhna, iska istemal karke patterns banaye ja sakte hai}


age = 12
lisence = "yes"
if (age>=18):
    if(lisence=="yes"):
        print("CAN DRIVE")
    else:
        print("CANNOT DRIVE")
else:
    print("CANNOT DRIVE")