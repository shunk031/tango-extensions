from tango.common.exceptions import IntegrationMissingError

try:
    import diffusers  # NOQA
except ModuleNotFoundError:
    raise IntegrationMissingError("diffusers")

from tango_ext.integrations.diffusers.format import DiffusersPipelineFormat  # NOQA
