import pygame

class Ship():
  #Класс для представления корабля игрока

  def __init__(self, ai_settings, screen):
    """Инициализирует корабль и задает его начальную позицию"""
    self.screen = screen
    self.ai_settings = ai_settings

    #Загрузка изображения корабля и получение прямоугольника
    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()
    #Каждый новый корабль появляется у нижнего края экрана
    self.rect.centerx = self.screen_rect.centerx
    self.rect.centery = self.screen_rect.centery
    self.rect.bottom = self.screen_rect.bottom

    #Сохранение вещественной координаты центра корабля
    self.xcenter = float(self.rect.centerx)
    self.ycenter = float(self.rect.centery)

    #Флаг перемещения корабля
    self.moving_up = False
    self.moving_right = False
    self.moving_down = False
    self.moving_left = False

  def update(self):
    """Обновление позиции корабля с учетом флага"""

    #Обновляем атрибут ycenter u xcenter, но не rect
    if self.moving_up and self.rect.top > 0:
      self.ycenter -= self.ai_settings.ship_speedy_factor
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.xcenter += self.ai_settings.ship_speedx_factor
    if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
      self.ycenter += self.ai_settings.ship_speedy_factor
    if self.moving_left and self.rect.left > 0:
      self.xcenter -= self.ai_settings.ship_speedx_factor

    #Обновляем атрибут rect на основании self.xcenter
    self.rect.centerx = self.xcenter
    self.rect.centery = self.ycenter

  def blitme(self):
    """Рисует корабль в текущей позиции"""
    self.screen.blit(self.image, self.rect)

  def center_ship(self):
    self.xcenter = self.screen_rect.centerx
    self.ycenter = self.screen_rect.bottom - 50