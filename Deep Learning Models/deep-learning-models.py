### SHALLOW VS. DEEP NEURAL NETWORK

# Shallow Neural Network has small number of hidden layers (such as only 1)
# Deep Neural Network has large number of neurons & hidden layers

# why Deep Learning Took off?
# - advancement in the field itself (such ReLU)
# - data (widely available)
# - computational power (like nVidia GPUs, offers training of large data in the matter of hours/day)

### Convolutional Neural Networks (CNNs)

# CNNs is similar to conventional neural networks. Made up of neurons which combines inputs received by doing dot product between each input & corresponding weight
# CNNs take inputs as images, allows to incorporate properties to make training process much more efficient & reduce parameters in network
# CNNs best for solving computer vision applications

# CNN architecture: 4-2-CNN-architecture.JPG
# it commonly consist of:
# - [Convolutional Layer, Pooling Layer] (2x)
# - fully connected layer
# - output (n class amount)

# conventional neural networks only take (n x 1) vector as input
# convolutional neural network's input is:
# - (n x m x 1) for grayscale images
# - (n x m x 3) for colored images (3 represents RGB)

# in convolutional layer we define filters, to compute convolution berween defined filters & each of 3 images
# example making a (2 x 2) filter -> (5 x 5) pixel is becoming (4 x 4) pixel
# ways to filter (example in RED): 
# - sliding the filter over the image
# - computing dot product between filter and overlapping pixel values
# - storing result to empty matrix
# - repeat until empty matrix is all covered
# - apply to the BLUE & GREEN too
# the more filter used, the more able to preserve spatial dimensions better
# example: 4-2-convolutional-layer.JPG

# why not just flatten the input image to (n x m x 1) vector, but use convolution instead?
# - it will end up with massive number of parameters to be optimized (computationally expensive)
# - it prevents overfitting the training data

# convolutional layer also consists of ReLU which will filter the output by passing only positive value (negative turn to 0)

# pooling layer is a layer which main objective is to reduce spatial dimensions of data propagating through network
# - it helps extract most important features & discarding less significant information
# - it will recognize objects even if the object doesn't resemble the original object

# 2 types of common pooling in CNNs:
# - max pooling: keep the highest value
# - average pooling: compute average of each area
# example (average pooling): 4-2-pooling-layer.JPG

# Fully Connected Layer will pass the flatten input from the last convolutional layer & connect every node of the current layer with every other node of the next layer
# in the end, it outputs an `n-dimensional` vector, where `n` is the number of the class (example: 10 for number of digits)

# commonly, it's good to apply the 2nd convolutional layer filter twice of the 1st convolutional layer
# commonly, output activation to be used is `softmax` to convert outputs to probabilities

### RECURRENT NEURAL NETWORKS (RNNs)

# RNNs are networks with loops that take input from the previous 'data point' that was fed into the network
# RNNs architecture: 
# - at t = 0, RNNs neural network starts with normal neural network
# - at t = 0, it takes input x0 & outputs a0
# - at t = 1, it takes input x1, (a0 weighted with w[0,1]), & outputs a1
# - at t = n, so on
# infographic: 4-3-RNN-architecture.JPG

# RNNs good at modelling patterns & sequences of data:
# - text
# - genomes
# - handwriting
# - stock markets

# RNNs algorithms take time & sequence into account, means it has temporal dimension

# LSTM (Long Short-Term Memory Model) is a popular RNN used for:
# - image generation
# - handwriting generation
# - describe images
# - describe videos

### AUTOENCODERS

# Autoencoding is data compression algorithm where `compression` & `decompression` functions learned automatically from data using neural networks
# autoencoders is data specific (only able to compress data similar to what they have been trained on)
# example: autoencoder trained on pictures of cars would rather poor job compressing building pictures

# interesting applications:
# - data denoising & dimensionality reduction for data visualization

# autoencoder architecture: 4-4-autoencoder-architecture.JPG
# - it takes image as an input
# - using encoder, it finds the optimal representation of the input image
# - using decoder, it restore the original image back

# autoencoder is an `unsupervised` neural network model
# - it uses backpropagation by setting the target variable to be the same as the input
# --- it tries to learn approximation of an identity function

# autoencoder can learn diverse data projections, not only linear transformation like PCA

# Restricted Boltzmann Machines (RBMs) is one of popular autoencoders that could fix imbalanced datasets:
# - RBMs learn the input to get insight on the distribution of the minority class
# - then RBMs generate more data points of the class

# RBMs could also estimate missing values in different features of dataset
# RBMs could also do automatic feature extraction for unstructured data  