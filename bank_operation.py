

def show_balance(balance):
    print(f"Your balance is ${balance: .2f}")

def deposit():
    amount = float(input("Enter amount for deposit: "))
    if amount <0:
        print("That is not valid amount")
        return 0
    else: 
        return amount
    

def withdraw(balance):
    amount_withdraw = float(input("Enter amount to be withdraw: "))
    if amount_withdraw > balance:
        print("You dont have funds")
        return 0
    elif amount_withdraw<0:
        print("That is not valid amount")
        return 0
    return amount_withdraw
        

def main():
    balance = 0
    is_running = True
    while is_running:
        print("input '1' for showing balance")
        print("input '2' for showing deposit")
        print("input '3' for showing withdraw")
        print("input '4' for exit")
        
        choice = input("Enter your number 1-4: ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance+= deposit()
        elif choice == '3':
            balance -=withdraw(balance)
        elif choice == '4':
            is_running = False
            break
        else:
            print("That is not valid choice")
            break
        
if __name__ == '__main__':
    main()