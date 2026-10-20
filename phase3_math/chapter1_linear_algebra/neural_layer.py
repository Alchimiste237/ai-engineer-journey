# Simulate a single neural network layer from scratch
import numpy as np
def neural_layer(X, W, b, activation="relu"):
    """
    X: input  (n_samples × n_inputs)
    W: weights (n_inputs × n_outputs)
    b: biases  (n_outputs,)
    """
    # Linear transformation (matrix multiply + bias)
    z = X @ W + b

    # Activation function
    if activation == "relu":
        return np.maximum(0, z)    # ReLU: max(0, x)
    elif activation == "sigmoid":
        return 1 / (1 + np.exp(-z))
    elif activation == "linear":
        return z
    return z

# 3 samples, 4 input features
X = np.array([
    [1.0, 2.0, 3.0, 4.0],
    [0.5, 1.5, 2.5, 3.5],
    [2.0, 0.5, 1.0, 2.5]
])
# Weight matrix: 4 inputs → 3 outputs
W = np.random.randn(4, 3) * 0.1
b = np.zeros(3)

output = neural_layer(X, W, b, activation="relu")
print("Input shape:", X.shape)       # (3, 4)
print("Weight shape:", W.shape)      # (4, 3)
print("Output shape:", output.shape) # (3, 3)
