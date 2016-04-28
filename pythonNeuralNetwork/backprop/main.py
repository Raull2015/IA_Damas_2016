from activation_functions import sigmoid_function, tanh_function, linear_function,\
                                 LReLU_function, ReLU_function, elliot_function, symmetric_elliot_function, softmax_function
from cost_functions import sum_squared_error, cross_entropy_cost, exponential_cost, hellinger_distance, softmax_cross_entropy_cost
from learning_algorithms import backpropagation, scaled_conjugate_gradient, scipyoptimize, resilient_backpropagation
from neuralnet import NeuralNet
from tools import Instance, confirm
import numpy as np

training_one = []

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
    #archivo = open("../../dataset.txt","r")
    #entrada = archivo.readline().split(' ')
    for n in entrada:
        if cont < 64:
            auxSalida.append(n)
            cont += 1
    return auxSalida

def leerSalidas(entrada):
    auxEntrada = []
    cont = 0
    #archivo = open("../../dataset.txt","r")
    #entrada = archivo.readline().split(' ')
    for n in entrada:
        if cont > 63:
            auxEntrada.append(n)
        cont += 1

    return auxEntrada

def obtener_datos():
    archivo = open("dataset.txt", "r")
    #archivo = open("../../dataset.txt", "r")
    for linea in archivo.readlines():
      entrada = np.array(linea.split(' ')).astype(float)
      entradas = leerEntradas(entrada)
      salidas = leerSalidas(entrada)
      training_one.append(Instance(entradas,salidas))

obtener_datos()

# Training sets
#training_one    = [ Instance( [0,0], [0] ), Instance( [0,1], [1] ), Instance( [1,0], [1] ), Instance( [1,1], [0] ) ]


settings = {
    # Required settings
    "cost_function"         : sum_squared_error,
    "n_inputs"              : 64,       # Number of network input signals
    "layers"                : [ (128, sigmoid_function),(64, sigmoid_function), (12, sigmoid_function)],
                                        # [ (number_of_neurons, activation_function) ]
                                        # The last pair in you list describes the number of output signals

    # Optional settings
    "weights_low"           : -5,     # Lower bound on initial weight range
    "weights_high"          : 5,      # Upper bound on initial weight range
    "save_trained_network"  : True,    # Whether to write the trained weights to disk

    "input_layer_dropout"   : 0.0,      # dropout fraction of the input layer
    "hidden_layer_dropout"  : 0.0,      # dropout fraction in all hidden layers
}


# initialize the neural network
#network = NeuralNet( settings )

# load a stored network configuration
network = NeuralNet.load_from_file( "network0.pkl" )

# Train the network using backpropagation
backpropagation(
        network,
        training_one,          # specify the training set
        ERROR_LIMIT     = 1.8, # define an acceptable error limit
        max_iterations  = 4000, # continues until the error limit is reach if this argument is skipped

        # optional parameters
        learning_rate   = 0.2, # learning rate
        momentum_factor = 0.7, # momentum
         )

resultados, esperados = network.print_test( training_one )


for resultado, esperado in zip(resultados,esperados):
    print 'El resultado es '
    print convertir(resultado)
    print 'Lo esperado es'
    print esperado
    print convertir(esperado)



# Train the network using SciPy
"""scipyoptimize(
        network,
        training_one,
        method = "Newton-CG",
        ERROR_LIMIT = 1e-4
    )

# Train the network using Scaled Conjugate Gradient
scaled_conjugate_gradient(
        network,
        training_one,
        ERROR_LIMIT = 1e-4
    )

# Train the network using resilient backpropagation
resilient_backpropagation(
        network,
        training_one,          # specify the training set
        ERROR_LIMIT     = 1e-3, # define an acceptable error limit
        #max_iterations = (),   # continues until the error limit is reach if this argument is skipped

        # optional parameters
        weight_step_max = 50.,
        weight_step_min = 0.,
        start_step = 0.5,
        learn_max = 1.2,
        learn_min = 0.5
    ) """
