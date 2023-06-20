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
