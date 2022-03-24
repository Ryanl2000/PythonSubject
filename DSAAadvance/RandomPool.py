# 重建哈希表
from random import randint


class RandomPool:
    def __init__(self) -> None:
        self.map1 = {}
        self.map2 = {}
        self.size = 0

    def insert(self, key):
        if key not in self.map1.keys():
            self.map1[key] = self.size
            self.map2[self.size] = key
            self.size += 1
        else:
            print('Aready exists')

    def delete(self, key):
        if key in self.map1.keys():
            if self.map1[key] == self.size - 1:
                del self.map1[key]
                del self.map2[self.size - 1]
                self.size -= 1
                print('Success delete')
            else:
                temp = self.map1[key]
                del self.map1[key]
                self.map2[temp] = self.map2[self.size - 1]
                self.map1[self.map2[self.size - 1]] = temp
                del self.map2[self.size - 1]
                self.size -= 1
                print('Success delete and replace')
        else:
            print('Not exists')

    def get_random(self):
        if self.size == 0:
            print('No values')
        else:
            rand = randint(0, self.size - 1)
            return self.map2[rand]


r = RandomPool()
r.insert('A')
r.insert('B')
r.insert('C')
r.insert('D')
r.insert('E')
r.insert('F')
r.insert('A')
print(r.map1.items())
r.delete('B')
print(r.map1.items())
print(r.map2.items())
print(r.get_random())