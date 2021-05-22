#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    if len(my_list) == 0:
        return 0
    unique = my_list[0]
    for idx in range(len(my_list)):
        if my_list[idx] not in my_list[:idx]:
            sum += my_list[idx]
        else:
            sum += 0
    return sum
