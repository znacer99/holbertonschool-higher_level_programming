#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            dividend = my_list_1[i] if i < len(my_list_1) else 0
            divisor = my_list_2[i] if i < len(my_list_2) else 1
            division = dividend / divisor
        except ZeroDivisionError:
            division = 0
            print("division by 0")
        except (TypeError, ValueError):
            division = 0
            print("wrong type")
        finally:
            result.append(division)
    if len(my_list_1) < list_length or len(my_list_2) < list_length:
        print("out of range")
    return result
