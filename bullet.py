import pygame
from pygame.sprite import Sprite

# Класс уравление пулями корабля
class Bullet(Sprite):
    def __init__(self, aiSetting, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        # Создание пули в позиции (0,0) и назначени правильной
        self.rect = pygame.Rect(0, 0, aiSetting.Bullet.Width, aiSetting.Bullet.hieght)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Позиция пули
        self.positionBulletY = float(self.rect.positionBulletY)

        # Параметры пули
        self.color       = aiSetting.Bullet.color
        self.speedFactor = aiSetting.Bullet.speed


    # Перемешение пули вверх
    def update(self):
        self.positionBulletY -= self.speedFactor
        self.rect.positionBulletY = self.y


    # Вывод пули
    def drawBullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
