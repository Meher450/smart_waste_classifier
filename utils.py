# utils.py

import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import pyttsx3

# Preprocessing function
def preprocess_image(image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0)

# Load model
@torch.no_grad()
def load_model(path="waste_classifier.pth"):
    model = models.mobilenet_v2(pretrained=False)
    model.classifier[1] = torch.nn.Linear(model.last_channel, 3)
    model.load_state_dict(torch.load(path, map_location=torch.device("cpu")))
    model.eval()
    return model

# Predict
def predict(model, image_tensor, class_names=["biodegradable", "non_recyclable", "recyclable"]):
    outputs = model(image_tensor)
    _, pred = torch.max(outputs, 1)
    return class_names[pred.item()]

# Text-to-speech
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 160)
    engine.say(text)
    engine.runAndWait()
