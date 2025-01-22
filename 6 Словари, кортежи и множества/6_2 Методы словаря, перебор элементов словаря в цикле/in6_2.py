'''

        Подвиг 3.

        На вход программе подается строка из русских букв и символов пробела.
        Необходимо ее прочитать и закодировать азбукой Морзе, где каждой букве ставится в соответствие код
        из точки и тире.
        После каждой закодированной буквы должен стоять пробел (символ окончания кода буквы).
        После последнего кода пробела быть не должно (в конце строки).
        Коды азбуки Морзе приведены ниже для русского алфавита и символа пробела:

        А    .-	    М    --	    Ш    ----
        Б    -...	Н    -.	    Щ    --.-
        В    .--	О    ---	Ъ    --.--
        Г    --.	П    .--.	Ы    -.--
        Д    -..	Р    .-.	Ь    -..-
        Е (Ё)    .	С    ...	Э    ..-..
        Ж    ...-	Т    -	    Ю    ..--
        З    --..	У    ..-	Я    .-.-
        И    ..	    Ф    ..-.	' '    -...-
        Й    .---	Х    ....
        К    -.-	Ц    -.-.
        Л    .-..	Ч    ---.

        Результат кодирования вывести в виде строки.

        P. S. Для очень ленивых готовый словарь азбуки Морзе можно скачать по адресу:
        https://github.com/selfedu-rus/others (файл morze-dict.py).
        Для практики лучше его составить самостоятельно.
        Да, работа программиста зачастую связана и с такой рутиной.


        Sample Input:

        Сергей Балакирев
        Sample Output:

        ... . .-. --. . .--- -...- -... .- .-.. .- -.- .. .-. . .--
'''
# # my_string = "Сергей Балакирев".lower()
morze = {
    "а": ".-", "б": "-...", "в": ".--", "г": "--.", "д": "-..", "е": ".", "ё": ".",
    "ж": "...-", "з": "--..", "и": "..", "й": ".---", "к": "-.-", "л": ".-..", "м": "--",
    "н": "-.", "о": "---", "п": ".--.", "р": ".-.", "с": "...", "т": "-", "у": "..-",
    "ф": "..-.", "х": "....", "ц": "-.-.", "ч": "---.", "ш": "----", "щ": "--.-", "ъ": "--.--",
    "ы": "-.--", "ь": "-..-", "э": "..-..", "ю": "..--", "я": ".-.-", ' ': "-...-"
}
my_string = input().lower()
out_string = ""
for b in my_string:
    out_string += morze[b]
    out_string += " "
print(out_string.rstrip())
#***********************************************************************************************
chars = {
    "А": ".-", "Б": "-...", "В": ".--", "Г": "--.", "Д": "-..", "Е": ".", "Ж": "...-",
    "З": "--..", "И": "..", "Й": ".---", "К": "-.-", "Л": ".-..", "М": "--", "Н": "-.",
    "О": "---", "П": ".--.", "Р": ".-.", "С": "...", "Т": "-", "У": "..-", "Ф": "..-.",
    "Х": "....", "Ц": "-.-.", "Ч": "---.", "Ш": "----", "Щ": "--.-", "Ъ": "--.--", "Ы": "-.--",
    "Ь": "-..-", "Э": "..-..", "Ю": "..--", "Я": ".-.-", " ": "-...-"
}

print(*[chars.get(i.upper()) for i in input()])




'''
        Подвиг 4. 
        
        На вход программе подается закодированная строка с помощью азбуки Морзе. 
        Коды разделены между собой пробелом. 
        Необходимо ее раскодировать, используя азбуку Морзе из предыдущего занятия. 
        Все буквы в строке должны быть малыми (нижний регистр). 
        Полученное сообщение (строку) вывести на экран.
        
        P.S. Буквам е(ё) соответствует один и тот же код Морзе, 
        поэтому всюду подставляется буква 'е'.
        
        Sample Input:
        
        .-- ... . -...- .-- . .-. -. ---
        Sample Output:
        
        все верно
'''

