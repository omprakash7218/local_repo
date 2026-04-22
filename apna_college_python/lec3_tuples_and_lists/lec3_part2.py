#Tuples are immutable just like strings
student = ('omprakash', 23, 54,'patna')
print(type(student))
print(student[1])
tup = ()
print(type(tup))

tup1 = (.0001)                      #python will think of it as an integer or string or float that the user has covered iside a small bracket.
print(type(tup1))


tup1_2 = (1,)
print(type(tup1_2))

print(student[:])
print(student.count(23))
print(student.index(54))