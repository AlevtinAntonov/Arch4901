from abc import ABC

from abstract_class import AbstractClassCar
from i_car_wash import ICarWash
from i_fuel_station import IFuelStation


class PickUp(AbstractClassCar, IFuelStation, ICarWash, ABC):
    load_capacity: int

    def __init__(self, brand, model, color, body_type, wheel_count, fuel_type, transmission_type, engine_capacity,
                 load_capacity):
        super().__init__(brand, model, color, body_type, wheel_count, fuel_type, transmission_type, engine_capacity)
        self.load_capacity = load_capacity

    @staticmethod
    def sweep_street():
        print('Подмееетаааееем, вжух, вжух)')

    def refill(self):
        print('Заправляемся, бульк)')