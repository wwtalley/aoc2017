from math import *
from itertools import count

#---- Part 1
# mem_point = 347991
# c_steps, len_layer, corner_val = 0, 1, 1
# while corner_val < mem_point:
#   c_steps += 1
#   len_layer = (c_steps*2+1)**2 - corner_val
#   corner_val = (c_steps*2+1)**2
#
# while mem_point < corner_val:
#   corner_val -= len_layer/4
#
# print(c_steps*2 - len_layer/8 + abs(corner_val + len_layer/8 - mem_point))

#----- Part 2



def sum_spiral():
    a, i, j = {(0,0) : 1}, 0, 0
    sn = lambda i,j: sum(a.get((k,l), 0) for k in range(i-1,i+2)
                                         for l in range(j-1,j+2))
    for s in count(1, 2):
        for _ in range(s):   i += 1; a[i,j] = sn(i,j); yield a[i,j]
        for _ in range(s):   j -= 1; a[i,j] = sn(i,j); yield a[i,j]
        for _ in range(s+1): i -= 1; a[i,j] = sn(i,j); yield a[i,j]
        for _ in range(s+1): j += 1; a[i,j] = sn(i,j); yield a[i,j]

    print(s)


def part2(n):
    for x in sum_spiral():
        if x>n: return x



sum_spiral()

answer = part2(347991)

print(answer)