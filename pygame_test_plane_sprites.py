import pygame
"""
精灵类
    将精灵对象放到精灵组中，直接调用精灵组的update方法，就会分别调用每个精灵的update方法，无需自己手动逐个调用    
"""


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image, speed=1):
        super().__init__()

        self.image =  pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed

    # 重写了update方法
    def update(self, *args, **kwargs) -> None:
        self.rect.y += self.speed

