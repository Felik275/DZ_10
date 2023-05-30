# Task 2
# 2. Напишіть програму, яка б приймала список з числами та перевіряла чи всі числа в ньому унікальні. Реалізуйте у функції декілька обробок виключень.
import sys
def unique_number_list() -> bool:

    try:

        user_input = input('Введіть числа через кому: ').split(',')

        if len(user_input) >= 1 and ',' not in user_input:
            raise Exception('Ви ввели значення не через кому')
            return None

        list_numbers = list(map(int, user_input))

        return print(len(list_numbers) == len(set(list_numbers)))

    except ValueError as ex:

        print('Ви ввели не числове значення', file=sys.stderr)
        return None

    except:

        print('Введено некоректний формат даних', file=sys.stderr)
        return None

unique_number_list()