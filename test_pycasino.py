import unittest
import pycasino as pyca

class TestPycasino(unittest.TestCase):
    def test_expand(self):
        result = pyca.expand("1.5K")
        self.assertEqual(result, 1500)

        result = pyca.expand("3.9k")
        self.assertEqual(result, 3900)

        result = pyca.expand("53m")
        self.assertEqual(result, 53_000_000)


if "__name__" == "__main__":
    unittest.main()
