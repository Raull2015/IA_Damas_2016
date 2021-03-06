import pygame, sys
from pygame.locals import *
from Tablero import Tablero
from Ficha import Ficha
from Herramientas import *
sys.path.append('../pythonNeuralNetwork/backprop')
from neuralnet import NeuralNet
from tools import Instance
#variables globales

#tamanio de ventana
ancho = 1080
alto = 700
#modo de juego
un_jugador = 0
dos_jugadores = 1
#Seleccion
seleccionado = False
fichaSel = None
#Turno
turno = Ficha.BLANCA
#Bloqueo de movimiento
bloqueo = False
#Red neuronal
network = NeuralNet.load_from_file("network0.pkl")
#archivo de salida de entrenamientos
archivo_data_set = '../DatosEntrenamiento/dataset.txt'

def cambiar_turno(turno,fichaTurno,ventana,tablero,grabar):
	if turno == Ficha.BLANCA:
		fichaTurno.cambiar_imagen(0)
		ventana.blit(fichaTurno.get_imagen(), fichaTurno.get_rect())
		print "Turno: Fichas Cafes"
		tablero.entradas_rna()
		return Ficha.CAFE
	else:
		fichaTurno.cambiar_imagen(2)
		ventana.blit(fichaTurno.get_imagen(), fichaTurno.get_rect())
		print "Turno: Fichas Blancas"
		if grabar:
			tablero.escribir_salida_rna(archivo_data_set)
		return Ficha.BLANCA

def marcador(ventana,tablero):
	cafes = tablero.contador_fichas_cafes()
	blancas = tablero.contador_fichas_blancas()
	fuente = pygame.font.Font(None, 40)
	marcadorCafes = fuente.render(str(cafes), 1, (255, 255, 255))
	marcadorBlancas = fuente.render(str(blancas), 1, (255, 255, 255))
	ventana.blit(marcadorBlancas,(945,605))
	ventana.blit(marcadorCafes,(945,655))

def victoria(ventana, tablero):
	cafes = tablero.contador_fichas_cafes()
	blancas = tablero.contador_fichas_blancas()
	cafes_mov = tablero.comprobar_ganador(Ficha.CAFE)
	blancas_mov = tablero.comprobar_ganador(Ficha.BLANCA)
	if (cafes == 0) | (cafes_mov):
		victoriaBlanca = pygame.image.load("../Resources/vBlanca.png")
		ventana.blit(victoriaBlanca,(71,304))
	elif (blancas == 0) | (blancas_mov):
		victoriaCafe = pygame.image.load("../Resources/vCafe.png")
		ventana.blit(victoriaCafe,(71,304))

def seleccionar_ficha(ventana, tablero, fichaSel):
	tablero.dibujar(ventana)
	pygame.draw.circle(ventana, (255,117,020), fichaSel.get_rect().center, 39)
	tablero.dibujar_fichas(ventana)

def movimiento_ia(ventana,fichaTurno,tablero):
	ventana.blit(fichaTurno.get_imagen(), fichaTurno.get_rect())
	vector = np.array(tablero.get_entrada_rna())
	vector = vector[:64].astype(float)

	entrada = [Instance(vector,[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])]
	salida, esperado = network.print_test(entrada)
	for i in salida:
		coordenadas = convertir(i)

	i = coordenadas[0]
	j = coordenadas[1]
	x = coordenadas[2]
	y = coordenadas[3]
	print "ficha selec: ", i , ",",j, "destino: ", x,",",y
	fichaSel = tablero.get_ficha(i,j)
	lugar = tablero.get_ficha(x,y)
	if  (fichaSel != 0) & (lugar != 0):
		if fichaSel.get_color() == Ficha.CAFE:	
			ocurrio_mov, tipo_mov = tablero.mover(fichaSel, lugar)
			#actualiza el marcador y dibuja el tablero
			marcador(ventana,tablero)
			tablero.convertir_dama()
			tablero.dibujar(ventana)
			tablero.dibujar_fichas(ventana)
			#Determina si existe victoria
			victoria(ventana,tablero)


