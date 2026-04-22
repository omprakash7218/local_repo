i = 1
while i<=5:
    print("hello" , i)
    i += 1

    #  '''i''' here is a iterator and the while loop the process is known as iteration

Z = 3
while Z >=1:
    print("HELLO", Z)
    Z -= 1

z = 0
while z>=1:
    print(z)
    z-=1

# break and continue in python 
loop = 0
while loop <= 9:
    print(loop) 
    if (loop == 3):
        break                   #break - used to terminate the loop when encountered 
    loop += 1
print('end of loop ')         
  
                        

# loops = 0 
# while loops <= 5:
#     print (loops)
#     loops  += 1

# what if we want to print 0 to 5 but not 3 
loops = 0
while loops <= 15:
    if (loops == 3):
        loops =  9
        continue                    #continue - terminates execution in the curren iteration & continues execution of the loop with the next iteration.

    print(loops)
    loops += 1