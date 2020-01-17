import math

class ComplexNumber:

    def __init__(self, real_part, imaginary_part):

        if type(real_part) != int and type(real_part) != float:
            raise TypeError("The real part of the number must be an integer or a floating point number.")

        if type(imaginary_part) != int and type(imaginary_part) != float:
            raise TypeError("The imaginary part of the number must be an integer or a floating point number.")

        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def add(self, complex_number):

        if type(complex_number) != ComplexNumber:
            raise TypeError("The argument must be a ComplexNumber object.")

        return ComplexNumber(self.real_part + complex_number.real_part, self.imaginary_part + complex_number.imaginary_part)

    def multiply(self, complex_number):

        if type(complex_number) != ComplexNumber:
            raise TypeError("The argument must be a ComplexNumber object.")

        return ComplexNumber(self.real_part * complex_number.real_part - self.imaginary_part * complex_number.imaginary_part, \
                             self.real_part * complex_number.imaginary_part + self.imaginary_part * complex_number.real_part)

    def conjugate(self):
        return ComplexNumber(self.real_part, -self.imaginary_part)

    def absolute_value(self):
        return math.sqrt(self.real_part ** 2 + self.imaginary_part ** 2)

    def divide(self, complex_number):

        if type(complex_number) != ComplexNumber:
            raise TypeError("The argument must be a ComplexNumber object.")

        if complex_number.real_part == 0 and complex_number.imaginary_part == 0:
               raise ValueError("The argument cannot be the complex number 0, as it would cause a division by 0.")

        multiplication_result = self.multiply(complex_number.conjugate())
        denominator = complex_number.absolute_value() ** 2
        return ComplexNumber(multiplication_result.real_part / denominator, multiplication_result.imaginary_part / denominator)

    def __str__(self):
        return str(self.real_part) + ("+" if self.imaginary_part >= 0 else "-") + str(self.imaginary_part) + "i"