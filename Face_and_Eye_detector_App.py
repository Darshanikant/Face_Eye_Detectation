import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Configure Streamlit app
st.set_page_config(
    page_title="Face & Eye Detector",
    layout="wide",
    page_icon="👁️‍🗨️"
)
# Add background image via CSS
st.markdown("""
    <style>
        .stApp {
            background-image: url("https://d1sr9z1pdl3mb7.cloudfront.net/wp-content/uploads/2022/03/07162020/synthetic-data-1024x640.jpg");
            background-size: cover;
            background-position: center center;
            background-attachment: fixed;
            
        }
    </style>
""", unsafe_allow_html=True)
# Sidebar setup
st.sidebar.title("App Options")
st.sidebar.markdown("""
### Face & Eye Detector App
This app uses Haar cascades for detecting:
- **Faces**
- **Eyes**

### Instructions:
1. Choose an option from the sidebar.
2. For **Image Detection**, upload an image.
3. For **Webcam Detection**, ensure your webcam is connected.
4. Click **Stop Webcam** to end real-time detection.
""")

# Sidebar options
option = st.sidebar.radio("Choose Detection Mode:", ["Image Detection", "Webcam Detection"])

# Load Haar cascades
face_classifier = cv2.CascadeClassifier(r"C:\Users\sunil\DK\vs code\Deap Learning\Work\FACE AND EYE DETECTOR APP\haarcascade_frontalface_default.xml")
eye_classifier = cv2.CascadeClassifier(r"C:\Users\sunil\DK\vs code\Deap Learning\Work\FACE AND EYE DETECTOR APP\haarcascade_eye.xml")

# Check if cascade files are loaded
if face_classifier.empty() or eye_classifier.empty():
    st.error("Error: Haar cascade file not loaded. Check the file path.")
    st.stop()

# Face and Eye Detection Function
def detect_faces_and_eyes(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_classifier.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)
            cv2.putText(roi_color, "Eye", (ex, ey - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    return img

# Image Detection
if option == "Image Detection":
    st.title("Face & Eye Detection from Image 📷")
    # Compact layout for file uploader
    col1, col2 = st.columns([2, 1])
    with col1:
       uploaded_file = st.file_uploader("upload Image", type=["jpg", "png", "jpeg"])
    

    if uploaded_file:
        input_image = Image.open(uploaded_file)
        st.image(input_image, caption="Uploaded Image", use_column_width=True)

        # Process image
        with st.spinner("Processing..."):
            img_np = np.array(input_image.convert("RGB"))
            processed_img = detect_faces_and_eyes(img_np)
            st.image(processed_img, caption="Processed Image", use_column_width=True)
            st.success("Detection Completed!")

# Webcam Detection
elif option == "Webcam Detection":
    st.title("Face & Eye Detection from Webcam 🎥")
    start_detection = st.button("Start Webcam Detection")

    if start_detection:
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            st.error("Error: Could not access the webcam.")
        else:
            FRAME_WINDOW = st.image([])

            st.session_state["_is_running"] = True
            stop_detection = st.button("Stop Webcam Detection")

            while st.session_state["_is_running"]:
                ret, frame = cap.read()
                if not ret:
                    st.error("Error: Failed to read frame from webcam.")
                    break

                # Process frame
                frame = detect_faces_and_eyes(frame)
                FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

                # Stop webcam if button is pressed
                if stop_detection:
                    st.session_state["_is_running"] = False
                    break

            cap.release()
            cv2.destroyAllWindows()
            st.success("Webcam Detection Stopped.")
