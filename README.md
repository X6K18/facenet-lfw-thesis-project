# 🎓 Face Recognition System using FaceNet and LFW Dataset

## 📌 Introduction

This project presents a complete **Face Recognition System** built using deep learning techniques, specifically the **FaceNet model**, and evaluated on the **Labeled Faces in the Wild (LFW)** dataset.

The system is designed to simulate real-world applications such as:

* Access control systems
* Attendance tracking
* Identity verification

---

## 🎯 Objectives

* Implement and evaluate FaceNet-based face recognition
* Compare two embedding variants:

  * FaceNet128 (128-dimensional)
  * FaceNet512 (512-dimensional)
* Analyze the impact of embedding size on:

  * Accuracy
  * Speed
  * System performance
* Build a complete system including:

  * Model training
  * Backend API
  * Web and desktop applications
  * Real-time recognition

---

## 🧠 Technologies Used

* TensorFlow / Keras
* OpenCV
* DeepFace
* Scikit-learn
* Flask (Backend API)
* React (Frontend Web)
* Tkinter (Desktop App)

---

## 📊 Dataset

* Dataset: Labeled Faces in the Wild (LFW)
* Contains thousands of face images collected in unconstrained environments
* Used for training and evaluating face recognition models

⚠️ Note: Dataset is not included in this repository due to size limitations.

---

## 🏗️ System Architecture

```id="arch1"
Image → Face Detection → Alignment → FaceNet → Embedding → Classifier → Output
```

### Components:

* Face Detection: MTCNN / RetinaFace
* Feature Extraction: FaceNet
* Classification: MLP
* Deployment:

  * Flask API
  * Web UI
  * Desktop App
  * Real-time Webcam

---

## 🔁 Workflow

```id="workflow1"
Data → Preprocessing → Training → Evaluation → Deployment
```

---

## 📁 Project Structure

```bash id="struct1"
├── data/          # Dataset (not included)
├── notebooks/     # Experiments & analysis
├── src/           # Core source code
├── models/        # Trained models
├── backend/       # Flask API
├── frontend/      # Web + Desktop app
├── realtime/      # Webcam recognition
├── reports/       # Results & evaluation
├── logs/          # System logs
├── documents/     # Thesis & documentation
```

---

## 🧪 Model Evaluation

The system is evaluated using:

* Accuracy
* Precision
* Recall
* FAR (False Acceptance Rate)
* FRR (False Rejection Rate)

---

## 📈 Key Findings

* FaceNet512 generally provides higher accuracy
* FaceNet128 offers faster inference
* Trade-off exists between performance and computational cost

---

## 🚀 Features

* 📷 Face recognition from images
* 🎥 Real-time webcam recognition
* 🌐 Web-based interface
* 💻 Desktop application
* 📊 Performance evaluation and visualization

---

## ⚙️ Installation

```bash id="install1"
git clone https://github.com/your-username/your-repo.git
cd your-repo
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run Backend

```bash id="run1"
cd backend
python app.py
```

---

### Run Web App

```bash id="run2"
cd frontend/web
npm install
npm start
```

---

### Run Desktop App

```bash id="run3"
cd frontend/app
python main.py
```

---

## ⚠️ Notes

* Large files (dataset, models) are excluded from GitHub
* Please refer to `data/README.md` for dataset setup
* Use GPU for faster training (recommended)

---

## 📌 Future Improvements

* Face anti-spoofing
* Mobile application (Flutter)
* Model optimization (quantization)
* Cloud deployment

---

## 👨‍💻 Author

* Student: *[Your Name]*
* Major: Information Technology / AI
* Project: Face Recognition System using FaceNet

---

## 📅 Version

* Last updated: 2026

---

## ⭐ Acknowledgements

* FaceNet model
* LFW dataset
* Open-source libraries and frameworks
