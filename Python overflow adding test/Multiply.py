import numpy as np
import Addition
import random

a = np.uint16(random.randint(0, 0xFFFF))
b = np.uint16(random.randint(0, 0xFFFF))

a = 0xAAAA
b = 0x1111

r1, r2 = Addition.add(a, b)
print(f'r1: {hex(r1)}, r2: {hex(r2)}')
exit()

a0 = a >> 8
a1 = a - (a0 << 8)

b0 = b >> 8
b1 = b - (b0 << 8)

# * 0x10000
r0 = a0*b0
# * 0x100
r1 = a1*b0 + a0*b1
# * 0x1
r2 = a1*b1

final_value_0, final_value_1, final_value_2, final_value_3 = Addition.combine3(r0, r1, r2)

print(f'{str(hex(final_value_0))[2:]}, {str(hex(final_value_1))[2:]}, {str(hex(final_value_2))[2:]}, {str(hex(final_value_3))[2:]}')

print(f'{hex(int(a)*int(b))}')

# Final step is to implement the adding ffs.... This also means i could have used a for loop of length b of adding a to itself. woudl have been slow like that tho

