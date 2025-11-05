# 🍌 Banana Ripeness Predictor

This project predicts the ripeness stage of a banana — **Unripe, Ripe, Overripe, or Rotten** — using a **Convolutional Neural Network (CNN)** trained on image data.  
It also includes a **Streamlit web app** for easy testing and visualization.


## 🚀 Features

- Classifies banana images into 4 stages:
  - 🍏 Unripe  
  - 🍌 Ripe  
  - 🍂 Overripe  
  - 💀 Rotten  
- Built using **TensorFlow**, **Keras**, and **Streamlit**  
- Simple UI for image upload and prediction  
- Easy to train, run, and modify  


## 🧠 Model Overview

The CNN model was trained using TensorFlow and Keras with the following configuration:

- Input image size: 128 × 128  
- Layers: Conv2D, MaxPooling, Flatten, Dense  
- Activation: ReLU (hidden layers), Softmax (output layer)  
- Optimizer: Adam  
- Loss: Categorical Crossentropy  
- Validation Accuracy: ~93%


## 📁 Project Files

- `fresh_bananas.ipynb` → Jupyter Notebook used for model training  
- `app_streamlit.py` → Streamlit app for user interface and prediction  


## ⚙️ How to Run Locally

1. Clone the repository:
git clone https://github.com/YashBansal9/banana-ripeness-predictor.git

cd banana-ripeness-predictor

2. Install dependencies:
pip install tensorflow streamlit pillow numpy matplotlib
3. Run the app:
streamlit run app_streamlit.py

## 📸 Dataset

Dataset used: [Banana Classification Dataset on Kaggle](https://www.kaggle.com/datasets/atrithakar/banana-classification/data)  
The dataset contains images of bananas categorized into:
- Unripe  
- Ripe  
- Overripe  
- Rotten  

## 🌐 Connect with Me

👤 **Yash Bansal**  
📍 BCA Student @Msi, Delhi | Data Science Enthusiast  
🔗 [LinkedIn](https://www.linkedin.com/in/yashbansal28/)  
🐙 [GitHub](https://github.com/YashBansal9)


## 📝 Acknowledgments

- Dataset credits to the original author on Kaggle.  
- Feel free to reuse and modify this project for learning and portfolio purposes.  
- If you use this project, consider giving it a ⭐ on GitHub!

