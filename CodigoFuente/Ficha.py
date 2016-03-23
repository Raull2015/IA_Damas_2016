import pygame
class Ficha(pygame.sprite.Sprite):
	
	def __init__(self, jugador, posX, posY):
			pygame.sprite.Sprite.__init__(self)
			self.jugador = jugador
			if(jugador == 0):
				self.imagen = pygame.image.load("../Resources/FichaCafe.png")
				self.rect = self.imagen.get_rect()
				self.rect.x = posX
				self.rect.y = posY
			elif(jugador == 2):
				self.imagen = pygame.image.load("../Resources/FichaBlanca.png")
				self.rect = self.imagen.get_rect()
				self.rect.x = posX
				self.rect.y = posY
			elif(jugador == -1):
				self.imagen = pygame.image.load("../Resources/FichaVacia.png")
				self.rect = self.imagen.get_rect()
				self.rect.x = posX
				self.rect.y = posY
        

	def get_jugador(self):
		return self.jugador

	def get_rect(self):
		return self.rect

	def get_imagen(self):
		return self.imagen

	def set_rect(self, x,y):
		self.rect = self.imagen.get_rect()
		self.rect.x = x
		self.rect.y = y

	def set_tipo(self,tipo):
		self.tipo = tipo

	def get_tipo(self):
		return self.tipo
	 	
		
		
		