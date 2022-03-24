#生成所有子集
def allSubset(str, i):
    if i == len(str):
        print(str)
        return
    allSubset(str, i+1)
    tmp = str[i]
    str[i] = ''
    allSubset(str, i+1)
    str[i] = tmp

#allSubset(list('abc'), 0)

def swap(str, i, j):
    temp = str[i]
    str[i] = str[j]
    str[j] = temp

#生成全排列(#掉的为不重复全排列)
def allArray(str, i):
    if i == len(str):
        print(str)
        return
    #visit = [0] * 26
    for j in range(i, len(str)):
        #if visit[ord(str[j]) - ord('a')] == 0:
            #visit[ord(str[j]) - ord('a')] = 1
            swap(str, i, j)
            allArray(str, i+1)
            swap(str, i, j)

allArray(list('aac'), 0)