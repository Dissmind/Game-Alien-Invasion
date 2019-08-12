import pygame

# Класс для поведения корабля
class Ship():
    def __init__(self, screen):
        # Инициализация корабля
        self.screen = screen

        # Загрузка изображения корабля и получение границ объекта
        self.image      = pygame.image.load('res/img/ship.bmp')
        self.rect       = self.image.get_rect()
        self.screenRect = screen.get_rect()

        # Спавн корабля у нижнего края
        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom  = self.screenRect.bottom

    # Отрисовка корабля
    def blitme(self):
        self.screen.blit(self.image, self.rect)