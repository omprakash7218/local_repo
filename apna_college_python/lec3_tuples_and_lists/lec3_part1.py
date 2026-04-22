#Tuples and List
# Unlike other programming languages . List can store different data types together.
# Strings, float, integer or boolean, etc

# List are similar to strings but list are mutable. We can change index in List but this cannot be done in Strings.


marks = [78.2, 34.2, 54.3, 98,64.23,78.45]
print(marks[0])
print(marks[1])
print(marks[3])
print(len(marks))
print(type(marks))
student_demographics = ["Name","age","Address"]
student1 = ["Omprakash Chaudhary",23,"Bajpatti, Sitamarhi, Bihar"]
student2 = ["Hemant Kumar Chaudhary",25,"New Delhi"]



list1 = ["raju",67, 23, "delhi"]
list1[0] = "Omprakash"
print(list1)
print(list1[5])                   # list index out of range
print(list1[:])
print(list1[-3:])

str1 = 'omprakash'
print(str1[2])
str1[2] = 't'                   # It will give error.

#=--------------------------------------------------

list2 = [29,88.34,5.34]

list2.append(6)
print(list2.sort())       #-sort function only works on same data type.. HERE it is float and int
print(list2)
print(list2.sort(reverse = True))
print(list2)

list3 = ["mango", "banana", "apricot"]   #- Here it is string
list3.sort(reverse = True)
print(list3)  


#- what if we want to revese the whole list
list4  = ['mango', 'vanilla', 'sdf', 'sfag', 'asge']
list4.reverse()  #it should give ['asge', 'sfag', 'sdf', 'vanilla', 'mango']
print(list4)

# what if we want to a new value to a certian index >????????????//
list5 = ['23','233', 'sdf','asger','ert']
list5.insert(1,233)  # HERE we added a int 233 in place of a str '233' and the other values shifted one index

print(list5)


#what if we want to remove a value from aa list REMOCW(remove) it removes the 1st value you provide
list5.remove(233)
print(list5)

# what if we want a value at a certain index
list5.pop(3)
print(list5)