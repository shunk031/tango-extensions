from albumentations import augmentations, pytorch
from albumentations.core.transforms_interface import (
    BasicTransform,
    DualTransform,
    ImageOnlyTransform,
)
from tango.common import Registrable


class AlbumentationsTransform(BasicTransform, Registrable):
    pass


for name, cls in augmentations.__dict__.items():
    if (
        isinstance(cls, type)
        and issubclass(cls, BasicTransform)
        and cls not in (BasicTransform, DualTransform, ImageOnlyTransform)
    ):
        AlbumentationsTransform.register("albumentations::" + name)(cls)


for name, cls in pytorch.__dict__.items():
    if isinstance(cls, type) and issubclass(cls, BasicTransform):
        AlbumentationsTransform.register("albumentations::" + name)(cls)
