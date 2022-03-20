class Node:
    def __init__(self, value) -> None:
        self.value = value  #节点编号/编码
        self.node_in = 0  #箭头指向该节点的数量
        self.node_out = 0  #箭头指出该节点的数量
        self.nexts = []  #该节点指向的下一节点
        self.edges = []  #该节点周围的边（和指向节点一一对应）

class Edge:
    def __init__(self, weight, edgeFrom, edgeTo) -> None:
        self.weight = weight  #边的长度
        self.edgeFrom = edgeFrom  #边的起点
        self.edgeTo = edgeTo  #边的终点

class Graph:
    def __init__(self) -> None:
        self.nodes = {}  #图的节点集合（编号：节点）
        self.edges = []  #图中包含的所有边

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

matrix = [
    [1,3,6],
    [3,2,2],
    [2,4,3],
    [3,4,1],
    [4,3,5]
]

CreatGraphFromMatrix(matrix)