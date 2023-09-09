from typing import TypedDict

import pytest
import torch
from diffusers import (
    StableDiffusionImg2ImgPipeline,
    StableDiffusionInpaintPipeline,
    StableDiffusionPipeline,
)

from tango_ext.common.testing import TangoExtentionsTestCase
from tango_ext.integrations.diffusers import (
    DiffusersPipelineForImage2Image,
    DiffusersPipelineForInpainting,
    DiffusersPipelineForText2Image,
)


class Params(TypedDict):
    pretrained_model_or_path: str
    torch_dtype: torch.dtype


class TestDiffusersPipeline(TangoExtentionsTestCase):
    @pytest.fixture
    def model_id(self) -> str:
        return "runwayml/stable-diffusion-v1-5"

    @pytest.fixture
    def params(self, model_id: str) -> Params:
        return {
            "pretrained_model_or_path": model_id,
            "torch_dtype": torch.float16,
        }

    def test_diffusers_pipeline_for_image_2_image(self, params: Params):
        pipeline = DiffusersPipelineForImage2Image.from_params(params)  # type: ignore
        assert isinstance(pipeline, StableDiffusionImg2ImgPipeline)

    def test_diffusers_pipeline_for_inpainting(self, params: Params):
        pipeline = DiffusersPipelineForInpainting.from_params(params)  # type: ignore
        assert isinstance(pipeline, StableDiffusionInpaintPipeline)

    def test_diffusers_pipeline_for_text_2_image(self, params: Params):
        pipeline = DiffusersPipelineForText2Image.from_params(params)  # type: ignore
        assert isinstance(pipeline, StableDiffusionPipeline)
