data = [ 
            {"name" : "Peter", "age" : 75, "balance": 25000, "dept":"mechanic", "accountNo" : 123455, "passbook" : []},
            {"name" : "Ram", "age" : 25, "balance": 12000, "dept":"it", "accountNo" : 123456, "passbook" : []},
            {"name" : "Shyam", "age" : 15, "balance": 500, "dept":"it", "accountNo" : 123457, "passbook" : []},
            {"name" : "Ravan", "age" : 55, "balance": 300, "dept":"doctor", "accountNo" : 123458, "passbook" : []},
            {"name" : "Laxman", "age" : 45, "balance": 1900, "dept":"mechanic", "accountNo" : 123459, "passbook" : []},
        ]


class BankServices :    

    def __init__(self, customers) -> None:
        self.bankCustomersData = customers

    def searchCustomer(self, accountNo):

        for customer in self.bankCustomersData:
            if customer["accountNo"] == accountNo:
                return customer
        return None
    
    def tranferMoney(self, senderAc, recieverAc, amount):

        if amount < 0:
            return "Transaction amount is invalid !"

        sender = self.searchCustomer(senderAc)
        reciever = self.searchCustomer(recieverAc)
        
        if sender == None :
            return "Transaction Failed. Sender Account No. is invalid !"
        
        if sender["balance"] < amount :
            return "Insufficient balance. Transaction failed !"
        
        if reciever == None:
            return "Transaction failed. Receiver Account is invalid !"
        
        sender["balance"] -= amount
        self.updatePassbook(amount, "debit", sender, reciever)
        
        reciever["balance"] += amount
        self.updatePassbook(amount, "credit", reciever, sender)    

        return "Transaction Success !"
    
    
    def updatePassbook(self, amount, transactionType, customer, toCustomer):
        passbookEntry = {}
        if transactionType == "debit":
            passbookEntry["particulars "] = f'Rs {amount} is debited and transefered to {toCustomer["name"]}'
            passbookEntry["debit"] = amount
            passbookEntry["credit"] = None

        if transactionType == "credit":
            passbookEntry["particulars "] = f'Rs {amount} is credited from {toCustomer["name"]}'
            passbookEntry["debit"] = None
            passbookEntry["credit"] = amount

        passbookEntry["balance"] = customer["balance"]
        customer["passbook"].append(passbookEntry)

    def printPassbook(self, accountNo):
        customer = self.searchCustomer(accountNo)
        if customer == None :
            return "Transaction Failed. Account No. is invalid !"
        return customer["passbook"]
        

        
manager = BankServices(data)

print(manager.tranferMoney(123455, 123456, -10000))
print(manager.tranferMoney(123455, 123456, 1000))
print(manager.tranferMoney(123455, 123456, 1000))
print(manager.tranferMoney(123455, 123456, 1000000))
print(manager.searchCustomer(123456))

print(manager.printPassbook(123455))
print(manager.printPassbook(123456))

