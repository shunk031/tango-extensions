from typing import Type

import pytest
import torch
from diffusers import (
    DiffusionPipeline,
    StableDiffusionImg2ImgPipeline,
    StableDiffusionInpaintPipeline,
    StableDiffusionPipeline,
)

from tango_ext.common.testing import TangoExtentionsTestCase
from tango_ext.integrations.diffusers import DiffusersPipeline


class TestDiffusersPipelineFormat(TangoExtentionsTestCase):
    @pytest.fixture(scope="class")
    def model_id(self) -> str:
        return "runwayml/stable-diffusion-v1-5"

    @pytest.fixture(scope="class")
    def revision(self) -> str:
        return "fp16"

    @pytest.fixture(scope="class")
    def torch_dtype(self) -> torch.dtype:
        return torch.float16

    def test_read_write(
        self, model_id: str, revision: str, torch_dtype: torch.dtype
    ) -> None:
        pipeline = StableDiffusionPipeline.from_pretrained(
            model_id, revision=revision, torch_dtype=torch_dtype
        )

        pipeline_format = DiffusersPipeline[StableDiffusionPipeline]()
        pipeline_format.write(artifact=pipeline, dir=self.TEST_DIR)  # type: ignore

        assert (self.TEST_DIR / "pipeline").exists()
        assert pipeline_format.read(self.TEST_DIR)

    @pytest.mark.parametrize(
        argnames="pipeline_cls, pipeline_model_id",
        argvalues=(
            (DiffusionPipeline, "runwayml/stable-diffusion-v1-5"),
            (StableDiffusionInpaintPipeline, "runwayml/stable-diffusion-inpainting"),
            (StableDiffusionImg2ImgPipeline, "runwayml/stable-diffusion-v1-5"),
        ),
    )
    def test_read_write_pipeline(
        self,
        pipeline_cls: Type[DiffusionPipeline],
        pipeline_model_id: str,
        revision: str,
        torch_dtype: torch.dtype,
    ) -> None:
        pipeline = pipeline_cls.from_pretrained(
            pipeline_model_id, revision=revision, torch_dtype=torch_dtype
        )

        pipeline_format = DiffusersPipeline[pipeline_cls](pipeline_cls=pipeline_cls)
        pipeline_format.write(artifact=pipeline, dir=self.TEST_DIR)

        assert (self.TEST_DIR / "pipeline").exists()
        assert pipeline_format.read(self.TEST_DIR)
