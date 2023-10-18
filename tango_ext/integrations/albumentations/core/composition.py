from albumentations.core import composition
from albumentations.core.composition import BaseCompose
from albumentations.core.utils import Params
from tango.common import Registrable


class AlbumentationsCompose(BaseCompose, Registrable):
    pass


class AlbumentationsParams(Params, Registrable):
    @classmethod
    def is_serializable(cls) -> bool:
        return True

    @classmethod
    def get_class_fullname(cls) -> str:
        return "RegistrableAlbumentationsParams"


for name, cls in composition.__dict__.items():
    if isinstance(cls, type) and issubclass(cls, BaseCompose) and cls != BaseCompose:
        AlbumentationsCompose.register("albumentations::" + name)(cls)
    elif isinstance(cls, type) and issubclass(cls, AlbumentationsParams):
        AlbumentationsParams.register("albumentations::" + name)(cls)
