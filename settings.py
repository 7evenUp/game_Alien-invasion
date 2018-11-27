class Settings():
  #Класс для хранения настроек игры

  def __init__(self):
    """Инициализирует настройки игры"""
    #Параметры экрана
    self.screen_width = 1200
    self.screen_height = 700
    self.bg_color = (230, 230, 230)

    #Параметры корабля
    self.ship_speedx_factor = 1.5
    self.ship_speedy_factor = 1.2
    self.ship_limit = 3

    #Параметры пули
    self.bullet_speed_factor = 2.5
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = 180,100,60
    self.bullets_allowed = 10

    #Параметры пришельцев
    self.alien_speed_factor = 1
    self.fleet_drop_speed = 10
    #fleet_direction: 1 означает движение вправо, -1 означает влево
    self.fleet_direction = 1