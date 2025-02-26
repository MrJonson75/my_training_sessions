


'''

        Подвиг 5. Пользователь может ввести с клавиатуры следующие команды в виде строки:

        top или Top или TOP
        bottom или Bottom или BOTTOM
        right или Right или RIGHT
        left или Left или LEFT

        cmd = input()
        С помощью оператора match/case необходимо определить тип команды cmd и при совпадении вывести на экран
        сообщение в формате:

        Команда <название команды малыми буквами>

        Например, при вводе Top, должны на выходе получить:

        Команда top

        И так для всех четырех команд. Если тип команды не определен, то вывести строку:

        Неверная команда

        Sample Input:

        BOTTOM
        Sample Output:

        Команда bottom
'''
from unittest import case

cmd = 'BOTTOM' #input()

match cmd.lower():
    case 'top' as comm:
        print(f'Команда {comm}')
    case 'bottom' as comm:
        print(f'Команда {comm}')
    case 'right' as comm:
        print(f'Команда {comm}')
    case 'left' as comm:
        print(f'Команда {comm}')
    case _:
        print(f'Неверная команда')





'''
        Подвиг 6. В функцию get_data() передается параметр value:

        def get_data(value):
            match value:
                # здесь продолжайте программу
            
            return None
        Необходимо дописать оператор match/case в этой функции так, чтобы для каждого типа данных 
        (int, float и str) формировалась переменная со значением value и возвращалась функцией 
        (непосредственно из блока case).
        
        P. S. Вызывать функцию не нужно, только дописать.
'''


def get_data(value):
    match value:
        # здесь продолжайте программу
        case str() as value:
            return value
        case int() as value:
            return value
        case float() as value:
            return value

    return None



print(get_data('cnhjrf'))





'''
        Подвиг 7. 
        
        В функцию get_data() передается параметр value:

        def get_data(value):
            match value:
                # здесь продолжайте программу
            
            return None
        Необходимо дописать оператор match/case со следующими шаблонами:
        
        если переменная value имеет тип int и больше нуля, то вернуть значение переменной value;
        если переменная value имеет тип float и находится в диапазоне [-100; 100], то вернуть значение переменной value;
        если переменная value имеет тип str, то просто вернуть ее значение.
        P. S. Вызывать функцию не нужно, только дописать шаблоны.
'''



def get_data(value):
    match value:
        # здесь продолжайте программу
        case str() as value:
            return value
        case int() as value if value > 0:
            return value
        case float() as value if -100 <= value <= 100:
            return value

    return None