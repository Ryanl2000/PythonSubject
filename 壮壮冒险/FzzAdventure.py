import pygame
from pygame.locals import *
import sys
from itertools import cycle
import random

SCREENWIDTH = 820
SCREENHRIGHT = 199
FPS = 30


class MyMap():
    def __init__(self, x, y):
        self.bg = pygame.image.load('image/bg.png')
        self.x = x
        self.y = y

    def map_roll(self):
        if self.x < -800:
            self.x = 800
        else:
            self.x -= 5

    def map_update(self):
        SCREEN.blit(self.bg, (self.x, self.y))


class Zhuangzhuang():
    def __init__(self):
        # 初始化壮壮矩形
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.jumpIf = False
        self.jumpHeight = 130  # 跳跃的高度
        self.lowest_y = 140  # 最低坐标？？？
        self.jumpValue = 0  # 跳跃增变量
        # 壮壮动图索引
        self.fzzIndex = 0
        self.fzzIndexGen = cycle([0, 1, 2])
        # 加载壮壮图片
        self.adventure_img = (
            pygame.image.load('image/FZZ1.png').convert_alpha(),
            pygame.image.load('image/FZZ2.png').convert_alpha(),
            pygame.image.load('image/FZZ3.png').convert_alpha()
        )
        self.jump_audio = pygame.mixer.Sound('audio/jump.wav')
        self.rect.size = self.adventure_img[0].get_size()
        self.x = 50
        self.y = self.lowest_y
        self.rect.topleft = (self.x, self.y)

    def jump(self):
        self.jumpIf = True

    def move(self):
        if self.jumpIf:
            if self.rect.y >= self.lowest_y:
                self.jumpValue = -5
            if self.rect.y <= self.lowest_y - self.jumpHeight:
                self.jumpValue = 5
            self.rect.y += self.jumpValue
            if self.rect.y >= self.lowest_y:
                self.jumpIf = False

    def draw_fzz(self):
        # 匹配壮壮动图
        fzzIndex = next(self.fzzIndexGen)
        SCREEN.blit(self.adventure_img[fzzIndex], (self.x, self.rect.y))


class Obstacle():
    score = 1
    move = 5
    obstacle_y = 150  # 障碍物y坐标

    def __init__(self):
        # 初始化障碍物矩形
        self.rect = pygame.Rect(0, 0, 0, 0)
        # 加载障碍物图片
        self.missile = pygame.image.load('image/missile.png').convert_alpha()
        self.pipe = pygame.image.load('image/pipe.png').convert_alpha()
        # 加载分数图片
        self.numbers = (
            pygame.image.load('image/0.png').convert_alpha(),
            pygame.image.load('image/1.png').convert_alpha(),
            pygame.image.load('image/2.png').convert_alpha(),
            pygame.image.load('image/3.png').convert_alpha(),
            pygame.image.load('image/4.png').convert_alpha(),
            pygame.image.load('image/5.png').convert_alpha(),
            pygame.image.load('image/6.png').convert_alpha(),
            pygame.image.load('image/7.png').convert_alpha(),
            pygame.image.load('image/8.png').convert_alpha(),
            pygame.image.load('image/9.png').convert_alpha()
        )
        # 加分音效
        self.score_audio = pygame.mixer.Sound('audio/score.wav')
        r = random.randint(0, 1)
        if r == 0:  # 如果是0显示导弹障碍物
            self.image = self.missile
            self.move = 15  # 导弹移动速度较快
            self.obstacle_y = 100
        else:
            self.image = self.pipe
        self.rect.size = self.image.get_size()
        self.width, self.height = self.rect.size
        # 障碍物绘制坐标
        self.x = 800
        self.y = self.obstacle_y
        self.rect.center = (self.x, self.y)

    def obstacle_move(self):
        self.rect.x -= self.move

    def draw_obstacle(self):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

    def getscore(self):
        tmp = self.score
        if tmp == 1:
            self.score_audio.play()
        self.score = 0
        return tmp

    def showScore(self, score):
        self.scoreDigits = [int(x) for x in list(str(score))]
        totalWidth = 0  # 要显示的所有数字的总宽度
        for digit in self.scoreDigits:
            totalWidth += self.numbers[digit].get_width()
        # 分数横向位置
        Xoffset = (SCREENWIDTH - (totalWidth + 30))
        for digit in self.scoreDigits:
            SCREEN.blit(self.numbers[digit], (Xoffset, SCREENHRIGHT * 0.1))
            # 随着数字的增加改变位置
            Xoffset += self.numbers[digit].get_width()


