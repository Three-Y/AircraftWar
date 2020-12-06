import pygame
import random

# 屏幕
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
REFRESH_TIMES_PER_SEC = 60
# 敌机生成事件
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image, speed=1):
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args, **kwargs) -> None:
        self.rect.y += self.speed


class Background(GameSprite):

    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -SCREEN_RECT.height

    def update(self, *args, **kwargs) -> None:
        super().update()

        if self.rect.top > SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height


class Enemy(GameSprite):

    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_RECT.width-self.rect.width)
        self.speed = random.randint(2, 3)

    def update(self, *args, **kwargs) -> None:
        super().update()
        if self.rect.top > SCREEN_RECT.height:
            self.kill()


class Hero(GameSprite):

    def __init__(self):
        super().__init__("./images/me1.png")
        self.rect.bottom = SCREEN_RECT.height - 50
        self.speed = 0
        self.rect.centerx = SCREEN_RECT.centerx
        self.bullet_group = pygame.sprite.Group()

    def fire(self):
        # 一次发射三颗子弹
        for i in [0, 1, 2]:
            bullet = Bullet(self.rect.centerx, self.rect.y + 10 + 13 * i)
            self.bullet_group.add(bullet)

    def update(self, *args, **kwargs) -> None:
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right


class Bullet(GameSprite):

    def __init__(self, x, y):
        super().__init__("./images/bullet1.png", -2)
        self.rect.centerx = x
        self.rect.y = y

    def update(self, *args, **kwargs) -> None:
        super().update()
        if self.rect.bottom < 0:
            self.kill()
