#Complex numbers calculator Version 1.0
import cmath

x1 = int(input("Please enter x1: "))
y1 = int(input("Please enter y1: "))

x2 = int(input("Please enter x2: "))
y2 = int(input("Please enter y2: "))


#x1,y1 = raw_input(int("Please enter first complex expression: ")).split()
#x2,y2 = raw_input(int("Please enter second complex expression: ")).split()  

z1 = complex(x1,y1)
z2 = complex(x2,y2)
  
print("\n" + "First imaginary complex number: " + str(z1) + "\n") 
print("Second imaginary complex number: " + str(z2) + "\n") 
print("Sum of two imaginary complex number: " + str((z1)+(z2)) + "\n")
print("Substraction of two imaginary complex number: " + str((z1)-(z2)) + "\n")
print("Multiply of two imaginary complex number: " + str((z1)*(z2)) + "\n")
print("Divition of two imaginary complex number: " + str((z1)/(z2)) + "\n")