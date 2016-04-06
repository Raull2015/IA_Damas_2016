import pygame
from pygame.locals import *

class Boton(pygame.sprite.Sprite):
	def __init__(self, x, y):
		self.reiniciar = pygame.image.load("../Resources/BotonReiniciar.png")
		self.clic = pygame.image.load("../Resources/clic.png")
		self.aux = self.reiniciar
		self.rect = self.clic.get_rect
		self.rect = self.reiniciar.get_rect()
		self.rect.left, self.rect.top = (x,y)

	def seleccion(self, superficie, cursor):
		if cursor.colliderect(self.rect):
			self.aux = self.clic
		else:
			self.aux = self.reiniciar

		superficie.blit(self.reiniciar,self.rect)

	def get_rect(self):
		return self.rect	
		
		