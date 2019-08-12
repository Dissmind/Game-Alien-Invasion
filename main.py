import sys
import pygame

# Импорт класса настроек
from setting import Setting
# Импорт класса Корабля
from ship import Ship
# Импорт модуля с вспомагательными функциями
import game_function as gf


def startGame():
    # Инициализация настроек игры, создания объект экрана
    pygame.init()
    aiSetting = Setting()

    # Создание отображание облости, установка размера окна
    screen = pygame.display.set_mode((aiSetting.screenWidth, aiSetting.screenHieght))
    # Установка заголовка окна
    pygame.display.set_caption('Alien Invasion')
    # Инициализация копрабля
    ship = Ship(screen)



    # Запуск игры

    # Отслежевание событий клавиатуры и мыши
    while True:

        # Обработка нажатия клавишь и события мыши
        gf.checkEvents()

        # Обоновляет изображение на экране и отображает новый экран
        gf.updateScreen(aiSetting, screen, ship)

startGame()
