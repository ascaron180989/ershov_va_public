from random import randrange
print('Добро пожаловать в числовую угадайку')


def set_range():  # Определяем игровой диапазон и число ответ
    print('Для начала определим диапазон значений!')
    x = is_valid(input('Введите нижнюю границу диапазона: '))
    y = is_valid(input('Введите верхнюю границу диапазона: '))
    if x > y:
        x, y = y, x
    _random_num = randrange(x, y)
    return _random_num, x, y


def is_valid(_num):  # Функция проверки ввода
    while True:
        if _num.isdigit():
            return int(_num)
        else:
            _num = input('Число должно быть целым и положительным: ')


def my_main():  # Основная программа
    count = 1
    while True:
        num = is_valid(input(f'Введите целое число от {x} до {y}: '))
        if num > random_num:
            count += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif num < random_num:
            count += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif num == random_num:
            print(f'Вы угадали, поздравляем! Правильный ответ {num}, вы угадали за {count} попыток')
            break


def continue_game():  # Функция запроса продолжения игры
    play = input('Хотите сыграть ещё? y / n ')
    if play == 'y':
        return True


while True:
    random_num, x, y = set_range()
    my_main()
    if continue_game():
        continue
    break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
