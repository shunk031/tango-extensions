from diffusers import (
    AutoPipelineForImage2Image,
    AutoPipelineForInpainting,
    AutoPipelineForText2Image,
)
from diffusers.configuration_utils import ConfigMixin
from tango.common import Registrable


class DiffusersPipelineForImage2Image(ConfigMixin, Registrable):
    default_implementation = "auto"


DiffusersPipelineForImage2Image.register("auto", constructor="from_pretrained")(
    AutoPipelineForImage2Image
)


class DiffusersPipelineForInpainting(ConfigMixin, Registrable):
    default_implementation = "auto"


DiffusersPipelineForInpainting.register("auto", constructor="from_pretrained")(
    AutoPipelineForInpainting
)


class DiffusersPipelineForText2Image(ConfigMixin, Registrable):
    default_implementation = "auto"


DiffusersPipelineForText2Image.register("auto", constructor="from_pretrained")(
    AutoPipelineForText2Image
)
