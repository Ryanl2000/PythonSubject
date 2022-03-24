#岛问题
def infect(list, x, y):
    if x < 0 or x > len(list) - 1:
        return
    if y < 0 or y > len(list[0]) - 1:
        return
    if list[x][y] == 1:
        list[x][y] = 2
        infect(list, x-1, y)
        infect(list, x+1, y)
        infect(list, x, y-1)
        infect(list, x, y+1)
    else:
        return

list = [
    [0,0,1,0,1,0],
    [0,1,1,0,1,0],
    [1,1,0,0,1,1],
    [0,0,1,0,0,0]
]
res = 0
for i in range(len(list)):
    for j in range(len(list[0])):
        if list[i][j] == 1:
            infect(list, i, j)
            res += 1
print(res)