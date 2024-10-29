class Neuron:
    def __init__(self):
        self.weight = 0.1
        self.bias = 0.1
        self.connections = []
    
    def forward(self, x):
        return x * self.weight + self.bias
    
    def backward(self, x, grad):
        self.weight -= x * grad
        self.bias -= grad
    

class Layer:
    def __init__(self, size):
        self.neurons = [Neuron() for _ in range(size)]

    def forward(self, x):
        return [neuron.forward(x) for neuron in self.neurons]
    
    def backward(self, x, grads):
        for neuron, grad in zip(self.neurons, grads):
            neuron.backward(x, grad)


class Model:
    def __init__(self):
        self.Layers = []

    def addLayer(self, layer):
        self.layers.append(layer)
        # make connections between layers
        for neuron in self.layers[-2].neurons:
            neuron.connections = self.layers[-1].neurons
    
    def forward(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x
    
    def backward(self, x, grads):
        for layer, grad in zip(self.layers[::-1], grads[::-1]):
            layer.backward(x, grad)
    
    def train(self, x, y, epochs):
        for _ in range(epochs):
            y_pred = self.forward(x)
            loss = (y_pred - y) ** 2
            grad = 2 * (y_pred - y)
            self.backward(x, [grad])
            print(loss)

model = Model()
model.addLayer(Layer(2))
