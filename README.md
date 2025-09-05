# 🌱 Bean Leaf Disease Classifier

A deep learning–based web app built with **PyTorch** and **Streamlit** to classify bean leaf images into three categories:

- **Angular Leaf Spot**  
- **Bean Rust**  
- **Healthy Leaf**

This tool can help farmers and researchers quickly identify common bean leaf diseases from simple images.

---

## 🌍 Live Demo
🔗 [Bean Leaf Classifier Web App](https://plant-disease-classification-prototype.streamlit.app/)

---

## ⚙️ Features
- 🧠 Transfer Learning with **GoogLeNet**
- 🎯 Fine-tuned on a custom dataset of bean leaves (~1,200 images, ~400 per class)
- 📸 Upload leaf images directly through the app
- ✅ Predicts the disease class with confidence
- ⚡ Easy to run locally or deploy on Streamlit Cloud

---

## 📂 Project Structure
bean-leaf-classifier/
│── app.py # Streamlit app
│── classname.txt # List of class names
│── model_state.pth # Trained model weights
│── requirements.txt # Python dependencies
│── README.md # Project documentation
│── project_3.ipynb # Model build on Google Colab

---


---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/Sinha-Saurav/bean-leaf-classifier.git
cd bean-leaf-classifier
### 2. Install Dependencies
pip install -r requirements.txt
### 3. Run the Streamlit App
streamlit run app.py
