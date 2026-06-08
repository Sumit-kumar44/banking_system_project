
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        
        

    def deposit(self, amount ):
        if amount > 0:
            self.balance += amount
            print(f'Deposiited ${amount}. Current balance: ${self.balance}')
            print('FUNDS DEPOSITED SUCCESSFULLY!!!')
        else:
            print('!!! DEPOSITED AMOUNT MUST BE POSITIVE.')

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f'Withdrawl ${amount}. Current balance: ${self.balance}')
                print('FUNDS WITHDRAWL SUCCESSFULLY!!!')
            else:
                print(f'INSUFFICIENT FUNDS. Current balance: ${self.balance}')

        else:
            print('WITHDRAWL MUST BE POSITIVE!!!')

    def check_balance(self):
        print(f'CURRENT BALANCE: ${self.balance}')

    
                  



def main():
    account = BankAccount('Sumit', 0)




    while True:
        print('\n----Banking System----')
        print('1. Deposit')
        print('2. Withdraw')
        print('3. Check Balance')
        print('4. Exit')

        choice= int(input('Choose an Option: '))

        if choice ==1:
            amount = float(input("Enter amount to deposit: $"))
            account.deposit(amount)
            

        elif choice == 2:
            amount = float(input("Enter amount to Withdraw: $"))
            account.withdraw(amount)
            

        elif choice == 3:
            account.check_balance()

        elif choice == 4:
            print('!!! EXITING THE BANKING SYSTEM !!!')
            break
        else:
            print('Invalid option. PLEASE TRY AGAIN')

if __name__ == "__main__":
    main()





