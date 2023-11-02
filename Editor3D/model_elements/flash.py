from Editor3D.model_elements import angle3D
from Editor3D.model_elements.angle3D import Angle3D
from Editor3D.model_elements.point3D import Point3D


class Flash:
    def __init__(self, location: Point3D, angle: Angle3D, color: Color, power: float) -> None:
        self.location = location
        self.angle = angle
        self.color = color
        self.power = power

    def rotate(data: angle3D) -> None:
        pass

    def move(data: Point3D) -> None:
        pass
