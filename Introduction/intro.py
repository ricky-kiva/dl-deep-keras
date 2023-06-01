### Introduction to Deep Learning

# applications of Deep Learning:
# - color restoration
# --- http://hi.cs.waseda.ac.jp/~iizuka/projects/colorization/extra.html
# - speech reenactment (lip synching with audio)
# --- obtained by training recurrent neural network on a large corpus of video data of a single person
# - automatic handwriting generation
# - automatic machine translation (translate text in image on the fly)
# - automatic add sounds to silent music
# --- obtained by selecting sound from pre-recorded sound database, to the scene
# - object classification & detection
# - self-driving car

### Neurons & Neural Networks

# deep learning algorithms are largely inspired by neurons & neural networks function that process data in the brain
# Neural Networks is a group/network of Neurons

# structures of neuron:
# - Soma: main body (contains nucleus)
# - Dendrites: arms out of the main body
# - Axon: long arm to other direction
# - Synapse / Terminal Button: whiskers at the end of axon

# workflow of neuron:
# - Dendrites receive electrical impulses which carry data from Terminal Button (sensor)
# - Dendrites carry the data to Soma
# - inside Soma, data processed by combining them together
# - data then passed to Axon, then to its Terminal Button
# - the output of this neuron, become the input for another neuron

# learning in brain occurs by repeatedly activating certain neural connections over other
# - it then reinforces those connections, making them more likely to produce desired outcome given specified input
# - once the desired outcome occurs, the neural connections causing that outcome become strengthened

# Artificial Neural Network behaves the same as biological neuron
# - it consists Soma, Dendrites, & Axon

### Artificial Neural Networks

# Network of Neurons (Neural Networks) often divided to different layers:
# - Input layer: first layer that feeds the input into the network
# - Output layer: last layer that act as an output for the network
# - Hidden layer: layers between input & output layer

# Forward Propagation:
# - is a process through which data passes through layers of neurons in neural network
# - from input layer all the way to output layer

# say image `1-3-forward-propagation.jpg`
# - properties:
# --- x1 & x2 = two inputs
# --- w1 & w2 = weights (of connection)
# --- b1 = bias
# --- z = linear combination of the inputs & weights
# --- a = output of the network

# - process:
# --- inputs passing through connection by adjusting with weights
# --- neuron process the information by outputting weighted sum of the inputs, and adding bias

# - ideal process:
# --- simply outputting weighted sum of inputs, will limits the task that can be performed by neural network
# --- a better processing of data would be to map the weighted sum to a nonlinear space (non-linear transformations)
# --- to do it, we could use an activation function. A popular one is called Sigmoid Function
# --- say image `1-3-forward-propagation-with-activation.jpg`
# --- in Sigmoid function, wen the weighted sum is a very large postitive, the output is close to 1
# ------ if very large negative number, the output is close to zero
# --- Sigmoid function = f(z) = 1/(1+(e^(-z)))

# Activation function decide whether a neuron should be activated or not
# - a neural network without activation function is essentially just a linear regression model
# - the activation function performs non-linear transformation to the input, enabling neural network performing complex tasks

# example in calculating Neural Network:
# `1-3-forward-propagation-calculation.jpg`