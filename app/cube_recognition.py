import cv2
import numpy as np
from .color_detection import detect_colors

# Rubik's cube face labels in standard order
FACE_ORDER = ['U', 'R', 'F', 'D', 'L', 'B']


def generate_cube_string(images):
    cube_string = ''

    for i, img_file in enumerate(images):
        # Convert file stream to OpenCV image
        npimg = np.frombuffer(img_file.read(), np.uint8)
        image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        # Detect color of each of the 9 stickers
        face_colors = detect_colors(image)

        # Append to full cube string
        cube_string += ''.join(face_colors)

    return cube_string
