#WORKING CODE



import os 



def get_withdraw_amount():
    global withdrawl_total
    withdrawl_total = float(input('how much would you like to withdraw '))
    return withdrawl_total

def get_deposit_amount():
    global deposit_total
    deposit_total = float(input('how much would you like to deposit '))
    return deposit_total

def bal_update():
    global new_total
    with open('balance.txt', 'w') as nb:
        new_total = str(new_total)
        nb.write(new_total)

def add_debit():
    global new_total
    with open("balance.txt") as f:
        current_bal = f.read()
        current_bal = float(current_bal)
        print(type(current_bal))
        get_withdraw_amount()
        new_total = current_bal - withdrawl_total
        print(new_total)
    bal_update()

def credit():
    global new_total
    with open("balance.txt") as f:
        current_bal = f.read()
        current_bal = float(current_bal)
        print(type(current_bal))
        get_deposit_amount()
        new_total = current_bal + deposit_total
        print(new_total)
    bal_update()



def view_balance():
    with open('balance.txt', 'r') as f:
        balance = f.read()
        print('Your balance is '+ balance)
    


# CODE CURRENTLY IN WORK 



def signout():
   print('Have an amazing day !')
   exit()





def menu():
    menu_op = input('''
        Enter a menu number to view that menu.
        1. View Balance 
        2. Record a debit (withdraw)
        3. Record a credit (credit)
        4. Exit 
    ''')
    if menu_op == '1': 
        view_balance()
    elif menu_op == '2':
        add_debit()
    elif menu_op == '3': 
        credit()
    elif menu_op == '4':
        signout()
    else:
        menu()

menu()
