# 🤖 Models Directory

This folder contains all **trained models** and related files used in the Face Recognition System.

---

## 📚 Purpose

The `models/` directory is responsible for storing:

* Pretrained FaceNet models
* Trained classification models
* Feature scaling objects
* Serialized model weights for deployment

---

## 📂 Structure

Typical contents include:

* `facenet128_model.h5`
  → FaceNet model with 128-dimensional embeddings

* `facenet512_model.h5`
  → FaceNet model with 512-dimensional embeddings

* `mlp_classifier.pkl`
  → Trained Multilayer Perceptron classifier

* `scaler.pkl`
  → Data scaler used before classification

* `README.md`
  → Documentation for this folder

---

## 🧠 Model Overview

### 🔹 FaceNet Models

Used for feature extraction:

* Convert face images into embedding vectors
* Two variants:

  * 128-d (faster, lighter)
  * 512-d (more accurate, heavier)

---

### 🔹 Classifier

* Input: Face embeddings
* Output: Identity label

Common choices:

* MLP (used in this project)
* SVM (optional alternative)

---

## 🔁 Workflow

```id="flow1"
Image → FaceNet → Embedding → Classifier → Prediction
```

---

## 💾 Model Format

* `.h5` → Keras/TensorFlow models
* `.pkl` → Scikit-learn models (pickle)

---

## ⚠️ Notes

* Large model files may NOT be included in the repository
* Use `.gitignore` to avoid pushing heavy files

Example:

```id="gitignore1"
models/*
!models/README.md
```

---

## 🚀 How to Use

### Load FaceNet model:

```python id="code1"
from tensorflow.keras.models import load_model

model = load_model("models/facenet128_model.h5")
```

---

### Load classifier:

```python id="code2"
import pickle

with open("models/mlp_classifier.pkl", "rb") as f:
    clf = pickle.load(f)
```

---

## 📊 Training Source

Models are trained using:

* Dataset: Labeled Faces in the Wild (LFW)
* Pipeline:

  * Face Detection
  * Alignment
  * Embedding extraction
  * Classification

---

## 🔒 Versioning

* Models should be versioned if updated
* Example naming:

```id="ver1"
facenet128_v1.h5
facenet128_v2.h5
```

---

## 📌 Role in Project

This folder is essential for:

* 🧠 Inference (prediction)
* 🌐 Backend API
* 💻 Application deployment
* 🎥 Real-time face recognition

---

## 👨‍💻 Author

* Student: *[Your Name]*
* Project: Face Recognition System using FaceNet

---

## 📅 Version

* Last updated: 2026
