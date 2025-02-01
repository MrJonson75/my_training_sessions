'''

        Подвиг 2.
        На вход программе подается целое положительное число N.
        Необходимо написать рекурсивную функцию с именем get_rec_N, которая отображает на экране
        последовательность целых чисел от 1 до N (включительно).
        Каждое число выводится с новой строки.

        В качестве единственного параметра функция get_rec_N должна принимать числовое значение.
        Начальный вызов функции уже дан в программе и выглядит так:

        get_rec_N(N)

        Sample Input:

        8
        Sample Output:

        1
        2
        3
        4
        5
        6
        7
        8
'''

# считывание числа N
N = int(input())


#здесь продолжайте программу
def get_rec_N(N):
    if N > 1:
        get_rec_N(N - 1)
    print(N)


get_rec_N(N)  # вызов рекурсивной функции





'''
        Подвиг 3. 
        
        На вход программе подаются целые числа, записанные через пробел. 
        Необходимо их прочитать и сохранить в виде списка (или кортежа). 
        Затем, объявить рекурсивную функцию с именем get_rec_sum для вычисления суммы прочитанных чисел. 
        То есть, функция get_rec_sum в итоге должна возвращать значение суммы. 
        (Выводить на экран она ничего не должна). 
        Первым параметром в функцию следует передавать список чисел. 
        Остальные параметры продумайте самостоятельно.
        
        Вызовите функцию get_rec_sum и выведите на экран значение суммы, которое она вернула.
        
        Sample Input:
        
        8 11 -5 4 3
        Sample Output:
        
        21
'''

def get_rec_sum(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + get_rec_sum(lst[1:])


list_in = list(map(int, input().split()))

print(get_rec_sum(list_in))





'''
        Подвиг 4. 
        
        На вход программе подается натуральное число N (N >= 2), которое читается с помощью команды:
        
        N = int(input())
        
        Необходимо с помощью рекурсивной функции сигнатуры:
        
        def fib_rec(N, f=[1, 1]): ...
        
        (здесь N - общее количество чисел Фибоначчи; f - начальный список этих чисел) 
        сформировать последовательность чисел Фибоначчи по правилу: первые два числа равны 1 и 1, 
        а каждое следующе значение равно сумме двух предыдущих. 
        Пример такой последовательности для первых 7 чисел: 1, 1, 2, 3, 5, 8, 13, ...
        
        Функция должна возвращать список сформированной последовательности длиной N. 
        Вызывать функцию не нужно, только объявить.
 
        
        Sample Input:
        
        7
        Sample Output:
        
        1 1 2 3 5 8 13
'''


# ввод числа N
N = int(input())

# здесь задается функция fib_rec (переменную N не менять!)

def fib_rec(N, f=[1, 1]):
    if N == 2:
        return f
    else:
        lst = fib_rec(N - 1, f)
        lst.append(lst[-1] + lst[-2])
        return lst


print(fib_rec(N))




'''
        Подвиг 5. 
        На вход программе подается целое неотрицательное число n, которое читается командой:
        
        n = int(input())
        
        Необходимо объявить рекурсивную функцию fact_rec со следующей сигнатурой:
        
        def fact_rec(n): ...
        для вычисления факториала числа n. Напомню, что факториал числа, равен:

        n!=1⋅2⋅3⋅...⋅n
        
        Функция должна возвращать вычисленное значение. Вызывать функцию не нужно, только объявить.
        
        Sample Input:
        
        6
        Sample Output:
        
        720
'''


def fact_rec(n):
    if n <= 1:
        return 1
    else:
        return n * fact_rec(n - 1)

print(fact_rec(6))




'''
        Подвиг 6. 
        В программе объявлен следующий многомерный список:
        
        d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
        
        С помощью рекурсивной функции get_line_list необходимо на его основе 
        создать одномерный список из значений элементов списка d. 
        Функция должна возвращать новый созданный одномерный список.  
        (Только возвращать, выводить на экран ничего не нужно.)
        
        Вызывать функцию не нужно, только объявить со следующей сигнатурой:
        
        def get_line_list(d,a=[]): ...
        
        где d - исходный список; a - новый формируемый.
'''
d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]


def get_line_list(d,a=[]):
    for i in d:
        if type(i) == list:
            get_line_list(i,a)
        else:
            a.append(i)
    return a

lst = get_line_list(d)
print(lst)





'''
        Подвиг 7. 
        Лягушка прыгает вперед и может скакнуть либо на одно деление, либо сразу на два. 
        Наша задача определить количество вариантов маршрутов, которыми лягушка может достичь 
        риски под номером N (натуральное число N подается на вход программе).

        Решать задачу следует с применением рекурсивной функции. 
        Назовем ее get_path. Алгоритм решения следующий. 
        Рассмотрим, например, риску под номером 4. Очевидно, 
        в нее лягушка может скакнуть либо с риски номер 2, либо с риски номер 3. 
        Значит, общее число вариантов перемещений лягушки можно определить как: 
        
        get_path(4) = get_path(3) + get_path(2)
        Аналогично будет справедливо и для любой риски N:
        
        get_path(N) = get_path(N-1) + get_path(N-2)
        А начальные условия задачи, следующие:
        
        get_path(1) -> 1
        get_path(2) -> 2
        Реализуйте такую рекурсивную функцию, которая должна возвращать количество 
        вариантов перемещений лягушки для риски под номером N.
        
        Вызовите эту функцию для введенного числа N и отобразите результат на экране.
       
        Sample Input:
        
        7
        Sample Output:
        
        21
'''


def get_path(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    else:
        return get_path(N-1) + get_path(N-2)


print(get_path(int(input())))





'''
        Великий подвиг 8. 
        На вход программе подаются целые числа, записанные через пробел. 
        Необходимо их прочитать и сохранить в списке. 
        Затем, выполнить сортировку этого списка по возрастанию с помощью алгоритма сортировки слиянием. 
        Функция должна возвращать новый отсортированный список.
        
        Вызовите результирующую функцию сортировки для введенного списка 
        и отобразите результат на экран в виде последовательности чисел, записанных через пробел.
        
        Подсказка: для разбиения списка и его последующей сборки используйте рекурсивные функции.
        
        P. S. Теория сортировки в видео предыдущего шага.
        
        Sample Input:
        
        8 11 -6 3 0 1 1
        Sample Output:
        
        -6 0 1 1 3 8 11
'''

list_in = list(map(int, input().split()))


# Функция сливает списки в целые
def connect_s_s(l1, l2 ):
    list = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            list.append(l1[i])
            i = i + 1
        else:
            list.append(l2[j])
            j = j + 1
    if i < len(l1):
        list += l1[i:]
    if j < len(l2):
        list += l2[j:]
    return list


# Функция разбивает список на 2 в рекурсии
def we_disassemble_list(lst):
    if len(lst) == 1:
        return lst
    center = len(lst) // 2
    left = we_disassemble_list(lst[:center])
    right = we_disassemble_list(lst[center:])
    return connect_s_s(left, right)


print(*we_disassemble_list(list_in))


# Вариант 2 модернизировал

list_in = [int(i) for i in input().split()]


def connect_s_s(a, b):
    res = []
    while a and b:
        res += [a.pop(0) if a[0] < b[0] else b.pop(0)]
    return res + a + b


def we_disassemble_list(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    a, b = lst[:mid], lst[mid:]
    return connect_s_s(we_disassemble_list(a), we_disassemble_list(b))


print(*we_disassemble_list(list_in))