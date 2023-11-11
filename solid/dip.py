# Переписать код в соответствии с Dependency Inversion Principle:
# Разорвать зависимость классов Car и PetrolEngine. У машины же может быть DieselEngine.
from abc import ABC, abstractmethod


class IEngine(ABC):
    @abstractmethod
    def start(self):
        pass


class Car:
    def __init__(self, engine: IEngine):
        self.engine = engine

    def start(self):
        self.engine.start()


class PetrolEngine(IEngine):
    def start(self):
        pass
