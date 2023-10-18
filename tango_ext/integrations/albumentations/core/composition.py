from albumentations.core import composition
from albumentations.core.composition import BaseCompose
from albumentations.core.utils import Params
from tango.common import Registrable


class AlbumentationsBaseCompose(BaseCompose, Registrable):
    pass


class AlbumentationsParams(Params, Registrable):
    @classmethod
    def is_serializable(cls) -> bool:
        return True

    @classmethod
    def get_class_fullname(cls) -> str:
        return cls.__name__


for name, cls in composition.__dict__.items():
    if isinstance(cls, type) and issubclass(cls, BaseCompose) and cls != BaseCompose:
        AlbumentationsBaseCompose.register("albumentations::" + name)(cls)
    elif isinstance(cls, type) and issubclass(cls, Params):
        AlbumentationsParams.register("albumentations::" + name)(cls)
