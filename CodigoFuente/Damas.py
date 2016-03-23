import pygame, sys 
from pygame.locals import *
from Tablero import *

#variables globales  
#tamanio de ventana
ancho = 1080
alto = 700


def damas():
	#crea la ventana de juego
	pygame.init()
	ventana = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption("Damas")
	#carga imagen de fono
	imagenFondo = pygame.image.load("../Resources/Fondo.jpg")
	ventana.blit(imagenFondo,(0,0))
	#crea el tablero de juego
	tablero = Tablero()
	tablero.dibujar(ventana)
	tablero.dibujar_fichas(ventana)
	
	while True:
		#recoge los evenetos del juego
		for evento in pygame.event.get():
			#eventos
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()

			if evento.type == pygame.MOUSEBUTTONUP:
				posX, posY = pygame.mouse.get_pos()
				fichas = tablero.cuadricula
				for i in fichas:		
					for j in i:	
						if j != 0:
							if j.get_rect().collidepoint(posX, posY):
								#j.set_rect(0,0)
								if tablero.comprobar_mov(j) == True:
									tablero.dibujar(ventana)
									pygame.draw.circle(ventana, (255,117,020), j.get_rect().center, 39)	
									tablero.dibujar_fichas(ventana)		

		pygame.display.update()
		

damas()

