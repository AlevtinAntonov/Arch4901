from editor_3_d.model_elements.point3D import Point3D
from editor_3_d.model_elements.poligon import Poligon
from editor_3_d.model_elements.texture import Texture


class PoligonalModel:
    def __init__(self, poligons: Poligon, textures: Texture) -> None:
        self.poligons = []
        self.textures = textures

        self.poligons.append(Poligon(Point3D))
