'''
        Подвиг 1.

        На вход программе подаются вещественные числа, записанные через пробел.
        Необходимо их прочитать и сохранить в списке lst. Затем, используя list comprehension
        (генератора списков) сформировать новый список lst_abs из модулей чисел списка lst
        (в итоговом списке должны храниться именно числа, а не строки). Список lst_abs вывести на экран командой:

        print(lst_abs)

        Sample Input:

        5.56 -8.7 1.0 3.14 77.845
        Sample Output:

        [5.56, 8.7, 1.0, 3.14, 77.845]

'''



# print([abs(i) for i in list(map(float, input().split()))])




'''
        Подвиг 2. На вход программе подается семизначное целое положительное число. 
        Необходимо его прочитать и с помощью list comprehension сформировать список lst, 
        содержащий цифры этого числа (в списке должны быть записаны числа, а не строки). 
        Полученный список вывести на экран командой:
        
        print(lst)
        
        
        Sample Input:
        
        4567397
        Sample Output:
        
        [4, 5, 6, 7, 3, 9, 7]
'''

# print([int(i) for i in str(input())])



'''
        Подвиг 3. 
        
        На вход программе подается натуральное число N. 
        Прочитайте его и с помощью list comprehension сформируйте двумерный список размером N x N, 
        состоящий из нулей, а по главной диагонали - единицы. 
        (Главная диагональ - это элементы, идущие по диагонали от верхнего левого угла матрицы 
        до ее нижнего правого угла). 
        Полученный двумерный список отобразите в виде таблицы чисел, как показано в примере ниже.
        
        
        Sample Input:
        
        4
        Sample Output:
        
        1 0 0 0
        0 1 0 0
        0 0 1 0
        0 0 0 1
'''

# n = int(input())
# lst = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
# for i in lst:
#     print(*i)


'''
        Подвиг 4. 
        
        На вход программе подается строка с названиями городов, записанных через пробел. 
        Необходимо прочитать эту строку и сформировать список с помощью list comprehension, 
        содержащий названия городов длиной более пяти символов. 
        Элементы полученного списка вывести в одну строчку через пробел.
        
        Sample Input:
        
        Казань Уфа Москва Челябинск Омск Тур Самара
        Sample Output:
        
        Казань Москва Челябинск Самара
'''



# print(*[i for i in list(map(str, input().split())) if len(i) > 5])




'''
        Подвиг 5. 
        
        На вход программе подается натуральное число n. 
        Необходимо его прочитать и сформировать список с помощью list comprehension, 
        состоящий из делителей числа n (включая и само число n). 
        Элементы полученного списка вывести в одну строчку через пробел.
        
        Ликбез: делителями числа n называются целые числа, которые делят n нацело (без остатка).
        
        
        Sample Input:
        
        10
        Sample Output:
        
        1 2 5 10
'''

# n = int(input())
# print(*[i for i in range(1, n+1) if n % i == 0])




'''
        Подвиг 6. 
        
        На вход программе подается натуральное число N. 
        Необходимо его прочитать и сгенерировать вложенный список с помощью list comprehension, 
        размером N x N, где первая строка содержала бы все нули, вторая - все единицы, третья - все двойки 
        и так до N-й строки. Результат вывести в виде таблицы чисел как показано в примере ниже.
        
        
        Sample Input:
        
        4
        Sample Output:
        
        0 0 0 0
        1 1 1 1
        2 2 2 2
        3 3 3 3
'''

# n = int(input())
# [print(*[j for i in range(n)]) for j in range(n)]




'''
        Подвиг 7. 
        
        На вход программе подаются вещественные числа, записанные через пробел.
         Необходимо их прочитать и сохранить в списке. 
         Затем, с помощью list comprehension сформировать еще один список, состоящий из элементов исходного списка, 
         имеющих четные индексы 
         (то есть, выбрать все элементы с четными индексами). 
         Элементы полученного списка вывести в одну строчку через пробел.
        
        
        Sample Input:
        
        8.5 11.3 1.0 -4.5 11.34 6.45
        Sample Output:
        
        8.5 1.0 11.34
'''

# lst_in = list(map(float, input().split()))
# print(*[lst_in[i] for i in range(len(lst_in)) if i % 2 == 0])




'''
        Подвиг 8. 
        
        На вход программе подаются два списка целых чисел одинаковой длины, каждый с новой строки. 
        Необходимо их прочитать и каждый сохранить в своем отдельном списке. 
        Затем, с помощью list comprehension сформировать третий список, состоящий из суммы 
        соответствующих пар чисел введенных списков. 
        Элементы полученного списка вывести в одну строчку через пробел.
        
        Sample Input:
        
        1 2 3 4 5
        6 7 8 9 10
        Sample Output:
        
        7 9 11 13 15
'''
# lst_in_one = list(map(int, input().split()))
# lst_in_two = list(map(int, input().split()))
# print(*[lst_in_two[i] + lst_in_one[i] for i in range(len(lst_in_one))])




'''

        Подвиг 9. 
        
        На вход программе подается строка в формате: 
        
        <город 1> <численность населения 1> <город 2> <численность населения 2> ... <город N> <численность населения N>
        
        Необходимо прочитать эту строку и с помощью list comprehension сформировать список lst, содержащий вложенные списки из пар:
        
        [[<город 1>, <численность населения 1>], [<город 2>, <численность населения 2>], ...]
        
        Численность населения - целое число в тыс. человек. Выведите полученный список командой:
        
        print(lst)
        
        Sample Input:
        
        Москва 15000 Уфа 1200 Самара 1090 Казань 1300
        Sample Output:
        
        [['Москва', 15000], ['Уфа', 1200], ['Самара', 1090], ['Казань', 1300]]

'''

lst_in = list(map(str, input().split()))
print([[lst_in[i], int(lst_in[i+1])] for i in range(len(lst_in)) if i % 2 == 0])