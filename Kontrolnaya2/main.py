def main():
    while True:
        brackets = take_input()
        if brackets == '0':
            print('Программа завершает работу')
            return
        if is_cbs(brackets):
            print('Скобочная последовательность правильная!')
        else:
            print('Скобочная последовательность неправильная :(')
            print('Нужно переместить ' + str(need_to_move(brackets))
                  + ' скобок!')


def is_cbs(brackets):
    opening_brackets_count = 0
    for c in brackets:
        if c == '(':
            opening_brackets_count += 1
        elif c == ')':
            if opening_brackets_count > 0:
                opening_brackets_count -= 1
            else:
                return False
        else:
            raise ValueError('Символ не является скобкой')
    if opening_brackets_count == 0:
        return True
    else:
        raise ValueError('Недостаточно закрывающихся скобок :(')


def need_to_move(input):
    brackets = input
    opening_brackets_count = 0
    moved_brackets = 0
    slice_brackets1 = ''
    slice_brackets2 = ''
    is_done = False
    has_moved = False
    i = 0
    while is_done is False:
        for c in brackets:
            has_moved = False
            if c == '(':
                opening_brackets_count += 1
                i += 1
            elif c == ')':
                if opening_brackets_count > 0:
                    opening_brackets_count -= 1
                    i += 1
                else:
                    slice_brackets1 = brackets[:i]
                    slice_brackets2 = brackets[i + 1:]
                    brackets = slice_brackets1 + slice_brackets2 + ')'
                    moved_brackets += 1
                    i = 0
                    opening_brackets_count = 0
                    print('Перемещена закрывающаяся скобка в конец строки:')
                    print(brackets)
                    has_moved = True
                    break
        if has_moved is False:
            is_done = True
    return moved_brackets


def take_input():
    is_wrong = False
    while True:
        user_input = input('Введите скобочную последовательность(0 = выход): ')
        if user_input == '0':
            return '0'
        is_wrong = False
        opening_brackets = 0
        closing_brackets = 0
        for c in user_input:
            if c == '(':
                opening_brackets += 1
            elif c == ')':
                closing_brackets += 1
            else:
                print('Нужно ввести только круглые скобки!')
                is_wrong = True
                break
        if opening_brackets != closing_brackets:
            is_wrong = True
            print('Открывающихся и закрывающихся скобок должно быть' +
                  ' одинаковое количество!')
        if is_wrong is False:
            return user_input


if __name__ == '__main__':
    main()
