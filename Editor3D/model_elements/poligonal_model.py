from Editor3D.model_elements.poligon import Poligon
from Editor3D.model_elements.texture import Texture


class PoligonalModel:
    def __init__(self, poligons: Poligon, textures: Texture) -> None:
        self.poligons = poligons
        self.textures = textures
