import sys

n1, m1, n2, m2 = map(int, sys.argv[1:])
arr1 = [str(i) for i in range(1, n1+1)]
arr2 = [str(i) for i in range(1, n2+1)]

flag1, flag2 = False, False
idx1 = 0
idx2 = 0
path1 = ''
path2 = ''
while not (flag1 and flag2):
    if not flag1:
        s1 = ''.join([arr1[(idx1+i)%n1] for i in range(m1)])
        idx1 += m1-1
        path1 += s1[0]
        if s1[-1] == '1':
            flag1 = True

    if not flag2:
        s2 = ''.join([arr2[(idx2+i)%n2] for i in range(m2)])
        idx2 += m2-1
        path2 += s2[0]
        if s2[-1] == '1':
            flag2 = True

print(path1+path2)        

