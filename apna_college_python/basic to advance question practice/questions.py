
#------------------------------------------------------------------------------------------------------------------
# # convert celcius to  Fahrenheit.
# celcius = int(input("celcius:"))
# fahrenheit = 1.8*celcius + 32
# print("Fahrenheit:", fahrenheit )


#------------------------------------------------------------------------------------------------------------------
# take name and age as input and print using f-string 
# name = str(input("Name of the candidate: "))
# age = int(input("Age of the candidate: "))

# print(f"The candidate name is {name} and is of {age} years of age.")

#------------------------------------------------------------------------------------------------------------------
#WAP to find the greatest of the 3 numbers entered by the user.

# a = int(input("1st number: "))

# b = int(input("2nd number: "))

# c = int(input("3rd number: "))

# if(a>b and a>c):
#     print(a)
# elif(b>c):
#     print(b)
# else:
#     print(c)


#----------------------------------------------------------------------------------------
# WAP to ask the user to enter names of their 3 favorite movies and store them in a list.
# list = []
# mov = input("Movie name please: ")
# list.append(mov)
# print(list)
# mov = input("Movie name please: ")
# list.append(mov)
# print(list)
# mov = input("Movie name please: ")
# list.append(mov)
# print(list)


#----------------------------------------------------------------------------------------
# # WAP to check if a list contains a palindrome of elements.Hint use copy() method

# list1  =  [1,2,3,2,1]
# list2 = list1.copy()
# list3 =list2.reverse()
# print(list3)
# if list2 == list1:
#     print('Palindrome')
# else:
#     print('Not a palindrome')

#   WAP to count the number of students with the "A" grade in the following tuple.Not A Directory Error

# grade = ("C", "D", "A", "A", "B", "B", "A")
# print(grade.count("A"))

# list1 = list(grade)
# list1.sort()
# print(list1)
#-------------------------------------------------------------------------------------------------------------------------------------------
# SETS AND DICTIONARIES
nerolac = {
    "exterior" :
    {
        "economy":"suraksha plus",
        "premium":"excel",
        "luxury":"excel total"
    },
    "interior" :
    {
        "economy":"beauty emulsion",
        "premium":"beauty gold",
        "luxury":"impression 24k gold"
    }
    }
# keys = tuple(nerolac.keys())
# print(keys)

# print(nerolac["interior"]["economy"])

# print(nerolac["interior"].keys())

# print(tuple(nerolac.keys()))
# print(list(nerolac.keys()))
# print(str(nerolac.keys()))

# print(nerolac["exterior"].items())
# print(nerolac.get("interior"))
# print(nerolac.get("intsoifgoih"))
# WAP to get marks of 3 subject from a user 

# marks_obtained = {}
# marks = int(input("marks obtained in history : "))
# marks_obtained.update({'history':marks})
# marks = int(input("marks obtained in chemistry : "))
# marks_obtained.update({'chemistry':marks})
# marks = int(input("marks obtained in geography : "))
# marks_obtained.update({'geography':marks})


# print(marks_obtained)

# LOOOOOOOOOOOOOOOOPSS
# print numbers from 1 to 100
# ints = 1
# while ints<=100:
#     print(ints)
#     ints += 1

# for i in range(1,101):
#     print(i)

# s = 100
# while s >= 1:
#     print(s)
#     s -= 1

# for i in range(100,0):
#     print(i)    # this code will never run because for loop increase by 1 it does not decrease . Let us fix this

# for i in range(100,0,-1):
#     print(i)    #sweet!!

# MULTIPLICATION TABLE OF A  NUMBER N 

# N = 4
# n = 1
# while n <=10:
#     print(N*n)
#     n  += 1

# # print the elements of the following list using a loop: [1,4,9,16,25,36,49,64,81,100]

# listy = [1,4,9,16,25,36,49,64,81,100]
# print(len(listy))

# for i in listy:
#     print(i)


#search for a number x in this tuyple using loops (1,4,9,16,25,36,49,64,81,100)
# tuply = (1,4,9,16,25,36,49,64,81,100)
# x = 63
# for i in tuply:
#     if i == x:
#         print(x , "found you bi*ch")
#         break
#     else:
#         continue
# print("where are you b*tch ?")    


# using while loop to make the code work
# x = 16
# i = 0
# while i <= len(tuply) - 1:
#     if tuply[i] == x:
#         print("found you bitch at index :", i)
#         break
#     else:
#         print("finding")
#     i += 1


# print all the even numbers from 1 to 100 using Break and continue
# for i in range(1,101):
#     if i%2 == 0:
#         print(i)
#     else:
#         continue

# USING WHILE LOOOP TO WRITE THE UPPER PROGRAMM

# i = 1 
# while i <= 100:
#     if i%2 == 0:
#         print(i)
#         i += 1
#         continue
#     else:
#         i += 1

#  FUNCTIONS AND RECURSIONS

# def sum(a,b):
#     print(a+b)

# sum(3,4)

# def printlen(a):
#     print(len(a))

# s = [2,2,12,4,4,3,4,34,3,4,34,34,34,34,34]
# printlen(s)


# print("omprakash","chaudhary", sep = '#', end = '12323')


# def multi(a=1,b=1):
#     # print(a*b)
#     return a*b
    

# print(multi(2,43))

#WAP to print 1 to 100 using recursion using function

# def count(n):
#     if (n==0):
#         return
#     print(n)
#     count(n-1)
#     print("end")

# count(10)

# def show(n):
#     if (n==0):
#         return
#     print(n)
#     show(n-1)    #  this is called call stacking 
#     print("end")
# show(5)

# factorial using recursion

# def fact(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * fact(n-1)

# print(fact(5))

# waf to print the elements of a list in a single line. (list is the parameter)

# def listy(n):
#     for element in n:
#         print(element, end = " ")


# heroes = ['hritik roshan','robert donny jr', 'chris hamsworth']
# # listy(heroes)

# def listy(arg):
#     i = 0
#     while i <= len(arg)-1:
#         print(arg[i] , end = ' ')
#         i +=1

# listy(heroes)

# WAP to find the factorial of any number n
# def facty(arg):
#     int = 1
#     num = 1
#     while int <= (arg):
#         num = num*int
#         int += 1
#     print(num)
# facty(5)
#  WAP to convert usd to inr 

# def usdinr(n):
#     print(n*83)


# usdinr(8)

# WAF that determines whether a given number is odd or even


# def oddeven(num):
#     if num%2 == 0:
#         print("The number is even ")
#     else: 
#         print("The number is odd")
# x = int(input("Give a number of your liking: "))

# oddeven(x)



### Recursion questions to practice 

# write a recursive function to print all elements in a list.

cars = ["tata siarra","tata punch","bmw sadan", "mercedese amg","bugati veron", "defender", "mercedese benz", "lamborghini", "ford mustang","ferrari"]
def element(list, index = 0):
    if index == len(list):
        return
    else: 
        print(list[index])
        index += 1
    element(list,index)

element(cars)

