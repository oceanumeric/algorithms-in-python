"""
A CreditCard Class with following method:
get_customer()
get_bank()
get_accunt()
get_limit()
get_balance()
charge(self, price)
make_payment(self, amount)
"""


class CreditCard:
    """A consumer credit card"""
    
    def __init__(self, customer, bank, acnt, limit):
        """[create a new credit card instance]

        Args:
            customer ([str]): [the name of customer]
            bank ([str]): [the name of bank]
            acnt ([str]): [account identifier]
            limit ([int]): [credit limit (measured in dollars)]
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
        
    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_account(self):
        return self._account
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
    
    def charge(self, price):
        """[Charge given price to the card, assuming sufficient credit limit]
        Return true if chare was processed: false if charge was denied

        Args:
            price ([float]): [price charged to the account]
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    
    def make_payment(self, amount):
        self._balance -= amount 
            
            

if __name__ == "__main__":
    wallet = []
    wallet.append(
        CreditCard("John Bowman", 'California Savings',
                   '5391 0375 9387 5309', 2500)
    )
    wallet.append(
        CreditCard('John Bowman', 'California Federal',
                   '3485 0399 3395 1954', 3500)
    )
    
    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(val*2)
        
    for c in range(2):
        print("Customer = ", wallet[c].get_customer())
        print("Bank =", wallet[c].get_bank())
        print("Account =", wallet[c].get_account())
        print("limit = ", wallet[c].get_limit())
        print("Balance =", wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("New Balance =", wallet[c].get_balance())
        print("-----------------------------------")