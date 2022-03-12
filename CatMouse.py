import random
class Animal(object):
    step = [-2, -1, 0, 1, 2]
    def __init__(self, gm, point = None):
        self.gm = gm
        if point == None:
            self.point = random.randint(0, 100)
        else:
            self.point = point
    def move(self ,aStep = random.choice(step)):
        if 0 <= self.point + aStep <= 50:
            self.point += aStep
class Cat(Animal):
    def __init__(self, gm, point = None):
        super(Cat, self).__init__(gm, point)
        self.gm.setPoint('cat', self.point)
    def move(self):
        aStep = int(input('请输入猫移动的步数：'))
        super(Cat, self).move(aStep)
        self.gm.setPoint('cat', self.point)
class Mouse(Animal):
    def __init__(self, gm, point = None):
        super(Mouse, self).__init__(gm, point)
        self.gm.setPoint('mouse', self.point)
    def move(self):
        super(Mouse, self).move()
        self.gm.setPoint('mouse', self.point)
class GameMap(object):
    def __init__(self):
        self.catPoint, self.mousePoint = None, None
    def setPoint(self, obj, point):
        if obj == 'cat':
            self.catPoint = point
        if obj == 'mouse':
            self.mousePoint = point
    def catched(self):
        print('老鼠：', self.mousePoint, '\t猫：', self.catPoint)
        if self.mousePoint is not None and self.catPoint is not None \
                and self.mousePoint == self.catPoint:
            return True
if __name__ == '__main__':
    gm = GameMap()
    mouse = Mouse(gm)
    cat = Cat(gm)
    while not gm.catched():
        mouse.move()
        cat.move()
    else:
        print('猫抓住老鼠，游戏结束！')