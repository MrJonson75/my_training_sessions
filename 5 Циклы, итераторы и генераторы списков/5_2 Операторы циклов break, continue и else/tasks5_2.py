'''
        test 2
'''

'''
        Подвиг 2. 
        
        Объявите в программе следующий одномерный список длиной 10 элементов, состоящий из нулей:

        p = [0] * 10
        На каждой итерации цикла запрашивайте у пользователя ввод целого числа - индекс элемента списка p, 
        по которому записывается значение 1, если ее там еще нет. 
        Если же 1 уже проставлена по текущему индексу, то список не менять. 
        Необходимо расставить так пять единиц в списке p. После этого цикл прерывается.
        
        Программу реализовать с помощью цикла while и с использованием оператора continue, 
        когда 1 уже проставлена в списке по текущему индексу, чтобы запросить другой индекс. 
        Результат вывести на экран в виде последовательности чисел, записанных через пробел.
        
        Sample Input:
        
        1
        2
        2
        5
        7
        5
        9
        Sample Output:
        
        0 1 1 0 0 1 0 1 0 1
'''


# p = [0] * 10
# n = 1
# while n <= 5:
#     ind = int(input())
#     if p[ind] == 1:
#         continue
#     else:
#         p[ind] = 1
#         n += 1
# print(*p)
# ************************************************
#
# p = [0] * 10
# while p.count(1) != 5:
#     d = int(input())
#     if p[d] == 1:
#         continue
#     p[d] = 1
# print(*p)
# ************************************************

# p = [0] * 10
#
# while sum(p) < 5:
#     p[int(input())] = 1
#
# print(*p)
#
# ****************************************************



'''
        Подвиг 3. 
        
        Напишите программу, в которой на каждой итерации цикла (while) 
        читается (из входного потока) целое число. 
        Необходимо подсчитать произведение только положительных чисел, до тех пор, пока не встретится число 0. 
        Реализовать пропуск вычислений с помощью оператора continue, 
        а также использовать цикл while. Полученное произведение вывести на экран.

            Sample Input:
            
            2
            -1
            3
            2
            -5
            7
            0
            Sample Output:
            
            84
'''

# m = 1
# while True:
#     n = int(input())
#     if n < 0:
#         continue
#     elif n == 0:
#         break
#     else:
#         m *= n
# print(m)
# ********************************************************




'''
        Подвиг 4. 
        
        На вход программе подается строка с названиями городов, записанных в одну строчку через пробел. 
        Прочитайте эту строку и сформируйте на ее основе список из названий городов. 
        Необходимо определить, что в этом списке все города имеют длину более 5 символов. 
        Если это так, то на экран вывести строку "ДА", иначе строку "НЕТ". 
        Программу реализовать с использованием цикла while и оператора break. 



            Sample Input:
            
            Самара Ульяновск Новгород Воронеж
            Sample Output:
            
            ДА
'''

# lst = list(map(str, input().split()))
# ind = 0
# while ind < len(lst):
#     if len(lst[ind]) < 5:
#         print("НЕТ")
#         break
#     ind += 1
# else:
#     print("ДА")
# *************************************************
#
# print(('НЕТ', 'ДА')[len(min(input().split(), key=len)) > 5])
#
# **********************************************************




'''
        Подвиг 5. 
        
        На вход программе подается строка с именами студентов, записанных в одну строчку через пробел. 
        Прочитайте эту строку и сформируйте на ее основе список из имен студентов. 
        Необходимо определить, что в этом списке хотя бы одно имя начинается и заканчивается 
        на ту же самую букву (без учета регистра). 
        Если это так, то на экран вывести строку "ДА", иначе строку "НЕТ". 
        
        Программу реализовать с использованием цикла while и оператора break. 


        
        Sample Input:
        
        Петр Анна Иван Сергей Михаил Федор
        
        Sample Output:
        
        ДА
'''

