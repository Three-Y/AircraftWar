import pygame
from game_sprite import *


class AircraftWarGame:

    def __init__(self):
        # 加载pygame模块
        pygame.init()
        # 设置窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 游戏时钟
        self.clock = pygame.time.Clock()
        # 创建游戏精灵
        self.__create_sprites()
        # 定时器事件
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    def statr_game(self):
        print("Game Start!")
        while True:
            # 更新帧率
            self.clock.tick(REFRESH_TIMES_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collision()
            # 更新精灵组
            self.__update_sprite_group()
            # 更新屏幕显示
            pygame.display.update()

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(is_alt=True)
        self.hero = Hero()
        self.bg_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.over_game()
            elif event.type == CREATE_ENEMY_EVENT:
                self.enemy_group.add(Enemy())

            # 方法一：长按不会一直触发
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            #     print("K_LEFT")

            # 方法二：长按会多次触发
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_LEFT]:
                self.hero.speed = -2
            elif pressed_keys[pygame.K_RIGHT]:
                self.hero.speed = 2
            elif not pressed_keys[pygame.K_LEFT] and not pressed_keys[pygame.K_RIGHT]:
                self.hero.speed = 0

    def __check_collision(self):
        pass

    def __update_sprite_group(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

    @staticmethod
    def over_game():
        print("Game Over!")
        pygame.quit()
        exit()


if __name__ == "__main__":
    game = AircraftWarGame()
    game.statr_game()