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

    def __str__(self):
        return "Equilateral Triangle, a = {}".format(self.a)

    @classmethod
    def get_perimeter_formula(cls):
        return "3 * a"

    @classmethod
    def get_area_formula(cls):
        return "(a2 sqrt(5(5+2sqrt(5))))/4"



class Rectangle(Shape):
    """
    This class represents Rectangle shape
    Parent Class: Shape
    Args:
        a (float): the length of the first side of the rectangle
        b (float): the length of the second side of the rectangle
    """

    def __init__(self, a, b):
        if (a <= 0) or (b <= 0):
            raise ValueError("Rectangle sides values are incorrect.")
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def get_perimeter(self):
        return 2 * (self.a + self.b)

    def __str__(self):
        return "Rectangle, a = {}, b = {}".format(self.a, self.b)

    @classmethod
    def get_perimeter_formula(cls):
        return "2 * (a + b)"

    @classmethod
    def get_area_formula(cls):
        return "a * b"


class Square(Rectangle):
    """
    This class represents Square shape
    Parent Class: Rectangle
    Args:
        a (float): the length of the side of the square
    """
    def __init__(self, a):
        Rectangle.__init__(self, a, b=a)

    def __str__(self):
        return "Square, a = {}".format(self.a)

    @classmethod
    def get_perimeter_formula(cls):
        return "4 * a"

    @classmethod
    def get_area_formula(cls):
        return "a * a"

class RegularPentagon(Shape):
    """
    This class represents Regular Pentagon shape
    Parent Class: Shape
    Args:
        a (float): the length of the side of the regular pentagon
    """

    def __init__(self, a):
        if a <= 0:
            raise ValueError("Regular pentagon side value is incorrect.")
        self.a = a

    def get_area(self):
        return pow(self.a, 2) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) / 4

    def get_perimeter(self):
        return self.a * 5

    def __str__(self):
        return "Regular pentagon, a = {}".format(self.a)

    @classmethod
    def get_perimeter_formula(cls):
        return "5 * a"

    @classmethod
    def get_area_formula(cls):
        return "a2 * sqrt(5(5+2sqrt(5))))/4"


class ShapeList:
    '''
    This class is meant to hold geometrical shapes (objects that inherit from Shape class).
    Parent Class: None
    Args:
        shapes: list of Shape objects
    '''

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        # Adds shape to shapes list
        # Check if shape's has Shape class as it's ancestor. If not it should raise `TypeError`
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            raise TypeError

    def get_shapes_table(self):
        # This method returns shapes list as string formatted into table

        list_heading = ["idx", "Class", "__str__", "Perimeter", "Formula", "Area", "Formula"]
        table = []
        idx = 0
        for shape in self.shapes:
            table.append([str(idx), shape.__class__.__name__, shape.__str__(), shape.get_perimeter(),
                          shape.__class__.get_perimeter_formula(), shape.get_area(),
                          shape.__class__.get_area_formula()])
            idx += 1
        table.insert(0, list_heading)
        print(table)

    def get_largest_shape_by_perimeter(self):
        # Returns shape with largest perimeter

        if self.shapes:
            largest_shape = self.shapes[0]
            for shape in self.shapes:
                if shape.get_perimeter().__gt__(largest_shape.get_perimeter()):
                    largest_shape = shape
            return largest_shape
        else:
            return False

    def get_largest_shape_by_area(self):
        # Returns shape with largest area

        if self.shapes:
            largest_shape = self.shapes[0]
            for shape in self.shapes:
                if shape.get_area().__gt__(largest_shape.get_area()):
                    largest_shape = shape
            return largest_shape
        else:
            return False




