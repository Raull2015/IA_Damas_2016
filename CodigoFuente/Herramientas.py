import numpy as np

def binario_ent(vector):
    return vector[0] * 4 + vector[1] * 2 + vector[2] * 1

def valor(num):
    if num > 0.5:
        return 1
    else:
        return 0

def convertir(resultado):
    res = []
    for i in resultado:
        res.append(valor(i))
    print res
    no1 = binario_ent(res[:3])
    no2 = binario_ent(res[3:6])
    no3 = binario_ent(res[6:9])
    no4 = binario_ent(res[9:12])
    return [no1,no2,no3,no4]

def leerEntradas(entrada):
    auxSalida = []
    cont = 0
    for n in entrada:
        if cont < 64:
            auxSalida.append(n)
            cont += 1
    return auxSalida

def leerSalidas(entrada):
    auxEntrada = []
    cont = 0
    for n in entrada:
        if cont > 63:
            auxEntrada.append(n)
        cont += 1

    return auxEntrada

def obtener_datos():
    archivo = open("dataset.txt", "r")
    for linea in archivo.readlines():
      entrada = np.array(linea.split(' ')).astype(float)
      entradas = leerEntradas(entrada)
      salidas = leerSalidas(entrada)
      training_one.append(Instance(entradas,salidas))

def normalizar_sin_uso( valor):
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

def normalizar( valor):
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