morze = {
    "а": ".-", "б": "-...", "в": ".--", "г": "--.", "д": "-..", "е": ".",
    "ж": "...-", "з": "--..", "и": "..", "й": ".---", "к": "-.-", "л": ".-..", "м": "--",
    "н": "-.", "о": "---", "п": ".--.", "р": ".-.", "с": "...", "т": "-", "у": "..-",
    "ф": "..-.", "х": "....", "ц": "-.-.", "ч": "---.", "ш": "----", "щ": "--.-", "ъ": "--.--",
    "ы": "-.--", "ь": "-..-", "э": "..-..", "ю": "..--", "я": ".-.-", ' ': "-...-"
}

my_str = ""
for i in input().split():
    for key, value in morze.items():
        if i == value:
            my_str += key

print(my_str)
# **********************************************************
[print(key, end="") for i in input().split() for key, value in morze.items() if i == value]
# *********************************************************************************************




'''
        Подвиг 5. 
        На вход программе подается список целых чисел, записанных в одну строчку через пробел. 
        Необходимо их прочитать и сохранить в виде списка. 
        Затем, с помощью словаря выделите только уникальные (не повторяющиеся) числа. 
        Сформируйте из них еще один список (уникальных чисел). 
        Числа в этом списке должны идти в том же порядке, что и при чтении (из входного потока). 
        Выведите уникальные числа на экран в одну строчку через пробел.
        
        P. S. Такая задача, обычно решается через множества, но мы их еще не проходили, 
        поэтому воспользуемся словарем.
        
        Sample Input:
        
        8 11 -4 5 2 11 4 8
        Sample Output:
        
        8 11 -4 5 2 4
'''

print(*dict.fromkeys(list(map(int, input().split()))).keys())





'''
        Подвиг 6. На вход программе подаются строки в формате:
        
        <день рождения 1> имя_1
        <день рождения 2> имя_2
        ...
        <день рождения N> имя_N
        
        Дни рождений и имена могут повторяться.
        
        В программе уже реализовано их считывание и сохранение в списке:
        
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        
        
        На основе списка lst_in сформировать словарь, где ключи - дни рождения (целое число), 
        а значения - имена (строка). Выведите полученный словарь в формате (см. пример ниже):
        
        день рождения 1: имя1, ..., имяN1
        день рождения 2: имя1, ..., имяN2
        ...
        день рождения M: имя1, ..., имяNM
        
        Sample Input:
        
        3 Сергей
        5 Николай
        4 Елена
        7 Владимир
        5 Юлия
        4 Светлана
        Sample Output:
        
        3: Сергей
        5: Николай, Юлия
        4: Елена, Светлана
        7: Владимир
'''

lst_in = ['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']

d = {}
for j in [i.split(' ') for i in lst_in]:
    d.setdefault(j[0], []).append(j[1])
for k, v in d.items():
    print(f"{k}: {", ".join(v)}")





'''
        Подвиг 7. 
        
        Объявите в программе словарь с наименованиями предметов и их весом (в граммах):
        
        things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 
                  'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
                  'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
                  
        Сергей собирается в поход и готов взвалить на свои хрупкие плечи максимальный вес в N кг (вводится с клавиатуры). 
        Он решил класть в рюкзак предметы в порядке убывания их веса (сначала самые тяжелые, затем, все более легкие) 
        так, чтобы их суммарный вес не превысил значения N кг. 
        Все предметы даны в единственном экземпляре. 
        Выведите список предметов (в строчку через пробел), которые берет с собой Сергей в порядке убывания их веса.
        
        P. S. 1 кг = 1000 грамм
        
        Sample Input:
        
        10
        Sample Output:
        
        палатка брезент удочка брюки пила карандаш спички
'''

things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

# вводим информацию максимальный вес в N кг
N = int(input())
# Переводим в граммы
N = N * 1000
new_backpack = []
# Получаем список пар кортежей в порядке убывания
things = sorted(things.items(), key=lambda item: item[1], reverse=True)
for items, weight in things:
    if N - weight < 0:
        continue
    else:
        new_backpack.append(items)
        N -= weight

print(*new_backpack)


# *********************************************************

things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
n=int(input())*1000
for i in sorted(things.values(), reverse=True):
    if n-i>=0:
        for k, v in things.items():
            if i==v:
                print(k,end=" ")
        n-=i