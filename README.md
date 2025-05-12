# Ransomware_Detection
"Binary classification of PE files for malware detection using static analysis features from executable metadata."

<img src="https://github.com/rpjinu/Ransomware_Detection/blob/main/Ransomware_image.png">

# 🛡️ Malware Detection using PE File Static Analysis

Binary classification of PE files (.dll) to detect malware based on static metadata features.

---

## 📂 Dataset Overview

The dataset contains **static attributes** extracted from Portable Executable (PE) files, such as `.dll` libraries.  
These features are used to classify files as **Benign (1)** or **Malicious (0)**.

**Key Features:**
- `DebugSize`, `ExportSize`, `IatVRA`, `ResourceSize`, `SizeOfStackReserve`, etc.
- `BitcoinAddresses` — indicator of potential malicious intent.
- `Benign` (Target Variable):  
  `1 = Benign`, `0 = Malicious`

---

## ⚙️ Project Pipeline

1️⃣ **EDA (Exploratory Data Analysis)**  
2️⃣ **Data Preprocessing**  
3️⃣ **Feature Selection**  
4️⃣ **Model Building (Binary Classifier)**  
5️⃣ **Model Evaluation**  
6️⃣ *(Optional)* **Deployment (Streamlit / API)**

---

## 🛠️ Technologies Used

- Python 🐍  
- Libraries:  
  `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `xgboost`, `streamlit` *(optional)*

---

## 📊 Exploratory Data Analysis (EDA)

- Dataset shape, missing values, unique values
- Correlation heatmap
- Target (`Benign`) class distribution

---

## ✨ Feature Engineering

- Dropped non-informative columns: `FileName`, `md5Hash`, `BitcoinAddresses`
- Handled missing values (if any)
- Feature importance using **RandomForestClassifier**

---

## 🤖 Model Building

✅ Trained multiple classifiers:  
- RandomForestClassifier  
- XGBoostClassifier  
- LogisticRegression

✅ Evaluation Metrics:
- Accuracy ⚡
- Precision 🧐
- Recall 🛡️
- F1-Score 🎯
- ROC-AUC 📈

---

## 📈 Results

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| RandomForest | **xx%** | xx% | xx% | xx% |
| XGBoost | **xx%** | xx% | xx% | xx% |
| LogisticRegression | xx% | xx% | xx% | xx% |

*(Replace `xx%` with your actual results)*

---

## 🚀 How to Run the Project

```bash
# Clone the repo
git clone https://github.com/yourusername/your-repo.git
cd your-repo

# Install dependencies
pip install -r requirements.txt

# Run EDA script
python eda.py

# Train models
python model.py
