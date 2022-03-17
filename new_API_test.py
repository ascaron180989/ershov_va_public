import json


def type_int(item):
    return isinstance(item, int)


def type_str(item):
    return isinstance(item, str)


def type_bool(item):
    return isinstance(item, bool)


def type_url(item):
    if isinstance(item, str):
        if 'http://' in item or 'https://' in item:
            return True
    return False


def type_val(item, val):
    if isinstance(item, str):
        if item in val:
            return True
    return False


# Словарь поле: значение, которые могут принемать соответсвующие поля
required_fields = {"timestamp": 'int', "referer": 'url', "location": 'url', "remoteHost": 'str', "partyId": 'str',
                   "sessionId": 'str', "pageViewId": 'str', "eventType": 'val', "item_id": 'str',
                   "item_price": 'int', "item_url": 'url', "basket_price": 'str', "detectedDuplicate": 'bool',
                   "detectedCorruption": 'bool', "firstInSession": 'bool', "userAgentName": 'str'}

# Списки ошибок
extra_fields = []
error_fields = []
missing_fields = []


# Чтение ответа API
with open('answer_API.json', encoding='utf8') as answer_json:
    answers = json.load(answer_json)

# Проход по словарю json
for i in range(len(answers)):
    for key, item in answers[i].items():
        if key in required_fields:
            if required_fields[key] == 'int':
                if not type_int(item):
                    error_fields.append(f'{i}: {key} - Не верный тип')
            elif required_fields[key] == 'str':
                if not type_str(item):
                    error_fields.append(f'{i}: {key} - Не верный тип')
            elif required_fields[key] == 'bool':
                if not type_bool(item):
                    error_fields.append(f'{i}: {key} - Не верный тип')
            elif required_fields[key] == 'url':
                if not type_url(item):
                    error_fields.append(f'{i}: {key} - Ошибка URL')
            elif required_fields[key] == 'val':
                if not type_val(item, ['itemBuyEvent', 'itemViewEvent']):
                    error_fields.append(f'{i}: {key} - Не верное значение')
        else:
            extra_fields.append(f'{i}: {key}')

# Вывод результата
if extra_fields or error_fields or missing_fields:
    print('Fail')
    print('Отсутствует поле: ', missing_fields)
    print('Лишнее поле: ', extra_fields)
    print('Ошибка в поле: ', error_fields)
else:
    print('Pass')
