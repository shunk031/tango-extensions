from pathlib import Path
from typing import Generic, Optional, Type, TypeVar

from diffusers import StableDiffusionPipeline
from tango.common.aliases import PathOrStr
from tango.format import Format

T = TypeVar("T")


@Format.register("diffuers::pipeline")
class DiffusersPipelineFormat(Format[T], Generic[T]):
    VERSION: str = "001"

    def __init__(self, pipeline_cls: Optional[Type[T]] = None) -> None:
        super().__init__()
        self.pipeline_cls = pipeline_cls or StableDiffusionPipeline

    def _check(self, artifact: T) -> None:
        if not isinstance(artifact, self.pipeline_cls):
            raise ValueError(
                f"Invalid pipeline type: {type(artifact)}. "
                f"Expected: {self.pipeline_cls}."
            )

    def write(self, artifact: T, dir: PathOrStr) -> None:
        self._check(artifact=artifact)

        filename = Path(dir) / "pipeline"
        artifact.save_pretrained(filename)  # type: ignore

    def read(self, dir: PathOrStr) -> T:
        filename = Path(dir) / "pipeline"
        return self.pipeline_cls.from_pretrained(filename)  # type: ignore
