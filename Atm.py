from datetime import datetime
balance=500
PIN=1234
transaction=[]
PIN1=[]
while True:
    print('Welcome to the ATM')
    print('Insert the card')
    option=int(input('1-yes,2-no: '))
    if option==1:
        user_pin=int(input('Insert 4 digit the pin: '))
        if user_pin == PIN:
            print('''
                    Select Language
                    1.English
                    2.Hindi''')
            language=int(input('Input any one of the language above: '))
            if language == 1:
                print('''
                        1.Deposit
                        2.Withdraw
                        3.Balance check
                        4.PIN change''')
                option01=int(input('Select your option above: '))
                if option01 == 1:
                    amount=int(input('Feed the cash: '))
                    if amount%100==0:
                        print('Cash has been accepted: ')
                        balance=balance+amount
                        transaction.append(amount)
                    else:
                        print('Cash has been rejected: ')
                elif option01==2:
                    amount=int(input('Enter the amount: '))
                    if amount<balance and amount%100==0:
                        print('withdraw the cash ')
                        balance=balance-amount
                        transaction.append(amount)
                    else:
                        print('No balance: ')
                elif option01==3:
                    datetime=datetime.now()
                    date=datetime.strftime('%d/%m/%Y')
                    time=datetime.strftime('%H:%M:%S')
                    print(
                        f'''
                                State Bank of India
                Date:{date}                           Time:{time}
                transactions:
                ''')
                    for transactions in transaction:
                        print(transaction)
                    print('balance:',balance)
                elif option01==4:
                    old_pin=int(input('Enter the old pin: '))
                    if old_pin==PIN:
                        new_pin=int(input('Enter the new pin: '))
                        PIN=new_pin
                        PIN1.append(int(new_pin))
                        print('PIN changed successfully')
        else:
            print('Invalid or Wrong PIN')
                




