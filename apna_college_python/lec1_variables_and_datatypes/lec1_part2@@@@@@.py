# ARITHMETIC OPERATOR

a = 5
b = 2
sum = a+b
print(a-b)
print(a+b)
print(a*b)
print(a/b)   # always returns a float value
print(a%b) #remainder
print(a**b) #a^b


# RELATIONAL/COMPARISON OPERATOR

a = 59

b = 20
print( a == b)

print(a!=b) # != means not equal to 
print( a>b)
print( a<=b)
print( a<b) #false
print( a>=b) #true

# ASSIGNMENT OPERATOR

num = 10
num = num + 10 # here we can use assignment operator which is    +=
print(num)     
num += 10 #30
print(num)

num2 = 10
num2 -= 10   # similarly we can use -= for substraction in the given variable

print(num2)  # 0

num3 = 10
num3 *= 5   # similarly we can use -= for multiplication in the given variable
print(num3)  # 50

num4 = 10
num4/=5     # similarly we can use -= for division in the given variable
print(num4) # 2.0

num5 = 10
num5 %= 5       # similarly we can use -= for remainder in the given variable
print(num5) # 0

num6 = 10
num6 **= 5 #100000      # similarly we can use -= for power in the given variable
print(num6)




#LOGICAL OPERATOR  (not , and , or)

# not operator gives opposite to the boolean value

print ( not True)
print ( not False)

a = 50
b = 70
print (not (a > b)) #true


# not operator confirms if both the variable is true or false if  true then it gives true else false it gives false otherwise if one of them is opposite it gives false always


var1 = False
var2 = False
print(var1 and var2)

var3 = True
var4 = True
print (var3 and var4)

var5 = False
var6 = True
print( var5 and var6)

# or operators gives true if any one of the two is true and false if both the value is false 

var7 = True 
var8 = False 
print( var7 or var8)

var9 = False
var10 = False 
print( var9 or var10)

print(a>=b and b<=a) # false

print(a<= b or b<=a)  #True