import math
# loop over integer values of a, b, c form 0 to 5
# if a^2b + bc^2+c^2a-ab^2 -bc^2-ca^2= 0, print a, b, c
# and count the number of solutions
count = 0
for a in range(0,6):
    for b in range(0,6):
        for c in range(0,6):
            y1 = a**2*b + b**2*c + c**2*a - a*b**2 - b*c**2 - c*a**2
            y2 =(b - c) *(b - a)*(c - a)
            if y1 == 0:
                # print out to a file
                f = open("solutions.txt", "a")
                f.write(str(y2)+" "+str(y1)+" >> "+str(a) + " " + str(b) + " " + str(c) + "\n")
                f.close()


                print(y1, y2, a,b,c)       
                count = count + 1

print("Number of solutions: ", count)


