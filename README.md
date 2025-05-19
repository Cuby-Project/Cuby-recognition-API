# 🧊 Rubik's Cube Color Detection API (Flask + KNN + OpenCV)

A Flask API that receives 6 centered images of a scrambled Rubik's Cube and returns the cube string (color layout) by detecting each sticker's color using OpenCV and a trained KNN model in HSV space.

---

## 🚀 Features

- 📷 Color detection from HSV-processed images  
- 🤖 KNN classifier trained on HSV color samples  
- 🧪 Full test suite: unit, integration  
- 🐳 Docker-ready + GitHub Actions CI/CD  

---

## ⚙️ Setup

### 🔧 Requirements

- Python 3.10+  
- OpenCV  
- Flask  
- Scikit-learn  

### 🧪 Install dependencies

```bash
pip install -r requirements.txt
```

### 📊 Generate and train color model

```bash
make train
```

This runs:
- `generate_synthetic_dataset.py`: generates HSV data for W, Y, R, O, B, G
- `train_color_model.py`: trains and saves a KNN classifier

---

## 🌐 API Usage

### 🟩 Endpoint: `/api/solve`

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

---

## 🧪 Testing

### ✅ Unit & integration tests

```bash
make test
```

### 📈 Coverage report

```bash
make coverage
```

### 🐳 Docker test

```bash
make docker-test
```

---

## 🐳 Docker

### Build the image

```bash
docker build -t rubik-api .
```

### Run the API

```bash
docker run -p 5000:5000 rubik-api
```

---

## 🧪 Continuous Integration (GitHub Actions)

- All pushes and PRs to `main` will trigger tests via `.github/workflows/ci.yml`
- Test results and coverage are displayed in the GitHub Actions tab

---

## 📎 Example image input

Make sure each input image:

- Is 1 face of the cube
- Is cropped and centered
- Has clear and visible stickers (ideally under good lighting)

---

## 🙌 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to change.

---

## 🛡️ License

MIT License

---

## 🏗️ Status

![Build](https://github.com/your-username/your-repo-name/actions/workflows/ci.yml/badge.svg)
