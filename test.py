import unittest
import main as main


class TestValidIds(unittest.TestCase):

    def test_valid(self):
        self.assertTrue(main.check_id_valid(3))

    def test_invalid(self):
        self.assertFalse(main.check_id_valid(51))


if __name__ == '__main__':
    unittest.main()
