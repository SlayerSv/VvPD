def main():
    while True:
        brackets = input('Введите скобочную последовательность: ')
        if brackets == '0':
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
                    print(brackets)
                    has_moved = True
                    break
        if has_moved is False:
            is_done = True
    return moved_brackets


if __name__ == '__main__':
    main()
