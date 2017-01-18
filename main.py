import geometry
import sys
import os


def main():

    round_value = 1  # set a value needed to print round values (1-place after ',')
    shapes = geometry.ShapeList()  # object containing all shapes added by the user
    while True:
        os.system('clear')
        print(
            "LEARN GEOMETRY\n\n"
            "What do you want to do?\n"
            "\t(1) Add new shape\n"
            "\t(2) Show all shapes\n"
            "\t(3) Show shape with the largest perimeter\n"
            "\t(4) Show shape with the largest area\n"
            "\t(5) Show formulas\n"
            "\t(0) Exit program\n"
        )

        option = input("Select an option: ")
        if option == "1":
            os.system('clear')
            print(
                "LEARN GEOMETRY\n\n"
                "What kind of shape do you want to add?:\n"
                "\t(1) Circle\n"
                "\t(2) Triangle\n"
                "\t(3) Equilateral Triangle\n"
                "\t(4) Rectangle\n"
                "\t(5) Square\n"
                "\t(6) Regular Pentagon\n"
                "\t(0) Back to menu\n"
            )
            user_choice = input('Select an option: ')
            if user_choice == '1':
                os.system('clear')
                print('Enter the length of circle radius: ')
                radius = input_value()
                circle = geometry.Circle(radius)
                shapes.add_shape(circle)

            elif user_choice == '2':
                os.system('clear')
                print('Enter length of first side of triangle: ')
                first_side = input_value()
                print('Enter length of second side of triangle: ')
                second_side = input_value()
                print('Enter length of third side of triangle: ')
                third_side = input_value()
                try:
                    triangle = geometry.Triangle(first_side, second_side, third_side)
                    shapes.add_shape(triangle)
                except ValueError:
                    input("Wrong value. Triangle cant be build with that length of sides {}, {}, {}."
                          .format(first_side, second_side, third_side))

            elif user_choice == '3':
                os.system('clear')
                print('Enter length of equilateral triangle side:')
                triangle_side = input_value()
                equilateral_triangle = geometry.EquilateralTriangle(triangle_side)
                shapes.add_shape(equilateral_triangle)

            elif user_choice == '4':
                os.system('clear')
                print('Enter length of first side of rectangle: ')
                first_side_of_rectangle = input_value()
                print('Enter length of secound side of rectangle: ')
                second_side_of_rectangle = input_value()
                rectangle = geometry.Rectangle(first_side_of_rectangle, second_side_of_rectangle)
                shapes.add_shape(rectangle)

            elif user_choice == '5':
                os.system('clear')
                print('Enter length of side of square: ')
                square_side = input_value()
                square = geometry.Square(square_side)
                shapes.add_shape(square)

            elif user_choice == '6':
                os.system('clear')
                print('Enter length of side of regular pentagon: ')
                pentagon_side = input_value()
                pentagon = geometry.RegularPentagon(pentagon_side)
                shapes.add_shape(pentagon)

            elif user_choice == '0':
                main()

            else:
                raise ValueError("Wrong input")

        elif option == "2":
            os.system('clear')
            if len(shapes.shapes) == 0:
                input('First add some shapes!\n Enter to back to menu')
            else:
                print(shapes.get_shapes_table())
                input('\nEnter = main menu')

        elif option == "3":
            os.system('clear')
            if len(shapes.shapes) == 0:
                input('First add some shapes! \n Enter to back to menu')
            else:
                print('Shape with the largest perimeter:\n' +
                      str(shapes.get_largest_shape_by_perimeter()) + '\tperimeter:',
                      round(shapes.get_largest_shape_by_perimeter().get_perimeter(), round_value))
                input('\nEnter to back to menu')

        elif option == "4":
            os.system('clear')
            if len(shapes.shapes) == 0:
                input('First add some shapes! \n Enter to back menu')
            else:
                print('Shape with the largest area:\n' +
                      str(shapes.get_largest_shape_by_area()) + '\tarea:',
                      round(shapes.get_largest_shape_by_area().get_area(), round_value))
                input('\n[Enter = main menu]')


        elif option == "5":
            # Show formulas
            pass
        elif option == "0":
            sys.exit()
        else:
            raise ValueError("Wrong input")


def input_value():
    float_value = None

    while float_value is None:
        try:
            chosen_value = input()
            if chosen_value == '':
                raise ValueError
            elif ',' in chosen_value:
                chosen_value = chosen_value.replace(',', '.')
                if float(chosen_value) <= 0:
                    raise ValueError
                float_value = float(chosen_value)
            elif float(chosen_value) <= 0:
                raise ValueError
            else:
                float_value = float(chosen_value)
        except ValueError:
            print('It is not a valid parameter! Try again')

    return float_value

if __name__ == "__main__":
    main()
