# 最大活动奖励
# N：活动数
# day：时长
# Matrix：首项为所需时长，第二项为奖励，后续为依赖关系
N = 8
day = 10
Matrix = [[3,2000,0,1,1,0,0,0,0,0],
          [3,4000,0,0,0,1,1,0,0,0],
          [2,2500,0,0,0,1,0,0,0,0],
          [1,1600,0,0,0,0,1,1,1,0],
          [4,3800,0,0,0,0,0,0,0,1],
          [2,2600,0,0,0,0,0,0,0,1],
          [4,4000,0,0,0,0,0,0,0,1],
          [3,3500,0,0,0,0,0,0,0,0]]

class ActNode:
    def __init__(self) -> None:
        self.map = {}


def MaxActivity():
    ActMap = []
    for i in range(N):
        ActMap.append(ActNode())
    ActMap[N-1].map[Matrix[N-1][0]] = [Matrix[N-1][1]]
    for i in range(N-2,-1,-1):
        for j in range(N):
            if Matrix[i][j+2] == 1:
                for k in range(len(ActMap[j].map)):
                    for m in range(len([*ActMap[j].map.values()][k])):
                        if not ActMap[i].map.get(Matrix[i][0]+[*ActMap[j].map.keys()][k]):
                            ActMap[i].map[Matrix[i][0]+[*ActMap[j].map.keys()][k]] = [Matrix[i][1] + [*ActMap[j].map.values()][k][m]]
                        else:
                            ActMap[i].map[Matrix[i][0]+[*ActMap[j].map.keys()][k]].append(Matrix[i][1] + [*ActMap[j].map.values()][k][m])
                            ActMap[i].map[Matrix[i][0]+[*ActMap[j].map.keys()][k]].sort(reverse=True)
                            ActMap[i].map[Matrix[i][0]+[*ActMap[j].map.keys()][k]] = [ActMap[i].map[Matrix[i][0]+[*ActMap[j].map.keys()][k]][0]]
    FinalMap = {}
    for i in range(N):
        print(len(ActMap[i].map))
        for j in range(len(ActMap[i].map)):
            if not FinalMap.get([*ActMap[i].map.keys()][j]):
                print([*ActMap[i].map.values()][j])
                FinalMap[[*ActMap[i].map.keys()][j]] = [*ActMap[i].map.values()][j][0]
            else:
                if [*ActMap[i].map.values()][j][0] > FinalMap[[*ActMap[i].map.keys()][j]]:
                    FinalMap[[*ActMap[i].map.keys()][j]] = [*ActMap[i].map.values()][j][0]
    #  可能还需要进行进一步排序



print(MaxActivity())


    