
# підлючення рудаме
import pygame
from random import randint

# кольори

YELLOW (200, 200, 0)
BLACK (0, 0, 0)
WHITE (255, 255, 255)
BLUE (0, 0, 255)
GREEN (0, 255, 0)
RED (255, 0, 0)

FPS = 50
SPEED = 5

# налаштування Рудаме

pygame.init()

screen pygame.display.set_mode((500, 500))
img_player pygame.image.load("DinoRun1.png").convert_alpha()
pygame.image.load("SmallCactus1.png") img_cactus


img_cloud pygame.image.load("Cloud.png")
img_ground pygame.image.load("Track.png")



   display.flip()
   class Object:
      def __init__(self, x, y, img):
         self.img img
         self.rect = pygame. Rect( # один рядок
            x, y, self.img.get_width(), # один рядок
      self.img.get_height()) # один рядок

      def draw(self, screen):
         screen.blit(self.img, (self.rect.left, self.rect.top))
# клас гравця з керуванням
   class Player (Object):
      def __init__(self, x, y):
         super().__init__(x, y, img_player)
   self.max_y = y
   self.velocity = 0
   self.GRAVITY = 0.7
   self.in_air = False
# реалізація керування і гравітації
      def update (self):
   keys = pygame.key.get_pressed()
      if keys [pygame.K_SPACE] and not self.in_air:
   self.velocity = 15
   self.in_air = True
      if self.in_air:
   self.rect.top = self.velocity
   self.velocity = self.GRAVITY
      if self.rect.top >= self.max_y:
   self.in_air = False
   self.rect.top = self.max_y

# реалізація переміщення та видалення об'єктів, що не взаємодіють з гравцем
class Enviroment (Object):
def __init__(self, x, y):
   def update(self):
      self.rect.left = SPEED
         if self.rect.right <= 500:
         self.rect.left = 0


def draw(self, screen):
   screen.blit(self.img, (self.rect.left, self.rect.top))








   display.flip()



