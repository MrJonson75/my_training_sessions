'''
        Подвиг 3.

        Объявите анонимную (лямбда) функцию с двумя параметрами для деления первого целого числа
        (первого параметра) на второй (второй параметр). Если происходит деление на ноль,
        то функция должна возвращать значение None, иначе - результат деления.

        Присвойте эту функцию переменной get_div. Вызывать функцию не нужно, только задать.

'''


get_div = lambda a, b: a / b if b != 0 else None



'''
        Подвиг 4. 
        
        Объявите анонимную (лямбда) функцию для вычисления модуля числа 
        (то есть, отрицательные числа нужно делать положительными). 
        Вызовите эту функцию для числа x, которое следует прочитать из входного потока командой:
        
        x = float(input())
        Отобразите результат работы функции на экране.
        
        Sample Input:
        
        -5.6
        Sample Output:
        
        5.6
'''


get_abs = lambda x: abs(x)
print(get_abs(float(input())))


# Модернизация

print((lambda x: abs(x))(float(input())))




'''
        Подвиг 5. 
        
        Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "ra". 
        То есть, функция должна возвращать True, если такой фрагмент присутствует в строке 
        и False в противном случае.
        
        Вызовите эту функцию для строки s, которую следует прочитать из входного потока командой:
        
        s = input()
        Отобразите результат работы функции на экране.
        
        Sample Input:
        
        abrakadabra
        Sample Output:
        
        True
'''

s = input()
is_str = lambda x: any(x[i:i+2] == "ra" for i, _ in enumerate(x))
print(is_str(s))
# Модернизация

print((lambda x: any(x[i:i+2] == "ra" for i, _ in enumerate(x)))(input()))

# Модернизация

print((lambda x: "ra" in x)(input()))




'''
        Подвиг 6. 
        
        В программе задана функция filter_lst (см. программу ниже), которая отбирает элементы, 
        переданного ей итерируемого объекта и возвращает сформированный кортеж значений.
        
        На вход программы поступает список целых чисел, записанных через пробел. 
        Необходимо прочитать эти числа и сохранить в списке digs. 
        Затем, вызовите функцию filter_lst несколько раз для формирования:
        
        * кортежа из всех значений списка digs (передается в параметр it);
        * кортежа только из отрицательных чисел переданного списка digs;
        * кортежа только из неотрицательных чисел (то есть, включая и 0) переданного списка digs;
        кортежа из чисел в диапазоне [3; 5] переданного списка digs.
        Для отбора нужных значений формальному параметру key следует передавать 
        соответствующие определения анонимной функции. 
        Каждый результат работы функции следует отображать с новой строки командой:
        
        print(*lst)
        где lst - кортеж, возвращенный функцией filter_lst.
        
        Sample Input:
        
        5 4 -3 4 5 -24 -6 9 0
        Sample Output:
        
        5 4 -3 4 5 -24 -6 9 0
        -3 -24 -6
        5 4 4 5 9 0
        5 4 4 5
'''

def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res

# здесь продолжайте программу

# digs = list(map(int, input().split()))

digs = [5, 4, -3, 4, 5, -24, -6, 9, 0]

print(*filter_lst(digs))
print(*filter_lst(digs, lambda x: x < 0))
print(*filter_lst(digs, lambda x: x >= 0))
print(*filter_lst(digs, lambda x: 3 <= x <= 5))