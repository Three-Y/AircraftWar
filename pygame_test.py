"""
飞机大战
    pygame.init() 游戏初始化，加载pygame模块
    pygame.quit() 退出游戏，卸载pygame模块
    pygame.display.set_mode((width, height)) 返回窗口对象
    pygame.image.load(图片路径) 加载图片
    screen.blit(绘制的东西, (x, y)) 绘图
    pygame.display.update() 将绘制好的画面显示到窗口
    pygame.Rect(x, y, width, height) 记录游戏中元素的坐标和大小
    pygame.time.Clock() 游戏时钟对象
    clock.tick(一秒多少帧) 游戏更新频率
    pygame.event.get() 返回一个列表，记录了监听到的所有事件
    image.get_rect() 返回一个x=0、y=0、宽高与图片相同的Rect对象
    pygame.time.set_timer(要触发的事件, 间隔时间) 定时器，定时触发某事件
    pygame.USEREVENT 用户事件
    pygame.KEYDOWN 按键按下事件
    事件对象.key 按下的按键
    pygame.key.get_pressed() 返回按下的按键的元组
"""

import pygame
from pygame_test_plane_sprites import *

# 导入并初始化所有pygame模块
pygame.init()

# 创建窗口对象，显示游戏窗口

screen = pygame.display.set_mode((480, 700))
# 加载背景图像，将背景图像绘制到窗口

background = pygame.image.load("./images/background.png")
screen.blit(background, (0, 0))

# 加载并绘制玩家飞机
player = pygame.image.load("./images/me1.png")
player_rect = pygame.Rect(189, 550, 102, 126)  # 记录坐标的对象
screen.blit(player, (player_rect.x, player_rect.y))

# 敌机（创建精灵对象，创建精灵组，将所有精灵对象加入到精灵组中）
enemy1 = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy1.png", 2)
enemy_group = pygame.sprite.Group(enemy1, enemy2)

# 更新窗口的显示
pygame.display.update()

# 游戏时钟
clock = pygame.time.Clock()

# 游戏循环
while True:
    # 1秒60帧
    clock.tick(60)

    # 事件监听
    for event in pygame.event.get():

        # 退出游戏
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # 玩家飞机的移动
    player_rect.y -= 3
    if player_rect.y < -126:
        player_rect.y = 700

    screen.blit(background, (0, 0))
    screen.blit(player, (player_rect.x, player_rect.y))

    # 精灵组
    enemy_group.update()
    enemy_group.draw(screen)  # 需要传递窗口对象

    # 更新窗口显示
    pygame.display.update()

# 卸载所有pygame模块
pygame.quit()