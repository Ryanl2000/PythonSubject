from collections import deque
from inspect import stack
from queue import PriorityQueue

class Node:  #节点
    def __init__(self, value) -> None:
        self.value = value  #节点编号/编码
        self.node_in = 0  #箭头指向该节点的数量
        self.node_out = 0  #箭头指出该节点的数量
        self.nexts = []  #该节点指向的下一节点
        self.edges = []  #该节点周围的边（和指向节点一一对应）

class Edge:  #边
    def __init__(self, weight, edgeFrom, edgeTo) -> None:
        self.weight = weight  #边的长度
        self.edgeFrom = edgeFrom  #边的起点
        self.edgeTo = edgeTo  #边的终点

class Graph:  #图
    def __init__(self) -> None:
        self.nodes = {}  #图的节点集合（编号：节点）
        self.edges = []  #图中包含的所有边

class MySet:  #创建Kruskal算法支持表
    def __init__(self) -> None:
        self.map = {}
    
    def fillSets(self, nodes):
        for cur in nodes:
            s = []
            s.append(cur)
            self.map[cur] = s

    def isSameSet(self, from_, to_):
        fromSet = self.map[from_]
        toSet = self.map[to_]
        return fromSet == toSet
    
    def union(self, from_, to_):
        fromSet = self.map[from_]
        toSet = self.map[to_]
        for i in toSet:  #无向树有两个箭头，所以这里只针对to进行操作
            fromSet.append(i)
            self.map[i] = fromSet

def CreatGraphFromMatrix(matrix):  #将非标准图转换为标准图
    graph = Graph()
    for i in range(len(matrix)):
        from_ = matrix[i][0]  #根据实际情况修改
        to_ = matrix[i][1]
        weight_ = matrix[i][2]
        if not graph.nodes.get(from_):
            graph.nodes[from_] = Node(from_)
        if not graph.nodes.get(to_):
            graph.nodes[to_] = Node(to_)
        fromNode = graph.nodes.get(from_)
        toNode = graph.nodes.get(to_)
        newEdge = Edge(weight_, fromNode, toNode)
        fromNode.nexts.append(toNode)
        fromNode.node_out += 1
        toNode.node_in += 1
        fromNode.edges.append(newEdge)
        graph.edges.append(newEdge)
    return graph

def GraphBFS(node): #宽度优先遍历
    if not node:
        return
    queue = deque()
    if_contain = []
    queue.append(node)
    if_contain.append(node)
    while queue:
        cur = queue.popleft()
        print(cur.value, end=',')
        for i in cur.nexts:
            if i not in if_contain:
                queue.append(i)
                if_contain.append(i)
        
def GraphDFS(node):  #深度优先遍历
    if not node:
        return
    stack = deque()
    if_contain = []
    stack.append(node)
    if_contain.append(node)
    print(node.value, end=',')
    while stack:
        cur = stack.pop()
        for i in cur.nexts:
            if i not in if_contain:
                stack.append(cur)
                stack.append(i)
                if_contain.append(i)
                print(i.value, end=',')
                break

def TopologySort(graph):  #拓扑排序
    inMap = {}
    inQueue = deque()
    for node in graph.nodes.values():
        inMap[node] = node.node_in
        if node.node_in == 0:
            inQueue.append(node)
    res = []
    while inQueue:
        cur = inQueue.popleft()
        res.append(cur)
        for next in cur.nexts:
            inMap[next] -= 1
            if inMap[next] == 0:
                inQueue.append(next)
    return res 

def KruskalMST(graph):  #使用Kruskal算法计算最小生成树
    unifound = MySet()
    unifound.fillSets(graph.nodes.values())
    prqueue = []
    for edge in graph.edges:
        prqueue.append(edge)
    prqueue.sort(key=lambda x:x.weight, reverse=True)
    res = []
    while prqueue:
        edge = prqueue.pop()
        if not unifound.isSameSet(edge.edgeFrom, edge.edgeTo):
            res.append(edge)
            unifound.union(edge.edgeFrom, edge.edgeTo)
    return res

def primMST(graph):  #prim算法计算最小生成树   
    prqueue = []
    if_contain = []
    res = []
    #for node in graph.nodes.values():  #随机找一个Node，目的是处理森林问题
    node = list(graph.nodes.values())[0]  #这一行和上一行只存在一个
    if node not in if_contain:
        if_contain.append(node)  #将该Node放入能识别是够存在的if数组中
        for edges in node.edges: 
            prqueue.append(edges)  #将新解锁的边加入到优先级队列中
            prqueue.sort(key=lambda x:x.weight, reverse=True)
        while prqueue:  
            edge = prqueue.pop()  #选取最小值，此后进行和以上相同的重复操作
            toNode = edge.edgeTo
            if toNode not in if_contain:
                if_contain.append(toNode)
                res.append(edge)
                for edges in toNode.edges:
                    prqueue.append(edges)
                    prqueue.sort(key=lambda x:x.weight, reverse=True)
    return res

def Dijkastra(graph):  #Dijkastra算法
    res = {}
    stack = []
    node = list(graph.nodes.values())[0]
    if_contain = []
    for nodes in graph.nodes.values():
        if nodes == node:
            res[nodes] = 0
        else:
            res[nodes] = float('inf')
    for i in node.edges:
        stack.append(i)
    stack.sort(key=lambda x:x.weight)
    while stack:
        edge = stack.pop()
        if edge.weight + res[edge.edgeFrom] < res[edge.edgeTo]:
            res[edge.edgeTo] = edge.weight + res[edge.edgeFrom]
        if not stack:
            if_contain.append(node)
            if len(if_contain) == len(graph.nodes.values()):
                break
            mins = float('inf')
            for nodes in graph.nodes.values():
                if nodes not in if_contain and res[nodes] < mins:
                    node = nodes
                    mins = res[nodes]
            for i in node.edges:
                stack.append(i)
            stack.sort(key=lambda x:x.weight)
    return res

matrix = [
     [1,3,6]  #1.1
    ,[3,1,6]  #1.2
    ,[3,2,2]  #2.1
    ,[2,3,2]  #2.2
    ,[2,4,3]  #3.1
    ,[4,2,3]  #3.2
    ,[3,4,5]  #4.1
    ,[4,3,5]  #4.2
    #,[1,4,1]  #5.1
]

g1 = CreatGraphFromMatrix(matrix)  #实例化对象

print('BFS:')
GraphBFS(list(g1.nodes.values())[0])

print('\nDFS:')
GraphDFS(list(g1.nodes.values())[0])

print('\nTop:')
for i in TopologySort(g1):
    print(i.value, end=',')

print('\nKruskal:')
for i in KruskalMST(g1):
    print(i.weight, end=',')

print('\nPrim:')
for i in primMST(g1):
    print(i.weight, end=',')

print('\nDijkastra:')
for i in Dijkastra(g1).items():
    print(i[-1], end=',')