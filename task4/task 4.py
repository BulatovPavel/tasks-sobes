# -*- coding: cp1251 -*-

import sys

_, path = sys.argv

def median(arr):
    if len(arr) % 2 == 1:
        return arr[len(arr)//2]
    else:
        return arr[len(arr)//2-1]
    
with open(path) as f:
    arr = list(map(int, f.read().split('\n')))

med = median(arr)

ans = sum([abs(i-med) for i in arr])

if ans > 20:
    ans = '20 ходов недостаточно для приведения всех элементов массива к одному числу'
print(ans)