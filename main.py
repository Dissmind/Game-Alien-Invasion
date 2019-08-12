import sys
import pygame

# Импорт класса настроек
from setting import Setting
# Импорт класса Корабля
from ship import Ship

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
        for event in pygame.event.get():
            # Постояные события

            # Отрисовка экрана
            screen.fill(aiSetting.bgColor)
            # Вывод корабля
            ship.blitme()


            # Обработка выхода
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()

startGame()
