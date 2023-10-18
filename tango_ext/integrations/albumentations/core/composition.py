from typing import Dict, List, Optional

from albumentations.core.composition import (
    BaseCompose,
    Compose,
    OneOf,
    OneOrOther,
    ReplayCompose,
    Sequential,
    SomeOf,
)
from tango.common import Registrable

from ..transforms import AlbumentationsTransform
from .utils import AlbumentationsBboxParams, AlbumentationsKeypointParams


class AlbumentationsBaseCompose(BaseCompose, Registrable):
    pass


@AlbumentationsBaseCompose.register("albumentations::Compose")
class AlbumentationsCompose(Compose):
    def __init__(
        self,
        transforms: List[AlbumentationsTransform],
        bbox_params: Optional[AlbumentationsBboxParams] = None,
        keypoint_params: Optional[AlbumentationsKeypointParams] = None,
        additional_targets: Optional[Dict[str, str]] = None,
        p: float = 1,
        is_check_shapes: bool = True,
    ) -> None:
        super().__init__(
            transforms,
            bbox_params,
            keypoint_params,
            additional_targets,
            p,
            is_check_shapes,
        )


@AlbumentationsBaseCompose.register("albumentations::OneOf")
class AlbumentationsOneOf(OneOf):
    def __init__(
        self,
        transforms: List[AlbumentationsTransform],
        p: float = 0.5,
    ) -> None:
        super().__init__(transforms, p)


@AlbumentationsBaseCompose.register("albumentations::OneOrOther")
class AlbumentationsOneOrOther(OneOrOther):
    def __init__(
        self,
        first: Optional[AlbumentationsTransform] = None,
        second: Optional[AlbumentationsTransform] = None,
        transforms: Optional[List[AlbumentationsTransform]] = None,
        p: float = 0.5,
    ) -> None:
        super().__init__(first, second, transforms, p)


@AlbumentationsBaseCompose.register("albumentations::SomeOf")
class AlbumentationsSomeOf(SomeOf):
    def __init__(
        self,
        transforms: List[AlbumentationsTransform],
        n: int,
        replace: bool = True,
        p: float = 1,
    ) -> None:
        super().__init__(transforms, n, replace, p)


@AlbumentationsBaseCompose.register("albumentations::ReplayCompose")
class AlbumentationsReplayCompose(ReplayCompose):
    def __init__(
        self,
        transforms: List[AlbumentationsTransform],
        bbox_params: Optional[AlbumentationsBboxParams] = None,
        keypoint_params: Optional[AlbumentationsKeypointParams] = None,
        additional_targets: Optional[Dict[str, str]] = None,
        p: float = 1,
        is_check_shapes: bool = True,
        save_key: str = "replay",
    ) -> None:
        super().__init__(
            transforms,
            bbox_params,
            keypoint_params,
            additional_targets,
            p,
            is_check_shapes,
            save_key,
        )


@AlbumentationsBaseCompose.register("albumentations::Sequential")
class AlbumentationsSequential(Sequential):
    def __init__(
        self,
        transforms: List[AlbumentationsTransform],
        p: float = 0.5,
    ) -> None:
        super().__init__(transforms, p)
