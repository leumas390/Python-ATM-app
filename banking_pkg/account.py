def show_balance(balance):
    print("balance is:", balance)
    
def deposit(balance):
    amount = input("Enter amount to deposit:")
    return float(balance) + float(amount)

def withdraw(balance):
    amount = input("Enter amount to withdraw:")
    return balance - float(amount)

def Check(balance):
    amount = input("Enter check Amount:")
    return balance + float(amount)

def logout(name):
    print("Goodbye", name)