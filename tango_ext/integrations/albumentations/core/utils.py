from typing import Optional, Sequence

from albumentations.core.composition import BboxParams, KeypointParams
from albumentations.core.utils import Params
from tango.common import Registrable


class AlbumentationsParams(Params, Registrable):
    @classmethod
    def is_serializable(cls) -> bool:
        return True

    @classmethod
    def get_class_fullname(cls) -> str:
        return cls.__name__


@AlbumentationsParams.register("albumentations::BboxParams")
class AlbumentationsBboxParams(BboxParams):
    def __init__(
        self,
        format: str,
        label_fields: Optional[Sequence[str]] = None,
        min_area: float = 0,
        min_visibility: float = 0,
        min_width: float = 0,
        min_height: float = 0,
        check_each_transform: bool = True,
    ) -> None:
        super().__init__(
            format,
            label_fields,
            min_area,
            min_visibility,
            min_width,
            min_height,
            check_each_transform,
        )


@AlbumentationsParams.register("albumentations::KeypointParams")
class AlbumentationsKeypointParams(KeypointParams):
    def __init__(
        self,
        format: str,
        label_fields: Optional[Sequence[str]] = None,
        remove_invisible: bool = True,
        angle_in_degrees: bool = True,
        check_each_transform: bool = True,
    ) -> None:
        super().__init__(
            format,
            label_fields,
            remove_invisible,
            angle_in_degrees,
            check_each_transform,
        )
