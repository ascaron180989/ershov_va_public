from random import choice

small_letters = 'abcdefghijklmnopqrstuvwxyz'
capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&*+-=?@^_'


#  Проверка ответа y / n во всех случаях, когда это требуется
def true_false(answer):
    while True:
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            answer = input('Неверный формат, введите y или n: ')


#  Проверка, что вводимое значение число
def verification_numbers(num):
    while True:
        if str(num).isdigit():
            return int(num)
        num = input('Неверный формат, введите целое число: ')


#  Основная программа
def main_generate():
    #  Выбор: количество паролей, количество символов в пароле.
    #  Включает ли пароль цифры, маленькие буквы, большие буквы, спец символы. Исключать ли неоднозначные символы.
    count_password = verification_numbers(input('Введите количество паролей для генерации: '))
    length_password = verification_numbers(input('Введите длину генерируемых паролей: '))
    include_numbers = true_false(input('Включать ли цифры 0123456789? y / n: '))
    include_small_letters = true_false(input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? y / n: '))
    include_capital_letters = true_false(input('Включать ли заглавные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? y / n: '))
    include_symbols = true_false(input('Включать ли символы !#$%&*+-=?@^_? y / n: '))
    ambiguous_symbols = true_false(input('Включать ли неоднозначные символы il1Lo0O? y / n: '))

    password_symbols = ''
    password_list = []

    #  Формирование строки символов password_symbols из которых могут состоять пароли
    if include_numbers:
        password_symbols += numbers
    if include_small_letters:
        password_symbols += small_letters
    if include_capital_letters:
        password_symbols += capital_letters
    if include_symbols:
        password_symbols += symbols
    if not ambiguous_symbols:
        for i in 'il1Lo0O':
            password_symbols = password_symbols.replace(i, '')

    #  Формирование паролей password и добавление их в список password_list
    for i in range(count_password):
        password = ''
        for j in range(length_password):
            n = choice(password_symbols)
            password += n
        password_list.append(password)

    print(password_list)


while True:
    main_generate()
    if not true_false(input('Создать новые пароли? y / n: ')):
        break