# lst = list(map(str, input().split()))
# ind = 0
# while ind < len(lst):
#     if lst[ind][0].lower() == lst[ind][-1].lower():
#         print("ДА")
#         break
#     ind += 1
# else:
#     print("НЕТ")
# ****************************************************
#
# students = input().lower().split()
# while students:
#     s = students.pop()
#     if s[0] == s[-1]:
#         print('ДА')
#         break
# else:
#     print('НЕТ')
# ***************************************************


'''
        Подвиг 6. 
        
        На вход программе подается натуральное число n (то есть, целое положительное). 
        Прочитайте это число. В цикле переберите все целые числа в интервале [1; n] (включая границы) 
        и сформируйте список из чисел, кратных 3 и 5 одновременно.
        
        Выведите на экран полученный список чисел в одну строчку через пробел, 
        если значение n меньше 100. Иначе выведите на экран сообщение (без кавычек):
        
        "слишком большое значение n"
        
        Продумать логику работы программы так, чтобы после цикла while шел блок else.
        
        
        Sample Input 1:
        
        49
        Sample Output 1:
        
        15 30 45
        Sample Input 2:
        
        100
        Sample Output 2:
        
        слишком большое значение n

'''

# n = list(range(1, int(input())+1))
# lst = []
# ind = 0
# while ind < len(n):
#     if len(n) >= 100:
#         print("слишком большое значение n")
#         break
#     if n[ind] % 3 == 0 and n[ind] % 15 == 0:
#         lst.append(n[ind])
#     ind += 1
# else:
#     print(*lst)
# ************************************************
#
# n = int(input())
# if n < 100:
#     print(*range(15, n, 15))
# else:
#     print('слишком большое значение n')
#
# *************************************************




'''
        Подвиг 7. 
        
        На вход программе подается натуральное число n. 
        Прочитайте это число и выведите первое найденное натуральное число 
        (то есть, перебирать числа, начиная с 1), квадрат которого больше значения n. 
        Программу реализовать с использованием цикла while.

            
            Sample Input:
            
            10
            Sample Output:
            
            4
'''

# n = int(input())
# i = 1
# while True:
#     if i ** 2 > n:
#         print(i)
#         break
#     i += 1
# *************************************************


'''
        Подвиг 8. 
        
        (На использование цикла while). 
        Начав тренировки, лыжник в первый день пробежал 10 км. 
        Каждый следующий день он увеличивал пробег на 10 % от пробега предыдущего дня. 
        Определить в какой день он пробежит больше x км 
        (натуральное число x читается из входного потока). 
        Результат (искомый день) вывести на экран.

            Sample Input:
            
            20
            Sample Output:
            
            9
'''

# n = int(input())
# dey = 2
# rez = 10
# if n < rez:
#     print(1)
# else:
#     while True:
#         rez *= 1.1
#         if rez > n:
#             print(dey)
#             break
#         dey += 1
# ****************************************************




'''
        Подвиг 9. 
        (На использование цикла while). 
        
        На вход программы подаются строки (названия книг). 
        В программе уже реализовано их чтение и сохранение в списке (каждый элемент - название книги). 
        После этого, из полученного списка нужно удалить все названия, состоящие из двух и более слов 
        (слова разделяются пробелом). 
        Результат выведите на экран в виде строки из оставшихся названий через пробел.

            Sample Input:
            
            Муму
            Евгений Онегин
            Сияние
            Мастер и Маргарита
            Пиковая дама
            Колобок
            Sample Output:
            
            Муму Сияние Колобок
'''

# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # # здесь продолжайте программу (используйте список lst_in)
#
# lst_in = ['Муму', 'Евгений Онегин', 'Сияние', 'Мастер и Маргарита', 'Пиковая дама', 'Колобок']
# ind = 0
# new_lst = []
# while ind < len(lst_in):
#     a = lst_in[ind]
#     if " " in lst_in[ind]:
#         ind +=1
#         continue
#     else:
#         new_lst.append(lst_in[ind])
#     ind += 1
# print(*new_lst)
# ********************************************************
#
# n = len(lst_in)
# while n:
#     n -= 1
#     if lst_in[n].count(' '):
#         del lst_in[n]
#
# print(*lst_in)
# *************************************************************