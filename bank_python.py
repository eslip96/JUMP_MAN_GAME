
print("* * * ATM MACHINE * * *")

user_balance = 0


def check_balance():
    print('*' * 8)
    print(f'{user_balance:.2f}')
    print('*' * 8)


def deposit_balance():
    global user_balance
    deposit_amount = float(input("How much would you like to deposit?:"))

    if deposit_amount < 0:
        print("ERROR: AMOUNT MUST BE GREATER THAN 0")
    else:
        user_balance += deposit_amount
        return print(f'Deposited amount ${deposit_amount:.2f}\nNew balance ${user_balance:.2f}')


def withdraw_amount():
    global user_balance

    withdraw_amount = float(input("How much would you like to withdraw?:"))

    if withdraw_amount < 0:
        print(f"ERROR: AMOUNT MUST BE GREATER THAN 0")
    elif withdraw_amount > user_balance:
        print(f"ERROR: AMOUNT MUST BE MORE THAN CURRENT BALANCE OF ${user_balance:.2f}")
    else:
        user_balance -= withdraw_amount
        print(f'Amount withdrawed ${withdraw_amount:.2f}.\nCurrent Balance ${user_balance:.2f}')


while True:
    user_input = input("\nWhat would you like to do?  \nCheck (B)alance, \n(D)eposit, \n(W)ithdraw \n(Q)uit: ").upper()

    if user_input == 'B':
        check_balance()
    elif user_input == 'D':
        deposit_balance()
    elif user_input == 'W':
        withdraw_amount()
    elif user_input == 'Q':
        print('Thank You come again!')
        break
    else:
        print()
        print("incorrect option. Please try again.")
        print()
