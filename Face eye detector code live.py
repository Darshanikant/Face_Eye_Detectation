import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Configure Streamlit app
st.set_page_config(page_title="Face & Eye Detector", layout="centered")
st.title("Face & Eye Detector App 👁️‍🗨️")
st.write("Upload an image to detect faces and eyes using Haar cascades.")

# Load Haar cascades
face_classifier = cv2.CascadeClassifier(r"C:\Users\sunil\DK\vs code\Deap Learning\Work\FACE AND EYE DETECTOR APP\haarcascade_frontalface_default.xml")
eye_classifier = cv2.CascadeClassifier(r"C:\Users\sunil\DK\vs code\Deap Learning\Work\FACE AND EYE DETECTOR APP\haarcascade_eye.xml")

# Check if cascade files are loaded
if face_classifier.empty() or eye_classifier.empty():
    st.error("Error: Haar cascade file not loaded. Check the file path.")
    st.stop()

# Function for face and eye detection
def detect_faces_and_eyes(image):
    img = np.array(image.convert("RGB"))  # Convert PIL Image to numpy array
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_classifier.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)
    return img

# Upload image
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display uploaded image
    input_image = Image.open(uploaded_file)
    st.image(input_image, caption="Uploaded Image", use_column_width=True)

    # Process image
    with st.spinner("Processing..."):
        output_image = detect_faces_and_eyes(input_image)
        st.image(output_image, caption="Processed Image", use_column_width=True)
        st.success("Face & Eye detection completed!")
