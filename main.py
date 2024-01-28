import numpy
import cv2
import matplotlib.pyplot as plt
from PIL import Image

def take_pic():
    # Initialize the camera
    camera = cv2.VideoCapture(0)  # '0' represents the default camera (usually the built-in webcam)

    # Capture an image
    return_value, image = camera.read()

    # Save the captured image to a file
    cv2.imwrite("baseball_card.jpg", image)

    rgb_frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display the image using matplotlib (for Jupyter notebooks)
    plt.imshow(rgb_frame)
    plt.axis('off')
    plt.show()
    # Release the camera
    camera.release()

    print("Hello World!")

