class Settings():
  #Класс для хранения настроек игры

  def __init__(self):
    """Инициализирует настройки игры"""
    #Параметры экрана
    self.screen_width = 1200
    self.screen_height = 700
    self.bg_color = (230, 230, 230)

    #Параметры корабля
    self.ship_limit = 3

    #Параметры пули
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = 180,100,60
    self.bullets_allowed = 10

    #Параметры пришельцев
    self.fleet_drop_speed = 10

    #Темп ускорения игры
    self.speedup_scale = 1.1

    self.initialize_dynamic_settings()

  def initialize_dynamic_settings(self):
    self.ship_speedx_factor = 1.5
    self.ship_speedy_factor = 1.2
    self.bullet_speed_factor = 2.5
    self.alien_speed_factor = 1

    self.fleet_direction = 1

  def increase_speed(self):
    self.ship_speedx_factor *= self.speedup_scale
    self.ship_speedy_factor *= self.speedup_scale
    self.bullet_speed_factor *= self.speedup_scale
    self.alien_speed_factor *= self.speedup_scale