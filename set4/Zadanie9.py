print("--- Welcome to the ZenBank ATM/CDM ---" + "\n")

balance = 5000

while True:

    command_string = str(input("Whitdrawl: (1)" + "\n" 
    + "Deposit: (2)" + "\n" 
    + "Balance check: (3)" + "\n" 
    + "Quit: (0)" + "\n" + "\n"
    + ">>> "))

    if command_string == '1':
        withdrawl = int(input("\n" + "--- Please enter your amount of withdrawl: "))
        balance = balance - withdrawl
        print("\n" + "--- Succeed ---" + "\n")
       
    if command_string == '2':
        pin_code = str(input("\n" + "--- Please enter your PIN Code: "))
        deposit = int(input("\n" + "--- Please enter your amount of deposit: "))
        balance = balance + deposit
        print("\n" + "--- Succeed ---" + "\n")

    if command_string == '3':
        pin_code = str(input("\n" + "--- Please enter your PIN Code: "))
        print("\n" + "--- Your current balance is %d$ ---" % balance + "\n")

    if command_string == '0':
        print("\n" + "--- Thank you for choosing us ---" + "\n" 
        + "--- Have a nice day ---" + "\n" 
        + "--- Don't forget to take your card ---" 
        + "\n")
        break
    
    if balance < 0:
        print("\n" + "---(Error) Insufficent Fund ---" + 
        "\n" + "--- Please make deposit to your bank account ---" + "\n")
        
    continue_string = str(input("--- DO YOU WANT TO CONTINUE TRANSACTION ? ---" +
    "\n" + "--- 1 for YES / 0 for NO ---"
    + "\n" + ">>> "))

    if continue_string == '0':
        continue

    if continue_string == '1':
        print("\n" + "--- Thank you for choosing us ---" + "\n" 
        + "--- Have a nice day ---" + "\n" 
        + "--- Don't forget to take your card ---" 
        + "\n")
        break
  

    




        


