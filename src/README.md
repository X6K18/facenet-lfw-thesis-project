# 🧩 Source Code Directory

This folder contains the **core source code** of the Face Recognition System.

---

## 📚 Purpose

The `src/` directory is responsible for:

* Implementing data processing pipelines
* Defining model architectures
* Training and evaluation logic
* Providing reusable utilities for the system

---

## 📂 Structure

```bash
src/
│
├── config/        # Configuration files
├── data/          # Data loading & preprocessing
├── models/        # Model definitions & training
├── evaluation/    # Metrics & evaluation logic
├── utils/         # Helper functions
```

---

## 🧠 Module Overview

### 🔹 `config/`

* Stores configuration settings:

  * Paths (data, models)
  * Hyperparameters
  * Training settings

---

### 🔹 `data/`

* Handles data-related operations:

  * Load dataset (LFW)
  * Preprocessing (resize, normalize)
  * Data augmentation

---

### 🔹 `models/`

* Defines and trains models:

  * FaceNet128
  * FaceNet512
  * MLP classifier

---

### 🔹 `evaluation/`

* Model evaluation:

  * Accuracy, Precision, Recall
  * FAR / FRR calculation
  * Visualization tools

---

### 🔹 `utils/`

* Utility functions:

  * Face detection
  * Face alignment
  * Embedding extraction
  * Logging

---

## 🔁 Core Pipeline

```id="pipeline1"
Image → Face Detection → Alignment → Embedding → Classification
```

---

## ⚙️ Technologies Used

* TensorFlow / Keras
* OpenCV
* DeepFace
* Scikit-learn
* NumPy / Pandas

---

## 🚀 How to Use

Example workflow:

```python
# Load and preprocess data
from src.data.load_data import load_dataset

# Train model
from src.models.train import train_model

# Evaluate model
from src.evaluation.metrics import evaluate
```

---

## ⚠️ Notes

* This folder contains **production-ready logic** (unlike notebooks used for experimentation)
* Code is modularized for scalability and maintainability
* Avoid hardcoding paths; use config files instead

---

## 📌 Best Practices

* Keep functions small and reusable
* Separate training and inference logic
* Use logging for debugging
* Maintain clean code structure

---

## 🎯 Role in Project

The `src/` folder is the **core backbone** of the system:

* 🧠 Model development
* ⚙️ System logic
* 🔄 Data processing pipeline
* 🌐 Backend integration

---

## 👨‍💻 Author

* Student: *[Your Name]*
* Project: Face Recognition System using FaceNet

---

## 📅 Version

* Last updated: 2026
