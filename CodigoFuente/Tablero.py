import numpy as np
import pygame, sys 
from pygame.locals import *
from Ficha import *
class Tablero(pygame.sprite.Sprite):

	fC = 0 # ficha cafe normal
	fCD = 1 # ficha cafe dama
	fV = -1 # espacio libre
	fB = 2 # ficha blanca normal
	fBD = 3 # ficha blanca dama
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.imagenTablero = pygame.image.load("../Resources/Tablero.png")
		self.rect = self.imagenTablero.get_rect()
		self.rect.x = 60
		self.rect.y = 50
		self.cuadricula = []
		self.llenar()


	def dibujar(self, superficie):
		superficie.blit(self.imagenTablero, self.rect) 

	def llenar(self):
		#Creacion de una matriz vacia de 8 * 8
		self.cuadricula = []
		for i in range(8):
			self.cuadricula.append([])
			for j in range(8):
				self.cuadricula[i].append(0)
		#print self.cuadricula
		#Llenado de la matriz con la posicion de las fichas por default
		ladoX = self.rect.x + 85.62
		ladoY = self.rect.y + 11
		ban = 0
		for j in range(3):
			if(ban == 0):
				ladoX = self.rect.x + 85.62
				for i in range(1,8,2):
					self.cuadricula[j][i] = Ficha(self.fC,ladoX,ladoY)
					ladoX += 149.24
				ban = 1
			else:
				ladoX = self.rect.x + 11
				for i in range(0,8,2):
					self.cuadricula[j][i] = Ficha(self.fC,ladoX,ladoY)
					ladoX += 149.24
				ban = 0
			ladoY += 75.12

		for j in range(3,5):
			if(ban == 0):
				ladoX = self.rect.x + 85.62
				for i in range(1,8,2):
					self.cuadricula[j][i] = Ficha(self.fV,ladoX,ladoY)
					ladoX += 149.24
				ban = 1
			else:
				ladoX = self.rect.x + 11
				for i in range(0,8,2):
					self.cuadricula[j][i] = Ficha(self.fV,ladoX,ladoY)
					ladoX += 149.24
				ban = 0
			ladoY += 75.12

		for j in range(5,8):
			if(ban == 0):
				ladoX = self.rect.x + 85.62
				for i in range(1,8,2):
					self.cuadricula[j][i] = Ficha(self.fB,ladoX,ladoY)
					ladoX += 149.24
				ban = 1
			else:
				ladoX = self.rect.x + 11
				for i in range(0,8,2):
					self.cuadricula[j][i] = Ficha(self.fB,ladoX,ladoY)
					ladoX += 149.24
				ban = 0
			ladoY += 75.12





	def imprimir_fichas(self):
		for i in self.cuadricula:
			for j in i:
				print j


	def  dibujar_fichas(self,superficie):
		#Dibuja las fichas en pantalla
		for i in self.cuadricula:		
			for j in i:	
				if j != 0:
					superficie.blit(j.get_imagen(), j.get_rect())

	def comprobar_mov(self,ficha):
		i,j = self.encontrar_ficha(ficha)
		return self.comprobar_movimiento(ficha,i,j) | self.comprobar_comer(ficha,i,j)

	def encontrar_ficha(self, ficha):
		i = 0
		j = 0
		for i in range(8):		
			for j in range(8):	
				if self.cuadricula[i][j] == ficha:
					return i,j

	def comprobar_movimiento(self, ficha,i,j):
		# Comprueba si la ficha puede moverse o no
		# retorna True si puede
		# retorna False si no puede
		
		#si la ficha es una ficha cafe normal
		if ficha.get_jugador() == self.fC:
			# si la ficha esta en el borde derecho
			if j == 7:
				if (self.cuadricula[i+1][j-1].get_jugador() != self.fC) & (self.cuadricula[i+1][j-1].get_jugador() != self.fCD):
					return True
			# si la ficha esta en el borde izquierdo
			elif j == 0:
				if(self.cuadricula[i+1][j+1].get_jugador() != self.fC) & (self.cuadricula[i+1][j+1].get_jugador() != self.fCD) :
					return True
			# si la ficha esta en cualquier posicion central		
			else:
				if ((self.cuadricula[i+1][j+1].get_jugador() != self.fC) & (self.cuadricula[i+1][j+1].get_jugador() != self.fCD)) | ((self.cuadricula[i+1][j-1].get_jugador() != self.fC) & (self.cuadricula[i+1][j-1].get_jugador() != self.fCD)):
					return True
			
		elif ficha.get_jugador() == self.fB:
			# si la ficha esta en el borde derecho
			if j == 7:
				if (self.cuadricula[i-1][j-1].get_jugador() != self.fB) & (self.cuadricula[i-1][j-1].get_jugador() != self.fBD):
					return True
			# si la ficha esta en el borde izquierdo
			elif j == 0:
				if(self.cuadricula[i-1][j+1].get_jugador() != self.fB) & (self.cuadricula[i-1][j+1].get_jugador() != self.fBD) :
					return True
			# si la ficha esta en cualquier posicion central		
			else:
				if ((self.cuadricula[i-1][j+1].get_jugador() != self.fB) & (self.cuadricula[i-1][j+1].get_jugador() != self.fBD)) | ((self.cuadricula[i-1][j-1].get_jugador() != self.fB) & (self.cuadricula[i-1][j-1].get_jugador() != self.fBD)):
					return True
		return False

	def comprobar_comer(self, ficha, i, j):
		#ficha cafe normal
		if ficha.get_jugador() == self.fC:
			if(j == 7):

				if (self.cuadricula[i+1][j-1].get_jugador() == self.fB) | (self.cuadricula[i+1][j-1].get_jugador() == self.fBD)  :
					if(self.cuadricula[i+2][j-2].get_jugador() == self.fV):
						return True
					else:
						return False
				else:
					return False

			elif(j == 0):

				if (self.cuadricula[i+1][j+1].get_jugador() != self.fB) | (self.cuadricula[i+1][j+1].get_jugador() != self.fBD):
					if(self.cuadricula[i+2][j+2].get_jugador() == self.fV):
						return True
					else:
					 	return False
				else:
					return False

			else:
				ladoD = False
				ladoI = False
				if (self.cuadricula[i+1][j-1].get_jugador() == self.fB) | (self.cuadricula[i+1][j-1].get_jugador() == self.fBD)  :
					if(j > 1):
						if(self.cuadricula[i+2][j-2].get_jugador() == self.fV):
							ladoI = True

				if (self.cuadricula[i+1][j+1].get_jugador() == self.fB) | (self.cuadricula[i+1][j+1].get_jugador() == self.fBD)  :
					if(j < 6):
						if(self.cuadricula[i+2][j+2].get_jugador() == self.fV):
							ladoD = True

				return ladoD | ladoI

		elif ficha.get_jugador() == self.fB:
			if(j == 7):

				if (self.cuadricula[i-1][j-1].get_jugador() == self.fC) | (self.cuadricula[i-1][j-1].get_jugador() == self.fCD)  :
					if(self.cuadricula[i-2][j-2].get_jugador() == self.fV):
						return True
					else:
						return False
				else:
					return False

			elif(j == 0):

				if (self.cuadricula[i-1][j+1].get_jugador() != self.fC) | (self.cuadricula[i-1][j+1].get_jugador() != self.fCD):
					if(self.cuadricula[i-2][j+2].get_jugador() == self.fV):
						return True
					else:
					 	return False
				else:
					return False

			else:
				ladoD = False
				ladoI = False
				if (self.cuadricula[i-1][j-1].get_jugador() == self.fC) | (self.cuadricula[i-1][j-1].get_jugador() == self.fCD)  :
					if(j > 1):
						if(self.cuadricula[i-2][j-2].get_jugador() == self.fV):
							ladoD = True

				if (self.cuadricula[i-1][j+1].get_jugador() == self.fC) | (self.cuadricula[i-1][j+1].get_jugador() == self.fCD)  :
					if(j < 6):
						if(self.cuadricula[i-2][j+2].get_jugador() == self.fV):
							ladoI = True

				return ladoD | ladoI

		return False






