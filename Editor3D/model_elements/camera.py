from Editor3D.model_elements.angle3D import Angle3D
from Editor3D.model_elements.point3D import Point3D


class Camera:
    def __init__(self, location: Point3D, angle: Angle3D) -> None:
        self.location = location
        self.angle = angle

    def rotate(data: Angle3D) -> None:
        pass

    def move(data: Point3D) -> None:
        pass
