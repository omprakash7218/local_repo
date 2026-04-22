# WAP to ask the user to enter names of their 3 favorite movies and store them in a list.
fav1 = input("Type in your first favorite movie: ")
fav2 = input("Type in your second favorite movie: ")
fav3 = input("Type in your third favorite movie: ")

fav = [fav1, fav2, fav3]
print(fav)

#  ALTERNATE WAY
fav = []
fav.append(fav1)
fav.append(fav2)
fav.append(fav3)

print(fav)


#  ALTERNATE WAY
movies = []
mov = input("enter your 1st movie: ")
movies.append(mov)
mov = input("enter your 2nd movie: ")
movies.append(mov)
mov = input("enter your 3rd movie: ")
movies.append(mov)
print(movies)


#ALTERNATE WAY OF DOING THIS WHICH IS MORE PROFESSIONAL AND LESS CODES

movies1 =[]
movies1.append(input("Enter 1st movie: "))
movies1.append(input("Enter 2nd movie: "))
movies1.append(input("Enter 3rd movie: "))
print(movies1)



#--------------------------------------------------------------------------------

# WAP to check if a list contains a palindrome of elements.Hint use copy() method

list1 = [1,23,2,3,2,1]

list2 = list1.copy()
list2.reverse()  # it reverses the actual string so we donot have to store it in a different variable
if (list2 == list1):
    print("Palindrome")
else:
    print("Not a palindrome")


#---------------------------------------------------------------------------------------------
#   WAP to count the number of students with the "A" grade in the following tuple.Not A Directory Error

grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

# Store the above values in a list and sort them from A to 

list1 = list(grade)
list1.sort()
print(list1)

# what if we want descending order 
list1.sort(reverse=True)
print(list1)