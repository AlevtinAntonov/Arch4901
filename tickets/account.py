import uuid
from decimal import Decimal


class Account:
    def __init__(self, balance: Decimal = 0):
        self.id_ = uuid.uuid4().hex  # Генерация уникального идентификатора
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостаточно средств на счете.")
