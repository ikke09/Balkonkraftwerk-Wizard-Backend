from unittest import TestCase
from api.models import VersionModel
from api.serializers import BalconySerializer


class VersionModelTest(TestCase):

    def test_default_version_is_correct(self):
        v = VersionModel()
        self.assertEqual(v.major, 0)
        self.assertEqual(v.minor, 0)
        self.assertEqual(v.patch, 1)


class BalconySerializerTest(TestCase):

    def test_with_valid_base64_img(self):
        img = "iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=="
        width = 1200
        height = 900
        data = {'img': img, 'width': width, 'height': height}

        serializer = BalconySerializer(data)

        self.assertTrue(serializer.is_valid())
