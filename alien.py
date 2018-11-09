import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
  """Класс, представляющий одного пришельца"""
  def __init__(self, ai_settings, screen):
    """Инициализирует пришельца и задает его начальную позицию"""
    super(Alien, self).__init__()
    self.ai_settings = ai_settings
    self.screen = screen

    #Загрузка изображения
    self.image = pygame.image.load('images/alien.bmp')
    self.rect = self.image.get_rect()

    #Появление в левом верхнем углу экрана
    self.rect.x = self.rect.width
    self.rect.y = self.rect.height

    #Сохранение позиции
    self.x = float(self.rect.x)

  def blitme(self):
    """Выводит пришельца в текущем положении"""
    self.screen.blit(self.image, self.rect)    