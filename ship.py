import pygame

# Класс для поведения корабля
class Ship():
    def __init__(self, screen, aiSetting):
        # Инициализация корабля
        self.screen = screen

        # Загрузка изображения корабля и получение границ объекта
        self.image      = pygame.image.load('res/img/ship.bmp')
        self.rect       = self.image.get_rect()
        self.screenRect = screen.get_rect()

        # Координата центра корабля
        self.center = float(self.rect.centerx)

        # Спавн корабля у нижнего края
        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom  = self.screenRect.bottom

        # Флаги перемещения
        self.movingRight = False
        self.movingLeft  = False

        # Настройки
        self.aiSetting = aiSetting


    # Обновление позиции корабля с учетом флага
    def update(self):
        if self.movingRight and self.rect.right < self.screenRect.right:
            self.rect.centerx += self.aiSetting.shipSpeed
        if self.movingLeft and self.rect.left > 0:
            self.rect.centerx -= self.aiSetting.shipSpeed



    # Отрисовка корабля
    def blitme(self):
        self.screen.blit(self.image, self.rect)