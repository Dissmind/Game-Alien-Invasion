import pygame
import sys


# Обработка нажатия клавишь и события мыши
def checkEvents():
    for event in pygame.event.get():
        # Обработка выхода
        if event.type == pygame.QUIT:
            sys.exit()



# Обоновляет изображение на экране и отображает новый экран
def updateScreen(aiSetting, screen, ship):
    # Отрисовка экрана
    screen.fill(aiSetting.bgColor)

    # Вывод корабля
    ship.blitme()

    # Отображение последнего отрисованого экрана
    pygame.display.flip()