def damas():
	#asigna variables
	turno = Ficha.BLANCA
	seleccionado = False
	fichaSel = None
	bloqueo = False
	#crea la ventana de juego
	pygame.init()
	ventana = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption("Damas")
	#Coloca el icono del juego
	icon = pygame.image.load("../Resources/Icono.png")
	pygame.display.set_icon(icon)
	#carga imagen de fono
	imagenFondo = pygame.image.load("../Resources/Fondo.jpg")
	ventana.blit(imagenFondo,(0,0))
	#crea el tablero de juego
	tablero = Tablero()
	tablero.dibujar(ventana)
	tablero.dibujar_fichas(ventana)
	#Botones y HUD
	imagenFondoBot = pygame.image.load("../Resources/FondoBotones.png")
	ventana.blit(imagenFondoBot,(750,0))
	#Interfaz
	fichaTurno = Ficha(2,880,440) #Ficha de turno
	ventana.blit(fichaTurno.get_imagen(), fichaTurno.get_rect()) #dibujo la ficha de turno
	marcador(ventana,tablero) #Coloca el marcador
	#establece el modo de juego
	modo = un_jugador
	#establece si registra los entrenamientos
	grabar = False
	#empieza a registrar los movimientos
	tablero.entradas_rna()

	print "Turno: Fichas Blancas"
	while True:
		#recoge los evenetos del juego
		for evento in pygame.event.get():
			#eventos
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()

			elif evento.type == pygame.KEYDOWN:
				tecla = pygame.key.get_pressed()
				if tecla[K_r]:
					print "Reincio"
					tablero.llenar()
					tablero.dibujar(ventana)
					tablero.dibujar_fichas(ventana)
					ventana.blit(imagenFondoBot,(750,0))
					turno = Ficha.BLANCA
					fichaTurno.cambiar_imagen(2)
					ventana.blit(fichaTurno.get_imagen(), fichaTurno.get_rect())
					marcador(ventana,tablero)
					tablero.entradas_rna()

				elif tecla[K_1]:
					print "Cambiado a modo: Un Jugador"
					modo = un_jugador
				elif tecla[K_2]:
					print "Cambiado a modo: Dos Jugadores"
					modo = dos_jugadores
				elif tecla[K_g]:
					if grabar == True:
						grabar = False
						print "Salidas de Entrenamiento: Apagadas"
					else :
						grabar = True
						print "Salidas de Entrenamiento: Encendidas"

			#Evento cuando se presiona el boton del mouse
			if evento.type == pygame.MOUSEBUTTONUP:
				#Obtiene la posicion del puntero
				posX, posY = pygame.mouse.get_pos()
				#Busqueda en las fichas de juego
				fichas = tablero.cuadricula
				for i in fichas:
					for j in i:
						if j != 0:
							if j.get_rect().collidepoint(posX, posY):
								print "Ficha de tipo: ", j.get_jugador()
								if j.get_color() == Ficha.LIBRE:
									print tablero.comprobar_espacio(j)
								#Si selecciona una ficha del color que es el turno
								if (j.get_color() == turno) & (bloqueo == False):
									#si la ficha ya estaba seleccionada se deselecciona
									if j == fichaSel:
										tablero.dibujar(ventana)
										tablero.dibujar_fichas(ventana)
										fichaSel = None
										seleccionado = False
									#la ficha es seleccionada solo si puede moverse
									elif tablero.comprobar_mov(j):
										seleccionar_ficha(ventana,tablero,j)
										fichaSel = j
										seleccionado = True
								#Si se selecciono una casilla libre
								elif j.get_color() == Ficha.LIBRE:
									if seleccionado == True:
										if bloqueo == True:
											ocurrio_mov = tablero.mover_comiendo(fichaSel,j)
											if ocurrio_mov:
												tablero.registrar_salida(fichaSel, j)
										else:
											ocurrio_mov, tipo_mov = tablero.mover(fichaSel, j)

										if ocurrio_mov:
											tablero.dibujar(ventana)
											tablero.dibujar_fichas(ventana)
											#verifica si la ficha aun puede seguir comiendo
											if (tablero.comprobar_sig_com(fichaSel)) & (tipo_mov == 0):
												#print j.get_jugador()
												seleccionar_ficha(ventana,tablero,fichaSel)
												bloqueo = True
												#ventana de menu
												ventana.blit(imagenFondoBot,(750,0))
												#Ficha de turno
												ventana.blit(fichaTurno.get_imagen(), fichaTurno.get_rect())
												#Actualiza el marcador
												marcador(ventana,tablero)
												#Salidas para entrenamiento
												if grabar:
													tablero.escribir_salida_rna()
												tablero.entradas_rna()
											#Si la ficha ya no puede moverse mas
											else:
												fichaSel = None
												seleccionado = False
												#ventana de menu
												ventana.blit(imagenFondoBot,(750,0))
												#Actualiza el marcador
												marcador(ventana,tablero)
												tablero.convertir_dama()
												tablero.dibujar_fichas(ventana)
												#Determina si existe victoria
												victoria(ventana,tablero)
												bloqueo = False
												if modo == dos_jugadores:
													#Cambia la imagen de turno
													turno = cambiar_turno(turno,fichaTurno,ventana,tablero,grabar)
												elif modo == un_jugador:
													movimiento_ia(ventana,fichaTurno,tablero)

		pygame.display.update()
damas()
