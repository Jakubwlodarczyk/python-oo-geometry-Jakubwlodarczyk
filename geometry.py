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
    perimeter_formula = '2 × π × r'
    area_formula = 'π × r^2'

    def __init__(self, r):
        if r <= 0:
            raise ValueError("Circle radius value is incorrect.")
        self.r = r
        self.perimeter = self.get_perimeter()
        self.area = self.get_area()

    def get_area(self):
        return round(math.pi * math.pow(self.r, 2))

    def get_perimeter(self):
        return round(2 * math.pi * self.r)

    def __str__(self):
        return "Circle, r = {}".format(self.r)

    @classmethod
    def get_area_formula(cls):
        return cls.area_formula

    @classmethod
    def get_perimeter_formula(cls):
        return cls.perimeter_formula


class Triangle(Shape):
    """
    This class represents Triangle shape
    Parent Class: Shape
    Args:
        a (float): the length of the first side of the triangle
        b (float): the length of the second side of the triangle
        c (float): the length of the third side of the triangle
    """

    perimeter_formula = "a + b + c"
    area_formula = "sqrt(s(s-a)(s-b)(s-c))"

    def __init__(self, a, b, c):
        if (a <= 0) or (b <= 0) or (c <= 0):
            raise ValueError("Value of the side of triangle is incorrect.")
        if (a >= b + c) or (b >= a + c) or (c >= a + b):
            raise ValueError("Wrong value. Triangle cant be build with that length of sides {}, {}, {}.".format(a, b, c))

        self.a = a
        self.b = b
        self.c = c
        self.perimeter = self.get_perimeter()
        self.area = self.get_area()

    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        return round(math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)))

    def get_perimeter(self):
        return round(self.a + self.b + self.c)

    def __str__(self):
        return "Triangle, a = {}, b = {}, c = {}".format(self.a, self.b, self.c)

    @classmethod
    def get_area_formula(cls):
        return cls.area_formula

    @classmethod
    def get_perimeter_formula(cls):
        return cls.perimeter_formula


class EquilateralTriangle(Triangle):
    """
    This class represents Equilateral Triangle shape
    Parent Class: Triangle
    Args:
        a (float): the length of the side of the triangle
    """

    perimeter_formula = "3 * a"
    area_formula = "(a2 sqrt(5(5+2sqrt(5))))/4"

    def __init__(self, a):
        Triangle.__init__(self, a, b=a, c=a)

    def __str__(self):
        return "Equilateral Triangle, a = {}".format(self.a)

    @classmethod
    def get_perimeter_formula(cls):
        return cls.perimeter_formula

    @classmethod
    def get_area_formula(cls):
        return cls.area_formula


class Rectangle(Shape):
    """
    This class represents Rectangle shape
    Parent Class: Shape
    Args:
        a (float): the length of the first side of the rectangle
        b (float): the length of the second side of the rectangle
    """

    perimeter_formula = "2 * (a + b)"
    area_formula = "a * b"

    def __init__(self, a, b):
        if (a <= 0) or (b <= 0):
            raise ValueError("Rectangle sides values are incorrect.")
        self.a = a
        self.b = b
        self.perimeter = self.get_perimeter()
        self.area = self.get_area()

    def get_area(self):
        return round(self.a * self.b)

    def get_perimeter(self):
        return round(2 * (self.a + self.b))

    def __str__(self):
        return "Rectangle, a = {}, b = {}".format(self.a, self.b)

    @classmethod
    def get_perimeter_formula(cls):
        return cls.perimeter_formula

    @classmethod
    def get_area_formula(cls):
        return cls.area_formula


class Square(Rectangle):
    """
    This class represents Square shape
    Parent Class: Rectangle
    Args:
        a (float): the length of the side of the square
    """

    perimeter_formula = "4 * a"
    area_formula = "a * a"

    def __init__(self, a):
        Rectangle.__init__(self, a, b=a)

    def __str__(self):
        return "Square, a = {}".format(self.a)

    @classmethod
    def get_perimeter_formula(cls):
        return cls.perimeter_formula

    @classmethod
    def get_area_formula(cls):
        return cls.area_formula

