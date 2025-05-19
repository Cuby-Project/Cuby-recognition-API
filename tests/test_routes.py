import os
import pytest
from app import create_app
from contextlib import ExitStack

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

def test_cube_string_api_with_missing_files(client):
    response = client.post('/cubeFacesToCubeString', data={})
    assert response.status_code == 400

def test_cube_string_api_with_dummy_images(client):
    filepaths = [f'tests/images/dummy.jpg'] * 6
    filenames = [f'face{i}.jpg' for i in range(1, 7)]
    with ExitStack() as stack:
        files = [stack.enter_context(open(fp, 'rb')) for fp in filepaths]
        data = {
            'images': [(file, name) for file, name in zip(files, filenames)]
        }
        response = client.post('/cubeFacesToCubeString', data=data, content_type='multipart/form-data')
        assert response.status_code == 200
        assert b'cube_string' in response.data

def test_cube_string_api_with_not_enough_images(client):
    # Envoie moins de 6 images
    data = [
        ('images', (open('tests/images/dummy.jpg', 'rb'), f'face{i}.jpg'))
        for i in range(1, 4)
    ]
    response = client.post('/cubeFacesToCubeString', data=dict(data), content_type='multipart/form-data')
    assert response.status_code == 400
    assert b'Exactly 6 images required' in response.data