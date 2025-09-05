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
│── Bean_leaf_model.ipynb # Model build on Google Colab

---


---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/Gaurav-S-c/Bean_leaf-disease-classification.git
cd Bean_leaf-disease-classification
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the Streamlit App
```bash
streamlit run app.py
```

---

## 🧠 Model Details

- **Architecture**: GoogLeNet (`torchvision.models.googlenet`)  
- **Approach**: Transfer Learning — replaced the final fully-connected layer and trained on 3 custom classes  
- **Input Size**: 128 × 128 pixels  
- **Dataset**: ~1,200 images (balanced, ~400 per class)  
- **Training Environment**: Google Colab with PyTorch  

---

## 📌 Requirements

Main dependencies:  
- **torch**  
- **torchvision**  
- **streamlit**  
- **Pillow**  

👉 For the complete list, see [`requirements.txt`](requirements.txt).

---

## 🙌 Future Improvements

- 🔼 Train on larger, more diverse datasets  
- 🌍 Deploy on Streamlit Cloud / Hugging Face Spaces  
- 📱 Build a mobile-friendly version  
- ⚡ Add more disease categories  

---

## 👨‍💻 Author
**Gaurav Sinha**


