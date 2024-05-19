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

    def test_abbrv(self):
        result = pycasino.abbrv(1_000)
        self.assertEqual(result, "1K")

        result = pycasino.abbrv(1_000_000)
        self.assertEqual(result, "1M")

        result = pycasino.abbrv(32_450)
        self.assertEqual(result, "32.45K")

        result = pycasino.abbrv(123_456_789)
        self.assertEqual(result, "123.46M")

        result = pycasino.abbrv(1_500)
        self.assertEqual(result, "1.5K")

        result = pycasino.abbrv(1_530)
        self.assertEqual(result, "1.53K")



if __name__ == "__main__":
    unittest.main()
