

'''
        Подвиг 2.

        На вход программы подаются два целых положительных числа n и m, записанных через пробел,
        причем, n < m.
        Необходимо прочитать эти числа и вывести в одну строку через пробел квадраты целых чисел в
        диапазоне [n; m]. Программу реализовать при помощи цикла while.


        Sample Input:

        2 4
        Sample Output:

        4 9 16

'''

# n, m = map(int, input().split())
# lst = []
# while n <= m:
#     lst.append(n**2)
#     n += 1
# print(*lst)
# ******************************************************

# start, stop = map(int, input().split())
#
# while start <= stop:
#     print(start ** 2, end=' ')
#     start += 1
# *********************************************************


'''
        Подвиг 3. 
        
        На вход программы подается вещественное число: 
        
        стоимость одной книги x рублей. 
        Необходимо прочитать это число и вывести на экран в одну строчку через пробел 
        стоимости 2, 3, ... 10-ти таких книг с точностью до десятых. 
        Программу реализовать при помощи цикла while.



        Sample Input:
        
        34.6
        Sample Output:
        
        69.2 103.8 138.4 173.0 207.6 242.2 276.8 311.4 346.0
'''

# price = float(input())
# i = 0
# new_price = price
# while  i < 9:
#     new_price += price
#     print(round(new_price, 1),  end=' ')
#     i += 1
#*******************************************************************************


'''
        Подвиг 4. 
        
        На вход программы подается целое положительное число n. 
        Прочитайте это число, а затем, вычислите и выведите на экран следующую сумму с 
        точностью до тысячных (три знака после запятой):

                            S = 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + 1/7 + 1/n                                   
 
        Программу реализовать при помощи цикла while.
        
        Sample Input:
        
        8
        Sample Output:
        
        2.718
'''

# n = int(input())
# s = 1
# i = 2
# while i <= n:
#     s += 1/i
#     i += 1
# print(round(s, 3))
#
# ************************************************
#
# n, sm = int(input()), 0
# while n:
#     sm += 1 / n
#     n -= 1
# print(round(sm, 3))


'''
        Подвиг 5. 
        
        Написать программу, в которой пользователь на каждой итерации цикла (while) должен вводить целое число. 
        Цикл должен продолжаться, пока пользователь не введет число 0. 
        Необходимо вычислить сумму введенных в цикле чисел и вывести результат (сумму) на экран. 
        Программу реализовать при помощи цикла while.

            Sample Input:
            
            8
            11
            2
            -4
            0
            Sample Output:
            
            17
'''
# sm = 0
# while True:
#     n = int(input())
#     if n == 0: break
#     else:
#         sm += n
#
# print(sm)
#
# ******************************************************



'''
        Подвиг 6. 
        
        На вход программе подается строка (слаг). 
        Прочитайте эту строку и замените в ней все подряд идущие дефисы (--, ---, ---- и т.д.) на одинарные (-). 
        Результат преобразования строки выведите на экран. Программу реализовать при помощи цикла while.

            Sample Input:
            
            osnovnye--metody-----slovarey
            Sample Output:
            
            osnovnye-metody-slovarey
'''


# slug = input()
#
# while "--" in slug:
#     string = slug.replace("--", "-")
#     slug = string[:]
#     del string
# print(slug)
# ****************************************************************




'''
        Подвиг 7. 
        
        На вход программе подается натуральное число (то есть, целое положительное) от трехзначного и более. 
        Необходимо прочитать это число и найти произведение всех его цифр. 
        Результат (произведение) вывести на экран. 
        Программу реализовать при помощи цикла while.



        Sample Input:
        
        821
        Sample Output:
        
        16
'''

# n = list(input())
#
# ind = 0
# m = 1
# while ind < len(n):
#     m *= int(n[ind])
#     ind += 1
# print(m)
# **************************************************
#
# n = int(input())
# summ = 1
#
# while n:
#     summ *= n % 10
#     n //= 10
#
# print(summ)

# *********************************************************




'''
        Подвиг 8. 
        
        Последовательность Фибоначчи образуется так: 
        
        первые два числа равны 1 и 1, а каждое последующее равно сумме двух предыдущих. 
        В итоге, получаем такую последовательность чисел: 1, 1, 2, 3, 5, 8, 13, ...
        
        На вход программе подается целое положительное число n (n >= 2). 
        Прочитайте это число и сформируйте последовательность Фибоначчи длиной n. 
        Например, при n = 4 получается последовательность:

            1 1 2 3

        Результат отобразите в виде строки полученных чисел, записанных через пробел. 
        Программу реализовать при помощи цикла while.

        Sample Input:

        8
        Sample Output:
        
        1 1 2 3 5 8 13 21
'''


# n = int(input())
# ind = 0
# fib = [1, 1]
# if n == 2:
#     print(*fib)
# else:
#     while ind < n - 2:
#         fib.append(fib[ind] + fib[ind+1])
#         ind += 1
#
#     print(*fib)
#*****************************************************************




'''
        Подвиг 9. 
        
        На вход программе подается целое положительное число n (количество часов). 
        Прочитайте это число и сохраните в переменной n.
        
        Пусть одноклеточная амеба каждые 3 часа делится на 2 клетки. 
        Необходимо определить, сколько клеток будет через n часов. 
        Считать, что изначально была одна амеба.
        
        Результат (итоговое число клеток) вывести на экран. 
        Задачу необходимо решить с использованием цикла while.

        Sample Input:
        
        11
        Sample Output:
        
        8
'''

# n = int(input())
#
# cycle = 3
# amoeba = 1
#
# while cycle <= n:
#     amoeba *= 2
#     cycle += 3
#
# print(amoeba)
# **********************************************




'''
        Подвиг 10. 
        
        Гражданин 1 января открыл счет в банке, вложив 1000 руб. 
        Каждый год размер вклада увеличивается на 5% от имеющейся суммы. 
        Определить сумму вклада через n лет 
        (n - целое положительное число, читаемое из входного потока). 
        
        Результат (сумму вклада) округлить до сотых и вывести на экран. 
        Программу реализовать при помощи цикла while.



            Sample Input:
            
            5
            Sample Output:
            
            1276.28
'''

# years = int(input())
#
# deposit_amount = 1000
# n = 1
#
# while n <= years:
#     deposit_amount *= 1.05
#     n += 1
# print(round(deposit_amount, 2))
# **************************************************




'''
        Подвиг 11. 
        
        На вход программе подаются два натуральных числа n и m, записанных в одну строчку через пробел, 
        причем n < m.
        
        Необходимо прочитать эти числа и напечатать все нечетные числа из интервала [n, m]. 
        
        Задачу следует решить без применения условного оператора. 
        Результат вывести на экран в виде строки чисел, записанных через пробел. 
        Программу реализовать при помощи цикла while.

        Sample Input:
        
        2 10
        Sample Output:
        
        3 5 7 9

'''

# n, m = map(int, input().split())
#
# while n < m:
#     while n % 2 == 0:
#         n += 1
#     print(n, end=" ")
#     n += 1
# ***************************************************




'''
        Подвиг 12. 
        
        Составить программу поиска всех трехзначных чисел, 
        которые при делении на 47 дают в остатке 43 и кратны 3. 
        Вывести найденные числа в одну строчку через пробел в порядке возрастания. 
        Программу реализовать при помощи цикла while.
        
        
        231 372 513 654 795 936
'''
n = 100
while 99 < n < 1000:
    if n % 47 == 43 and n % 3 == 0:
        print(n, end=' ')
        n += 1
    else:
        n += 1