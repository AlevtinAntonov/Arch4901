import random
from abc import ABC, abstractmethod


class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass


class ItemFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass


class Gold(IGameItem):
    def open(self):
        return 'Gold!'


class Gem(IGameItem):
    def open(self):
        return 'Gem!'


class Silver(IGameItem):
    def open(self):
        return 'Silver!'


class Platinum(IGameItem):
    def open(self):
        return 'Platinum!'


class Copper(IGameItem):
    def open(self):
        return 'Copper!'


class Emerald(IGameItem):
    def open(self):
        return 'Emerald!'


class Diamond(IGameItem):
    def open(self):
        return 'Diamond!'


class GoldGenerator(ItemFabric):
    def create_item(self):
        return Gold()


class GemGenerator(ItemFabric):
    def create_item(self):
        return Gem()


class SilverGenerator(ItemFabric):
    def create_item(self):
        return Silver()


class PlatinumGenerator(ItemFabric):
    def create_item(self):
        return Platinum()


class CopperGenerator(ItemFabric):
    def create_item(self):
        return Copper()


class EmeraldGenerator(ItemFabric):
    def create_item(self):
        return Emerald()


class DiamondGenerator(ItemFabric):
    def create_item(self):
        return Diamond()


if __name__ == '__main__':

    # Вводим количество комплектов наград в заданном соотношении
    n = int(input('Введите количество комплектов -> '))

    # Списки с типами наград и их соотношениями
    reward_types = [GoldGenerator().create_item().open(), GemGenerator().create_item().open(),
                    SilverGenerator().create_item().open(), PlatinumGenerator().create_item().open(),
                    CopperGenerator().create_item().open(), EmeraldGenerator().create_item().open(),
                    DiamondGenerator().create_item().open()]
    # Награды должны генерироваться в соотношении: 3(золото GOLD):1(алмазы GEM):10:10:10:10:10(ваши награды)
    ratios = [3, 1, 10, 10, 10, 10, 10]

    # Инициализируем список для хранения наград
    rewards = []

    # Генерируем список в соответствии с заданными соотношениями
    for i, ratio in enumerate(ratios):
        rewards.extend([reward_types[i]] * ratio * n)

    # Перемешиваем список, чтобы получить случайный порядок
    random.shuffle(rewards)
    print(f'{rewards=}')

    # Считаем количество каждого типа наград
    count = {'Gold!': 0, 'Gem!': 0, 'Silver!': 0, 'Platinum!': 0, 'Copper!': 0, 'Emerald!': 0, 'Diamond!': 0}
    for reward in rewards:
        count[reward] += 1
    # Выводим результат

    print(f"Сгенерировано {len(rewards)} награды:")
    print(f"Gold!: {count['Gold!']}")
    print(f"Gem!: {count['Gem!']}")
    print(f"Silver!: {count['Silver!']}")
    print(f"Platinum!: {count['Platinum!']}")
    print(f"Copper!: {count['Copper!']}")
    print(f"Emerald!: {count['Emerald!']}")
    print(f"Diamond!: {count['Diamond!']}")
