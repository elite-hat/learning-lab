def find_max(list):
    max = list[0]
    for number in list:
        if max < number:
            max = number
    return max