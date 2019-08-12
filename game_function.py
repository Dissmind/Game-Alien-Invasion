import pygame
import sys



# Обработка нажатия клавишь и события мыши
def checkEvents(ship):
    for event in pygame.event.get():
        # Обработка выхода
        if event.type == pygame.QUIT:
            sys.exit()

        # Управление кораблем
        # if event.type == pygame.KEYDOWN:

            #   Перемешение
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False

        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         ship.moving_right = True
        # elif event.key == pygame.K_LEFT:
        #     ship.moving_left = True
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_RIGHT:
        #         ship.moving_right = False
        # elif event.key == pygame.K_LEFT:
        #     ship.moving_left = False

            # # Вправо
            # if event.key == pygame.K_RIGHT:
            #     ship.moving_right = True
            #
            #
            # elif event.type == pygame.KEYUP:
            #     if event.key == pygame.K_RIGHT:
            #         ship.moving_right = False
            #
            #     elif event.type == pygame.KEYDOWN:
            #         if event.key == pygame.K_RIGHT:
            #             ship.moving_right = False
            #
            #
            # # Влево
            # if event.key == pygame.K_LEFT:
            #     ship.moving_left = True
            #
            # elif event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT:
            #         ship.moving_left = False
            #
            #     elif event.type == pygame.KEYDOWN:
            #         if event.key == pygame.K_LEFT:
            #             ship.moving_left = False




# Обоновляет изображение на экране и отображает новый экран
def updateScreen(aiSetting, screen, ship):
    # Отрисовка экрана
    screen.fill(aiSetting.bgColor)

    # Вывод корабля
    ship.blitme()

    # Отображение последнего отрисованого экрана
    pygame.display.flip()