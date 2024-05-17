#!/usr/bin/env python3

class CashRegister:
    all = []

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.item_prices = []
        CashRegister.add_new_register(self)

    @classmethod
    def add_new_register(cls, new_register):
        cls.all.append(new_register)

    @classmethod
    def count(cls):
        return len(cls.all)

    @classmethod
    def total_earnings(cls):
        # create list of all totals and sum them using sum function
        # all_total = 0
        # for register in cls.all:
        #     all_total += register.total
        # return all_total
        return sum([register.total for register in cls.all])

    def add_item(self, title, price, quantity=1):
        self.total += (price * quantity)
        self.item_prices.append(price * quantity)
        for num in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount:
            discount_to_apply = self.total * (self.discount / 100)
            self.total -= int(discount_to_apply)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        last_transaction = self.item_prices.pop()
        self.total -= last_transaction
        

cr1 = CashRegister()
cr1.add_item('apple', 10)
cr2 = CashRegister()
cr2.add_item('potato', 100)
CashRegister()

import ipdb; ipdb.set_trace()