import streamlit as st
import torch
from torchvision import transforms, models
from PIL import Image

# Device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Transforms (must match training)
transform = transforms.Compose([
    transforms.Resize((128,128)),
    transforms.ToTensor(),
    transforms.ConvertImageDtype(torch.float)
])

# Load class names
with open("classname.txt", "r") as f:
    class_names = [line.strip() for line in f]

# Rebuild the GoogLeNet model (must match training architecture)
num_classes = len(class_names)
model = models.googlenet(weights=None, aux_logits=False)   # no pretrained weights
model.fc = torch.nn.Linear(model.fc.in_features, num_classes)

# Load trained weights
model.load_state_dict(torch.load("model_state.pth", map_location=device))
model.to(device)
model.eval()

# Prediction function
def predict_image(image: Image.Image):
    image = image.convert("RGB")
    img_t = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(img_t)
        _, predicted = torch.max(outputs, 1)
    return class_names[predicted.item()]

# ------------------- STREAMLIT APP -------------------

st.title("🌱 Bean Leaf Disease Classifier")
st.write("Upload a leaf image to detect the disease : [Angular Leaf Spot ,Bean Rust ,Healthy Leaf]")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Predict"):
        prediction = predict_image(image)
        st.success(f"✅ Predicted Disease: **{prediction}**")

