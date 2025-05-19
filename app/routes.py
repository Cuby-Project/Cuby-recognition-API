from flask import Blueprint, request, jsonify
from .cube_recognition import generate_cube_string

main = Blueprint('main', __name__)

@main.route('/cubeFacesToCubeString', methods=['POST'])
def upload_faces():
    if 'images' not in request.files:
        return jsonify({'error': 'No images part'}), 400

    images = request.files.getlist('images')

    if len(images) != 6:
        return jsonify({'error': 'Exactly 6 images required'}), 400

    try:
        cube_string = generate_cube_string(images)
        return jsonify({'cube_string': cube_string})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
