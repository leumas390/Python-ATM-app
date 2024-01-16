def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 5.     Check      | 6.   Support       |")
    print("------------------------------------------")

from banking_pkg import account


print("          === Automated Teller Machine ===          ")


name = input("Enter name to register:")
pin = input('Enter Pin:')
balance = 0.0

print(name)
print(pin)
print(name + "has been registered with a string balance of $" + str(balance))



while True:
    name_to_validate = input("Enter name:")
    pin_to_validate = input("Enter Pin:")

    if name_to_validate == name and pin_to_validate == pin:
        print("signed in")    
        
    else:
        print("incorrect name or pin please try again")
        break
    
    while True:
        atm_menu("name")
        option = input("choose an option: ")

        if option == "1":
            account.show_balance(balance)
            print("          === Automated Teller Machine ===          ")
        if option == "2":
            balance = account.deposit(balance)
            account.show_balance(balance)
            print("          === Automated Teller Machine ===          ")
        if option == "3":
            balance = account.withdraw(balance) 
            print("          === Automated Teller Machine ===          ")
            account.show_balance(balance)
        elif option == "4":
            account.logout(name)
        elif option == "5":
            balance = account.Check(balance)
            account.show_balance(balance)
            print("          === Automated Teller Machine ===          ")
        elif option == "6":
            print("CALL 1800-542-3202")
        break
    else:
        print("please select valid option")
    
   

