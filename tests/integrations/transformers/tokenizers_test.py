from tango.common import Params
from tango.integrations.transformers.tokenizer import Tokenizer
from transformers import CLIPTokenizer


def test_clip_tokenizer():
    params = Params(
        {
            "pretrained_model_name_or_path": "runwayml/stable-diffusion-v1-5",
            "subfolder": "tokenizer",
            "use_fast": False,
        }
    )
    tokenizer_tango = Tokenizer.from_params(params)

    tokenizer_transformers = CLIPTokenizer.from_pretrained(
        pretrained_model_name_or_path="runwayml/stable-diffusion-v1-5",
        subfolder="tokenizer",
    )

    breakpoint()
