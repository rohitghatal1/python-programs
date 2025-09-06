import tensorflow as tf
from tensorflow.keras import datasets, layers, models

# 1. Load dataset
(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()

# Flatten 28x28 images into 784-dimensional vectors
x_train = x_train.reshape((x_train.shape[0], 28*28)).astype("float32") / 255
x_test = x_test.reshape((x_test.shape[0], 28*28)).astype("float32") / 255

# 2. Build ANN model
model = models.Sequential([
    layers.Dense(128, activation='relu', input_shape=(784,)),  # hidden layer
    layers.Dense(64, activation='relu'),                      # hidden layer
    layers.Dense(10, activation='softmax')                    # output layer
])

# 3. Compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 4. Train model
model.fit(x_train, y_train, epochs=5, batch_size=64, validation_split=0.1)

# 5. Evaluate model
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"Test accuracy: {test_acc:.4f}")
