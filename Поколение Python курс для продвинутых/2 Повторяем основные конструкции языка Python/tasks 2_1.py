

'''

                На easy
        На вход программе подаются два целых числа a и b. Напишите программу, которая выводит:

        сумму чисел a и b;
        разность чисел a и b;
        произведение чисел a и b;
        частное чисел a и b;
        целую часть от деления числа a на b;
        остаток от деления числа a на b;
        корень квадратный из суммы их 10-х степеней: a ** 10 + b ** 10 * 0.5

        Формат входных данных
        На вход программе подаются два целых числа a и b (b≠0), каждое на отдельной строке.

        Формат выходных данных
        Программа должна вывести результаты математических операций в соответствии с условием задачи.

        Тестовые данные 🟢
        Sample Input 1:

        3
        8
        Sample Output 1:

        11
        -5
        24
        0.375
        0
        3
        32768.90100384814

        Sample Input 2:

        123
        2

        Sample Output 2:

        125
        121
        246
        61.5
        61
        1
        28153056843.0

        Sample Input 3:
        454
        322
        Sample Output 3:

        776
        132
        146188
        1.4099378881987579
        1
        132
        19595820067580.043
'''

a = 776 #int(input())
b = 132 #int(input())

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(((a ** 10) + (b ** 10)) ** 0.5)





'''
        Индекс массы тела
        
        Напишите программу для вычисления и оценки индекса массы тела (ИМТ) человека. 
        ИМТ показывает, человек весит больше или меньше нормы для своего роста. 
        ИМТ человека рассчитывают по формуле:
        
        ИМТ = масса (кг) / рост(м) × рост(м),
        
        где масса измеряется в килограммах, а рост – в метрах.
        
        Масса человека считается оптимальной, если его ИМТ находится между 18.5 и 25. Если ИМТ меньше 
        18.5, то считается, что человек весит ниже нормы. Если значение ИМТ больше 25, то считается, 
        что человек весит больше нормы.
        
        Программа должна вывести "Оптимальная масса", если ИМТ находится между 18.5 и 25 (включительно). 
        "Недостаточная масса", если ИМТ меньше 18.5 и "Избыточная масса", если значение ИМТ больше 25.
        
        `Формат входных данных`
        На вход программе подается два числа: масса и рост человека, каждое на отдельной строке. 
        Все входные числа являются действительными, используйте для них тип данных float.
        
        `Формат выходных данных`
        Программа должна вывести текст в соответствии с условием задачи.
        
        Тестовые данные 🟢
        Sample Input 1:
        
        65
        1.75
        Sample Output 1:
        
        Оптимальная масса
        Sample Input 2:
        
        80
        2.23
        Sample Output 2:
        
        Недостаточная масса
        Sample Input 3:
        
        80
        1.6
        Sample Output 3:
        
        Избыточная масса
'''

weight = 80.0  #float(input())
height = 1.6  #float(input())


def imt(w, h):
    imt_ = w / h ** 2
    return "Оптимальная масса" if 18.5 <= imt_ <= 25 else "Недостаточная масса" if imt_ < 18.5 else "Избыточная масса"


print(imt(weight, height))



'''
        Стоимость строки
        
        Дана строка текста.
        Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ 
        (в том числе пробел) стоит 60 копеек. 
        Ответ дайте в рублях и копейках в соответствии с примерами.
        
        Формат входных данных
        На вход программе подается строка текста.
        
        Формат выходных данных
        Программа должна вывести стоимость строки.
        
        Тестовые данные 🟢
        Sample Input 1:
        
        Привет, как дела?!
        Sample Output 1:
        
        10 р. 80 коп.
        Sample Input 2:
        
        Тимур - лучший математик на свете!!
        Sample Output 2:
        
        21 р. 0 коп.
        Sample Input 3:
        
        Я собираюсь сделать ему предложение, от которого он не сможет отказаться.
        Sample Output 3:
        
        43 р. 80 коп.
        Sample Input 4:
        
        w
        Sample Output 4:
        
        0 р. 60 коп.
'''

s = 'Привет, как дела?!'

print(f"{len(s)*60//100} р. {len(s)*60%100} коп.")

print(*divmod(len(s) * 60, 100), sep=' р. ', end=' коп.')

print()


'''
        Количество слов
        
        Дана строка, состоящая из слов, разделенных пробелами. 
        Напишите программу, которая подсчитывает количество слов в этой строке.
        
        Формат входных данных
        На вход программе подается строка.
        
        Формат выходных данных
        Программа должна вывести количество слов в строке.
        
        Примечание 1. Кроме слов в тексте могут присутствовать только пробелы (один или несколько).
        
        Примечание 2. Решите задачу в одну строчку кода. 😎
        
        Тестовые данные 🟢
        Sample Input 1:
        
        Hello world
        Sample Output 1:
        
        2
        Sample Input 2:
        
        Timur forever young
        Sample Output 2:
        
        3
        Sample Input 3:
        
        The future belongs to those who believe in beauty of their dreams
        Sample Output 3:
        
        12
'''

