# # using for and range
# # print numbers from 1 to 100
# for digit in range(1,101):
#     print(digit)

# # print numbers from 100 to 1
# for digit2 in range(100,0,-1):
#     print(digit2)


# #print multiplication table of a number n 
# n = 12
# for digit3 in range (n,n*11,n):
#     print(digit3)

# n1 = 21
# for digit4 in range(1,11):
#     print(n1*digit4)


# # wap to find the sum of first n natural numbers (using while loop)
# sum = 0
# int = 1
# while int <=20:
#     sum = sum + int
#     int +=1 

# print(sum)


# # same question in for loop 
# int1 = 10
# sum = 0
# for num in range (1,int1+1):
#     sum += num

# print(sum)    

#---------------------------------------------------------------------------------
#wap to find the factorial of first n natural numbers. (using for)
int2 =10
fct = 1
for num in range(1,int2+1):
    fct *= num

print(fct)

# same question using while loop
int3 = 10
fact = 1
q=1
while (q<=int3):
    fact *= q
    q += 1
print (fact)