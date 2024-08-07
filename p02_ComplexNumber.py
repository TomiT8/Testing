# todo:
#   Nadefinovať triedu ComplexNumber reprezentujúcu komplecné číslo a metódy:
#   __init__ (konstruktor)
#   __eq__ (rovnosť)
#   __lt__ (<)
#   __gt__ (>)
#   __repr__
#   __str__
#   properties (pre reálnu a imaginárnu časť)
#   add (sčítanie)
#   subtract (odčítanie)
#   multiply (násobenie)
#   divide (delenie)
#   conjugate (číslo komplexné združené)
#   absolute_nalue (absolútna hodnota)
#   ku všetkému napísať test

import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, real):
        if isinstance(real, int) or isinstance(real, float):
            self.__real = real
        else:
            raise Exception

    @property
    def imaginary(self):
        return self.__imaginary

    @imaginary.setter
    def imaginary(self, imaginary):
        if isinstance(imaginary, int) or isinstance(imaginary, float):
            self.__imaginary = imaginary
        else:
            raise Exception

    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imaginary == other.imaginary
        return False

    def __lt__(self, other):
        if isinstance(other, ComplexNumber):
            return math.sqrt(self.real ** 2 + self.imaginary ** 2) < math.sqrt(other.real ** 2 + other.imaginary ** 2)
        return False

    def __gt__(self, other):
        if isinstance(other, ComplexNumber):
            return math.sqrt(self.real ** 2 + self.imaginary ** 2) > math.sqrt(other.real ** 2 + other.imaginary ** 2)
        return False

    def __repr__(self):
        return f'ComplexNumber {self.real}, {self.imaginary}i'

    def __str__(self):
        if self.imaginary >= 0:
            return f'ComplexNumber is {self.real} +{self.imaginary}i.'
        else:
            return f'ComplexNumber is {self.real} {self.imaginary}i.'

    def add(self, other):
        new_real = (self.real + other.real)
        new_imaginary = (self.imaginary + other.imaginary)
        if ((isinstance(new_real, int) or isinstance(new_real, float)) and
                (isinstance(new_imaginary, int) or isinstance(new_imaginary, float))):
            return ComplexNumber(new_real, new_imaginary)

    def subtract(self, other):
        new_real = (self.real - other.real)
        new_imaginary = (self.imaginary - other.imaginary)
        if ((isinstance(new_real, int) or isinstance(new_real, float)) and
                (isinstance(new_imaginary, int) or isinstance(new_imaginary, float))):
            return ComplexNumber(new_real, new_imaginary)

    def multiply(self, other):
        new_real = (self.real * other.real - self.imaginary * other.imaginary)
        new_imaginary = (self.real * other.imaginary + self.imaginary * other.real)
        if ((isinstance(new_real, int) or isinstance(new_real, float)) and
                (isinstance(new_imaginary, int) or isinstance(new_imaginary, float))):
            return ComplexNumber(new_real, new_imaginary)

    def divide(self, other):
        try:
            new_real = round(((self.real * other.real + self.imaginary * other.imaginary) /(other.real ** 2 + other.imaginary ** 2)),3)
            new_imaginary = round(((self.imaginary * other.real - self.real * other.imaginary) / (other.real ** 2 + other.imaginary ** 2)),3)
            if ((isinstance(new_real, int) or isinstance(new_real, float)) and
                    (isinstance(new_imaginary, int) or isinstance(new_imaginary, float))):
                return ComplexNumber(new_real, new_imaginary)
        except:
            return None

    def conjugate(self):
        new_imaginary = - self.imaginary
        return f'Conjugate is {self.real} {new_imaginary}i'
    def absolute_value(self):
        return round(math.sqrt(self.real ** 2 + self.imaginary ** 2),3)

num1 = ComplexNumber(1, 2)
num2 = ComplexNumber(3, 8)
print(f'Num1 real part is {num1.real} and imaginary part is {num1.imaginary}i.')
print(num1.add(num2))                   # 4 +10i
print(num1.subtract(num2))              # -2 -6i
print(num1.multiply(num2))              # -13 147i
print(num1.divide(num2))                # 0.260 -0,027i
print(num1 == num2)                     # False
print(num1 < num2)                      # True
print(num1 > num2)                      # False
print(num2.absolute_value())            # 8.544
print(f'{num2} {num2.conjugate()}.')    # 3 -8i
