from unittest import (
    mock,
    TestCase,
)


class TestDummy(TestCase):

    def test_dummy(self):
        magic = mock.MagicMock()
        magic.cast = 'spell'
        self.assertEqual(magic.cast, 'spell')

    def test_other_dummy(self):
        magic = mock.MagicMock()
        magic.cast = 'spell'
        self.assertEqual(magic.cast, 'spell')
