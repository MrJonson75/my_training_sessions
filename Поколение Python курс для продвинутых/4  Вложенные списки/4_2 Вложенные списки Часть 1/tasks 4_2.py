
'''

        Что покажет приведенный ниже код?

'''

list1 = [[1, 8, 9], [4, 8, 12, 16], [0, 2, 7]]
print(list1[0][1] + list1[1][2] + list1[2][2])


# 5
#
# 27    <----  Правильно.
#
# 20
#
# 13
#
# 15
#
# 6
#
# произойдет ошибка


'''
        Что покажет приведенный ниже код?

        list1 = [[1, 8, 9], [4, 8, 12, 16], [0, 2, 7]]
        print(list1[0][1] + list1[3][2] + list1[2][2])       
        
        Выберите один вариант из списка
'''
        
        # 27
        #
        # 5
        #
        # 13
        #
        # 15
        #
        # 20
        #
        # 6
        #
        # произойдет ошибка     <----  Прекрасный ответ.



'''
        Используя списочный метод append(), дополните приведенный ниже код так, чтобы список list1 имел вид:

        list1 = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
'''


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)
print(list1)




'''
        Используя списочный метод extend(), дополните приведенный ниже код так, 
        чтобы список list1 имел вид:
        
        list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
        Подсписок для расширения  sub_list = ['h', 'i', 'j'].
'''


list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sub_list = ['h', 'i', 'j']
list1[2][1][2].extend(sub_list)
print(list1)





'''
        Используя цикл for и встроенную функцию max(), дополните приведенный ниже код так, чтобы он 
        выводил максимальный элемент среди всех элементов вложенных списков списка list1.
'''


list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = max([max(i) for i in list1])

print(maximum)




'''
        Дополните приведенный ниже код так, чтобы список list1 имел вид:

        list1 = [[8, 7, 1], [102, 7, 9], [105, 106, 102], [103, 98, 99, 100], [3, 2, 1]]
'''

list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
list1 = [i[::-1] for i in list1]

print(list1)




'''
        Дополните приведенный ниже код так, чтобы он выводил единственное число – 
        сумму всех чисел списка list1, разделенную на общее количество всех чисел.
'''


list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = sum([sum(i) for i in list1])
counter = sum([len(i) for i in list1])
print(total/counter)

