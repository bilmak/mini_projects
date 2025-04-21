import random
import time


def spin_row():
    symbols = ["🍎", "🍉", "🍒", "🍓"]
    result = []
    for symbol in range(3):
        result.append(random.choice(symbols))

    return result


def print_row(row):
    print("Spining...")
    time.sleep(2)
    print("|".join(row))


def get_payout(row, bet):
    if row[0] == row[1] and row[0] == row[2] and row[1] == row[2]:
        if row[0] == "🍎":
            bet *= 2
        elif row[0] == "🍉":
            bet *= 3
        elif row[0] == "🍓":
            bet *= 3
        elif row[0] == "🍒":
            bet *= 5

        print(f"Congratulation, you win ${bet}")
    else:
        bet=0

    return bet


def main():
    balance = 100
    print("Welcome to Python Slots")
    print(f"You have ${balance}")

    while balance > 0:
        bet = input("Please input your bet amount: ")
        if not bet.isdigit():
            print("Please Enter digit")

        bet = int(bet)
        if bet > balance:
            print("You dont have fund")
            continue
        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        
        row = spin_row()
        print_row(row)
        payout = get_payout(row, bet)
        if payout > 0:
            balance += payout
        else:
            balance -= bet
            
        print(f"Your balance is ${balance}")
        


if __name__ == '__main__':
    main()
