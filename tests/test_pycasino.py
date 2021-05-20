import sys
import unittest

sys.path.append('..')

import pycasino

class TestPycasino(unittest.TestCase):
    def test_expand(self):
        result = pycasino.expand("1.5K")
        self.assertEqual(result, 1500)

        result = pycasino.expand("3.9k")
        self.assertEqual(result, 3900)

        result = pycasino.expand("53m")
        self.assertEqual(result, 53_000_000)


if __name__ == "__main__":
    unittest.main()
