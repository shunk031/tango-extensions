from tango_ext.common.testing import TangoExtentionsTestCase
from tango_ext.integrations.albumentations import AlbumentationsTransform


class TestAugmentations(TangoExtentionsTestCase):
    def test_all_transforms_registered(self):
        assert len(AlbumentationsTransform.list_available()) == 90

    def test_blue_transforms(self):
        assert "albumentations::Blur" in AlbumentationsTransform.list_available()

    def test_crop_transforms(self):
        assert "albumentations::RandomCrop" in AlbumentationsTransform.list_available()

    def test_dropout_transforms(self):
        assert (
            "albumentations::ChannelDropout" in AlbumentationsTransform.list_available()
        )

    def test_resize_transforms(self):
        assert "albumentations::RandomScale" in AlbumentationsTransform.list_available()

    def test_rotate_transforms(self):
        assert (
            "albumentations::RandomRotate90" in AlbumentationsTransform.list_available()
        )

    def test_geometric_transforms(self):
        assert (
            "albumentations::ShiftScaleRotate"
            in AlbumentationsTransform.list_available()
        )

    def test_domain_adaptation(self):
        assert (
            "albumentations::HistogramMatching"
            in AlbumentationsTransform.list_available()
        )

    def test_transforms(self):
        assert "albumentations::Normalize" in AlbumentationsTransform.list_available()
