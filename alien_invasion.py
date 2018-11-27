import pygame
from pygame.sprite import Group

from game_stats import GameStats
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
  # Инициализирует игру, settings и создаёт объект экрана.
  pygame.init()
  ai_settings = Settings()
  stats = GameStats(ai_settings)
  screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
  pygame.display.set_caption('Alien Invasion')

  #Создание корабля
  ship = Ship(ai_settings, screen)
  #Создание группы для хранения пуль
  bullets = Group()
  #Создание пришельца
  aliens = Group()
  gf.create_fleet(ai_settings, screen, ship, aliens)

  #Запуск основного цикла игры
  while True:
    #Отслеживание событий клавиатуры и мыши.
    gf.check_events(ai_settings, screen, ship, bullets)

    if stats.game_active:
      ship.update()
      gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
      gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
    
    gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
