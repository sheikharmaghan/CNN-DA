
# 🎗️ Cancer Prediction Using Decision Tree Classifier

## 📌 Project Overview
This project uses Machine Learning to predict cancer diagnosis using a Decision Tree Classification algorithm.

The model classifies cancer cases into two categories:
- **Benign (B):** Non-cancerous
- **Malignant (M):** Cancerous

The project includes Exploratory Data Analysis (EDA), data visualization, model training, testing, and prediction through a Streamlit web application.

## 📊 Dataset Information

- Dataset: Cancer Data
- Source: Kaggle
- Dataset Path: `Cancer_Data.csv`
- Target Column: `diagnosis`
- Features: Numerical characteristics of cell nuclei

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Removed unnecessary ID columns.
- Removed duplicate records.
- Handled missing values.
- Encoded diagnosis labels.
- Separated features and target variable.

## 📈 Exploratory Data Analysis (EDA)

The following visualizations were generated:

- Cancer Diagnosis Pie Chart
- Numerical Feature Histograms
- Correlation Heatmap
- Boxplots for Outlier Detection
- Benign vs Malignant Count Plot

## 🤖 Machine Learning Algorithm

**Decision Tree Classifier**

Model Configuration:
- Algorithm: Decision Tree
- Criterion: Gini
- Maximum Depth: 5
- Random State: 42

## 📂 Train-Test Split

The dataset was divided into:

| Dataset | Percentage |
|---|---:|
| Training Data | 80% |
| Testing Data | 20% |

The model was trained using 80% of the dataset and evaluated using the remaining 20%.

## 📊 Model Evaluation

The model was evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report

Actual performance results are generated when the notebook is executed.

## 📁 Project Structure

```text
Cancer-Prediction/
│
├── app.py
├── cancer_decision_tree_model.pkl
├── requirements.txt
└── README.md
```

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

## 🚀 Installation and Setup

### 1. Clone Repository

```bash
git clone https://github.com/YOUR-USERNAME/Cancer-Prediction.git
```

### 2. Open Project Folder

```bash
cd Cancer-Prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Streamlit Application

```bash
streamlit run app.py
```

## 🌐 Deployment

This project can be deployed using Streamlit Community Cloud.

1. Upload project files to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub repository.
4. Select `app.py` as the main file.
5. Click Deploy.

## 🎯 Project Objectives

- Analyze cancer dataset using EDA.
- Visualize cancer diagnosis distribution.
- Train a Decision Tree Classification model.
- Evaluate model performance using 80/20 splitting.
- Build an interactive cancer prediction application.

## ⚠️ Disclaimer

This project is developed for educational and machine learning purposes only. Predictions are not a substitute for professional medical diagnosis.

## 👨‍💻 Author

Machine Learning Project

**Cancer Prediction Using Decision Tree Classifier**
