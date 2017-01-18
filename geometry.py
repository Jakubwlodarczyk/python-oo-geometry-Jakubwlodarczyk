import math

class Shape:
    """
    This is a abstract class representing geometrical shape.
    """

    def __init__(self):
        """
        Constructs Shape object

        Raises:
            ValueError: If any of the parameters is below 0.
        """
        pass

    def get_area(self):
        """
        Calculates shape's area.

        Returns:
            float: area of the shape
        """
        pass

    def get_perimeter(self):
        """
        Calculates shape's perimeter.

        Returns:
            float: perimeter of the shape
        """
        pass

    def __str__(self):
        """
        Returns information about the shape as string.

        Returns:
            str: information bout shape
        """
        pass

    @classmethod
    def get_area_formula(cls):
        """
        Returns formula for the area of the shape as a string.

        Returns:
            str: area formula
        """
        pass

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns formula for the perimeter of the shape as a string.

        Returns:
            str: perimeter formula
        """
        pass


class Circle(Shape):
    """
    This class represents Circle shape
    Parent Class: Shape
    Args:
        r (float): circle radius length
    """

    def __init__(self, r):
        if r <= 0:
            raise ValueError("Circle radius value is incorrect.")
        self.r = r

    def get_area(self):
        # calculates the area of circle = π×r^2
        return math.pi * math.pow(self.r, 2)

    def get_perimeter(self):
        # calculates the perimeter of circle = 2×π×r
        return 2 * math.pi * self.r

    def __str__(self):
        return "Circle, r = {}".format(self.r)

    @classmethod
    def get_area_formula(cls):
        return "π×r2"

    @classmethod
    def get_perimeter_formula(cls):
        return "2×π×r"



class Triangle(Shape):
    """
    This class represents Triangle shape
    Parent Class: Shape
    Args:
        a (float): the length of the first side of the triangle
        b (float): the length of the second side of the triangle
        c (float): the length of the third side of the triangle
    """

    def __init__(self, a, b, c):
        if (a <= 0) or (b <= 0) or (c <= 0):
            raise ValueError("Value of the side of triangle is incorrect.")
        if (a >= b + c) or (b >= a + c) or (c >= a + b):
            raise ValueError("Wrong value. Triangle cant be build with that length of sides {}, {}, {}.".format(a, b, c))

        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        """
        calculates the area of a triangle using the formula:
        a, b, b - length of sides of triangle
        s = half of the length of the perimeter of the triangle
        area = square root of ((s-a) * (b-s) * (p-c))
        """
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def get_perimeter(self):
        return self.a + self.b + self.c

    def __str__(self):
        return "Triangle, a = {}, b = {}, c = {}".format(self.a, self.b, self.c)

    @classmethod
    def get_area_formula(cls):
        return "sqrt(s(s-a)(s-b)(s-c)), s = (a+b+c)/2"

    @classmethod
    def get_perimeter_formula(cls):
        return "a + b + c"


class EquilateralTriangle(Triangle):
    """
    This class represents Equilateral Triangle shape
    Parent Class: Triangle
    Args:
        a (float): the length of the side of the triangle
    """

    def __init__(self, a):
        Triangle.__init__(self, a, b=a, c=a)

    def get_area(self):
        return ((a*a) * math.sqrt(3)) / 4

    def get_perimeter(self):
        return 3 * self.a

    def __str__(self):
        return "Equilateral Triangle, a = {}".format(self.a)

    @classmethod
    def get_perimeter_formula(cls):
        return "3 * a"

    @classmethod
    def get_area_formula(cls):
        return "(a2 * sqrt(3))/4"



class Rectangle(Shape):
    pass


class Square(Rectangle):
    pass


class RegularPentagon(Shape):
    pass


class ShapeList:
    pass
