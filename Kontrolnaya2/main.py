def main():
    while True:
        brackets = input('Введите скобочную последовательность: ')
        if brackets == '0':
            return
        if check_brackets(brackets):
            print('Скобочная последовательность правильная!')
        else:
            print('Скобочная последовательность неправильная :(')


def check_brackets(brackets):
    opening_brackets_count = 0
    for i in brackets:
        if i == '(':
            opening_brackets_count += 1
        elif i == ')':
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


if __name__ == '__main__':
    main()
