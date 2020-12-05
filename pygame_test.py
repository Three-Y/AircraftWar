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
"""

import pygame

# 导入并初始化所有pygame模块
pygame.init()

# 创建窗口对象，显示游戏窗口
screen = pygame.display.set_mode((480, 700))
# 加载背景图像，将背景图像绘制到窗口
background = pygame.image.load("./images/background.png")
screen.blit(background, (0, 0))
# 加载并绘制飞机
player = pygame.image.load("./images/me1.png")
player_rect = pygame.Rect(189, 550, 102, 126)  # 记录坐标的对象
screen.blit(player, (player_rect.x, player_rect.y))
# 更新窗口的显示
pygame.display.update()
# 游戏时钟
clock = pygame.time.Clock()

# 游戏循环
while True:
    # 1秒60帧
    clock.tick(60)

    player_rect.y -= 3
    if player_rect.y < -126:
        player_rect.y = 700

    screen.blit(background, (0, 0))
    screen.blit(player, (player_rect.x, player_rect.y))
    pygame.display.update()

# 卸载所有pygame模块
pygame.quit()