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

    # Release the camera
    camera.release()

    #print("Hello World!")

def extract_data():
    original_image = cv2.imread("test_back.jpg")
    
    #if original_image is None:
    #    print("Error: Unable to load the original image.")
    #else:
        #print("Original image loaded successfully.")

    roi_player_name = (565, 275, 590, 480)
    print("Original Image Shape:", original_image.shape)
    print("ROI Coordinates:", roi_player_name)

    # Verify coordinates
    if (
        0 <= roi_player_name[0] < roi_player_name[2] <= original_image.shape[1]
        and 0 <= roi_player_name[1] < roi_player_name[3] <= original_image.shape[0]
    ):

        print("Coordinates are valid.")
    else:
        print("Error: Invalid coordinates for cropping.")
    cropped_player_name = original_image[roi_player_name[1]:roi_player_name[3], roi_player_name[0]:roi_player_name[2]]
    cv2.imwrite("cropped_player_name.jpg", cropped_player_name)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # Perform OCR on the preprocessed image
    text = pytesseract.image_to_string(Image.open("cropped_player_name.jpg"))

    print("Extracted Text:")
    print(text)


extract_data()