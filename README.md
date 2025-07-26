# ♻️ Smart Waste Classifier

An AI-powered waste classification app built using Streamlit and PyTorch.  
It allows users to upload or capture images of waste materials and instantly classifies them into one of the following categories:

- ✅ Biodegradable
- ♻️ Recyclable
- 🚫 Non-Recyclable

### 🚀 Features

- 📸 Upload or capture images using webcam (mobile-friendly)
- 🧠 Trained deep learning model using MobileNetV2
- 🔍 Real-time classification
- 🗣️ Optional voice output using text-to-speech (desktop only)
- 🎨 Clean and responsive UI with Streamlit
- 📱 Fully optimized for mobile and desktop devices

---

### 🛠️ Technologies Used

- Python 3.13.5
- Streamlit
- PyTorch & TorchVision
- Pillow
- pyttsx3 (text-to-speech)

---

### 💡 How It Works

1. Upload or take a picture of the waste item.
2. The model processes the image and predicts the waste type.
3. Optionally, the app can speak the classification result out loud (on desktop).

---

### 📦 Setup Instructions

```bash
git clone https://github.com/your-username/smart-waste-classifier.git
cd smart-waste-classifier
pip install -r requirements.txt
streamlit run app.py
