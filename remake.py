from random import random

#[input, [# hidden layer:[neuron:[weight, bias]]], output]
#0 = weight, 1= bias

def initialize_neural_network(n_input =0,n_hidden_layers =[0,0,0], n_output =0):
    neural_network = []
    hidden_layers = []
    for i in range(0,len(n_hidden_layers)):
        layer = []
        if i == 0:
            for j in range(0,n_hidden_layers[i]):
                neuron = []
                for k in range(0,n_input):
                    connection ={}
                    connection['Weight'] =random()
                    connection['Bias'] = random()
                    neuron.append(connection)
                layer.append(neuron)
        else:
            for j in range(0,n_hidden_layers[i]):
                neuron = []
                for k in range(0,n_hidden_layers[i-1]):
                    connection ={}
                    connection['Weight'] =random()
                    connection['Bias'] = random()
                    neuron.append(connection)
                layer.append(neuron)
        hidden_layers.append(layer)
    output_layer = []
    
    for i in range(0,n_output):
        neuron = []
        for j in range(0,n_hidden_layers[-1]):
            connection = {}
            connection['Weight'] =random()
            connection['Bias'] = random()
            neuron.append(connection)
        output_layer.append(neuron)
    neural_network.append(hidden_layers)
    neural_network.append(output_layer)
    return neural_network

neural_network = initialize_neural_network(2,[2,2],1)
print(neural_network)