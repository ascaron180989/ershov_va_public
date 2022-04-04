# Функция верификации ввода
def verification(num: str) -> list:
    try:
        if len(num) < 1:
            raise ValueError
        num = list(map(int, num.split()))
        return num
    except ValueError:
        print('Не верный формат ввода')


# Функция сортировки
def insert_sort(num: list) -> list:
    for i in range(1, len(num)):
        while i > 0 and num[i - 1] > num[i]:
            num[i - 1], num[i] = num[i], num[i - 1]
            i -= 1
    return num


# Функция бинарного поиска позиции
def binary_search(num: list, n: int):
    if n < num[0]:
        return f'Число {n} меньше минимального'
    elif n > num[len(num) - 1]:
        return f'Число {n} больше максимального'
    elif n == num[0]:
        return f'Число {n} индекс 0'

    start = 0
    finish = len(num)

    while start <= finish:
        mid = (start + finish) // 2

        if start == finish or n == num[mid]:
            if n <= num[mid]:
                return f'Число {n} между индексами {mid - 1} и {mid}'
            elif n > num[mid]:
                return f'Число {n} между индексами {mid} и {mid + 1}'

        elif n < num[mid]:
            finish = mid - 1

        elif n > num[mid]:
            start = mid + 1

    return 'Баг!!! Не учтенная в алгоритме ситуация'


# Основной цикл программа
flag = 0
while True:
    if flag == 0:
        numbers = verification(input('Введите последовательность чисел (через пробел): '))
        flag += numbers is not None
    elif flag == 1:
        n = verification(input('Введите любое число: '))
        flag += n is not None
    elif flag == 2:
        # Сортировка
        insert_sort(numbers)

        # Поиск позиции
        position = binary_search(numbers, n[0])

        # Вывод
        print(numbers, position, sep='\n')
        break
    else:
        print(f'Не допустимое значение flag={flag}')
        break
