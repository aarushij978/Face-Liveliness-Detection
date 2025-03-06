import tensorflow as tf
import os
import splitfolders
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Split dataset (80% Train, 20% Validation)
splitfolders.ratio("Dataset", "Dataset_Split", seed=42, ratio=(0.8, 0.2))

# Directories
train_dir = "Dataset_Split/train"
val_dir = "Dataset_Split/val"

# Image Augmentation
train_datagen = ImageDataGenerator(rescale=1./255, rotation_range=20, width_shift_range=0.1,
                                   height_shift_range=0.2, horizontal_flip=True, shear_range=0.2,
                                   zoom_range=0.2, fill_mode='nearest')

val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(train_dir, target_size=(150, 150), class_mode='binary')
val_generator = val_datagen.flow_from_directory(val_dir, target_size=(150, 150), class_mode='binary')

# CNN Model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPool2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPool2D(2,2),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPool2D(2,2),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPool2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile Model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train Model
model.fit(train_generator, epochs=50, validation_data=val_generator)

# Save Model
model.save("face_liveness_model.h5")
print("Model training completed and saved as face_liveness_model.h5")
