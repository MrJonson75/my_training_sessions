
'''

        Подвиг 1.

        На вход программе поступают две последовательности целых чисел, каждая с новой строки.
        Необходимо прочитать эти последовательности и сохранить в отдельных списках или кортежах.
        Затем, попарно перебрать их элементы и перемножить между собой.
        При реализации программы используйте функции zip и map.
        Выведите на экран первые три значения, используя функцию next.
        Значения выводятся в строчку через пробел.
        (Полагается, что три выходных значения всегда будут присутствовать).

        Sample Input:

        -7 8 11 -1 3
        1 2 3 4 5 6 7 8 9 10
        Sample Output:

        -7 16 33
'''

s1 = '-7 8 11 -1 3'
s2 = '1 2 3 4 5 6 7 8 9 10'

rez = map(lambda x: int(x[0])*int(x[1]), list(zip(s1.split(), s2.split())))
print(*[next(rez) for _ in range(3)])



'''
        Подвиг 2. 
        
        На вход программе подается неравномерная таблица целых чисел. 
        В программе уже реализовано считывание ее строк  и сохранение в списке lst_in:

        lst_in = list(map(str.strip, sys.stdin.readlines()))
        
        С помощью функции zip необходимо выравнить эту таблицу, приведя ее к прямоугольному виду, 
        отбросив выходящие элементы в строках. 
        Вывести результат на экран в виде такой же таблицы чисел. 
        В конце строк при выводе пробелов быть не должно.
        
        Sample Input:
        
        1 2 3 4 5 6
        3 4 5 6
        7 8 9
        9 7 5 3 2
        Sample Output:
        
        1 2 3
        3 4 5
        7 8 9
        9 7 5
'''

lst_in = ['1 2 3 4 5 6', '3 4 5 6', '7 8 9', '9 7 5 3 2']

[print(*i) for i in zip(*zip(*(i.split() for i in lst_in)))]



'''
        Подвиг 3. 
        
        На вход программе подается таблица целых чисел. 
        В программе уже реализовано считывание ее строк  и сохранение в списке lst_in:

        lst_in = list(map(str.strip, sys.stdin.readlines()))
        
        Необходимо сначала список строк lst_in представить двумерным (вложенным) списком чисел, 
        а затем, с помощью функции zip выполнить транспонирование этой таблицы 
        (то есть, строки заменить на соответствующие столбцы). 
        Результат вывести на экран в виде таблицы чисел (числа в строках следуют через пробел). 
        В конце строк при выводе пробелов быть не должно.

        
        Sample Input:
        
        1 2 3 4
        5 6 7 8
        9 8 7 6
        Sample Output:
        
        1 5 9
        2 6 8
        3 7 7
        4 8 6
'''

lst_in = ['1 2 3 4', '5 6 7 8', '9 8 7 6']


[print(*i) for i in zip(*[i.split() for i in lst_in])]




'''
        Подвиг 4. 
        
        На вход программе подается строка из слов, записанных через пробел. 
        Необходимо прочитать эту строку, разбить на слова на основе полученного списка составить 
        прямоугольную таблицу из трех столбцов и N строк 
        (число строк столько, сколько получится). 
        Лишнее (выходящее) слово - отбросить. 
        Реализовать эту программу с использованием функции zip. 
        Результат отобразить на экране в виде прямоугольной таблицы из слов, записанных через пробел 
        (в каждой строчке).
        
        Sample Input:
        
        Москва Уфа Тула Самара Омск Воронеж Владивосток Лондон Калининград Севастополь
        Sample Output:
        
        Москва Уфа Тула
        Самара Омск Воронеж
        Владивосток Лондон Калининград
'''

s = 'Москва Уфа Тула Самара Омск Воронеж Владивосток Лондон Калининград Севастополь'

x = iter(s.split())
[print(*i) for i in zip(x, x, x)]



'''
        Подвиг 5. 
        
        На вход программе подается строка. 
        Требуется ее прочитать и сформировать N=10 пар кортежей в формате:

        (символ, порядковый индекс)
        
        Например, подается строка "Sergey Balakirev", на выходе формируются кортежи (сохраненные в списке):
        
        [('S', 0), ('e', 1), ('r', 2), ('g', 3), ('e', 4), ('y', 5), (' ', 6), ('B', 7), ('a', 8), ('l', 9)]
        
        Первый индекс имеет значение 0. Строка может быть короче 10 символов, а может быть и длиннее. 
        То есть, число пар может быть 10 и менее. 
        Используя функцию zip сформируйте указанные кортежи и сохраните их списке с именем lst.
        
        P.S. Программа ничего не должна отображать на экране, только формировать список lst из кортежей.
'''


s = "Sergey Balakirev"

l = list(zip(s, range(10)))
