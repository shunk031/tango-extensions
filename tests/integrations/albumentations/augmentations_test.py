from tango_ext.common.testing import TangoExtentionsTestCase
from tango_ext.integrations.albumentations import AlbumentationsTransform


class TestAugmentations(TangoExtentionsTestCase):
    def test_all_transforms_registered(self):
        assert len(AlbumentationsTransform.list_available()) == 89

    def test_blue_transforms(self):
        assert "albumentations::Blur" in AlbumentationsTransform.list_available()

    def test_crop_transforms(self):
        assert "albumentations::RandomCrop" in AlbumentationsTransform.list_available()

    def test_dropout_transforms(self):
        assert (
            "albumentations::ChannelDropout" in AlbumentationsTransform.list_available()
        )
