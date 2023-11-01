from Editor3D.model_elements.flash import Flash
from Editor3D.model_elements.poligonal_model import PoligonalModel


class Scene:
    def __init__(self, id: int, models: PoligonalModel, flashes: Flash) -> None:
        self.id = id
        self.models = models
        self.flashes = flashes

    def method_1(data: None) -> None:
        pass

    def method_2(data_1: None, data_2: None) -> None:
        pass
