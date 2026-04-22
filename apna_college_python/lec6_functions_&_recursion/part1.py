# functions and recursion 

# Function - a generalized block of statements that perform a specific task.
# if a same type of code is to be run again and again(redunt)  
# we can def them with a function 

def sum(a,b):
    s = a + b
    print(s)

sum(6,5)

# print is also a built in function in python 
# (function) def print(
#     *values: object,
#     sep: str | None = " ",
#     end: str | None = "\n",
#     file: SupportsWrite[str] | None = None,
#     flush: Literal[False] = False


# There are so many built in functions in python 
# let's understand these one by one 
print("omprakash" , "chaudhary", sep = ' $ ', end = "123441324")
print('this and that')

# range function 
# range()

#len function 
# len()
#type function 
# type()
# so these are all built in functions 

# --------------------------------------------------------------

# default parameter 
def mul(a,b):
    print(a*b)
    return a*b


# mul()    # it gives missing 2 required positional arguments 
# so we will have to give them some default parameters

def mult(a=1 , b=1):      # we can only give default values from the last variable  we cannot do mult(a =1 , b) this will show me an error 
    print(a*b)
    return a*b

mult()    # it will give 1*1 = 1

mult(7,5)

# def multi(a=3, b):  # parameter without a default follows parameter with a default error error error 
#     print(a+b)

# multi(5)