

# Face & Eye Detection App 👁️‍🗨️

## Overview

This **Face & Eye Detection App** leverages **Haar cascades** to detect faces and eyes in both images and real-time webcam footage. Built with **Streamlit** for a clean and interactive interface, this app allows users to upload images or use their webcam for detection. Once detected, the app highlights faces with rectangles and labels the detected faces and eyes for better clarity.

This project serves as an introduction to **computer vision** and **AI**, using popular libraries like **OpenCV**, **Streamlit**, and **NumPy**.

## Features

- **Image Upload Detection**: Upload an image to detect faces and eyes.
- **Real-Time Webcam Detection**: Use your webcam to detect faces and eyes in real-time.
- **Face & Eye Highlighting**: Detected faces and eyes are highlighted with rectangles and labels for clear visibility.
- **Interactive Interface**: Start and stop webcam detection easily via buttons in the app.
- **Compact Design**: The app layout is optimized for a smooth user experience.

## Technologies Used

- **Python**: The main programming language used for this project.
- **Streamlit**: A fast way to build web apps for data science and machine learning projects.
- **OpenCV**: A powerful library used for real-time computer vision and image processing tasks.
- **Haar Cascade Classifiers**: Used for detecting faces and eyes in images and video.
- **NumPy**: Used for efficient image processing and manipulation.

## Installation

To run this app on your local machine, follow these steps:


Your browser should automatically open with the app running on [`http://localhost:8501`.](https://faceeyedetectation-5u9qytappbfgenzsgwzbhrr.streamlit.app/)

## Usage

### 1. **Face & Eye Detection from Image**

- Click on the "Upload Image" section.
- Choose an image (JPG, PNG, or JPEG format).
- The app will automatically detect faces and eyes in the uploaded image and display them with bounding boxes.

### 2. **Face & Eye Detection from Webcam**

- Click on the "Start Face & Eye Detection" button to activate webcam detection.
- The app will start processing real-time video from your webcam.
- Detected faces and eyes will be highlighted with rectangles and labeled accordingly.
- You can stop the webcam detection by clicking the "Stop Webcam" button.

## Key Highlights

- **Real-Time Detection**: The app works in real-time to detect faces and eyes from the webcam feed.
- **User-Friendly Interface**: Streamlit provides a simple yet interactive interface to make the experience smooth.
- **Customizable**: You can extend the app by integrating other machine learning models or add more detection capabilities (e.g., smile detection).
- **Security and Privacy**: Only the images or video processed locally on the machine, no data is sent to a remote server.

## Use Cases

- **Security**: Build the foundation for facial recognition systems.
- **Photography**: Automatically identify faces and eyes for photo editing or face filters.
- **Education**: Demonstrates basic computer vision concepts for students and enthusiasts.
- **Real-Time Analytics**: Can be extended for use in real-time analysis and tracking in video feeds.

## Conclusion
- The Face & Eye Detection App is a simple yet powerful tool for demonstrating real-time computer vision using Python. With easy-to-use interfaces and the ability to detect faces and eyes from images and webcams, this app is perfect for anyone wanting to explore the possibilities of image processing and AI. Whether you want to integrate this technology into security systems, improve photography tools, or just learn more about computer vision, this app offers an excellent starting point.

- Thanks to Streamlit, the app provides an interactive, easy-to-deploy solution, and with further development, you can enhance it to serve many other use cases in AI-powered applications.
