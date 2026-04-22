# # Loops are used for sequential traversing list, string, tuples, etc
# for x in [10, 20, 30]:  # list 
#     print(x)


# for item in (1, 2, 3):   #tuple
#     print(item)


# for ch in "Omprakash":   # strings and its characters 
#     print(ch)


# for i in range(5):    # range()
#     print(i)

# for i in range(2, 6):   #range varition 
#     print(i)

# for i in range(1, 11, 2):   # range start , stop , step
#     print(i)

# d = {"a": 1, "b": 2}        # loop through dictionary

# for key in d:
#     print(key)

#  -----------------------------------------------------------
list = [1,2,53,532]
for num in list:
    print (num)


veggies = ['lassi', 'potato', 'ladyfingers' , 'rajhafohi']
for veg in veggies :
    print (veg)


veggie = ('lassi', 'potato', 'ladyfingers' , 'rajhafohi')
for vegi in veggie :
    print (vegi)



str = 'my n'
for char in str:
    print (char)

str = 'my n'
for char in str:
    print (char)
else:               #else is used for specific cases where we use break
     print('end') 



# range function 
# range functions returns a sequence of numbers, 
# starting from 0 (by default), and increments by (by default), 
# and stops before a specified number. 



# range(start?, stop, step?)
# wap and use range to print odd numbers from 1 to 89
for num in range(1,89,2):
    print(num)
# wap and use range to print even numbers from 1 to 890
for numa in range(2,80,2):
    print(numa)


#  PASS STATMENT 
#   pass is a null statement that does nothing. It is used as a placeholder for future code.


for eg in range(12,123441,124):
    pass      # we just making an empty space here nothing is being coded here 


print ( 'some useful work')