'''

        Подвиг 1. В программе объявите три следующие переменные с указанными значениями:

        a = 7
        b = -4
        c = 3
        Выведите в консоль их значения, используя одну функцию print (между значениями переменных
        должен стоять один пробел).
'''

# put your python code here
a = 7
b = -4
c = 3

print(a, b, c)

'''
        Подвиг 2. В программе объявите три следующие переменные с указанными значениями:
        
        a = 7
        b = -4
        c = 3
        Выведите в консоль их значения в столбик (каждое новое значение отображается с новой строчки), используя 
        одну функцию print.
'''
a = 7
b = -4
c = 3

print(a, b, c, sep='\n')

'''
        Подвиг 3. В программе объявите две следующие переменные с указанными значениями:
        
        s1 = "Hello"
        s2 = "Balakirev"
        С помощью двух функций print (каждая отображает соответствующую строку) выведите строки 
        в консоль так, чтобы они шли друг за другом через пробел.
'''

# put your python code here
s1 = "Hello"
s2 = "Balakirev"

print(s1, end=' ')
print(s2)

'''
        Подвиг 4. В программе вводятся строки в переменные s1 и s2. Необходимо их отобразить в консоли в формате:

        Word 1: s1 | Word 2: s2
        
        Например, если s1 = "abc"; s2 = "defsg", то выводится строка:
        
        Word 1: abc | Word 2: defsg
        
        Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/2/2.4.4
        
        Sample Input:
        
        I love
        Sample Output:
        
        Word 1: I | Word 2: love
'''


s1, s2 = map(str.strip, input().split())

# здесь продолжите программу


print(f'Word 1: {s1} | Word 2: {s2}')

'''
        Подвиг 5. Напишите программу, в которой вводятся (читаются) два целых положительных числа, 
        записанных в одну строчку через пробел, и в консоль выводится результат возведения первого числа в 
        степень второго.

        Например, при вводе:
        
        5 3
        вычисляется: 
         =125

        Sample Input:
        
        2 3
        Sample Output:
        
        8
'''

# put your python code here
a, b = map(int, input().split())

print(a**b)

'''
        Подвиг 8. Напишите программу, которая принимает на входе два вещественных числа, записанных в одну строку через пробел, и выводит на экран их сумму.



            Sample Input:
            
            8 11
            Sample Output:
            
            19.0
'''

# put your python code here

a, b = map(float, input().split())

print(a + b)


'''
        Подвиг 9. В магазине продается X синих ручек, Y зеленых, черных в два раза больше, чем синих,
        а красных в четыре раза больше зеленых. Напишите программу, в которой вводятся целые значения
        X, Y в одну строку через пробел с помощью команды:

        X, Y = map(int, input().split())

        и выводится на экран общее число ручек в виде целого числа.
'''

x, y = map(int, input().split())

print(x + (x * 2) + y + (y * 4))


'''
        Подвиг 10. На вход программе подаются длина и ширина прямоугольника 
        (вещественные значения, каждое с новой строки). Необходимо прочитать эти значения и вычислить 
        периметр прямоугольника (сумму длин сторон). Результат (периметр) вывести на экран 
        в виде вещественного числа.

        Sample Input:
        
        8
        11
        Sample Output:
        
        38.0
'''

# put your python code here
a = float(input())
b = float(input())

print((a + b) * 2)


'''
        Подвиг 11. Напишите программу вывода переменной math.pi с точностью до тысячных (три знака после запятой).
'''


# put your python code here
import math

print(round(math.pi, 3))


'''
        Подвиг 12. Составить программу вывода на экран вещественного числа, вводимого с клавиатуры. 
        Выводимому числу должно предшествовать сообщение "Вы ввели число" (без кавычек).


        Sample Input:
        
        7.54
        Sample Output:
        
        Вы ввели число 7.54
'''

# put your python code here
a = float(input())

print(f'Вы ввели число {a}')


