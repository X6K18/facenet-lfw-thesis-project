# 📓 Notebooks Directory

This folder contains Jupyter Notebooks used for **experimentation, analysis, and model development** in the Face Recognition System project.

---

## 📚 Purpose

The notebooks are designed to:

* Explore and understand the dataset
* Perform preprocessing and feature extraction
* Train and evaluate FaceNet-based models
* Visualize results and performance metrics

---

## 📂 Structure

The main notebooks include:

### 1. `01_exploration.ipynb`

* Dataset exploration (LFW)
* Number of identities and images
* Distribution analysis
* Data visualization

---

### 2. `02_preprocessing.ipynb`

* Face detection (MTCNN / RetinaFace)
* Face alignment (landmarks: eyes, nose, mouth)
* Image resizing (160x160)
* Data cleaning and normalization

---

### 3. `03_training.ipynb`

* Extract embeddings using:

  * FaceNet128
  * FaceNet512
* Train classifier:

  * Multilayer Perceptron (MLP)
* Save trained models

---

### 4. `04_evaluation.ipynb`

* Evaluate model performance using:

  * Accuracy
  * Precision
  * Recall
  * FAR (False Acceptance Rate)
  * FRR (False Rejection Rate)
* Generate:

  * Confusion matrix
  * ROC curve
  * Precision-Recall curve

---

## 🔁 Workflow

Typical workflow across notebooks:

```
Exploration → Preprocessing → Training → Evaluation
```

---

## 🧠 Models Used

* FaceNet (128-dimensional embedding)
* FaceNet (512-dimensional embedding)
* MLP classifier

---

## 📊 Outputs

The notebooks generate:

* Processed datasets
* Embedding vectors
* Trained models
* Evaluation reports
* Visualization charts

---

## ⚠️ Notes

* Notebooks are for **research and experimentation only**
* Production code is implemented in the `src/` directory
* Some outputs (large files) may not be included in the repository

---

## 🚀 How to Run

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Launch Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

3. Run notebooks in order:

   * `01 → 02 → 03 → 04`

---

## 📌 Recommendations

* Use a GPU environment (Google Colab recommended) for faster training
* Avoid running all cells at once without verifying outputs
* Save intermediate results (embeddings, models) for reuse

---

## 🎯 Role in Project

This folder plays a critical role in:

* 📊 Experimental validation
* 🧪 Model comparison (FaceNet128 vs FaceNet512)
* 📈 Supporting results for thesis/report

---

## 👨‍💻 Author

* Student: *[Your Name]*
* Project: Face Recognition System using FaceNet

---

## 📅 Version

* Last updated: 2026
