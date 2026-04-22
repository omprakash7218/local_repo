#Store following word meanings in a python dictionary:
# table:"a piece of furniture", "list of facts and figures"
# cat :"a small animal"

dict ={
    "cat":"a small animal",
    "table":["a piece of furinuture","list of facts and figure"]
    
}
print(dict)



#-----------------------------------------------------------------------------------
# You are given a list of subjects for students. Assume one classroom is required for q subject.
# How many classrooms are needed by all students
set1 = {
    "python","java","c++","python","javascript","java","python","java","c++","c"
}
print("Total number of students needed: ", len(set1))


#-----------------------------------------------------------------------------
# WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
# Start with an empty dictionary and add one by one. Use subjects name as key and marks as value.

# subject_wise_marks = {
# }
# sub = int(input("Marks obtained in History: "))
# subject_wise_marks.update({"history":sub})
# sub = int(input("Marks obtained in science: "))
# subject_wise_marks.update({"science":sub})
# sub = int(input("Marks obtained in geography: "))
# subject_wise_marks.update({"geography":sub})

# print(subject_wise_marks)



#figure out a way to store 9 and 9.0 as separate values in the set.
#(you can take help of built-in data types)

# fl = 9.0
# set3 = {9 , float(9.0)}
# print(set3)

# values = set()
# values.add('9')
# values.add(9.0)    # 1 way is this
values = {(int, 9), (float, 9.0)}   #or we can say values = {("int",9), ("float",9.0)}
print (values)

