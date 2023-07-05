import pygame
from settings import *

class Plataforma():
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load("Recursos\Plataformas\plataforma1.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.x = x
        self.rect.y = y


class Rectangulo():
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.x = x
        self.rect.y = y
        self.lados_rectangulo = obtener_rectangulos(self.rect)