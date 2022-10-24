import sys
import re
import os 
import math
import random

print("--- WELCOME TO THE WORLD'S BEST CALCULATOR, USER ---" + "\n")

print("--- BEFORE USE WARNING: ---" + "\n" +
          "--- CALCULATOR ONLY CAN DO OPERATIONS BETWEEN TWO NUMBERS !!! ---" + "\n" +
          "--- DO NOT TRY ENTER MORE THAN TWO NUMBERS ---")

while True :

    command_string = str(input("\n" + "--- PLEASE CHOOSE YOUR OPERATIONS: ---- " + "\n" + "\n"
                               "--- ADD OPERATION : TYPE(+)" + "\n" +
                               "--- SUBSTRACTION OPERATION : TYPE(-)" + "\n" +
                               "--- MULTIPLY OPERATION: TYPE(*)" + "\n" +
                               "--- DIVIDE OPEARTION: TYPE(/)" + "\n" + 
                               "--- EXPONENTIATE FUNCTION: (WARNING EXPONENTS OF BOTH NUMBERS): TYPE(^)" + "\n" +
                               "--- ROOT FUNCTION: (WARNING ROOT FUNCTION OF BOTH NUMBERS): TYPE(#)" + "\n" +
                               "--- PICK RANDOM NUMBER BETWEEN THE TWO NUMBERS: TYPE(RANDOM)"+ "\n" + 
                               "--- FOR QUIT: TYPE(Q)" + "\n"
                               + "--- >>> "))

    if command_string == '+':
        number_a = int(input("--- PLEASE ENTER THE A NUMBER: "))
        number_b = int(input("--- PLEASE ENTER THE B NUMBER: "))
        print("\n" + "--- RESULT: [%d] ---" % (number_a + number_b) + "\n")

    if command_string == '-':
        number_a = int(input("--- PLEASE ENTER THE A NUMBER: "))
        number_b = int(input("--- PLEASE ENTER THE B NUMBER: "))
        print("\n" + "--- RESULT: [%d] ---" % (number_a - number_b) + "\n")

    if command_string == '*':
        number_a = int(input("--- PLEASE ENTER THE A NUMBER: "))
        number_b = int(input("--- PLEASE ENTER THE B NUMBER: "))
        print("\n" + "--- RESULT: [%d] ---" % (number_a * number_b) + "\n")

    if command_string == '/':
        number_a = int(input("--- PLEASE ENTER THE A NUMBER: "))
        number_b = int(input("--- PLEASE ENTER THE B NUMBER: "))
        print("\n" + "--- RESULT: [%f] ---" % (number_a / number_b) + "\n")

    if command_string == '^':
        number_a = int(input("--- PLEASE ENTER THE A NUMBER: "))
        number_b = int(input("--- PLEASE ENTER THE B NUMBER: "))
        exponent_degree = int(input("\n" + "--- PLEASE ENTER EXPONENT DEGREE: "))
        print("\n" + "--- RESULT: ---" + "\n" +  
              "EXPONENT OF A NUMBER: [%d]" % pow(int(number_a) , int(exponent_degree)) + "\n"
              "EXPONENT OF A NUMBER: [%d]" % pow(int(number_b) , int(exponent_degree)) + "\n"
             )

    if command_string == '#':
        number_a = int(input("--- PLEASE ENTER THE A NUMBER: "))
        number_b = int(input("--- PLEASE ENTER THE B NUMBER: "))
        root_degree = int(input("\n" + "--- PLEASE ENTER ROOT DEGREE: "))
        print("\n" + "--- RESULT: ---" + "\n" +  
        "ROOT OF A NUMBER: [%f]" % pow(int(number_a) , 1/(int(root_degree))) + "\n"
        "ROOT OF A NUMBER: [%f]" % pow(int(number_b) , 1/(int(root_degree))) + "\n")

    if command_string == "RANDOM":
        print("\n" + "--- WARNING !, THIS FUNCTION WILL GENERATE RANDOM NUMBER BETWWEN A AND B NUMBERS ---" + "\n")
        number_a = int(input("--- PLEASE ENTER THE A NUMBER: "))
        number_b = int(input("--- PLEASE ENTER THE B NUMBER: "))   
        print("\n" + "--- RESULT: ---" + "\n" +  
              "RANDOM NUMBER: [%d]" %  + random.randrange(number_a , number_b) + "\n"
             )
             
    if command_string == 'Q':
        print("\n" + "--- CALCULATOR PROGRAM IS ENDING ---" + "\n" 
        + "--- Have a nice day ---" + "\n" 
        + "\n")
        break

    continue_string = str(input("--- DO YOU WANT TO CONTINUE ? ---" +
    "\n" + "--- Y for YES / N for NO ---"
    + "\n" + ">>> "))

    if continue_string == 'Y':
        continue

    if continue_string == 'N':
        print("\n" + "--- CALCULATOR PROGRAM IS ENDING ---" + "\n" 
        + "--- Have a nice day ---" + "\n" 
        + "\n")
        break
                               
    