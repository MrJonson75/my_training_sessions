
'''

        Подвиг 4. Имеется следующий фрагмент программы с функцией parse_json и словарем json_data:

        def parse_json(data):
            match data:
                case {'id': ids, 'data': [_, {'login': login}, _, _]}:
                    return ids, login

            return None


        json_data =

        {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}

        С помощью оператора match/case в функцию parse_json добавьте в самое начало шаблон для выделения
        значения ключа access с проверкой на тип bool и для выделения даты (первое значение списка)
        из поля data с проверкой, что data является списком.
         Возвратите выделенные два значения в виде кортежа в формате (access, date).

        P. S. В программе нужно только дописать шаблон. Вызывать функцию не нужно.
'''


def parse_json(data):
    match data:
        # здесь прописывайте шаблон
        case {'access': bool(access), 'data': list([data, _, _, _])}:
            return access, data

        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login

    return None

json_data = {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}


print(parse_json(json_data))





'''
        Подвиг 5. Имеется следующий фрагмент программы с функцией parse_json и словарем json_data:

        def parse_json(data):
            match data:
                case {'id': ids, 'data': [_, {'login': login}, _, _]}:
                    return ids, login
            
            return None
        
        json_data = 
        {'id': 2, 'access': True, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}
        
        С помощью оператора match/case в функцию parse_json добавьте в самое начало шаблон для выделения 
        значений ключей login и email с проверкой, что они являются строками и при условии, что поле 
        access принимает значение True. 
        Возвратите выделенные два значения в виде кортежа в формате (login, email).
        
        P. S. В программе нужно только дописать шаблон. Вызывать функцию не нужно.
'''


def parse_json(data):
    match data:
        # здесь прописывайте шаблон
        case {'access': bool() as access, 'data': [_, {'login': str(login), 'email': str(email)}, _, _]} if access:
            return login, email

        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login

    return None

json_data = {'id': 2, 'access': True, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}


print(parse_json(json_data))