# 🎨 Cuby Recognition API

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/Cuby-Project/Cuby-recognition-API.svg)](https://github.com/Cuby-Project/Cuby-recognition-API/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Cuby-Project/Cuby-recognition-API.svg)](https://github.com/Cuby-Project/Cuby-recognition-API/network)
[![GitHub issues](https://img.shields.io/github/issues/Cuby-Project/Cuby-recognition-API.svg)](https://github.com/Cuby-Project/Cuby-recognition-API/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/Cuby-Project/Cuby-recognition-API.svg)](https://github.com/Cuby-Project/Cuby-recognition-API/commits/main)

</div>

## 📝 Description

A Flask API that receives 6 centered images of a scrambled Rubik's Cube and returns the cube string (color layout) by detecting each sticker's color using OpenCV and a trained KNN model in HSV space.

## 🔗 Related Projects

- [Cuby Client](https://github.com/Cuby-Project/Cuby-Client) - Main desktop application
- [Cuby Mobile App](https://github.com/Cuby-Project/Cuby-mobile-app) - Mobile version
- [Cuby Solve API](https://github.com/Cuby-Project/Cuby-solve-API) - Cube solving algorithm API
- [Cuby Capture API](https://github.com/Cuby-Project/Cuby-capture-API) - Cube state capture API
- [Cuby Capture Website](https://github.com/Cuby-Project/Cuby-capture-website) - Web interface

## ✨ Features

- 📷 Color detection from HSV-processed images
- 🤖 KNN classifier trained on HSV color samples
- 🧪 Full test suite: unit, integration
- 🐳 Docker-ready + GitHub Actions CI/CD
- 🔄 Real-time color recognition
- 📊 High accuracy color detection

## 🚀 Setup

### 🔧 Requirements

- Python 3.10+
- OpenCV
- Flask
- Scikit-learn

### 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/Cuby-Project/Cuby-recognition-API.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Generate and train color model:

```bash
make train
```

This runs:

- `generate_synthetic_dataset.py`: generates HSV data for W, Y, R, O, B, G
- `train_color_model.py`: trains and saves a KNN classifier

## 🌐 API Usage

### Endpoint: `/cubeFacesToCubeString`

**Method**: `POST`
**Content-Type**: `multipart/form-data`

**Fields**: Upload 6 images named exactly:

- `face1`, `face2`, `face3`, `face4`, `face5`, `face6`

**Returns**:

```json
{
  "cube_string": "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
}
```

Optional (if solver is included):

```json
{
  "cube_string": "...",
  "solution": "R U R' U'"
}
```

## 🧪 Testing

### Unit & Integration Tests

```bash
make test
```

### Coverage Report

```bash
make coverage
```

### Docker Test

```bash
make docker-test
```

## 🐳 Docker

### Build the Image

```bash
docker build -t rubik-api .
```

### Run the API

```bash
docker run -p 5000:5000 rubik-api
```

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- [Report a bug](https://github.com/Cuby-Project/Cuby-recognition-API/issues/new/choose)
- [Request a feature](https://github.com/Cuby-Project/Cuby-recognition-API/issues/new/choose)
