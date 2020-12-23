import unittest
from Weight import Weight


class TestWeight(unittest.TestCase):
    test = Weight(45.78)
    test1 = Weight(100.75)
    test2 = Weight(100.25)
    test3 = Weight(65.2)
    t4 = Weight(2.2)
    t5 = Weight(1.1)

    def test_str(self):
        self.assertEqual(self.test.__str__(), '45.0 centners and 78.0 kilos')
        self.assertTrue(self.test.__str__(), isinstance(self.test.__str__(), str))

    def test_add(self):
        self.assertEqual(self.test1 + self.test2, (201.0, 0.0))
        self.assertRaises(TypeError, self.test.__add__, 'k')

    def test_sub(self):
        self.assertEqual(self.test2 - self.test3, (35.0, 5.0))

    def test_mul(self):
        self.assertEqual(self.t4*self.t5,(4.0,0.0))


if __name__ == '__main__':
    unittest.main()
