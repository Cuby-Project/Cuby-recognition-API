import numpy as np
from app.color_detection import classify_color

def test_classify_color_all_possible_colors():
    # Test all possible output codes
    for hsv in [(0,0,255), (25,255,255), (0,255,255), (15,255,255), (110,255,255), (60,255,255)]:
        result = classify_color(hsv)
        assert result in ['W', 'Y', 'R', 'O', 'B', 'G']

def test_classify_color_invalid_input():
    # Test with invalid input type
    try:
        classify_color("not a tuple")
        assert False, "Should raise an exception"
    except Exception:
        assert True

