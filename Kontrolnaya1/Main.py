import math as m


def main():
    print('Добро пожаловать в программу, которая определяет характеристики')
    print('треугольника по введенным параметрам. Программа проверяет является')
    print('ли треугольник равносторонним, равнобедренным или прямоугольным.')
    print('\nДля этого вам нужно ввести длины двух сторон треугольника и угол')
    print('между ними. Для того, чтобы выйти из программы введите "0"\n')
    while True:
        message = 'Введите длину первой стороны (0 для выхода): '
        first_side = input_check(message, 0, 9999999)
        if first_side == 0:
            return
        message = 'Введите длину второй стороны (0 для выхода): '
        second_side = input_check(message, 0, 9999999)
        if second_side == 0:
            return
        message = 'Введите угол между сторонами в градусах (0 для выхода): '
        angle_deg = input_check(message, 0, 180)
        if angle_deg == 0:
            return
        angle_rad = m.radians(angle_deg)
        third_side = calculate_third_side(first_side, second_side, angle_rad)
        print('Третья сторона треугольника равна ' + str(third_side))
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
    if m.sqrt(round(m.pow(hypotenuse, 2), 1)) == m.sqrt(m.pow(katet_a, 2)
                                                        + m.pow(katet_b, 2)):
        return True
    else:
        return False


def input_check(message, min_value, max_value):
    while True:
        try:
            user_input = input(message)
            user_input = int(user_input)
        except ValueError:
            try:
                user_input = float(user_input)
            except ValueError:
                print('Нужно ввести число!')
                continue
        if user_input < min_value or user_input >= max_value:
            print('Число должно быть между ' + str(min_value)
                  + ' и ' + str(max_value))
            continue
        return user_input


def calculate_third_side(first_side, second_side, angle_radians):
    return round(m.sqrt(m.pow(first_side, 2) + m.pow(second_side, 2) - 2
                 * first_side * second_side
                 * m.cos(angle_radians)), 2)


def define_triangle(first_side, second_side, third_side):
    if first_side == second_side == third_side:
        print('Все стороны равны! Это равносторонний треугольник!')
    elif is_right_triangle(first_side, second_side, third_side):
        print('Квадрат гипотенузы равен сумме квадратов катетов!')
        print('Это прямоугольный треугольник!')
        if (first_side == second_side) or (first_side == third_side) \
                or (second_side == third_side):
            print('Две стороны равны! Это равнобедренный треугольник!')
    elif (first_side == second_side) or (first_side == third_side) \
            or (second_side == third_side):
        print('Две стороны равны! Это равнобедренный треугольник!')
    else:
        print('Треугольник не является ни равносторонним,')
        print('ни равнобедренным, ни прямоугольным :(')


if __name__ == '__main__':
    main()
