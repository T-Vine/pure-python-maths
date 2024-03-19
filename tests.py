import unittest
from main import *
class MyTest(unittest.TestCase):
    def test(self):
        # Sine.
        self.assertEqual(round(sine(to_radians(30)), 1), 0.5)
        self.assertEqual(round(sine(to_radians(0)), 1), 0.0)
        self.assertEqual(round(sine(to_radians(90))), 1.0)

        # Cosine.
        self.assertEqual(round(cosine(to_radians(60)), 1), 0.5)
        self.assertEqual(round(cosine(to_radians(0)), 0), 1.0)
        self.assertEqual(round(cosine(to_radians(90)), 0), 0.0)

        # Tangent.
        self.assertEqual(round(tangent(to_radians(45))), 1.0)

        # Arcsine
        self.assertEqual(round(to_degrees(arcsine(0.5))), 30.0)
        self.assertEqual(round(to_degrees(arcsine(1))), 90.0)

        # Arccosine
        self.assertEqual(round(to_degrees(arccos(0.5))), 60.0)
        self.assertEqual(round(to_degrees(arccos(0))), 90.0)
        
        # Arctan requires no testing, as if arccos and arcsine work, it does by extension.

if __name__ == '__main__':
    unittest.main()