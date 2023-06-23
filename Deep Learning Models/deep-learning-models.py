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
