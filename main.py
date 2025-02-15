import os

from keras.layers import Conv2D

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
import tensorflow as tf


def make_model(input_shape):
    model = Sequential()

    # model.add(Flatten(input_shape=input_shape))
    # model.add(Dense(units=128, activation="relu"))
    # model.add(Dense(units=64, activation="relu"))
    # model.add(Dense(units=12, activation="softmax"))

    model.add(Conv2D(filters=4, kernel_size=(3,3), activation="relu", input_shape=input_shape))
    model.add(Conv2D(filters=4, kernel_size=(3,3), activation="relu",))
    model.add(Conv2D(filters=8, kernel_size=(3,3), activation="relu",))
    model.add(Conv2D(filters=8, kernel_size=(3,3), activation="relu",))
    model.add(Conv2D(filters=16, kernel_size=(3,3), activation="relu",))
    model.add(Conv2D(filters=16, kernel_size=(3,3), activation="relu",))
    model.add(Conv2D(filters=32, kernel_size=(3,3), activation="relu",))
    model.add(Conv2D(filters=32, kernel_size=(3,3), activation="relu",))
    model.add(Conv2D(filters=64, kernel_size=(3,3), activation="relu",))
    model.add(Conv2D(filters=64, kernel_size=(3,3), activation="relu",))
    model.add(Conv2D(filters=128, kernel_size=(3,3), activation="relu",))
    model.add(Conv2D(filters=128, kernel_size=(3,3), activation="relu",))
    model.add(Flatten())
    model.add(Dense(units=256, activation="relu"))
    model.add(Dense(units=12, activation="softmax"))

    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

    return model


def main():

    checkpoint_path = "data/model_checkpoint"

    input_directory = "data/"

    #flow_images_from_directory
    image_generator = ImageDataGenerator()
    train_generator = image_generator.flow_from_directory(input_directory+"train/", target_size=(96,96), batch_size=256, class_mode="binary")
    test_generator = image_generator.flow_from_directory(input_directory+"test/", target_size=(96,96), batch_size=256, class_mode="binary", shuffle=False)

    output_directory = ""
    input_shape = (96, 96, 3)
    model = make_model(input_shape)

    checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath=checkpoint_path,
        save_weights_only=True,
        monitor="val_accuracy",
        mode="max",
        save_best_only=True
    )

    history = model.fit(train_generator,
                        steps_per_epoch=len(train_generator),
                        validation_data=test_generator,
                        validation_steps=len(test_generator),
                        callbacks=[checkpoint_callback],
                        epochs=5)


if __name__ == "__main__":
    main()