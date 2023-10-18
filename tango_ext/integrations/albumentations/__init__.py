from tango.common.exceptions import IntegrationMissingError

try:
    import albumentations  # NOQA
except ModuleNotFoundError:
    raise IntegrationMissingError("albumentations")

from .core import *  # NOQA
from .augmentations import *  # NOQA
