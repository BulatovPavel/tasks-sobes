import sys

path1, path2 = sys.argv[1:]

coords = []
with open(path1, 'r') as f:
    for line in f:
        coords.append(list(map(int, line.split(' '))))

dots = []
with open(path2, 'r') as f:
    for line in f:
        dots.append(list(map(int, line.split(' '))))

x0 = coords[0][0]
y0 = coords[0][1]
a = coords[1][0]
b = coords[1][1]

for dot in dots:
    x = dot[0]
    y = dot[1]
    uravn = ((x-x0)/a)**2 + ((y-y0)/b)**2
    # print(f'>>>>>>>>> {uravn}')
    if uravn == 1:
        print(0)
    elif uravn < 1:
        print(1)
    else:
        print(2)

