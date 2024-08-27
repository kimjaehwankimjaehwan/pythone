import tensorflow as tf
def getNetwork():
  flatten = tf.keras.layers.Flatten(input_shape=(28, 28))
  dense1 = tf.keras.layers.Dense(200, activation='relu')
  dense2 = tf.keras.layers.Dense(100, activation='relu')
  dense3 = tf.keras.layers.Dense(50, activation='relu')
  drop1 = tf.keras.layers.Dropout(0.2)
  dense4 = tf.keras.layers.Dense(10, activation='softmax')
  model = tf.keras.Sequential([flatten, dense1, dense2,dense3,drop1,dense4])
  model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
  return model