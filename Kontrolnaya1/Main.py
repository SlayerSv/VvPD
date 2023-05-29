import math as m
import sys


def main(args):
    try:
        first_side = input_check_side(args[1])
        second_side = input_check_side(args[2])
        angle_deg = input_check_angle(args[3])
    except ValueError as exception:
        print(exception)
        return
    except IndexError:
        print("Not enough arguments! You need to enter two sides "
              + "and an angle between them!")
        return
    angle_rad = m.radians(angle_deg)
    third_side = calculate_third_side(first_side, second_side, angle_rad)
    print("Third side's length is: " + str(round(third_side, 2)))
    define_triangle(first_side, second_side, third_side)


def is_right_triangle(first_side, second_side, third_side):
    if first_side > second_side:
        if third_side > first_side:
            hypotenuse = third_side
            katet_a = first_side
            katet_b = second_side
        else:
            hypotenuse = first_side
            katet_a = second_side
            katet_b = third_side
    else:
        if third_side > second_side:
            hypotenuse = third_side
            katet_a = first_side
            katet_b = second_side
        else:
            hypotenuse = second_side
            katet_a = first_side
            katet_b = third_side
    print()
    if m.sqrt(round(m.pow(hypotenuse, 2), 2)) == m.sqrt(m.pow(katet_a, 2)
                                                        + m.pow(katet_b, 2)):
        return True
    else:
        return False


def input_check_side(length):
    try:
        length = float(length)
    except ValueError as exception:
        raise ValueError("Side's length must be a number!") from exception
    if length <= 0:
        raise ValueError("Side's length must be greater than zero!")
    return length


def input_check_angle(angle):
    try:
        angle = float(angle)
    except ValueError as exception:
        raise ValueError("Angle must be a number!") from exception
    if angle <= 0 or angle >= 180:
        raise ValueError("Angle must be between 0 and 180 degrees !")
    return angle


def calculate_third_side(first_side, second_side, angle_radians):
    return m.sqrt(m.pow(first_side, 2) + m.pow(second_side, 2) - 2
                  * first_side * second_side
                  * m.cos(angle_radians))


def define_triangle(first_side, second_side, third_side):
    if round(first_side, 2) == round(second_side, 2) == round(third_side, 3):
        print("All sides are equal! This is an equilateral triangle!")
    elif is_right_triangle(first_side, second_side, third_side):
        print("Power of hypotenuse equals the sum of powers of the other "
              + "sides! This is a right triangle!")
        if (first_side == second_side) or (first_side == third_side) \
                or (second_side == third_side):
            print("Two sides are equal! This is an isosceles triangle!")
    elif (first_side == second_side) or (first_side == third_side) \
            or (second_side == third_side):
        print("Two sides are equal! This is an isosceles triangle!")
    else:
        print("Triangle is not equilateral, isosceles or right :(")


if __name__ == '__main__':
    main(sys.argv)
