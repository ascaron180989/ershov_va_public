from random import choice
small_letters = 'abcdefghijklmnopqrstuvwxyz'
capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&*+-=?@^_'
var_list = [small_letters, capital_letters, numbers, symbols]


def true_false(answer):
    while True:
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            answer = input('Неверный формат, введите y или n: ')

            
def verification_numbers(num):
    while True:
        if str(num).isdigit():
            return int(num)
        num = input('Неверный формат, введите целое число: ')


def main_generate():
    count_password = verification_numbers(input('Введите количество паролей для генерации: '))
    length_password = verification_numbers(input('Введите длину генерируемых паролей: '))
    include_numbers = true_false(input('Включать ли цифры 0123456789? y / n: '))
    include_small_letters = true_false(input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? y / n: '))
    include_capital_letters = true_false(input('Включать ли заглавные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? y / n: '))
    include_symbols = true_false(input('Включать ли символы !#$%&*+-=?@^_? y / n: '))
    ambiguous_symbols = true_false(input('включать ли неоднозначные символы il1Lo0O? y / n: '))

    password = []
    password_list = []

    for i in range(count_password):
        for j in range(length_password):
            password.append(choice(var_list[choice()]))

            
main_generate()
