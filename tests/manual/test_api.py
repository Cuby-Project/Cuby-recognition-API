import requests
import os

def test_api():
    url = 'http://localhost:5000/cubeFacesToCubeString'
    
    image_files = [
        'tests/images/up.png',
        'tests/images/right.png',
        'tests/images/front.png',
        'tests/images/down.png',
        'tests/images/left.png',
        'tests/images/back.png'
    ]
    
    for img_file in image_files:
        if not os.path.exists(img_file):
            print(f"Erreur: Le fichier {img_file} n'existe pas")
            return
    
    files = []
    for img_file in image_files:
        files.append(('images', (os.path.basename(img_file), open(img_file, 'rb'), 'image/png')))
    
    try:
        response = requests.post(url, files=files)
        
        if response.status_code == 200:
            result = response.json()
            print("Succès! Réponse de l'API:")
            print(f"Cube string: {result.get('cube_string')}")
        else:
            print(f"Erreur: {response.status_code}")
            print(response.text)
    
    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion: {e}")
        assert False, f"API connection failed: {e}"
    
    finally:
        for _, (_, file, _) in files:
            file.close()

if __name__ == '__main__':
    test_api() 