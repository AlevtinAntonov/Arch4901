import uuid
from datetime import datetime
from decimal import Decimal


class Ticket:
    def __init__(self, departure_zone: int, arrival_zone: int, route_number: int, departure_time: datetime,
                 arrival_time: datetime, buyer_id: int, price: Decimal, place: str, is_used: bool = False):
        self.id_ = uuid.uuid4().hex  # Генерация уникального идентификатора
        self.departure_zone = departure_zone
        self.arrival_zone = arrival_zone
        self.route_number = route_number
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.buyer_id = buyer_id
        self.price = price
        self.place = place
        self.is_used = is_used

    def __str__(self):
        return (f' Зона отправления {self.departure_zone}, прибытия {self.arrival_zone}, маршрут {self.route_number}, '
                f'цена {self.price}')


