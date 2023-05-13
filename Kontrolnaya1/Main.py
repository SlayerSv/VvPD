import math as m


def main():
    print('Добро пожаловать в программу, которая определяет характеристики')
    print('треугольника по введенным параметрам. Программа проверяет является')
    print('ли треугольник равносторонним, равнобедренным или прямоугольным.')
    print('\nДля этого вам нужно ввести длины двух сторон треугольника и угол')
    print('между ними. Для того, чтобы выйти из программы введите "0"\n')
    while True:
        first_side = int(input('Введите длину первой стороны (0 = exit): '))
        if first_side == 0:
            return
        second_side = int(input('Введите длину второй стороны (0 = exit): '))
        if second_side == 0:
            return
        angle_deg = (int(input('Введите угол между сторонами (0 = exit):')))
        if angle_deg == 0:
            return
        angle_rad = m.radians(angle_deg)
        third_side = m.sqrt(m.pow(first_side, 2) + m.pow(second_side, 2) - 2
                            * first_side * second_side
                            * round(m.cos(angle_rad), 2))
        third_side = round(third_side, 2)
        print('Третья сторона треугольника равна ' + str(third_side))
        if first_side == second_side == third_side:
            print('Все стороны равны! Это равносторонний треугольник!')
            continue
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


def is_right_triangle(first_side, second_side, third_side):
    if first_side > second_side:
        if third_side > first_side:
            hypotenuse = third_side
            leg_a = first_side
            leg_b = second_side
        else:
            hypotenuse = first_side
            leg_a = second_side
            leg_b = third_side
    else:
        if third_side > second_side:
            hypotenuse = third_side
            leg_a = first_side
            leg_b = second_side
        else:
            hypotenuse = second_side
            leg_a = first_side
            leg_b = third_side
    if m.sqrt(m.pow(hypotenuse, 2)) == m.sqrt(m.pow(leg_a, 2)
                                              + m.pow(leg_b, 2)):
        return True
    else:
        return False


if __name__ == '__main__':
    main()
