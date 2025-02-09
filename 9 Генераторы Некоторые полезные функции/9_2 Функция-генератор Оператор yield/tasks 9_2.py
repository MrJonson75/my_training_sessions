
'''
        Подвиг 1.

        На вход программе подается натуральное число N. Оно уже читается в программе командой:

        N = int(input())
        Объявите в программе функцию-генератор с именем get_sum с сигнатурой:

        def get_sum(total): ...

        которая бы возвращала текущую сумму чисел последовательности длины
        total = N в диапазоне целых чисел [1; N] (включительно).
        То есть, при вызове get_sum в качестве аргумента передается переменная N.
        В результате должны получить следующие результаты работы функции-генератора:

        при первом вызове get_sum возвращает сумму 1;
        при втором вызове get_sum возвращает сумму чисел 1+2 = 3;
        при третьем вызове get_sum возвращает сумму чисел 1+2+3 = 6;
        ....
        для N-го вызова get_sum возвращает сумму 1+2+...+(N−1)+N.
        Реализовать функцию-генератор get_sum без использования коллекций.
        Вызывать ее не нужно, только объявить.

        Sample Input:

        5
        Sample Output:

        1 3 6 10 15
'''
import random

N = 5

def get_sum(total):
    sum_in = 0
    for x in range(1, total+1):
        yield x + sum_in
        sum_in += x


print(*get_sum(N))



'''
        Подвиг 2. 
        
        Мы с вами в заданиях несколько раз генерировали последовательность чисел Фибоначчи, 
        которая строится по правилу: 
        каждое последующее число равно сумме двух предыдущих. 
        Для разнообразия давайте будем генерировать каждое последующее как сумму трех предыдущих чисел. 
        При этом первые три числа равны 1. Получаем такую последовательность:

        1, 1, 1, 3, 5, 9, 17, 31, 57, ...
        
        Не знаю, есть ли у нее название, поэтому, в рамках уроков, я скромно назову ее 
        последовательностью Балакирева. 
        
        Итак, на вход программе поступает натуральное число N (N > 5), 
        которое необходимо прочитать и сохранить в переменной. 
        Затем (или в начале программы), объявить функцию-генератор с сигнатурой:
        
        def balak_seq(max_len): ...
        
        которая бы возвращала max_len = N первых чисел последовательности 
        Балакирева (включая первые три единицы).
        
        Реализуйте эту функцию без использования коллекций (списков, кортежей, словарей и т.п.). 
        Вызовите ее N раз для получения N чисел и выведите полученные числа 
        на экран в одну строчку через пробел.

        Sample Input:
        
        7
        Sample Output:
        
        1 1 1 3 5 9 17
'''

N = 7


def balak_seq(max_len):
    a, b, c = 1, 1, 1
    for x in range(1, max_len+1):
        yield a
        a, b, c = b, c, a + c + b


step = balak_seq(N)
for i in range(1, N+1):
    print(next(step), end=' ')



'''
        Подвиг 3. 
        
        На вход программе подается натуральное число N (N > 8). 
        Необходимо его прочитать и объявить функцию-генератор, которая бы выдавала пароль длиной N 
        символов из случайных букв, цифр и некоторых других знаков. 
        Значение N передается в функцию-генератор первым аргументом. 
        Для получения последовательности допустимых символов для генерации паролей в программе импортированы 
        две строки: ascii_lowercase, ascii_uppercase (см. листинг ниже), 
        на основе которых формируется общий список:

        from string import ascii_lowercase, ascii_uppercase
        chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
        
        Функция-генератор должна при каждом вызове возвращать новый пароль из случайно выбранных 
        символов chars длиной N и делать это бесконечно, то есть, вызывать ее можно бесконечное число раз.
        
        Сгенерируйте с помощью функции-генератора первые пять паролей и выведите их в столбик 
        (каждый с новой строки).
        
        Подсказка: сгенерировать случайный индекс indx в диапазоне [a; b] для выбора символа из chars 
        можно с помощью функции randint модуля random:

        import random
        random.seed(1)
        indx = random.randint(a, b)
        
        Sample Input:
        
        10
        Sample Output:
        
        riGp?58WAm
        !dX3a5IDnO
        dcdbWB2d*C
        4?DSDC6Lc1
        mxLpQ@2@yM
'''
from string import ascii_lowercase, ascii_uppercase
import random
random.seed(1)
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
N = 10

def password_generator(len_password, char):
    yield "".join([random.choice(char) for _ in range(len_password)])


for x in range(5):
    print(next(password_generator(N, chars)))




'''
        Подвиг 4. 
        
        На вход программе подается натуральное число N, которое необходимо прочитать и сохранить через переменную. 
        Используя строки из латинских букв ascii_lowercase и ascii_uppercase:

        from string import ascii_lowercase, ascii_uppercase
        chars = ascii_lowercase + ascii_uppercase
        
        объявите функцию-генератор с одним параметром max_size, которая бы возвращала случайно 
        сформированные email-адреса с доменом mail.ru и длиной max_size = N символов. 
        Например, при N=6 адрес может выглядеть так: SCrUZo@mail.ru
        
        Функция-генератор должна возвращать бесконечное число таких адресов, то есть, генерировать постоянно. 
        Выведите первые пять сгенерированных email и выведите их в столбик (каждый с новой строки).
        
        Подсказка: для формирования случайного индекса для выбора символа из строки chars, 
        используйте функцию randint модуля random:
        
        import random
        random.seed(1)
        indx = random.randint(0, len(chars)-1)

        Sample Input:
        
        8
        Sample Output:
        
        iKZWeqhF@mail.ru
        WCEPyYng@mail.ru
        FbyBMWXa@mail.ru
        SCrUZoLg@mail.ru
        ubbbPIay@mail.ru        
'''

from string import ascii_lowercase, ascii_uppercase
import random
random.seed(1)
chars = ascii_lowercase + ascii_uppercase

N = 8
def email_generator(max_size, char):
    yield "".join([random.choice(char) for _ in range(max_size)])+"@mail.ru"


for x in range(5):
    print(next(email_generator(N, chars)))



'''
        Подвиг 5. 
        
        Объявите функцию-генератор, которая бы возвращала простые числа. 
        (Простое число - это натуральное число, которое делится только на себя и на 1). 
        Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) 
        в одну строчку через пробел.
'''

def prime_number(n):
    def prime_num(a):
        k=0
        for i in range(2, a//2+1):
            if a % i == 0:
                k += 1
        if k <= 0:
            return True
        else:
            return False
    a = 2
    for j in range(n):
        while True:
            if prime_num(a):
                yield a
                a += 1
                break
            a += 1


print(*prime_number(20))

#*************************************************************************

def prime_number():
    number = 1
    while True:
        number += 1
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                break
        else:
            yield number


gen = prime_number()
for i in range(20):
    print(next(gen), end=' ')