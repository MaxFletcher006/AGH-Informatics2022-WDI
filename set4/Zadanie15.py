x1 = int(input("Please enter the x1: "))
y1 = int(input("Please enter the y1: "))

x2 = int(input("Please enter the x2: "))
y2 = int(input("Please enter the y2: "))

print ("Sum of z1 and z2: (%d , %d(i))" %((x1+x2) , (y1+y2)))
print ("Sub of z1 and z2: (%d , %d(i))" %((x1-x2) , (y1-y2)))
print ("Mult of z1 and z2: (%d , %d(i^2) , %d(i))" %((x1*x2) , (y1*y2) , (x1*y2 + x2*y1)))
print ("Div of z1 and z2: (%d ,%d(i))" %( ((x1*x2)+(y1*y2)/((x2**2)+(y2**2))) , ((x2*y1)-(x1*y2)/((x2**2)+(y2**2))) ))
 
    
    