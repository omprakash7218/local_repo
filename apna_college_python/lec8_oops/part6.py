# POLYMORPHISM  opertor overloading 
#  POLY = BAHUT SARE MORPH - CHAHRE
# When the operator is allowed to have different meaning according to the context
# operators & Dunder functions
print(1+2)                      #3
print("OM" + "PRAKASH")             #concatenate
print([1,2,3]+[4,5,6])                 #merge
print((1,2,3,1)+(0,1,2,4,5,6))   #** set donot merge or add + doesnot work to merge two sets together 
# this is called operator overloading 


# Q. make a class complex to store complex number in i and j format

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real , "i + ",self.img,"j")

n1 = Complex(5,3)
print(n1.showNumber())

n2 = Complex(6,8)
print(n2.showNumber())

# what if we need to add these two n1 and n2 number . here comes the dunder function 
# 2 ways 1st without dunder and 2nd with dunder
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real , "i + ",self.img,"j")

    def add(object1,object2):
        sumreal = object1.real + object2.real
        sumimg = object1.img + object2.img
        return Complex(sumreal , sumimg)

n1 = Complex(5,3)
n1.showNumber()
n2 = Complex(6,8)
n2.showNumber()

n3 = n1.add(n2)
n3.showNumber()

# i could not understand well so i decided to code it myself and try to come up with some logic
# class Complex2:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img
#         # print(self.real, "i + " , self.img, "j")
#     def shownum(self):
#         print(self.real, "i + " , self.img, "j")

#     def addition(self,obj2):
#         self.obj2 = obj2
#         newreal = self.real + obj2.real
#         newimg = self.img + obj2.img

#         return  Complex2(newreal,newimg)
# c1 = Complex2(5,3)
# c1.shownum()
# c1.real = 75
# c1.shownum()
# c2 = Complex2(-8,5)
# # c2.shownum()
# c3 = c1.addition(c2)

# c3.shownum()


# 2nd way

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real , "i + ",self.img,"j")

    def __add__(object1,object2):                        #we will use dunder function here
        sumreal = object1.real + object2.real
        sumimg = object1.img + object2.img
        return Complex(sumreal , sumimg)

n1 = Complex(5,3)
n1.showNumber()
n2 = Complex(6,8)
n2.showNumber()

n3 = n1 + n2
n3.showNumber()

# what if i want to subract
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real , "i + ",self.img,"j")

    def __sub__(object1,object2):                        #we will use dunder function here
        sumreal = object1.real - object2.real
        sumimg = object1.img - object2.img
        return Complex(sumreal , sumimg)

n1 = Complex(5,3)
n1.showNumber()
n2 = Complex(6,8)
n2.showNumber()

n3 = n1 - n2
n3.showNumber()

# other dunder function 
# Eg
# a__mul__b
# a__truediv__b    a/b division
# a__mod__b       a%b remainder
# __len__   len()
# __str__ print(object)
# __init__ object is created
# real world programming interview point of view job me bhi use hoga