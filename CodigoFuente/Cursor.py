import pygame
from pygame.locals import *

#crear un rectangulo de 1*1 para que se mueva con el cursor
class Cursor(pygame.Rect):
	def __init__(self):
		pygame.Rect.__init__(self,0,0,1,1)

	def mover(self):
		self.left, self.top = pygame.mouse.get_pos()
		