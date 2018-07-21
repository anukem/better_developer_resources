# first attempt at writing a neural network from scratch
# July 20th, 2018 

class NeuralNetwork(object):
	"""docstring for NeuralNetwork"""
	def __init__(self, in_size, hl_size, out_size):
		super(NeuralNetwork, self).__init__()
		self.in_size = in_size
		self.hl_size = hl_size
		self.out_size = out_size

		# create arrays
		self.input_layer, self.hidden_layer, self.output_layer = [], [], []

		# initialize num of weights
		self.num_weights = 0

		self.ih_weights = []
		self.ho_weights = []

		# initialize bias
		self.h_bias = []
		self.o_bias = []

	def initialize_arrays(self):
		for i in range(self.in_size):
			self.input_layer.append(0)
		for i in range(self.hl_size):
			self.hidden_layer.append(0)
		for i in range(self.out_size):
			self.output_layer.append(0) 

	def initialize_weights(self):
		self.num_weights = self.in_size*self.hl_size + self.hl_size * self.out_size

		# weights for the input to hidden layer
		for i in range(self.in_size):
			self.ih_weights.append([0 for x in range(self.hl_size)])

		# weights for the hidden layer to the output layer
		for i in range(self.hl_size):
			self.ho_weights.append([0 for x in range(self.out_size)])

	def initialize_bias(self):
		for i in range(self.hl_size):
			self.h_bias.append(0)
		for i in range(self.out_size):
			self.o_bias.append(0)

nn = NeuralNetwork(3, 4, 2)
nn.initialize_arrays()
nn.input_layer = [1,2,3]
nn.initialize_weights()
nn.initialize_bias()
print(nn.h_bias,"\n" ,nn.o_bias)