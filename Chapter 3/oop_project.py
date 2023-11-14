from bank_accounts import *

Archie = BankAccount(1000, "Archie")
Max = BankAccount(2000, "Max")

Archie.get_balance()
Max.get_balance()

Max.deposit(500)

Archie.withdraw(10000)
Archie.withdraw(10)

Archie.transfer(10000, Max)
Archie.transfer(100, Max)

GuiZhen = InterestRewardsAcct(1000, "GuiZhen")

GuiZhen.get_balance()

GuiZhen.deposit(100)

GuiZhen.transfer(100, Archie)

Amira = SavingsAcct(1000, "Amira")

Amira.get_balance()

Amira.deposit(100)

Amira.transfer(10000, Max)
Amira.transfer(1000, Max)