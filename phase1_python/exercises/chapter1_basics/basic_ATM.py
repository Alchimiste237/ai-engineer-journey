print("Welcome to the basic ATM ")
balance = 0.0

status = "running"


while status == "running":
    value = input(' choose option: \n 1) Deposit \n  2) Withdraw \n 3) check balance  \n and exit to quit \n ')

    if value == '1':
        amount = float(input(' Enter deposit amount'))
        balance += amount
        print(f" new balance, {balance} ")
      

    elif value == '2':
      amount = float(input(' Enter withdraw amount '))
      if amount > balance:
        print(f" insufficient funds, {amount - balance} ")
      else:        
        balance -= amount
        print(f" new balance, {balance} ")

    elif value == '3':
      print(f'balance is: {balance} ')
    
    elif value == "exit":
      print('Good bye')
      status = "quit"
    else:
       print('Wrong value entered, try again ')