import unittest
import business_logic as bl

class ComplexNumberConstructorTests(unittest.TestCase):

    def test_normal_constructor(self):
        real_part = 1
        imaginary_part = 2
        number = bl.ComplexNumber(real_part, imaginary_part)
        self.assertEqual(real_part, number.real_part)
        self.assertEqual(imaginary_part, number.imaginary_part)

    def test_first_argument_type(self):
        with self.assertRaises(TypeError):
            number = bl.ComplexNumber([1, 2], 2.)

    def test_second_argument_type(self):
        with self.assertRaises(TypeError):
            number = bl.ComplexNumber(3, [1, 5])

class ComplexNumberMethodTests(unittest.TestCase):

    def test_add_argument_type(self):
        number = bl.ComplexNumber(1, 2)
        with self.assertRaises(TypeError):
            result = number.add(1)

    def test_multiply_argument_type(self):
        number = bl.ComplexNumber(1, 2)
        with self.assertRaises(TypeError):
            result = number.multiply(1)

    def test_divide_argument_type(self):
        number = bl.ComplexNumber(1, 2)
        with self.assertRaises(TypeError):
            result = number.divide(1)  

    def test_divide_by_zero(self):
        number = bl.ComplexNumber(1, 2)
        zero = bl.ComplexNumber(0, 0)
        with self.assertRaises(ValueError):
            result = number.divide(zero)      
