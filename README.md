# Face-Liveliness-Detection
Face Liveness Detection – A real-time deep learning-based system to detect spoofing attacks (photos, videos, deepfakes) using a webcam. Built with TensorFlow, OpenCV, MobileNetV3, and trained on CelebA-Spoof. Runs locally for privacy-focused authentication.

# Face Liveness Detection – Browser-Based & Real-Time

## **A machine learning-powered face liveness detection system** designed to distinguish between real faces and spoof attacks (like photos, videos, and masks) using deep learning. This project runs **in real-time** using a webcam and is optimized for **browser-based applications** with TensorFlow.js.

---

## **📌 Features**
✅ **Real-Time Liveness Detection** – Uses a webcam to detect if a face is real or spoofed.  
✅ **Deep Learning-Based Model** – Trained using CNNs (MobileNetV3) for lightweight and efficient performance.  
✅ **Handles Spoofing Attacks** – Detects printed photos, replayed videos, and deepfake attempts.  
✅ **Optimized for Web Applications** – Can be integrated into browser-based authentication systems.  
✅ **Privacy-Focused** – Runs locally on the device without sending data to external servers.  

---

## **🛠️ Tech Stack**
- **Python** (TensorFlow, OpenCV, NumPy)  
- **Deep Learning Models** (MobileNetV3, EfficientNet)  
- **Dataset** – [CelebA Spoof](https://www.kaggle.com/attentionlayer241/celeba-spoof-for-face-antispoofing)  
- **Frontend (Optional for Web Deployment)** – TensorFlow.js, WebRTC  

---

## **📂 Project Structure**
```
📁 FaceLivenessDetection
│── 📂 dataset/             # Training dataset (real vs spoofed faces)
│── 📂 models/              # Saved models (.h5 format)
│── 📂 scripts/
│   ├── extract_dataset.py  # Extracts and processes dataset
│   ├── train_model.py      # Trains the deep learning model
│   ├── liveness_test.py    # Runs live liveness detection using a webcam
│── 📜 README.md             # Project documentation
```

---

## **🚀 Setup & Installation**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/FaceLivenessDetection.git
cd FaceLivenessDetection
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Extract and Process Dataset**
```bash
python scripts/extract_dataset.py
```

### **4️⃣ Train the Model**
```bash
python scripts/train_model.py
```

### **5️⃣ Run Liveness Detection (Webcam)**
```bash
python scripts/liveness_test.py
```

Press **'q'** to exit the webcam window.

---

## **📊 Model Performance**
- Trained on **CelebA-Spoof** dataset  
- Achieved **over 95% accuracy** in classifying real vs spoof faces  
- Successfully detects **print, video, and deepfake attacks**  

---

## **🔗 Future Improvements**
- ✅ Improve deepfake detection with **GAN-based adversarial training**  
- ✅ Deploy as a **browser-based TensorFlow.js app** for online authentication  
- ✅ Enhance accuracy with **multi-frame analysis and eye blink detection**  
