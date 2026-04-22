# # print numbers from  1 to 100 
# num = 1 
# while num < 101:
#     print(num)
#     num += 1

# # print numbers from  100 to 1
# num1 = 100
# while num1 >0:     #stoppin condn
#     print (num1)
#     num1 -= 1

#print the multiplication table of a number n.
# n = int(input("please give a number: "))
# multiplier = 1
# while multiplier <=10:
#     print(n*multiplier)
#     multiplier += 1



# # print the elements of the following list using a loop: [1,4,9,16,25,36,49,64,81,100]
# listy = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i < len(listy):
#     print(listy[i])
#     i += 1
#search for a number x in this tuyple using loops (1,4,9,16,25,36,49,64,81,100)
x = 16

# tu = (1,4,9,16,25,36,49,64,16,81,100,16,16)
# i= 0
# while i<len(tu):
#     if tu[i] == x:
#        print('found at index ' ,i)
#        break
#     else:
#        print('finding...')
#     i += 1
    

# print all the even numbers from 1 to 100 using Break and continue

# x = 1 
# while x <= 100:
#    if (x%2 != 0):
#       x += 1
#       continue 
#    print(x)
#    x += 1

# search for a number x in this tuple using loop:
#        [1,4,9,16,25,36,49,64,81,100]

tup = (1,4,9,16,25,36,49,64,81,100,64)
x = 64
index = 0
for z in tup:
   if z == x :
      print('found at index:',index,  z)
      break      # if we donot use this here we will get indx 10 
   index += 1

# the way we are looking for values one by one means LINEAR SEARCH

