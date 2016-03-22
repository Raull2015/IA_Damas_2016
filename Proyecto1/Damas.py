import pygame, sys 
from pygame.locals import *
from Tablero import *

#variables globales
ancho = 1080
alto = 700


def damas():
	pygame.init()
	ventana = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption("Damas")

	tablero = Tablero()
	while True:
		
		for evento in pygame.event.get():

			if evento.type == QUIT:
				pygame.quit()
				sys.exit()

			if evento.type == pygame.MOUSEBUTTONUP:
				posX, posY = pygame.mouse.get_pos()
				fichas = tablero.cuadricula
				for i in fichas:		
					for j in i:	
						if j != 0:
							if j.collidepoint(posX, posY):
								j.set_rect(0,0)

				
		tablero.dibujar(ventana)
		tablero.dibujar_fichas(ventana)
		pygame.display.update()

damas()