s = 'The future belongs to those who believe in beauty of their dreams'

print(len(s.split()))





'''
        Зодиак
        
        Китайский гороскоп назначает животным годы в 12-летнем цикле. Один 12-летний цикл показан в таблице ниже. 
        Таким образом, 2012 год будет очередным годом дракона.
        
        Год	Животное
        2000	Дракон
        2001	Змея
        2002	Лошадь
        2003	Овца
        2004	Обезьяна
        2005	Петух
        2006	Собака
        2007	Свинья
        2008	Крыса
        2009	Бык
        2010	Тигр
        2011	Заяц
        
        Напишите программу, которая считывает год и отображает название связанного с ним животного. 
        Ваша программа должна корректно работать с любым годом, не только теми, что перечислены в таблице.
        
        Формат входных данных
        На вход программе подается одно целое число – год.
        
        Формат выходных данных
        Программа должна вывести текст – название животного.
        
        Тестовые данные 🟢
        Sample Input 1:
        
        2020
        Sample Output 1:
        
        Крыса
        Sample Input 2:
        
        1945
        Sample Output 2:
        
        Петух
        Sample Input 3:
        
        2000
        Sample Output 3:
        
        Дракон
'''


z = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц"]

a = 2020
print(z[a % 12 - 8])




'''
        Переворот числа 🔄
        Дано пятизначное или шестизначное натуральное число. 
        Напишите программу, которая изменит порядок его последних пяти цифр на обратный.
        
        Формат входных данных
        На вход программе подается одно натуральное пятизначное или шестизначное число.
        
        Формат выходных данных
        Программа должна вывести число, которое получится в результате разворота, 
        указанного в условии задачи. Число нужно выводить без незначащих нулей.
        
        Тестовые данные 🟢
        Sample Input 1:
        
        12345
        Sample Output 1:
        
        54321
        Sample Input 2:
        
        987654
        Sample Output 2:
        
        945678
        Sample Input 3:
        
        25000
        Sample Output 3:
        
        52
        Sample Input 4:
        
        560000
        Sample Output 4:
        
        500006
'''

s = '12345'
print(int(s[::-1]) if len(s) == 5 else s[0] + s[1::][::-1])




'''
        Standard American Convention
        На вход программе подается натуральное число. 
        
        Напишите программу, которая вставляет в заданное число запятые в соответствии со стандартным 
        американским соглашением о запятых в больших числах.
        
        Формат входных данных
        На вход программе подается натуральное число 
        n (0 < n < 10 ** 100).
        
        Формат выходных данных
        Программа должна вывести число с запятыми в соответствии с условием задачи.
        
        Тестовые данные 🟢
        Sample Input 1:
        
        1000000
        Sample Output 1:
        
        1,000,000
        Sample Input 2:
        
        100
        Sample Output 2:
        
        100
        Sample Input 3:
        
        12345
        Sample Output 3:
        
        12,345
'''

n = "10000000000000000000"
print(f"{int(n):,}")    #    10,000,000,000,000,000,000




'''
                                Задача Иосифа Флавия 🌶️🌶️
        n человек, пронумерованных числами от 1 до n, стоят в кругу. Они начинают считаться, каждый 
        k-й по счету человек выбывает из круга, после чего счет продолжается со следующего 
        за ним человека. 
        Напишите программу, определяющую номер человека, который останется в кругу последним.
        
        Формат входных данных
        На вход программе подаются два натуральных числа 
        
        n и k, каждое на отдельной строке.
        
        Формат выходных данных
        Программа должна вывести одно число – номер человека, который останется в кругу последним.
        
        Примечание 1. Подробнее ознакомиться с классической задачей Иосифа Флавия можно по ссылке.
            https://ru.wikipedia.org/wiki/Задача_Иосифа_Флавия
        
        Тестовые данные 🟢
        Sample Input 1:
        
        2
        1
        Sample Output 1:
        
        2
        Sample Input 2:
        
        5
        2
        Sample Output 2:
        
        3
        Sample Input 3:
        
        7
        5
        Sample Output 3:
        
        6
'''

n = 7 #int(input())
k = 5 #int(input())
lst = [i for i in range(1, n + 1) ]
count = 0
while len(lst) != 1:
    if count < k -1:
        lst_t = lst.pop(0)
        lst.append(lst_t)
        count += 1
    else:
        count = 0
        del lst[0]

print(*lst)

n = 7 #int(input())
k = 5 #int(input())

res = 0
for j in range(1, n + 1):
    res = (res + k) % j
print(res + 1)