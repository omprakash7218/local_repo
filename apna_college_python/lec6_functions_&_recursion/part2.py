# RECURSION
# WE CAN use recursion for the same purpose as we use loops



# def show(n):
#     if (n==0):
#         return
#     print(n)
#     show(n-1)    #  this is called call stacking 
#     print("end")


# show(5)

# heroes = [ 'a', 'b', 'c', 'd']
# def el(list):
#     int = 0
#     for xyz in list:
#         print(list[int] , end = ' ')
#         int += 1

# el(heroes)

# let us understand recursion using factorial 
#  I will try to make a program using function recursion 

# def fact(x):
#     if (x == 1 or x == 0 ):
#         return 1
   
#     return fact(x-1) * x

# print(fact(6))

# n!   =   n * (n-1)!   this type of relation is called recurrence relation yaha badi(n)! wali value chhote(n-1)! wale pe depend kar raha hai

def factorial(x):
    if (x == 1 or x== 0):
        return 1
    # print(factorial(x-1))*x
    print(x)
    return factorial(x-1)*x
    
print(factorial(6))