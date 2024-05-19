import sys
import unittest

sys.path.append("..")

import utils


class TestUtils(unittest.TestCase):
    def test_expand(self):
        result = utils.expand("1.5K")
        self.assertEqual(result, 1500)

        result = utils.expand("3.9k")
        self.assertEqual(result, 3900)

        result = utils.expand("53m")
        self.assertEqual(result, 53_000_000)

    def test_abbrv(self):
        result = utils.abbrv(1_000)
        self.assertEqual(result, "1K")

        result = utils.abbrv(1_000_000)
        self.assertEqual(result, "1M")

        result = utils.abbrv(32_450)
        self.assertEqual(result, "32.45K")

        result = utils.abbrv(123_456_789)
        self.assertEqual(result, "123.46M")

        result = utils.abbrv(1_500)
        self.assertEqual(result, "1.5K")

        result = utils.abbrv(1_530)
        self.assertEqual(result, "1.53K")


if __name__ == "__main__":
    unittest.main()
