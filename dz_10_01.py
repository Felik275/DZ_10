#Task 1
#1. Напишіть функцію, яка б приймала номер місяця, а вертала його назву. Реалізуйте у функції декілька обробок виключень.

import datetime
import sys


def month_name(month_number: int) -> str:

    try:

        month_name = datetime.datetime(2023, month_number, 1).strftime('%B')
        return print(month_name)

    except TypeError as ex:

        print('Введено некоректний символ', file = sys.stderr)
        return None

    except ValueError as ex:

        print('Номер місяця має бути від 1 до 12', file = sys.stderr)
        return None