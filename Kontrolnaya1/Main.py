import math as m
import sys


def main(args):
    try:
        first_side = input_check_side(args[1])
        second_side = input_check_side(args[2])
        angle_deg = input_check_angle(args[3])
        if len(args) > 4:
            rounding = input_check_rounding(args[4])
        else:
            rounding = 2
    except ValueError as exception:
        print(exception)
        return
    except IndexError:
        print("Not enough arguments! You need to enter two sides "
              + "and an angle between them!")
        return
    angle_rad = m.radians(angle_deg)
    third_side = calculate_third_side(first_side, second_side, angle_rad)
    print("Third side's length is: " + str(round(third_side, rounding)))
    define_triangle(first_side, second_side, third_side, rounding)


def is_right_triangle(first_side, second_side, third_side, rounding):
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
    if m.sqrt(round(m.pow(hypotenuse, 2), rounding))\
            == m.sqrt(m.pow(katet_a, 2) + m.pow(katet_b, 2)):
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


def input_check_rounding(rounding):
    try:
        rounding = int(rounding)
    except ValueError as exception:
        raise ValueError("Rounding value must be a number!") from exception
    if rounding <= 0:
        raise ValueError("Rounding value must be greater than zero!")
    return rounding


def calculate_third_side(first_side, second_side, angle_radians):
    return m.sqrt(m.pow(first_side, 2) + m.pow(second_side, 2) - 2
                  * first_side * second_side
                  * m.cos(angle_radians))


def define_triangle(first_side, second_side, third_side, rounding):
    if first_side == second_side == round(third_side, rounding):
        print("All sides are equal! This is an equilateral triangle!")
    elif is_right_triangle(first_side, second_side, third_side, rounding):
        print("Power of hypotenuse equals the sum of powers of the other "
              + "sides! This is a right triangle!")
        if (first_side == second_side)\
                or (first_side == round(third_side, rounding))\
                or (second_side == round(third_side, rounding)):
            print("Two sides are equal! This is an isosceles triangle!")
    elif (first_side == second_side)\
            or (first_side == round(third_side, rounding))\
            or (second_side == round(third_side, rounding)):
        print("Two sides are equal! This is an isosceles triangle!")
    else:
        print("Triangle is not equilateral, isosceles or right :(")


if __name__ == '__main__':
    main(sys.argv)
