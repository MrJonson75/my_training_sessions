
'''
        Подвиг 2.

        На вход программе подается строка со списком оценок, например:

        2 неудовлетворительно удовлетворительно хорошо отлично

        Первая цифра - это числовое значение первой оценки.
        Остальные оценки имеют возрастающие числа на 1.

        Необходимо прочитать эту строку и с помощью генератора словарей сформировать словарь d,
        в котором ключами будут выступать числа, а значениями - слова.
        Например:

        d = {2: 'неудовлетворительно', 3: 'удовлетворительно', 4: 'хорошо', 5: 'отлично'}

        Вывести на экран значение сформированного словаря с ключом 4
        (полагается, что такой ключ всегда существует).

        Sample Input:

        1 ужасно неудовлетворительно удовлетворительно прилично отлично
        Sample Output:

        прилично
'''
import sys

lst_in = input().split()
d = {key: value for key, value in enumerate(lst_in[1:], int(lst_in[0]))}
print(d[4])





'''
        Подвиг 3. 
        
        На автомойку в течение квартала заезжали машины. 
        Их гос. номера фиксировались в журнале, следующим образом (пример):

        Е220СК
        А120МВ
        В101АА
        Е220СК
        А120МВ
        
        В программе уже реализовано чтение этих строк и сохранение в списке:
        
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        
        На основе этого списка через генератор множеств сформировать еще один список уникальных машин. 
        На экран вывести число уникальных машин.

        Sample Input:
        
        А323ГД
        Д456ВВ
        Б001ББ
        Д456ВВ
        С111СС
        Sample Output:
        4

'''


lst_in = ["А323ГД", "Д456ВВ", "Б001ББ", "Д456ВВ", "С111СС"]
print(len({i for i in lst_in}))





'''
        Подвиг 4. 
        
        На вход программе подается строка со словами, записанными через пробел. 
        Необходимо прочитать эту строку и с помощью генератора множеств сформировать множество 
        из уникальных слов без учета регистра и длина которых не менее трех символов. 
        Вывести на экран размер этого множества.

        
        Sample Input:
        
        Хижина изба машина и снова хижина машина
        Sample Output:
        
        4
'''
lst_in = input().lower().split()
list_out = len({i for i in lst_in if len(i) >= 3})
print(list_out)
# Вариант 2

print(len({i for i in input().lower().split() if len(i) >= 3}))






'''
        Подвиг 5. 
        
        На вход программе подается строка со словами, записанными через пробел. 
        Необходимо прочитать эту строку и с помощью генераторов множеств и словарей 
        сформировать словарь в формате:

        {слово_1: количество_1, слово_2: количество_2, ..., слово_N: количество_N}
        
        То есть, ключами выступают уникальные слова (без учета регистра), 
        а значениями - число их встречаемости в тексте. 
        На экран вывести значение словаря для слова (союза) 'и'. 
        Если такого ключа нет, то вывести 0.

        Sample Input:
        
        И что сказать и что сказать и нечего и точка
        Sample Output:
        
        4
'''
lst_in = input().lower().split()
d = {key: lst_in.count(key) for key in set(lst_in)}
print(d.get("и") if "и" in lst_in else 0)

# Вариант 2
lst_in = input().lower().split()
print({key: lst_in.count(key) for key in set(lst_in)}.get("и") if "и" in lst_in else 0)






'''
        Подвиг 6. 
        
        На вход программе подаются строки с информацией по книгам некоторого книжного магазина в формате:
        
        <автор 1>: <название 1>
        ...
        <автор N>: <название N>
        
        Авторы с названиями могут повторяться. 
        Также в программе уже реализовано чтение этих строк и сохранение в списке:
        
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        
        Необходимо, используя генераторы, сформировать словарь с именем d вида:
        
        {'автор 1': {'название 1', 'название 2', ..., 'название M'}, ..., 
        'автор K': {'название 1', 'название 2', ..., 'название S'}}
        
        То есть, ключами выступают уникальные авторы, а значениями - множества 
        с уникальными названиями книг соответствующего автора.
        
        На экран ничего выводить не нужно, только сформировать словарь обязательно с именем 
        d - он, далее будет проверяться в тестах!
        
        Sample Input:
        
        Пушкин: Сказка о рыбаке и рыбке
        Есенин: Письмо к женщине
        Тургенев: Муму
        Пушкин: Евгений Онегин
        Есенин: Русь
        Sample Output:
'''

lst_in = [
        "Пушкин: Сказка о рыбаке и рыбке",
        "Есенин: Письмо к женщине",
        "Тургенев: Муму",
        "Пушкин: Евгений Онегин",
        "Есенин: Русь",
        "Есенин: Русь"
]

lst = [i.split(": ") for i in lst_in]
d = {key[0]: {j[1] for j in lst if j[0] == key[0]} for key in lst}
