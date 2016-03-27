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
		#para pruebas con fichas damas
		ladoX = self.rect.x + 85.62
		ladoY = self.rect.y + 11
		ban = 0
		for j in range(1):
			if(ban == 0):
				ladoX = self.rect.x + 85.62
				for i in range(1,8,2):
					self.cuadricula[j][i] = Ficha(self.fCD,ladoX,ladoY)
					ladoX += 149.24
				ban = 1
			else:
				ladoX = self.rect.x + 11
				for i in range(0,8,2):
					self.cuadricula[j][i] = Ficha(self.fCD,ladoX,ladoY)
					ladoX += 149.24
				ban = 0
			ladoY += 75.12

		for j in range(1,7):
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

		for j in range(7,8):
			if(ban == 0):
				ladoX = self.rect.x + 85.62
				for i in range(1,8,2):
					self.cuadricula[j][i] = Ficha(self.fBD,ladoX,ladoY)
					ladoX += 149.24
				ban = 1
			else:
				ladoX = self.rect.x + 11
				for i in range(0,8,2):
					self.cuadricula[j][i] = Ficha(self.fBD,ladoX,ladoY)
					ladoX += 149.24
				ban = 0
			ladoY += 75.12

	"""	#Llenado de la matriz con la posicion de las fichas por default
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
			ladoY += 75.12 """

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
		#Busca en la matriz de fichas
		#y retorna las coordenas i,j de la posicion de la ficha respecto a la matriz
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

		#si la ficha es una ficha cafe normal o dama
		if ficha.get_color() == Ficha.CAFE:
			if i != 7:
				# si la ficha esta en el borde derecho
				if j == 7:
					if self.cuadricula[i+1][j-1].get_color() == Ficha.LIBRE:
						return True
				# si la ficha esta en el borde izquierdo
				elif j == 0:
					if self.cuadricula[i+1][j+1].get_color() == Ficha.LIBRE:
						return True
				# si la ficha esta en cualquier posicion central
				else:
					if (self.cuadricula[i+1][j+1].get_color() == Ficha.LIBRE) | (self.cuadricula[i+1][j-1].get_color() == Ficha.LIBRE):
						return True
		#si la ficha es una ficha blanca normal o dama
		elif ficha.get_color()== Ficha.BLANCA:
			if i != 0:
				# si la ficha esta en el borde derecho
				if j == 7:
					if self.cuadricula[i-1][j-1].get_color() == Ficha.LIBRE:
						return True
				# si la ficha esta en el borde izquierdo
				elif j == 0:
					if self.cuadricula[i-1][j+1].get_color() == Ficha.LIBRE :
						return True
				# si la ficha esta en cualquier posicion central
				else:
					if (self.cuadricula[i-1][j+1].get_color() == Ficha.LIBRE) | (self.cuadricula[i-1][j-1].get_color() == Ficha.LIBRE):
						return True

		#retorna falso si la ficha no puede moverse
		return False

	def comprobar_sig_com(self, ficha):
		#Comprueba si la ficha aun puede comer despues de moverse
		i,j = self.encontrar_ficha(ficha)
		return self.comprobar_comer(ficha,i,j)

	def comprobar_comer(self, ficha, i, j):
		#ficha cafe normal
		if ficha.get_jugador() == self.fC:
			if i != 7:
				if(j == 7):

					if self.cuadricula[i+1][j-1].get_color() == Ficha.BLANCA  :
						if self.cuadricula[i+2][j-2].get_color() == Ficha.LIBRE :
							return True
						else:
							return False
					else:
						return False

				elif (j == 0):

					if self.cuadricula[i+1][j+1].get_color() == Ficha.BLANCA:
						if self.cuadricula[i+2][j+2].get_color() == Ficha.LIBRE:
							return True
						else:
						 	return False
					else:
						return False

				else:
					ladoD = False
					ladoI = False
					if self.cuadricula[i+1][j-1].get_color() == Ficha.BLANCA  :
						if(j > 1):
							if self.cuadricula[i+2][j-2].get_color() == Ficha.LIBRE:
								ladoI = True

					if self.cuadricula[i+1][j+1].get_color() == Ficha.BLANCA:
						if (j < 6):
							if self.cuadricula[i+2][j+2].get_color() == Ficha.LIBRE:
								ladoD = True

					return ladoD | ladoI
		#Ficha blanca normal
		elif ficha.get_jugador() == self.fB:
			if i != 0:
				if(j == 7):

					if self.cuadricula[i-1][j-1].get_color() == Ficha.CAFE :
						if self.cuadricula[i-2][j-2].get_color() == Ficha.LIBRE:
							return True
						else:
							return False
					else:
						return False

				elif(j == 0):

					if self.cuadricula[i-1][j+1].get_color() == Ficha.CAFE:
						if self.cuadricula[i-2][j+2].get_color() == Ficha.LIBRE:
							return True
						else:
						 	return False
					else:
						return False

				else:
					ladoD = False
					ladoI = False
					if self.cuadricula[i-1][j-1].get_color() == Ficha.CAFE  :
						if(j > 1):
							if self.cuadricula[i-2][j-2].get_color() == Ficha.LIBRE:
								ladoD = True

					if self.cuadricula[i-1][j+1].get_color() == Ficha.CAFE  :
						if(j < 6):
							if self.cuadricula[i-2][j+2].get_color() == Ficha.LIBRE:
								ladoI = True

					return ladoD | ladoI

		elif ficha.get_jugador() == self.fCD:
			pass #TODO agregar comparacion
		elif ficha.get_jugador() == self.fBD:
			pass #TODO agregar comparacion
		return False

	def mover_espacio(self, ficha, lugar):
			#Funcion que mueve la ficha seleccionada al lugar seleccionado
			if ficha.get_jugador() == self.fB:
				#verifica que se mueva a un lugar libre
				if lugar.get_color() == Ficha.LIBRE:
					x, y = self.encontrar_ficha(lugar)
					i, j = self.encontrar_ficha(ficha)
					if ((i - x) == 1) & (((j - y) == 1) | ((j - y) == -1)):
						posX = ficha.get_rect().x
						posY = ficha.get_rect().y
						ficha.set_rect(lugar.get_rect().x,lugar.get_rect().y )
						lugar.set_rect(posX,posY)
						#cambio de posicion en la matriz
						self.cuadricula[x][y] = ficha
						self.cuadricula[i][j] = lugar
						return True

			elif ficha.get_jugador() == self.fC:
				#verifica que se mueva a un lugar libre
				if lugar.get_color() == Ficha.LIBRE:
					x, y = self.encontrar_ficha(lugar)
					i, j = self.encontrar_ficha(ficha)
					if ((i - x) == -1) & (((j - y) == 1) | ((j - y) == -1)):
						posX = ficha.get_rect().x
						posY = ficha.get_rect().y
						ficha.set_rect(lugar.get_rect().x,lugar.get_rect().y )
						lugar.set_rect(posX,posY)
						#cambio de posicion en la matriz
						self.cuadricula[x][y] = ficha
						self.cuadricula[i][j] = lugar
						return True

			elif ficha.get_jugador() == self.fCD:
				pass #TODO agregar comparacion
			elif ficha.get_jugador() == self.fBD:
				if lugar.get_color() == Ficha.LIBRE:
					x, y = self.encontrar_ficha(lugar)
					i, j = self.encontrar_ficha(ficha)

					for x in range(i-1,-1,-1):
						for y in range(j+1,8):
							pass

			return False

	def mover_comiendo(self, ficha, lugar):
			#Funcion que verifica que si la ficha intenta moverse comiendo
			if ficha.get_jugador() == self.fB:
				#verifica que se mueva a un lugar libre
				if lugar.get_color() == Ficha.LIBRE:
					x, y = self.encontrar_ficha(lugar)
					i, j = self.encontrar_ficha(ficha)
					#Si la ficha esta intenando comer
					if (i - x) == 2:
					 	if (j - y) == 2:
							if self.cuadricula[i-1][j-1].get_color() == Ficha.CAFE:
								self.cuadricula[i-1][j-1].cambiar_imagen(-1)
								posX = ficha.get_rect().x
								posY = ficha.get_rect().y
								ficha.set_rect(lugar.get_rect().x,lugar.get_rect().y )
								lugar.set_rect(posX,posY)
								#cambio de posicion en la matriz
								self.cuadricula[x][y] = ficha
								self.cuadricula[i][j] = lugar
								return True
						elif (j - y) == -2:
							if self.cuadricula[i-1][j+1].get_color() == Ficha.CAFE:
								self.cuadricula[i-1][j+1].cambiar_imagen(-1)
								posX = ficha.get_rect().x
								posY = ficha.get_rect().y
								ficha.set_rect(lugar.get_rect().x,lugar.get_rect().y )
								lugar.set_rect(posX,posY)
								#cambio de posicion en la matriz
								self.cuadricula[x][y] = ficha
								self.cuadricula[i][j] = lugar
								return True

			elif ficha.get_jugador() == self.fC:
				#verifica que se mueva a un lugar libre
				if lugar.get_color() == Ficha.LIBRE:
					x, y = self.encontrar_ficha(lugar)
					i, j = self.encontrar_ficha(ficha)
					#Si la ficha esta intenando comer
					if (i - x) == -2:
					 	if (j - y) == 2:
							if self.cuadricula[i+1][j-1].get_color() == Ficha.BLANCA:
								self.cuadricula[i+1][j-1].cambiar_imagen(-1)
								posX = ficha.get_rect().x
								posY = ficha.get_rect().y
								ficha.set_rect(lugar.get_rect().x,lugar.get_rect().y )
								lugar.set_rect(posX,posY)
								#cambio de posicion en la matriz
								self.cuadricula[x][y] = ficha
								self.cuadricula[i][j] = lugar
								return True
						elif (j - y) == -2:
							if self.cuadricula[i+1][j+1].get_color() == Ficha.BLANCA:
								self.cuadricula[i+1][j+1].cambiar_imagen(-1)
								posX = ficha.get_rect().x
								posY = ficha.get_rect().y
								ficha.set_rect(lugar.get_rect().x,lugar.get_rect().y )
								lugar.set_rect(posX,posY)
								#cambio de posicion en la matriz
								self.cuadricula[x][y] = ficha
								self.cuadricula[i][j] = lugar
								return True

			elif ficha.get_jugador() == self.fCD:
				pass #TODO agregar comparacion
			elif ficha.get_jugador() == self.fBD:
				pass #TODO agregar comparacion
			return False

	def mover(self, ficha, lugar):
		mov_normal = self.mover_espacio(ficha, lugar)
		if mov_normal == False:
			mov_comiendo = self.mover_comiendo(ficha, lugar)
			if mov_comiendo == False:
				return False, -1 #Si no se movio
			else:
				return True, 0 #Si se movio comiendo
		else:
			return True, 1 #Si fue un movimiento normal

	def convertir_dama(self):
		#revisa si una ficha blanca se convierte en dama
		for j in range(1,8,2):
			if self.cuadricula[0][j].get_jugador() == self.fB:
				self.cuadricula[0][j].cambiar_imagen(self.fBD)
		#revisa si una ficha cafe se convierte en dama
		for j in range(0,8,2):
			if self.cuadricula[7][j].get_jugador() == self.fC:
				self.cuadricula[7][j].cambiar_imagen(self.fCD)
