import cv2
import streamlit as st
import numpy as np
import tempfile

st.title('Edge-er')

uploaded_file = st.file_uploader("Choose a file", type=['jpg', 'png'])
if uploaded_file is not None:
    # Save the uploaded file to a temporary location
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(uploaded_file.read())

    # Read the image using OpenCV
    img = cv2.imread(temp_file.name)

    # Convert image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    img_canny = cv2.Canny(img_gray, 150 , 150)

    # Display the edge-detected image
    st.image(img_canny, width=300)

    # Remove the temporary file
    temp_file.close()
