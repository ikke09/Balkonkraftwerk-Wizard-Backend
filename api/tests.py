import unittest
from api.models import Version


class VersionModelTest(unittest.TestCase):

    def test_default_version_is_correct(self):
        v = Version()
        self.assertEqual(v.major, 0)
        self.assertEqual(v.minor, 0)
        self.assertEqual(v.patch, 1)


if __name__ == '__main__':
    unittest.main()
