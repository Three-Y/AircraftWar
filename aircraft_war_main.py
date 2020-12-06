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
        pygame.time.set_timer(HERO_FIRE_EVENT, 400)

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
                self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                self.enemy_group.add(Enemy())
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

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
        pygame.sprite.groupcollide(self.enemy_group, self.hero.bullet_group, True, True)
        died_enemys = pygame.sprite.spritecollide(self.hero,self.enemy_group, True)

        if len(died_enemys) > 0:
            self.hero.kill()
            self.__game_over()

    def __update_sprite_group(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("Game Over!")
        pygame.quit()
        exit()


if __name__ == "__main__":
    game = AircraftWarGame()
    game.statr_game()
