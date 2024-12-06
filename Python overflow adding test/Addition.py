import numpy as np

def left_extract(a):
    return a >> 8

def right_extract(a):
    return a - (left_extract(a) << 8)

def add(a, b):

    a0 = left_extract(a)
    a1 = right_extract(a)

    b0 = left_extract(b)
    b1 = right_extract (b)

    print(f'number: {hex(a)} \nlex: {hex(a0)}, rex: {hex(a1)}')

    right_result_inc_remainder = a1+b1
    remainder = left_extract(right_result_inc_remainder)
    right_result_final = right_extract(right_result_inc_remainder)


    print(f'remainder: {hex(remainder)}')
    left_result_final = remainder + a0+b0
    print(f'a0{hex(a0)}, b0{hex(b0)}')

    print(f'result: {str(hex(left_result_final))[2:]}{str(hex(right_result_final))[2:]}')

    print(f'correct result: {str(hex(int(a)+int(b)))[2:]}')

    return left_result_final, right_result_final

def combine3(x10000, x100, x):
    final_value_0 = right_extract(x)
    intermediate = left_extract(x)
    intermediate, final_value_1 = add(x100, intermediate)
    final_value_3, final_value_2 = add(x10000, intermediate)

    return final_value_3 , final_value_2, final_value_1, final_value_0