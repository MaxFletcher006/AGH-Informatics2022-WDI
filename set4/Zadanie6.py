user_number_a = input("Please enter A number: ")
user_number_b = input("Please enter B number: ")

#In this section we gathering two numbers from user

if (int(user_number_a) > 0 and int(user_number_b) > 0):
    sum_numbers = (int(user_number_a) + int(user_number_b))
    sub_numbers = (int(user_number_a) - int(user_number_b))
    pro_numbers = (int(user_number_a) * int(user_number_b))
    quo_numbers = (int(user_number_a) / int(user_number_b))
    square_a = (int(user_number_a) * int(user_number_a))
    square_b = (int(user_number_b) * int(user_number_b))
    square_root_a = (int(user_number_a) ** (1/2))
    square_root_b = (int(user_number_b) ** (1/2))  

    print("--Sum of numbers: %d" % sum_numbers + "\n"
      "--Substraction of numbers: %d" % sub_numbers + "\n"
      "--Product of numbers: %d" % pro_numbers + "\n"
      "--Quotient of numbers: %d" % quo_numbers + "\n"
      "--Square of A number: %d" % square_a + "\n"
      "--Square of B number: %d" % square_b + "\n"
      "--Square root of A number: %d" % square_root_a + "\n"
      "--Square root of B number: %d" % square_root_b
      )

elif (int(user_number_a) <= 0 and int(user_number_b) <= 0):
    print("-----Program is ending-----")

elif (int(user_number_a) > 0 and int(user_number_b) <= 0):
    sum_numbers = (int(user_number_a) + int(user_number_a))
    sub_numbers = (int(user_number_a) - int(user_number_a))
    pro_numbers = (int(user_number_a) * int(user_number_a))
    quo_numbers = (int(user_number_a) / int(user_number_a))
    square_a = (int(user_number_a) * int(user_number_a))
    square_root_a = (int(user_number_a) ** (1/2))

    print("--Sum of numbers: %d" % sum_numbers + "\n"
      "--Substraction of numbers: %d" % sub_numbers + "\n"  
      "--Product of numbers: %d" % pro_numbers + "\n"
      "--Quotient of numbers: %d" % quo_numbers + "\n"
      "--Square of A number: %d" % square_a + "\n"
      "--Square root of A number: %d" % square_root_a + "\n"
      )

elif (int(user_number_a) <= 0 and int(user_number_b) > 0):
    sum_numbers = (int(user_number_b) + int(user_number_b))
    sub_numbers = (int(user_number_b) - int(user_number_b))
    pro_numbers = (int(user_number_b) * int(user_number_b))
    quo_numbers = (int(user_number_b) / int(user_number_b))
    square_a = (int(user_number_b) * int(user_number_b))
    square_root_a = (int(user_number_b) ** (1/2))

    print("--Sum of numbers: %d" % sum_numbers + "\n"
      "--Substraction of numbers: %d" % sub_numbers + "\n"  
      "--Product of numbers: %d" % pro_numbers + "\n"
      "--Quotient of numbers: %d" % quo_numbers + "\n"
      "--Square of B number: %d" % square_a + "\n"
      "--Square root of B number: %d" % square_root_a + "\n"
      )

if (int(pro_numbers) == 10):
    print ("--- yay! ---")