class Music_Button():
    is_open = True

    def __init__(self):
        self.open_img = pygame.image.load('image/btn_open.png').convert_alpha()
        self.close_img = pygame.image.load('image/btn_close.png').convert_alpha()
        self.bg_music = pygame.mixer.Sound('audio/bg_music.wav')

    # 判断鼠标是否在按钮的范围内
    def is_select(self):
        point_x, point_y = pygame.mouse.get_pos()
        w, h = self.open_img.get_size()
        in_x = point_x > 20 and point_x < 20 + w
        in_y = point_y > 20 and point_y < 20 + h
        return in_x and in_y


def gameover():
    bump_audio = pygame.mixer.Sound('audio/bump.wav')
    bump_audio.play()  #播放撞击音效
    #获取窗体宽和高
    screen_w = pygame.display.Info().current_w
    screen_h = pygame.display.Info().current_h
    #加载游戏结束图片
    over_img = pygame.image.load('image/gameover.png').convert_alpha()
    SCREEN.blit(over_img,((screen_w - over_img.get_width())/2, (screen_h - over_img.get_height())/2))


def mainGame():
    score = 0
    over = False
    global SCREEN, FPSLOCK
    pygame.init()  # 程序初始化
    FPSLOCK = pygame.time.Clock()  # 创建Clock对象
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHRIGHT))  # 创建窗体
    pygame.display.set_caption('壮壮冒险')  # 设置窗体标题
    bg1 = MyMap(0, 0)
    bg2 = MyMap(800, 0)
    fzz = Zhuangzhuang()
    addObstacleTimer = 0
    list = []
    music_button = Music_Button()
    btn_img = music_button.open_img
    music_button.bg_music.play(-1)  # 循环播放
    while True:  # 检测
        for event in pygame.event.get():
            if event.type == QUIT:  # 如果鼠标单击关闭，则退出程序
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                if fzz.rect.y >= fzz.lowest_y:
                    fzz.jump_audio.play()
                    fzz.jump()
                if over == True:
                    mainGame()
            if event.type == pygame.MOUSEBUTTONUP:
                if music_button.is_select():
                    if music_button.is_open:
                        btn_img = music_button.close_img
                        music_button.is_open = False
                        music_button.bg_music.stop()
                    else:
                        btn_img = music_button.open_img
                        music_button.is_open = True
                        music_button.bg_music.play(-1)
        pygame.display.update()
        FPSLOCK.tick(FPS)
        if over == False:
            # 绘制地图，并更新地图
            bg1.map_update()
            bg1.map_roll()
            bg2.map_update()
            bg2.map_roll()
            fzz.move()
            fzz.draw_fzz()
            if addObstacleTimer >= 1300:
                r = random.randint(0, 100)
                if r > 40:
                    obstacle = Obstacle()
                    list.append(obstacle)
                addObstacleTimer = 0  # 重置添加障碍物时间
            # 循环遍历障碍物
            for i in range(len(list)):
                list[i].obstacle_move()
                list[i].draw_obstacle()
                if pygame.sprite.collide_circle(fzz, list[i]):
                    over = True
                    gameover()
                    music_button.bg_music.stop()
                else:
                    if (list[i].rect.x + list[i].rect.width) < fzz.rect.x:
                        score += list[i].getscore()
                list[i].showScore(score)
        addObstacleTimer += 20
        SCREEN.blit(btn_img, (20, 20))



if __name__ == '__main__':
    mainGame()
