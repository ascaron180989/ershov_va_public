import json


def decorator_type(func):
    def wrapper(*args):
        result = str(func(*args))
        if 'int' in result:
            return 'int'
        if 'str' in result:
            return 'str'
        if 'bool' in result:
            return 'bool'
    return wrapper


# Проверка наличия обязательных полей
def req_fields(answer: dict) -> list:
    missing_field = []
    count = 0
    for i in required_fields:
        if i in answer:
            count += 1
        else:
            missing_field.append(i)
    return [] if count == 16 else missing_field


# Прверка наличия лишних полей
def false_fields(answer: dict) -> list:
    extra_field = []
    for i in answer:
        if i not in required_fields:
            extra_field.append(i)
    return [] if not extra_field else extra_field


# Проверка полей: тип, URL, значение
def type_fields(answer: dict) -> dict:
    error_field = {}
    for key, ans_i in answer.items():
        if key in required_fields:
            for req_i in required_fields[key]:

                #  Проверка типа
                if req_i in ['int', 'str', 'bool']:
                    if type(ans_i) != req_i:
                        if key not in error_field:
                            error_field[key] = ['Не верный тип данных']
                        else:
                            error_field[key].append('Не верный тип данных')

                #  Проверка URL
                elif req_i == 'url':
                    if 'http://' not in str(ans_i) and 'https://' not in str(ans_i):
                        if key not in error_field:
                            error_field[key] = ['Не верный формат ссылки URL']
                        else:
                            error_field[key].append('Не верный формат ссылки URL')

                #  Проверка вхождения значения
                else:
                    if str(ans_i) not in required_fields[key][1:]:
                        if key not in error_field:
                            error_field[key] = ['Не верное значение']
                        else:
                            error_field[key].append('Не верное значение')
                    break
    return error_field


type = decorator_type(type)
required_fields = {"timestamp": ['int'], "referer": ['str', 'url'], "location": ['str', 'url'], "remoteHost": ['str'],
                   "partyId": ['str'], "sessionId": ['str'], "pageViewId": ['str'],
                   "eventType": ['str', 'itemBuyEvent', 'itemViewEvent'], "item_id": ['str'],
                   "item_price": ['int'], "item_url": ['str', 'url'], "basket_price": ['str'],
                   "detectedDuplicate": ['bool'], "detectedCorruption": ['bool'], "firstInSession": ['bool'],
                   "userAgentName": ['str']}


if __name__ == '__main__':

    #  Чтение ответа API
    with open('answer_API.json', encoding='utf8') as answer_json:
        answers = json.load(answer_json)

    # Проверка и вывод
    for item in range(len(answers)):
        print(f'Ответ №{item + 1}')
        print('Отсутствуют поля:', req_fields(answers[item]))
        print('Лишние поля:', false_fields(answers[item]))
        print('Ошибки в поле:', type_fields(answers[item]))
        print()
