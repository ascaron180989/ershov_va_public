########################################################################################################################
#                                             Поиск слова                                                              #
########################################################################################################################
import string

def max_count_word(word_list: list) -> dict:
    word_dict = {}
    for word in word_list:
        if len(word) < 3:
            continue
        else:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    max_value = max(word_dict.values())
    return {k: v for k, v in word_dict.items() if v == max_value}


def lond_en_word(word_list: list) -> list:
    en_word_list = []
    for word in word_list:
        for letter in word:
            if letter not in string.ascii_lowercase:
                break
        else:
            if word not in en_word_list:
                en_word_list.append(word)
    max_value = max(len(word) for word in en_word_list)
    return [word for word in en_word_list if len(word) == max_value]


print('Программа получает от пользователя имя файла, открывает этот файл в текущем каталоге, читает его и выводит два слова. \n'
      '1) Наиболее часто встречающееся из тех, что имеют размер более трех символов. \n'
      '2) Наиболее длинное слово на английском языке.\n')
try:
    file_name = input('Введите имя файла: ')

    # Чтение из файла
    with open(file_name, encoding='utf8') as fn:
        dict_reads_file = fn.read().replace('\n', '').lower().split()

    # Вывод результата
    print('Наиболее часто встречающиеся слова:', max_count_word(dict_reads_file))
    print('Самые длинные английские слова:', lond_en_word(dict_reads_file))

except FileNotFoundError:
    print('Не верное имя файла')
