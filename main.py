import numpy
import pytesseract
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

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plt.imshow(gray_image)
    plt.axis('off')
    plt.show()

    # Thresholding
    _, thresholded_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

    # Save the preprocessed image
    cv2.imwrite("preprocessed_card.jpg", thresholded_image)


    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # Perform OCR on the preprocessed image
    text = pytesseract.image_to_string(Image.open("preprocessed_card.jpg"))

    print("Extracted Text:")
    print(text)
    # Release the camera
    camera.release()

    #print("Hello World!")

take_pic()