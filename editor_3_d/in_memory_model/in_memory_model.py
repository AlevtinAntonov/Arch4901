from typing import List

from editor_3_d.model_elements.camera import Camera
from editor_3_d.model_elements.flash import Flash
from editor_3_d.model_elements.poligonal_model import PoligonalModel
from editor_3_d.model_elements.scene import Scene


class IModelChangedObserver:
    def apply_update_model(self):
        pass


class IModelChanger:
    def notify_change(self, sender: IModelChanger):
        pass


class ModelStore(IModelChanger):

    def __init__(self, models: PoligonalModel,
                 scenes: Scene,
                 flashes: Flash,
                 cameras: Camera,
                 changed_observer: List[IModelChangedObserver]) -> None:

        self.models = models
        self.scenes = scenes
        self.flashes = flashes
        self.cameras = cameras
        self.__changed_observer = changed_observer

    def get_scena(self, id):
        for scene in self.scenes:
            if scene.id == id:
                return scene

    def notify_change(self, sender: IModelChanger):
        pass
