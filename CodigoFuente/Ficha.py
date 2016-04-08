import pygame
class Ficha(pygame.sprite.Sprite):
	CAFE = 0
	BLANCA = 1
	LIBRE = 2
	def __init__(self, jugador, posX, posY):
			pygame.sprite.Sprite.__init__(self)
			self.jugador = jugador
			if(jugador == 0):
				self.imagen = pygame.image.load("../Resources/FichaCafe.png")
				self.rect = self.imagen.get_rect()
				self.rect.x = posX
				self.rect.y = posY
			elif(jugador == 1):
				self.imagen = pygame.image.load("../Resources/FichaCafeDama.png")
				self.rect = self.imagen.get_rect()
				self.rect.x = posX
				self.rect.y = posY
			elif(jugador == 2):
				self.imagen = pygame.image.load("../Resources/FichaBlanca.png")
				self.rect = self.imagen.get_rect()
				self.rect.x = posX
				self.rect.y = posY
			elif(jugador == 3):
				self.imagen = pygame.image.load("../Resources/FichaBlancaDama.png")
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

	def get_color(self):
		if (self.jugador == 0) | (self.jugador == 1):
			return self.CAFE
		elif(self.jugador == 2) | (self.jugador == 3):
			return self.BLANCA
		else:
			return self.LIBRE
	
	def es_dama(self):
		if (self.jugador == 1) | (self.jugador == 3):
			return True
		else:
			return False  

	def cambiar_imagen(self, tipo):
		if(tipo == 0):
			self.jugador = tipo
			self.imagen = pygame.image.load("../Resources/FichaCafe.png")
			posX = self.rect.x
			posY = self.rect.y
			self.rect = self.imagen.get_rect()
			self.rect.x = posX
			self.rect.y = posY

		elif(tipo == 1):
			self.jugador = tipo
			self.imagen = pygame.image.load("../Resources/FichaCafeDama.png")
			posX = self.rect.x
			posY = self.rect.y
			self.rect = self.imagen.get_rect()
			self.rect.x = posX
			self.rect.y = posY

		elif(tipo == 2):
			self.jugador = tipo
			self.imagen = pygame.image.load("../Resources/FichaBlanca.png")
			posX = self.rect.x
			posY = self.rect.y
			self.rect = self.imagen.get_rect()
			self.rect.x = posX
			self.rect.y = posY

		elif(tipo == 3):
			self.jugador = tipo
			self.imagen = pygame.image.load("../Resources/FichaBlancaDama.png")
			posX = self.rect.x
			posY = self.rect.y
			self.rect = self.imagen.get_rect()
			self.rect.x = posX
			self.rect.y = posY

		elif(tipo == -1):
			self.jugador = tipo
			self.imagen = pygame.image.load("../Resources/FichaVacia.png")
			posX = self.rect.x
			posY = self.rect.y
			self.rect = self.imagen.get_rect()
			self.rect.x = posX
			self.rect.y = posY


	def get_rect(self):
		return self.rect

	def get_imagen(self):
		return self.imagen

	def set_rect(self, x,y):
		self.rect = self.imagen.get_rect()
		self.rect.x = x
		self.rect.y = y


