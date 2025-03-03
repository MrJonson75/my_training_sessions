

'''
        Подвиг 1. В программе объявлен следующий список:

        lst = [5.4, 6.7, 10.4]

        На вход программе подаются целые числа, записанные через пробел. Необходимо прочитать эти числа
        и сохранить в отдельном списке digs.
        Добавить в конец списка lst список digs отдельным элементом (как вложенный).
        Результирующий список lst вывести на экран командой:

        print(lst)
        Sample Input:

        8 11
        Sample Output:

        [5.4, 6.7, 10.4, [8, 11]]

'''

lst = [5.4, 6.7, 10.4]

digs = list(map(int, input().split()))

lst.append(digs)

print(lst)




'''
        Подвиг 2. На вход программе подаются три строки стихотворения (каждая с новой строки). 
        
        Необходимо прочитать эти строки и каждую представить в виде отдельного списка слов (слова разделяются пробелом). 
        Все полученные списки вложить в список lst и вывести его командой:

        print(lst)
        
        
        Sample Input:
        
        Мороз и солнце день чудесный
        Еще ты дремлешь друг прелестный
        Пора красавица проснись
        Sample Output:

        [['Мороз', 'и', 'солнце', 'день', 'чудесный'], 
        ['Еще', 'ты', 'дремлешь', 'друг', 'прелестный'], 
        ['Пора', 'красавица', 'проснись']]
'''

a = list(map(str, input().split()))
b = list(map(str, input().split()))
c = list(map(str, input().split()))
lst = list()
lst.append(a)
lst.append(b)
lst.append(c)
print(lst)


'''
        Подвиг 3. 
        
        На вход программе подается матрица чисел из трех строк. В каждой строке числа разделяются пробелом. 
        Необходимо прочитать эти числа и сохранить в виде двумерного (вложенного) списка. 
        Затем, вывести на экран последний столбец этой матрицы (двумерного списка) в виде строки из трех чисел, 
        записанных через пробел.



        Sample Input:
        
        8 11 12 1
        9 4 36 -4
        1 12 49 5
        Sample Output:
        
        1 -4 5
'''

mat = [list(map(str, input().split())),
       list(map(str, input().split())),
       list(map(str, input().split()))
    ]


print(f"{mat[0][3]} {mat[1][3]} {mat[2][3]}")
          # Тоже самое
print(input().split()[-1], input().split()[-1], input().split()[-1])



'''
        Подвиг 6. 
        
        В программе объявлен следующий вложенный список из трех строк:

        t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
            ["Я", "Python", "выучил", "с", "каналом"],
            ["Балакирев", "что", "раздавал?"]]
            
        На вход программе подается строка, содержащее одно слово. 
        Необходимо прочитать это слово и реализовать проверку на наличие его в списке t. 
        Результат (булево True или False) вывести на экран. 
        Решить задачу необходимо без применения условного оператора.


        Sample Input:
        
        дядя
        Sample Output:
        
        True
'''

t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
     ["Я", "Python", "выучил", "с", "каналом"],
     ["Балакирев", "что", "раздавал?"]]

str = input()

print(str in t[0] or str in t[1] or str in t[2])


t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
["Я", "Python", "выучил", "с", "каналом"],
["Балакирев", "что", "раздавал?"]]

a = input()
print(a in str(t))
#

t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
    ["Я", "Python", "выучил", "с", "каналом"],
    ["Балакирев", "что", "раздавал?"]]

a = sum(t, [])  # преобразовать вложенный список в одноуровневый
print(a)

print(input() in sum(t, []))