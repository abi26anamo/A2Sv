class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1<=len(self.balance) and account2<=len(self.balance):
            if self.balance[account1-1]>=money:
                self.balance[account1-1]-=money
                self.balance[account2-1]+=money
                return True
            else:
                return False
   


    def deposit(self, account: int, money: int) -> bool:
        if account <=len(self.balance):
            self.balance[account-1]+=money
            return True
        return False
        

    def withdraw(self, account: int, money: int) -> bool:
        if account>len(self.balance):
            return False
        elif account<=len(self.balance) and money >self.balance[account-1]:
            return False
    
        self.balance[account-1]-=money
        return True
