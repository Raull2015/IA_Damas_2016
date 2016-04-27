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
		self.entradas_ia = ''


	def dibujar(self, superficie):
		superficie.blit(self.imagenTablero, self.rect)

	def llenar(self):
		#Creacion de una matriz vacia de 8 * 8
		self.cuadricula = []
		for i in range(8):
			self.cuadricula.append([])
			for j in range(8):
				self.cuadricula[i].append(0)

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

		#si la ficha es una ficha cafe normal
		if ficha.get_jugador() == self.fC:
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
		#si la ficha es una ficha blanca normal
		elif ficha.get_jugador() == self.fB:
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
		#si la ficha es una dama blanca o cafe
		elif (ficha.get_jugador() == self.fCD) | (ficha.get_jugador() == self.fBD):
			puede_moverse = False
			y = j + 1
			for x in range(i-1,-1,-1):
				if y < 8:
					if self.cuadricula[x][y].get_color() == Ficha.LIBRE:
						puede_moverse = True
						break
				break

			y = j - 1
			for x in range(i-1,-1,-1):
				if y > -1:
					if self.cuadricula[x][y].get_color() == Ficha.LIBRE:
						puede_moverse = True
						break
				break

			y = j + 1
			for x in range(i+1,8):
				if y < 8:
					if self.cuadricula[x][y].get_color() == Ficha.LIBRE:
						puede_moverse = True
						break
				break

			y = j - 1
			for x in range(i+1,8):
				if y > -1:
					if self.cuadricula[x][y].get_color() == Ficha.LIBRE:
						puede_moverse = True
						break
				break

			return puede_moverse


		#retorna falso si la ficha no puede moverse
		return False

	def comprobar_sig_com(self, ficha):
		#Comprueba si la ficha aun puede comer despues de moverse
		i,j = self.encontrar_ficha(ficha)
		return self.comprobar_comer(ficha,i,j)

	def comprobar_comer(self, ficha, i, j):
		#ficha cafe normal
		if ficha.get_jugador() == self.fC:
			if i < 6:
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
			if i > 1:
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

		# ficha cafe dama
		elif ficha.get_jugador() == self.fCD:
			puede_comer = False
			y = j + 1
			for x in range(i-1,0,-1):
				if y < 7:
					if self.cuadricula[x][y].get_color() == Ficha.BLANCA:
						if self.cuadricula[x-1][y+1].get_color() == Ficha.LIBRE:
							puede_comer = True
							break
						break
					if self.cuadricula[x][y].get_color() == Ficha.CAFE:
						break
					y += 1

			y = j - 1
			for x in range(i-1,0,-1):
				if y > 0:
					if self.cuadricula[x][y].get_color() == Ficha.BLANCA:
						if self.cuadricula[x-1][y-1].get_color() == Ficha.LIBRE:
							puede_comer = True
							break
						break
					if self.cuadricula[x][y].get_color() == Ficha.CAFE:
						break
					y += -1

			y = j + 1
			for x in range(i+1,7):
				if y < 7:
					if self.cuadricula[x][y].get_color() == Ficha.BLANCA:
						if self.cuadricula[x+1][y+1].get_color() == Ficha.LIBRE:
							puede_comer = True
							break
						break
					if self.cuadricula[x][y].get_color() == Ficha.CAFE:
						break
					y += 1

			y = j - 1
			for x in range(i+1,7):
				if y > 0:
					if self.cuadricula[x][y].get_color() == Ficha.BLANCA:
						if self.cuadricula[x+1][y-1].get_color() == Ficha.LIBRE:
							puede_comer = True
							break
						break
					if self.cuadricula[x][y].get_color() == Ficha.CAFE:
						break
					y += -1

			return puede_comer

		# ficha blanca Dama
		elif ficha.get_jugador() == self.fBD:
			puede_comer = False
			y = j + 1
			for x in range(i-1,0,-1):
				if y < 7:
					if self.cuadricula[x][y].get_color() == Ficha.CAFE:
						if self.cuadricula[x-1][y+1].get_color() == Ficha.LIBRE:
							puede_comer = True
							break
						break
					if self.cuadricula[x][y].get_color() == Ficha.BLANCA:
						break
					y += 1

			y = j - 1
			for x in range(i-1,0,-1):
				if y > 0:
					if self.cuadricula[x][y].get_color() == Ficha.CAFE:
						if self.cuadricula[x-1][y-1].get_color() == Ficha.LIBRE:
							puede_comer = True
							break
						break
					if self.cuadricula[x][y].get_color() == Ficha.BLANCA:
						break
					y += -1

			y = j + 1
			for x in range(i+1,7):
				if y < 7:
					if self.cuadricula[x][y].get_color() == Ficha.CAFE:
						if self.cuadricula[x+1][y+1].get_color() == Ficha.LIBRE:
							puede_comer = True
							break
						break
					if self.cuadricula[x][y].get_color() == Ficha.BLANCA:
						break
					y += 1

			y = j - 1
			for x in range(i+1,7):
				if y > 0:
					if self.cuadricula[x][y].get_color() == Ficha.CAFE:
						if self.cuadricula[x+1][y-1].get_color() == Ficha.LIBRE:
							puede_comer = True
							break
						break
					if self.cuadricula[x][y].get_color() == Ficha.BLANCA:
						break
					y += -1

			return puede_comer

		return False

	def comprobar_espacio(self, ficha):
		i,j = self.encontrar_ficha(ficha)
		if i != 0:
			# si la ficha esta en el borde derecho
			if j == 7:
				if self.cuadricula[i-1][j-1].get_color() == Ficha.CAFE:
					return True
			# si la ficha esta en el borde izquierdo
			elif j == 0:
				if self.cuadricula[i-1][j+1].get_color() == Ficha.CAFE :
					return True
			# si la ficha esta en cualquier posicion central
			else:
				if (self.cuadricula[i-1][j+1].get_color() == Ficha.CAFE) | (self.cuadricula[i-1][j-1].get_color() == Ficha.CAFE):
					return True

		puede_moverse = False
		#esquina superior derecha
		y = j + 1
		for x in range(i-1,-1,-1):
			if y < 8:
				if self.cuadricula[x][y].get_jugador() == self.fCD:
					puede_moverse = True
					break
				if self.cuadricula[x][y].get_color() != Ficha.LIBRE:
					break
			y += 1
		#esquina superior izquierda
		y = j - 1
		for x in range(i-1,-1,-1):
			if y > -1:
				if  self.cuadricula[x][y].get_jugador() == self.fCD:
					puede_moverse = True
					break
				if self.cuadricula[x][y].get_color() != Ficha.LIBRE:
					break
			y += -1
		#esquina inferior derecha
		y = j + 1
		for x in range(i+1,8):
			if y < 8:
				if  self.cuadricula[x][y].get_jugador() == self.fCD:
					puede_moverse = True
					break
				if self.cuadricula[x][y].get_color() != Ficha.LIBRE:
					break
			y += 1
		#esquina inferior izquierda
		y = j - 1
		for x in range(i+1,8):
			if y > -1:
				if  self.cuadricula[x][y].get_jugador() == self.fCD:
					puede_moverse = True
					break
				if self.cuadricula[x][y].get_color() != Ficha.LIBRE:
					break
			y += -1

		if puede_moverse:
			return True

		#si al espacio se puede llegar comiendo
		if i > 1:
			if(j == 7):

				if self.cuadricula[i-1][j-1].get_color() == Ficha.BLANCA :
					if self.cuadricula[i-2][j-2].get_color() == Ficha.CAFE:
						return True

			elif(j == 0):

				if self.cuadricula[i-1][j+1].get_color() == Ficha.BLANCA:
					if self.cuadricula[i-2][j+2].get_color() == Ficha.CAFE:
						return True

			else:
				ladoD = False
				ladoI = False
				if self.cuadricula[i-1][j-1].get_color() == Ficha.BLANCA  :
					if(j > 1):
						if self.cuadricula[i-2][j-2].get_color() == Ficha.CAFE:
							ladoD = True

				if self.cuadricula[i-1][j+1].get_color() == Ficha.BLANCA  :
					if(j < 6):
						if self.cuadricula[i-2][j+2].get_color() == Ficha.CAFE:
							ladoI = True
				if ladoD | ladoI :
					return True

		#si puede llegar una dama comiendo
		puede_comer = False
		y = j + 1
		for x in range(i-1,-1,-1):
			if y < 7:
				if self.cuadricula[x][y].get_color() == Ficha.BLANCA:
					y += 1
					for q in range(x-1,-1,-1):
						if y < 7:
							if self.cuadricula[q][y].get_jugador() == self.fCD:
								return True
							elif self.cuadricula[q][y].get_color() != Ficha.LIBRE:
								break
						y += 1
				break

		y = j - 1
		for x in range(i-1,-1,-1):
			if y > 0:
				if self.cuadricula[x][y].get_color() == Ficha.BLANCA:
					y += -1
					for q in range(x-1,-1,-1):
						if y > 0:
							if self.cuadricula[q][y].get_jugador() == self.fCD:
								return True
							elif self.cuadricula[q][y].get_color() != Ficha.LIBRE:
								break
						y += -1
				break

		y = j + 1
		for x in range(i+1,8):
			if y < 7:
				if self.cuadricula[x][y].get_color() == Ficha.BLANCA:
					y += 1
					for q in range(x+1,8):
						if y < 7:
							if self.cuadricula[q][y].get_jugador() == self.fCD:
								return True
							elif self.cuadricula[q][y].get_color() != Ficha.LIBRE:
								break
						y += 1
				break

		y = j - 1
		for x in range(i+1,8):
			if y > 0:
				if self.cuadricula[x][y].get_color() == Ficha.BLANCA:
					y += -1
					for q in range(x+1,8):
						if y > 0:
							if self.cuadricula[q][y].get_jugador() == self.fCD:
								return True
							elif self.cuadricula[q][y].get_color() != Ficha.LIBRE:
								break
						y += -1
				break

		return False



	def mover_espacio(self, ficha, lugar):
			#Funcion que mueve la ficha seleccionada al lugar seleccionado
			#Si es una ficha blanca normal
			if ficha.get_jugador() == self.fB:
				#verifica que se mueva a un lugar libre
				if lugar.get_color() == Ficha.LIBRE:
					x, y = self.encontrar_ficha(lugar)
					i, j = self.encontrar_ficha(ficha)
					if ((i - x) == 1) & (((j - y) == 1) | ((j - y) == -1)):
						#Regla
						self.regla_comer_obligado(ficha.get_color())
						posX = ficha.get_rect().x
						posY = ficha.get_rect().y
						ficha.set_rect(lugar.get_rect().x,lugar.get_rect().y )
						lugar.set_rect(posX,posY)
						#cambio de posicion en la matriz
						self.cuadricula[x][y] = ficha
						self.cuadricula[i][j] = lugar
						return True

			#Si es una ficha cafe normal
			elif ficha.get_jugador() == self.fC:
				#verifica que se mueva a un lugar libre
				if lugar.get_color() == Ficha.LIBRE:
					x, y = self.encontrar_ficha(lugar)
					i, j = self.encontrar_ficha(ficha)
					if ((i - x) == -1) & (((j - y) == 1) | ((j - y) == -1)):
						#Regla
						self.regla_comer_obligado(ficha.get_color())
						posX = ficha.get_rect().x
						posY = ficha.get_rect().y
						ficha.set_rect(lugar.get_rect().x,lugar.get_rect().y )
						lugar.set_rect(posX,posY)
						#cambio de posicion en la matriz
						self.cuadricula[x][y] = ficha
						self.cuadricula[i][j] = lugar
						return True

			#Si es una ficha dama blanca o cafe
			elif (ficha.get_jugador() == self.fCD) | (ficha.get_jugador() == self.fBD):
				#verifica que se mueva a un lugar libre
				if lugar.get_color() == Ficha.LIBRE:
					x, y = self.encontrar_ficha(lugar)
					i, j = self.encontrar_ficha(ficha)
					puede_moverse = True
					#Comprueba que el movimiento se en diagonal
					if(pow(x - i,2)) != (pow(y - j,2)):
						puede_moverse = False
					else:
						n = j
						if (x - i) < 0 :
							if(y - j) > 0:
								for m in range(i-1,x,-1):
									n += 1
									if self.cuadricula[m][n].get_color() != ficha.LIBRE:
										puede_moverse = False
							elif(y - j) < 0:
								for m in range(i-1,x,-1):
									n += -1
									if self.cuadricula[m][n].get_color() != ficha.LIBRE:
										puede_moverse = False
						elif (x - i) > 0 :
							if(y - j) > 0:
								for m in range(i+1,x):
									n += 1
									if self.cuadricula[m][n].get_color() != ficha.LIBRE:
										puede_moverse = False
							elif(y - j) < 0:
								for m in range(i+1,x):
									n += -1
									if self.cuadricula[m][n].get_color() != ficha.LIBRE:
										puede_moverse = False

						if puede_moverse:
							#Regla
							self.regla_comer_obligado(ficha.get_color())
							posX = ficha.get_rect().x
							posY = ficha.get_rect().y
							ficha.set_rect(lugar.get_rect().x,lugar.get_rect().y )
							lugar.set_rect(posX,posY)
							#cambio de posicion en la matriz
							self.cuadricula[x][y] = ficha
							self.cuadricula[i][j] = lugar
							return True

			return False

	def mover_comiendo(self, ficha, lugar):
			#Funcion que verifica que si la ficha intenta moverse comiendo
			#Ficha blanca normal
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
			#Ficha cafe normal
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

			#Ficha cafe Dama
			elif ficha.get_jugador() == self.fCD:
				print "ficha cafe va a comprobar que come"
				#verifica que se mueva a un lugar libre
				if lugar.get_color() == Ficha.LIBRE:
					print "La posicion que eligio esta libre"
					x, y = self.encontrar_ficha(lugar)
					i, j = self.encontrar_ficha(ficha)
					#Comprueba que sea un movimiento en diagonal
					if(pow(x - i,2)) == (pow(y - j,2)):
						n = j
						if (x - i) < 0 :
							if(y - j) > 0:
								print "esquina superior derecha"
								for m in range(i-1,x,-1):
									n += 1
									if m == (x+1):
										if self.cuadricula[m][n].get_color() == Ficha.BLANCA:
											self.cuadricula[m][n].cambiar_imagen(-1)
											posX = ficha.get_rect().x
											posY = ficha.get_rect().y
											ficha.set_rect(lugar.get_rect().x,lugar.get_rect().y )
											lugar.set_rect(posX,posY)
											#cambio de posicion en la matriz
											self.cuadricula[x][y] = ficha
											self.cuadricula[i][j] = lugar
											return True
									elif self.cuadricula[m][n].get_color() != Ficha.LIBRE:
										return False

							elif(y - j) < 0:
								print "esquina superior izquierda"
								for m in range(i-1,x,-1):
									n += -1
									if m == (x+1):
										if self.cuadricula[m][n].get_color() == Ficha.BLANCA:
											self.cuadricula[m][n].cambiar_imagen(-1)
											posX = ficha.get_rect().x
											posY = ficha.get_rect().y
											ficha.set_rect(lugar.get_rect().x,lugar.get_rect().y )
											lugar.set_rect(posX,posY)
											#cambio de posicion en la matriz
											self.cuadricula[x][y] = ficha
											self.cuadricula[i][j] = lugar
											return True
									elif self.cuadricula[m][n].get_color() != Ficha.LIBRE:
										return False
						elif (x - i) > 0 :
							if(y - j) > 0:
								print "esquina inferior derecha"
								for m in range(i+1,x):
									n += 1
									if m == (x-1):
										if self.cuadricula[m][n].get_color() == Ficha.BLANCA:
											self.cuadricula[m][n].cambiar_imagen(-1)
											posX = ficha.get_rect().x
											posY = ficha.get_rect().y
											ficha.set_rect(lugar.get_rect().x,lugar.get_rect().y )
											lugar.set_rect(posX,posY)
											#cambio de posicion en la matriz
											self.cuadricula[x][y] = ficha
											self.cuadricula[i][j] = lugar
											return True
									elif self.cuadricula[m][n].get_color() != Ficha.LIBRE:
										return False
							elif(y - j) < 0:
								print "esquina inferior izquierda"
								for m in range(i+1,x):
									n += -1
									if m == (x-1):
										if self.cuadricula[m][n].get_color() == Ficha.BLANCA:
											self.cuadricula[m][n].cambiar_imagen(-1)
											posX = ficha.get_rect().x
											posY = ficha.get_rect().y
											ficha.set_rect(lugar.get_rect().x,lugar.get_rect().y )
											lugar.set_rect(posX,posY)
											#cambio de posicion en la matriz
											self.cuadricula[x][y] = ficha
											self.cuadricula[i][j] = lugar
											return True
									elif self.cuadricula[m][n].get_color() != Ficha.LIBRE:
										return False

			elif ficha.get_jugador() == self.fBD:
					#verifica que se mueva a un lugar libre
					print "ficha blanca va a comprobar que come"
					if lugar.get_color() == Ficha.LIBRE:
						x, y = self.encontrar_ficha(lugar)
						i, j = self.encontrar_ficha(ficha)
						#Comprueba que sea un movimiento en diagonal
						if(pow(x - i,2)) == (pow(y - j,2)):
							n = j
							if (x - i) < 0 :
								if(y - j) > 0:
									print "esquina superior derecha"
									for m in range(i-1,x,-1):
										n += 1
										if m == (x+1):
											if self.cuadricula[m][n].get_color() == Ficha.CAFE:
												self.cuadricula[m][n].cambiar_imagen(-1)
												posX = ficha.get_rect().x
												posY = ficha.get_rect().y
												ficha.set_rect(lugar.get_rect().x,lugar.get_rect().y )
												lugar.set_rect(posX,posY)
												#cambio de posicion en la matriz
												self.cuadricula[x][y] = ficha
												self.cuadricula[i][j] = lugar
												return True
										elif self.cuadricula[m][n].get_color() != Ficha.LIBRE:
											return False

								elif(y - j) < 0:
									print "esquina superior izquierda"
									for m in range(i-1,x,-1):
										n += -1
										if m == (x+1):
											if self.cuadricula[m][n].get_color() == Ficha.CAFE:
												self.cuadricula[m][n].cambiar_imagen(-1)
												posX = ficha.get_rect().x
												posY = ficha.get_rect().y
												ficha.set_rect(lugar.get_rect().x,lugar.get_rect().y )
												lugar.set_rect(posX,posY)
												#cambio de posicion en la matriz
												self.cuadricula[x][y] = ficha
												self.cuadricula[i][j] = lugar
												return True
										elif self.cuadricula[m][n].get_color() != Ficha.LIBRE:
											return False
							elif (x - i) > 0 :
								if(y - j) > 0:
									print "esquina inferior derecha"
									for m in range(i+1,x):
										n += 1
										if m == (x-1):
											if self.cuadricula[m][n].get_color() == Ficha.CAFE:
												self.cuadricula[m][n].cambiar_imagen(-1)
												posX = ficha.get_rect().x
												posY = ficha.get_rect().y
												ficha.set_rect(lugar.get_rect().x,lugar.get_rect().y )
												lugar.set_rect(posX,posY)
												#cambio de posicion en la matriz
												self.cuadricula[x][y] = ficha
												self.cuadricula[i][j] = lugar
												return True
										elif self.cuadricula[m][n].get_color() != Ficha.LIBRE:
											return False
								elif(y - j) < 0:
									print "esquina inferior izquierda"
									for m in range(i+1,x):
										n += -1
										if m == (x-1):
											if self.cuadricula[m][n].get_color() == Ficha.CAFE:
												self.cuadricula[m][n].cambiar_imagen(-1)
												posX = ficha.get_rect().x
												posY = ficha.get_rect().y
												ficha.set_rect(lugar.get_rect().x,lugar.get_rect().y )
												lugar.set_rect(posX,posY)
												#cambio de posicion en la matriz
												self.cuadricula[x][y] = ficha
												self.cuadricula[i][j] = lugar
												return True
										elif self.cuadricula[m][n].get_color() != Ficha.LIBRE:
											return False
			return False

	def mover(self, ficha, lugar):
		if ficha.get_color() == Ficha.CAFE:
			i,j = self.encontrar_ficha(ficha)
			x,y = self.encontrar_ficha(lugar)


		mov_normal = self.mover_espacio(ficha, lugar)
		if mov_normal == False:
			mov_comiendo = self.mover_comiendo(ficha, lugar)
			if mov_comiendo == False:
				print "la ficha no se movio"
				return False, -1 #Si no se movio
			else:
				print "la ficha se movio comiendo"
				if ficha.get_color() == Ficha.CAFE:
					self.entradas_ia += self.normalizar(i) + ' ' + self.normalizar(j) + ' ' + self.normalizar(x) + ' ' + self.normalizar(y)
					print "i:" +str(i)+ " j:"+str(j)+" x:"+str(x)+ " y:"+str(y) 
				if ficha.es_dama() == False:
					self.regla_dama_come_antes(ficha.get_color())
				return True, 0 #Si se movio comiendo
		else:
			print "la ficha se movio normalmente"


			if ficha.get_color() == Ficha.CAFE:
				self.entradas_ia += self.normalizar(i) + ' ' + self.normalizar(j) + ' ' + self.normalizar(x) + ' ' + self.normalizar(y)
				print "i:" +str(i)+ " j:"+str(j)+" x:"+str(x)+ " y:"+str(y) 
			return True, 1 #Si fue un movimiento normal

	def convertir_dama(self):
		#revisa si una ficha blanca se convierte en dama
		for j in range(1,8,2):
			if self.cuadricula[0][j].get_jugador() == self.fB:
				self.cuadricula[0][j].cambiar_imagen(self.fBD)
				print "ficha en posicion 0,", j ," se convirtio en dama"
		#revisa si una ficha cafe se convierte en dama
		for j in range(0,8,2):
			if self.cuadricula[7][j].get_jugador() == self.fC:
				self.cuadricula[7][j].cambiar_imagen(self.fCD)
				print "ficha en posicion 7,", j ," se convirtio en dama"

	def contador_fichas_blancas(self):
		i = 0
		j = 0
		cont = 0
		for i in range(8):
			for j in range(8):
				if self.cuadricula[i][j] != 0:
					if self.cuadricula[i][j].get_color() == Ficha.BLANCA:
						cont += 1

		return cont

	def contador_fichas_cafes(self):
		i = 0
		j = 0
		cont = 0
		for i in range(8):
			for j in range(8):
				if self.cuadricula[i][j] != 0:
					if self.cuadricula[i][j].get_color() == Ficha.CAFE:
						cont += 1

		return cont

	def regla_comer_obligado(self, color):
		for i in range(8):
			for j in range(8):
				if self.cuadricula[i][j] != 0:
					if self.cuadricula[i][j].get_color() == color:
						if self.comprobar_sig_com(self.cuadricula[i][j]) == True:
							self.cuadricula[i][j].cambiar_imagen(-1)
							return True
		return False

	def regla_dama_come_antes(self, color):
		for i in range(8):
			for j in range(8):
				if self.cuadricula[i][j] != 0:
					if (self.cuadricula[i][j].get_color() == color) & (self.cuadricula[i][j].es_dama()):
						if self.comprobar_sig_com(self.cuadricula[i][j]) == True:
							self.cuadricula[i][j].cambiar_imagen(-1)
							return True
		return False

	def entradas_rna(self):
		entrada = ''
		self.entradas_ia = ''
		for i in range(8):
			for j in range(8):
				if self.cuadricula[i][j] != 0:
					if self.cuadricula[i][j].get_color() == Ficha.CAFE:
						entrada += str(self.cuadricula[i][j].get_jugador())
						if self.comprobar_mov(self.cuadricula[i][j]):
							entrada += ' 1 '
						else:
							entrada += ' 0 '
					elif self.cuadricula[i][j].get_color() == Ficha.LIBRE:
						entrada += str(self.cuadricula[i][j].get_jugador())
						if self.comprobar_espacio(self.cuadricula[i][j]):
							entrada += ' 1 '
						else:
							entrada += ' 0 '

					elif self.cuadricula[i][j].get_color() == Ficha.BLANCA:
						entrada += str(self.cuadricula[i][j].get_jugador()) + " 0 "

		self.entradas_ia = entrada


	def salida_rna(self):
		outfile = open('../DatosEntrenamiento/dataset.txt', 'a')
		outfile.write( self.entradas_ia + '\n')
		outfile.close()

	def registrar_salida(self,fichaSel,lugar):
		if fichaSel.get_color() == Ficha.CAFE:
			x,y = self.encontrar_ficha(fichaSel)
			i,j = self.encontrar_ficha(lugar)

			self.entradas_ia += str(self.normalizar(i)) + ' ' + str(self.normalizar(j)) + ' ' + str(self.normalizar(x)) + ' ' + str(self.normalizar(y))
			print "i:" +str(i)+ " j:"+str(j)+" x:"+str(x)+ " y:"+str(y) 


	def comprobar_ganador(self, color):
		for i in range(8):
			for j in range(8):
				if self.cuadricula[i][j] != 0:
					if self.cuadricula[i][j].get_color() == color:
						if self.comprobar_mov(self.cuadricula[i][j]):
							return False
		return True

	def normalizar_sin_uso(self, valor):
		if valor == 0:
			return 0.062
		elif valor == 1:
			return 0.187
		elif valor == 2:
			return 0.312
		elif valor == 3:
			return 0.437
		elif valor == 4:
			return 0.562
		elif valor == 5:
			return 0.687
		elif valor == 6:
			return 0.812
		elif valor == 7:
			return 0.937

	def normalizar(self, valor):
		if valor == 0:
			return '0 0 0'
		elif valor == 1:
			return '0 0 1'
		elif valor == 2:
			return '0 1 0'
		elif valor == 3:
			return '0 1 1'
		elif valor == 4:
			return '1 0 0'
		elif valor == 5:
			return '1 0 1'
		elif valor == 6:
			return '1 1 0'
		elif valor == 7:
			return '1 1 1'