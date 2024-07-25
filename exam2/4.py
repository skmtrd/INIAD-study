class Wallet:
    def __init__ (self, b):
        self.balance = b
    
    def deposit (self, amount):
        self.balance += amount
        

    def withdraw(self, amount):
        if self.balance - amount < 0:
            return "NG"
        self.balance -= amount
        return "OK"
    
    
    

c1 = Wallet(0)

c1.deposit(1000) # 1000円預け入れ
print(c1.withdraw(700)) # 700円引き出し(成功し、残高は300になる)
print(c1.withdraw(800)) # 800円引き出し(失敗するため、残高は変わらない)

print(c1.balance) # 300円