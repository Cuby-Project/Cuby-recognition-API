import pytest
from app.knn_classifier import classify_hsv_pixel

def test_knn_predict_known_colors():
    # Valeurs proches des moyennes entraînées
    test_samples = [
        ((0, 0, 255), 'W'),
        ((25, 255, 255), 'Y'),
        ((0, 255, 255), 'R'),
        ((15, 255, 255), 'O'),
        ((110, 255, 255), 'B'),
        ((60, 255, 255), 'G'),
    ]
    for hsv, expected in test_samples:
        assert classify_hsv_pixel(hsv) == expected

def test_knn_predict_invalid_input():
    # Test with invalid HSV tuple (wrong length)
    with pytest.raises(ValueError):
        classify_hsv_pixel((0, 255))  # Only 2 values

def test_knn_predict_out_of_range():
    # HSV values out of typical range
    result = classify_hsv_pixel((300, 500, 500))
    assert isinstance(result, str)
    assert result in ['W', 'Y', 'R', 'O', 'B', 'G']