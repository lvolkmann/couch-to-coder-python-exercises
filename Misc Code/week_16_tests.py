#Week 16 Session 1 Tests
import week_16_code as main
import unittest

class TestSample(unittest.TestCase):
    def test_get_area_rect_normal(self):
        area = main.get_area_rect(5,5)
        self.assertEqual(area, 25, "Did not return 25")
    def test_get_area_rect_zero(self):
        with self.assertRaises(ValueError):
            area = main.get_area_rect(5,0)
    def test_validate_input_normal(self):
        x = main.validate_input(5)
        self.assertEqual(x, True)
    def test_validate_input_neg(self):
        x = main.validate_input(-5)
        self.assertEqual(x, False)
    def test_true_if_hello_normal(self):
        x = main.true_if_hello("hello")
        self.assertEqual(x, True)
    def test_true_if_hello_bad_string(self):
        x = main.true_if_hello('dog')
        self.assertEqual(x, False)
    def test_true_if_hello_int(self):
        x = main.true_if_hello(7)
        self.assertEqual(x, False)

unittest.main()
