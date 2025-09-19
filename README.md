# Cartoon Face

This project is an **AI-powered cartoonization system** that transforms human face images into cartoon-style representations using deep learning models.

## 📂 Project Structure

- `main.py` → Entry point to run the application (Flask/Django based).  
- `model.py` → Handles model loading and prediction logic.  
- `my_model.h5` → Trained deep learning model for cartoonization.  
- `Model/ayur_model.h5` → Additional trained model variant.  
- `static/` → Contains images, styles, and outputs.  
  - `original/` → Original input images.  
  - `Output/` → Cartoonized output images.  
  - `cartoon/` → Sample cartoon images.  
  - `style.css` → Web styling.  

## 🚀 Features

- Upload an image and get a **cartoonized version**.  
- Pre-trained models ensure high-quality transformation.  
- Web interface for easy interaction.  
- Organized storage for input, output, and style references.  

## ⚙️ Installation & Setup

1. Clone this repository or extract the zip file:
   ```bash
   git clone <repo-url>
   cd cartoon_01
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

4. Open the app in your browser at:
   ```
   http://127.0.0.1:5000/
   ```

## 🖼️ Example Workflow

1. Place your image in the `static/original/` folder or upload via UI.  
2. Run the application.  
3. The cartoonized image will be saved in `static/Output/`.  

## 📌 Requirements

- Python 3.7+  
- TensorFlow / Keras  
- Flask (or Django, depending on implementation)  
- OpenCV  
- NumPy  

## ✨ Future Improvements

- Add multiple cartoon styles.  
- Improve UI with real-time preview.  
- Deploy as a web service or mobile app.  

---

👨‍💻 Developed as an AI project for **face cartoonization** using deep learning.
