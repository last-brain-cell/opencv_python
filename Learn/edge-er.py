import cv2
import streamlit as st
import tempfile

st.title('Edge-er')

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(uploaded_file.read())

    img = cv2.imread(temp_file.name)

    imgCanny = cv2.Canny(img, 200, 200)
    st.image(imgCanny, width=300)

    temp_file.close()
