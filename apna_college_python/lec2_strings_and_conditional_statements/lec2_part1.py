Str1 = "My name is Anthony Gonjalwish. "
str2 = 'What is your name? '
str3 = '''May I know what exaclty do you do?'''
str4 = Str1 +str2 + str3
# Escape sequence characters  1. next line \n  2.tab \t 3.



print("My name is Omprakash Chaudhary. \nI am 23 yrs old. \nI like to watch Anime. \tI like to play cricket too.")

# we can print using f-string. Lets quickly see, how it's done
print(f"{str2} \n{Str1}")

# Basic opreraiton in python 1. concatenation 2. length of string

print( "hello" + "world")
print(str4)

len1 = len(Str1)
print(len1)

# In python numbering of strings start from 0 and all the spaces are also counter for.

#INDEXING OF STRINGS

str5 = "Guddu Hardware"
print(str5[6])

# SLICING SLICING SLICING RELEVANT FOR MACHINE LEARNING(ML) \\ ACCESSING PARTS OF THE STRING


# str[starting_idx : ending_idx] ending index is not included

string = "I am a data analyst currently pursuing my BBA from Shoolini University."
print(string[3:len(string)]) # [:4] means [0:4] and [3:] means [3:len(string)]
print(len(string))

print(string[-71:-1]) # This is very unique for python. It is not seen in any other programming language





# String Functions
# endswith function 
# The endswith() method is a built-in string method in Python that checks if a string ends with a specified suffix. 
# It returns True if the string ends with the specified suffix, otherwise False.
string2 = "i want to learn how to speak english fluently."
print(string2.endswith("."))

# 2.capitalize. it capitalizes the 1st character  of the string. 
# It creates a new string. it does not interfare of distrubs the original string

print(string2.capitalize())

#3. Replace 
#it replaces the word or character with a new one that you provide

print(string2.replace("want" , "hate"))
print(string2.replace("a", "z"))

#4. find returns 1st index of the 1st occurrer
print(string2.find("."))

#5. count counts number of occurrens

print(string2.count('a'))