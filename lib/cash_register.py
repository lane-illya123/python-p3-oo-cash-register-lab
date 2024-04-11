#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount = 0):
    
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, title, price, quantity=1):
    
    self.items.append((title, price, quantity))
    self.total += price * quantity

  def apply_discount(self):
    
    if self.discount == 0:
      print("There is no discount to apply.")
      
      return 

    percent = float(self.discount)
    percent /= 100
    difference = self.total * percent
    self.total = self.total - difference
    self.total = int(self.total)
    print(f"After the discount, the total comes to ${self.total}.")

  def get_items(self):
    return self.items  

      