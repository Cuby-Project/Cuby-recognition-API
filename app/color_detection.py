import cv2
import numpy as np
from app.knn_classifier import classify_hsv_pixel

def classify_color(hsv_pixel):
    return classify_hsv_pixel(hsv_pixel)


def detect_colors(image):
    height, width, _ = image.shape

    # Coordinates for 3x3 grid center points
    step_y = height // 4
    step_x = width // 4
    centers = [(step_y * i, step_x * j) for i in range(1, 4) for j in range(1, 4)]

    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    colors = []

    for y, x in centers:
        hsv_pixel = hsv_img[y, x]
        color = classify_color(hsv_pixel)
        colors.append(color)

    return colors
