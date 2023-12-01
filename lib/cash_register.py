#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_item = 0
  
  def add_item(self, title, price, quantity = 1):
    self.last_item = (price*quantity)
    self.total += (price * quantity)
    i = 0
    while i < quantity:
      self.items.append(title)
      i+=1
  
  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      discount = self.total * (self.discount / 100)
      self.total -= discount
      print(f"After the discount, the total comes to ${round(self.total)}.")
  
  def void_last_transaction(self):
    self.total -= self.last_item
  

cash_register = CashRegister()
cash_register_with_discount = CashRegister()
#cash_register_with_discount.add_item("apple", 0.99)
cash_register_with_discount.add_item("tomato", 1.76, 2)
print(cash_register_with_discount.total)
print(cash_register_with_discount.last_item)