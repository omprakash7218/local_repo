# WAP  to print the length of a list (list is the parameter)

food = ['aam', 'imli', 'aloo','baigan']
def printlen(a):
    print(len(a))

printlen(food)

# waf to print the elements of a list in a single line. (list is the parameter)

heroes = ['hritik roshan','robert donny jr', 'chris hamsworth']
# print(heroes[0] , end = ' ')
# print(heroes[1] , end= ' ')

# using for loop

def oneline2 (arg):
    for el in arg:
        print(el, end = ' ')
oneline2(heroes)

# using while loop

def oneline (arg):
    i = 0
    while i <=len(arg) - 1 :
        print(arg[i], end = ' ')
        i += 1
oneline(heroes)

# ---?--------------------------------------------------------------------------------------------------""
# wap to find the factorial of n. (n is the parameter)
# using while loop
print(end = "\n")
int = 5
def fact(num):
    i = 1
    fact = 1

    while i <= num:
        fact = fact*i
        i += 1
    print(fact) 

fact(int)    

# using for loop
n = 6
def fact(xyz):
    facto = 1
    for i in range(1, xyz+1):
        facto *=i
    print(facto)
fact(n)

# waf to convert USD to INR
def convo(usd_value):
    print(usd_value*83)

convo(2)


# wap that takes in a number and returns odd when no. is odd and even when num is even

def oddeven(num):
    if num%2 == 0:
        print("---EVEN---")
    else:
        print("---ODD---")


oddeven(6)




#------------------------------------------------------------
# recursion questions 
# write a recursive function to calculate the sum of first n natural numbers.


def sum(xyz):
    if xyz == 1 or xyz == 0:
        return 1
    return sum(xyz - 1) + xyz

print(sum(5))


# write a recursive function to print all elements in a list.

cars = ["bugati cheron", "scorpio s5", "aulto 800", "renault duster"]

index = 0
def elements(lists):
    global index
    if len(lists)==index:
        return 0
    print( lists[index]) 
    index += 1 
    elements(lists)

(elements(cars))


# (f"{index+1}. {lists[index]}")
#     index +=1
#     elements(lists)
#     print("end")

# def elements(list,index = 0):
#     if index == len(list):
#         return
#     print(list[index])
#     index += 1
#     elements(list,index)


# elements(cars)
    