import numpy as np
import pygame, sys 
from pygame.locals import *
from Ficha import *
class Tablero(pygame.sprite.Sprite):
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.imagenTablero = pygame.image.load("Imagenes/Tablero.png")
	#	self.imageFichaBlanca = pygame.image.load("Imagenes/FichaBlanca.png")
	#	self.imageFichaCafe = pygame.image.load("Imagenes/FichaCafe.png")
	#	self.imageFichaBlancaD = pygame.image.load("Imagenes/FichaBlancaDama.png")
	#	self.imageFichaCafeD = pygame.image.load("Imagenes/FichaCafeDama.png")
		self.rect = self.imagenTablero.get_rect()
		self.rect.x = 100
		self.rect.y = 80
		self.cuadricula = []
		self.llenar()
		#self.cuadricula = np.array([[5,0,5,0,5,0,5,0],[0,5,0,5,0,5,0,5],[5,0,5,0,5,0,5,0],[-1,5,-1,5,-1,5,-1,5],[5,-1,5,-1,5,-1,5,-1],[2,5,2,5,2,5,2,5],[5,2,5,2,5,2,5,2],[2,5,2,5,2,5,2,5]])

	def dibujar(self, superficie):
		superficie.blit(self.imagenTablero, self.rect) 

	def llenar(self):
		#Creacion de una matriz vacia de 8 * 8
		for i in range(8):
			self.cuadricula.append([])
			for j in range(8):
				self.cuadricula[i].append(0)
		print self.cuadricula
		#Llenado de la matriz con la posicion de las fichas por default
		ladoX = 185.62
		ladoY = 91
		ban = 0
		for j in range(3):
			if(ban == 0):
				ladoX = 185.62
				for i in range(1,8,2):
					self.cuadricula[j][i] = Ficha(1,ladoX,ladoY)
					ladoX += 149.24
				ban = 1
			else:
				ladoX = 111
				for i in range(0,8,2):
					self.cuadricula[j][i] = Ficha(1,ladoX,ladoY)
					ladoX += 149.24
				ban = 0
			ladoY += 75.12

		for j in range(3,5):
			if(ban == 0):
				ladoX = 185.62
				for i in range(1,8,2):
					self.cuadricula[j][i] = Ficha(2,ladoX,ladoY)
					ladoX += 149.24
				ban = 1
			else:
				ladoX = 111
				for i in range(0,8,2):
					self.cuadricula[j][i] = Ficha(2,ladoX,ladoY)
					ladoX += 149.24
				ban = 0
			ladoY += 75.12

		for j in range(5,8):
			if(ban == 0):
				ladoX = 185.62
				for i in range(1,8,2):
					self.cuadricula[j][i] = Ficha(0,ladoX,ladoY)
					ladoX += 149.24
				ban = 1
			else:
				ladoX = 111
				for i in range(0,8,2):
					self.cuadricula[j][i] = Ficha(0,ladoX,ladoY)
					ladoX += 149.24
				ban = 0
			ladoY += 75.12





	def imprimir_fichas(self):
		for i in self.cuadricula:
			for j in i:
				print j


	def  dibujar_fichas(self,superficie):
		
		for i in self.cuadricula:		
			for j in i:	
				if j != 0:
					superficie.blit(j.get_imagen(), j.get_rect())
		 



