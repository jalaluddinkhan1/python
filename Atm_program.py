class Atm:
    def __init__(self):
        self.pin=''
        self.balance=0
        self.dis()
    def dis(self):
        n=int(input("""
        1> create pin :-- 
        2> deposite amount:--
        3> withdraw amout:--
        4> chek balalnce :--
        5> exit
        """))
        
        if n==1:
            self.createPin()
        elif n==2:
            self.depositeAmount()
        elif n==3:
            self.withdrawAmount()
        elif n==4:
            self.checkBalance()
        else:
            return 
        
    
    def createPin(self):
        self.pin=input("Please Enter your Pin :")
        print("your Pin updated sucess fully ")
    def depositeAmount(self):
        n=input(" Enter pin : ")
        if n== self.pin:
            am=int(input("Enter amount to deposite: - "))
            self.balance=self.balance +am
            
            print(' deposited successfully')
        else:
            print('!!!invalid pin !!!')
    def withdrawAmount(self):
        n=input(" Enter pin : ")
        if n== self.pin:
            am=int(input(" Enter amount to withdraw : - "))
            if am<self.balance:
                print(am,' withdawl success fully')
                self.balance=self.balance-am
            else:
                print(" you don't have sufficent amount to witdraw")
        else:
            print('!!!invalid pin !!!')
    def checkBalance(self):
        n=input(" Enter pin : ")
        if n== self.pin:
            print("your current balance is ",self.balance)
        else:
            print('!!!invalid pin !!!')

sbi=Atm()
