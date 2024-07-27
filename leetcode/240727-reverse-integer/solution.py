def reverse(x: int) -> int:
    str_x = str(x)

    if str_x[0] == '-':
        reversed_str_x = '-' + str_x[:0:-1]
    else: 
        reversed_str_x = str_x[::-1]

    if int(reversed_str_x) > 2 ** 31 - 1 or int(reversed_str_x) < -2 ** 31:
        return 0
    
    return int(reversed_str_x)

