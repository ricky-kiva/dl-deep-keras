### GRADIENT DESCENT

# Cost Function: to find the value of w that would generate a `line` that `best fits data`
# - example: J(w) = (1/2m) Σ (xi - w(zi))^2
# - tips: if the function is parabola, then the best `w` is the `minimum`

# in real datasets, variable `z` would commonly be dependent to more than one variable
# - Gradient Descent: algorithm to find the best w's if there are `many weights to optimize`

# Gradient Descent is an iterative optimization algorithm to find minumum of a function
# to find manimum in Gradient Descent: one takes steps proportional to the negative of the gradient of the function at the current point
# - start at random initial value of w (w0)
# - move in `direction` of `computed gradient loss` function at `current value of w`
# - the magnitude of the step is controlled by `learning rate` parameter (miu)
# --- the larger the learning rate, the bigger the step will be taken, vice versa
# - move to the next value (w1), which will be:
# --- w1 = w0 - ((learning rate) * (gradient at w0))
# ------ gradient at w0 = dJ / dW
# - do the next iteration with the same learning rate, until hit the minumum (this is the 1st iteration)
# --- example: 2-1-integration-gradient-descent.jpg

# note on gradient:
# - gradient will be postive if it goes `up` and `from left to right`
# - gradient will be negative if it goes `down` and to `from left to right`
# --- infographic: 2-1-gradient-positive-negative

# - Gradient Descent's objective is to move towards the minimum following the negative gradient direction, `regardless of whether the gradient is positive or negative`
# - so if the weight is initialized in the `right of the gradient`, it will `still go left & down`

# caution on learning rate:
# - large learning rate can result missing the minumum
# - small learning rate can result long time to find minimum point

### BACKPROPAGATION

# Backpropagation: is a way neural networks train & optimize their weights & biases for gien problem & data set
# - it happened after the network have already making predictions using forward propagation, which gave the initial weights & bias

# Supervised Learning: each data point has corresponding 'Label' / 'Ground Truth'
# - trainig is needed when predicted value of neural network doesn't match Ground Truth

# ways of Backpropagation:
# - calculate error (E) between Ground Truth & estimated output
# --- the error represents the cost function
# - propagate the error back into the network & update each weight & bias using these equations:
# --- wi -> wi - (learning rate) • dE/dwi
# --- bi -> bi - (learning rate) • dE/dbi

# given this simple neural network: 2-2-backpropagation-algorithm.JPG
# - E = (1/2m) Σ (T - a[2,i])^2
# --- T = Ground Truth

# from the given simple neural network, we need to update each element as follows:
# - w2 -> w2 - (learning rate) • dE/dw2
# - b2 -> b2 - (learning rate) • dE/db2
# - w1 -> w1 - (learning rate) • dE/dw1
# - b1 -> b1 - (learning rate) • dE/db1
# --- full calculations could be found in: 2-2-partial derivative-example.pdf

# given calculated forward propagation for the simple neural network for input 0.1:
# - 2-2-backpropagation-calculated-forward-prop.JPG

# assume the ground truth is 0.25
# - then we plug the calculated values (a2, a1, z2, z1) to update
# - update values from: w2 -> b2 -> w1 -> b1
# - the formula to calculate is the one within 2-2-partial derivative-example.pdf

# summarize of way: Complete Training Algorithm
# - initializy `weights` & `biases` randomly
# - iteratively repeat following steps:
# --- calculate output using forward propagation
# --- calculate error between Ground Truth & predicted output
# --- update weights & biases through Backpropagation
# --- repeat above 3 steps until number of epoch is reached / output is elow predefined threshold

### VANISHING GRADIENT PROBLEM

# Vanishing Gradient: is a problem where Sigmoid Activation Function prevent neural networks to bloom sooner

# take a look at this picture: 2-3-sigmoid-simple-neural-network.JPG
# - the gradients is small, especially the one with respect to w1
# - it is because Sigmoid Function make all the intermediate values in network are between 0 & 1
# - thus made the gradients tend to get smaller as it move backwards in the network
# - it makes the earlier layers in network are the slowest to train & the accuracy is compromised
# --- infographic: 2-3-vanishing-gradient.JPG

# ACTIVATION FUNCTIONS

# types of activation functions to build neural network:
# - Binary Step Function
# - Linear Function
# - Sigmoid Function
# - Hyperbolic Tangent Function
# - ReLU (Rectified Linear Unit)
# - Leaky ReLU
# - Softmax Function

# Sigmoid Function: 2-4-sigmoid-function.JPG
# - a = 1/(1+exp(-z))
# - the function only range from 0 to 1
# --- the values received are all positive (which not all time we desire all neuron to be the same sign)
# --- NOT symmetric around the origin
# - shortcoming is function is pretty flat beyond +3 & -3
# --- means once the function falls in that region, the gradients become very small (vanishing gradient)

# Hyperbolic Tangent Function (tanh): 2-4-hyperbolic-tangent-function.JPG
# - a = (exp(z)-exp(-z)) / (exp(z) + exp(-z))
# - it's a scaled function of Sigmoid Function (include negative)
# - it ranges from -1 to 1
# - it's symmetric around the origin
# - it still has issues with Vanishing Gradient

# Rectified Linear Unit (ReLU): 2-4-rectified-linear-unit-function.JPG
# - a = max(0,z)
# --- if the input is negative, it will be converted to 0, and the neuron will NOT get activated
# ------ it makes the network sparse & efficient
# - is the most widely used activation function when designing networks today (2023)
# - main advantage is, it doesn NOT activate all the neurons at the same time
# - it overcome the vanishing gradient problem

# Softmax Function:
# a = (e^zi) / Σ[m, k=1] e^zk
# - it's a type of sigmoid function that is handy for 'Classification Problems'
# - it's ideally used when trying to get probabilities to define class of each input
# - example: output = [1.6, 0.55, 0.98] --SOFTMAX--> [0.51, 0.18, 0.31]
# --- it made classification easier to determine which category it belongs

# conclusion of activation function:
# - sigmoid & tanh function are avoided in many applications nowadays, since they lead to vanishing gradient problem
# - ReLU function is widely used, but only used in `hidden layers`
# - generally, in building a model, can begin using ReLU function then switch to another function if it doesn't yield a good performance