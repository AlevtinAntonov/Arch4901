import hashlib
import uuid
from typing import List

from tickets.account import Account
from tickets.ticket import Ticket


def hash_password(password):
    # Создаем объект хэша соответствующего алгоритма (например, SHA256)
    hash_object = hashlib.sha256()

    # Преобразуем пароль в байтовую строку
    password_bytes = password.encode('utf-8')

    # Обновляем хэш-объект с байтовой строкой пароля
    hash_object.update(password_bytes)

    # Получаем хеш-код в виде шестнадцатеричной строки
    hash_code = hash_object.hexdigest()

    return hash_code


class User:
    def __init__(self, name: str, login: str, password: str, account: Account = 0):
        self.id_ = uuid.uuid4().hex  # Генерация уникального идентификатора
        self.name = name
        self.tickets = []  # Инициализируем пустой список билетов
        self.login = login
        self.password_hash_code = hash_password(password)
        self.account = account

    def verify_password(self, input_password):
        input_password_hash = hash_password(input_password)
        return self.password_hash_code == input_password_hash

    # Добавляет купленный билет в список
    def add_ticket(self, ticket: Ticket):
        self.tickets.append(ticket.__str__()) # Используется метод __str__() объекта Ticket

    def get_tickets(self):
        return self.tickets
