import numpy as np
class player:
    raise_amount = 1.1
    contract_years = 2
    
    def __init__(self, first, last, pay, team):
        self.first = first
        self.last = last
        self.pay = pay
        self.team = team

    def extend_contract(self, years):
        self.contract_years += years

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = (self.pay * self.raise_amount)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

class defender(player):
    contract_years = 5

class offender(player):
    contract_years = 1.5

spurs_striker = player("Harry", "Kane", 25000000, "Tottenham Spurs")
print(help(defender))