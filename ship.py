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

        # Флаги перемещения
        self.moving_right = False
        self.moving_left  = False


    # Обновление позиции корабля с учетом флага
    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1


    # Отрисовка корабля
    def blitme(self):
        self.screen.blit(self.image, self.rect)