from tango_ext.common.testing import TangoExtentionsTestCase
from tango_ext.integrations.albumentations import (
    AlbumentationsBaseCompose,
    AlbumentationsParams,
)


class TestComposition(TangoExtentionsTestCase):
    def test_all_compotisions_registered(self):
        assert len(AlbumentationsBaseCompose.list_available()) == 6

    def test_composition(self):
        assert "albumentations::Compose" in AlbumentationsBaseCompose.list_available()

    def test_all_params_registered(self):
        assert len(AlbumentationsParams.list_available()) == 2

    def test_params(self):
        assert "albumentations::BboxParams" in AlbumentationsParams.list_available()