class RegularPentagon(Shape):
    """
    This class represents Regular Pentagon shape
    Parent Class: Shape
    Args:
        a (float): the length of the side of the regular pentagon
    """

    perimeter_formula = "5 * a"
    area_formula = "a2 * sqrt(5(5+2sqrt(5))))/4"

    def __init__(self, a):
        if a <= 0:
            raise ValueError("Regular pentagon side value is incorrect.")
        self.a = a
        self.perimeter = self.get_perimeter()
        self.area = self.get_area()

    def get_area(self):
        return round(pow(self.a, 2) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) / 4)

    def get_perimeter(self):
        return round(self.a * 5)

    def __str__(self):
        return "Regular pentagon, a = {}".format(self.a)

    @classmethod
    def get_perimeter_formula(cls):
        return cls.perimeter_formula

    @classmethod
    def get_area_formula(cls):
        return cls.area_formula


class ShapeList:
    """
    This class is meant to hold geometrical shapes (objects that inherit from Shape class).
    Parent Class: None
    Args:
        shapes: list of Shape objects
    """

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        """
        Adds shape to shapes list
        Check if shape's has Shape class as it's ancestor. If not it should raise `TypeError`
        """

        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            raise TypeError

    def get_shapes_table(self):
        """
        Create table with data of all objects
        Return: table(str)
        """

        title_list = ['idx', 'Class', '__str__', 'Perimeter', 'Perimeter Formula', 'Area', 'Area Formula']
        cell_length = []
        table = ''
        for title in title_list:
            cell_length.append(len(title))
        cell_length = self.get_length(cell_length)
        for i in range(len(cell_length)):
            cell_length[i] += 2
        table += '/' + '-' * (sum(cell_length) + len(title_list)-1) + '\\\n'
        for i in range(len(title_list)):
            table += '|{:^{}}'.format(title_list[i], cell_length[i])
        table += '|\n'
        idx = 0
        for shape in self.shapes:
            table += '|' + '-' * (sum(cell_length) + len(title_list)-1) + '|\n'
            table += '|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|\n'. \
                format(idx, cell_length[0], shape.__class__.__name__, cell_length[1],
                       shape.__str__(), cell_length[2], round(shape.perimeter, 2), cell_length[3],
                       shape.get_perimeter_formula(), cell_length[4], round(shape.area, 2),
                       cell_length[5], shape.get_area_formula(), cell_length[6])
        table += '\\' + '-' * (sum(cell_length) + len(title_list) - 1) + '/\n'
        return table

    def get_length(self, start_length):
        """
        Calculate cell size for table
        param: start_length: list contain cell size
        Return start_length: list contain update cell size
        """

        id_shape = 0
        for shape in self.shapes:
            if len(str(id_shape)) > start_length[0]:
                start_length[0] = len(str(id_shape))
            if len(shape.__class__.__name__) > start_length[1]:
                start_length[1] = len(shape.__class__.__name__)
            if start_length[2] < len(shape.__str__()):
                start_length[2] = len(shape.__str__())
            if len(str(round(shape.perimeter, 2))) > start_length[3]:
                start_length[3] = len(str(round(shape.perimeter, 2)))
            if len(shape.perimeter_formula) > start_length[4]:
                start_length[4] = len(shape.perimeter_formula)
            if len(str(round(shape.area, 2))) > start_length[5]:
                start_length[5] = len(str(round(shape.area, 2)))
            if len(shape.area_formula) > start_length[6]:
                start_length[6] = len(shape.area_formula)
            id_shape += 1
        return start_length

    def get_largest_shape_by_perimeter(self):
        """
        Returns shape with largest perimeter
        """

        if self.shapes:
            largest_shape = self.shapes[0]
            for shape in self.shapes:
                if shape.get_perimeter().__gt__(largest_shape.get_perimeter()):
                    largest_shape = shape
            return largest_shape
        else:
            return False

    def get_largest_shape_by_area(self):
        """
        Returns shape with largest area
        """

        if self.shapes:
            largest_shape = self.shapes[0]
            for shape in self.shapes:
                if shape.get_area().__gt__(largest_shape.get_area()):
                    largest_shape = shape
            return largest_shape
        else:
            return False
