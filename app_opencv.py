import streamlit as st
import cv2
from PIL import Image
import numpy as np

def gray_scale_conversion(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return gray_image

def black_and_white_conversion(image):
    _, bw_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    return bw_image

def main():
    st.header("App de procesamiento de imágenes usando OpenCV")
    st.subheader("Prueba de OpenCV")
    st.title("Convertir imagen")

    uploaded_file = st.file_uploader("Sube una imagen", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        image = np.array(Image.open(uploaded_file))
        st.image(image, caption='Imagen Original', use_column_width=True)

        # Crear las pestañas en el sidebar
        tabs = st.sidebar.radio("Operaciones", ("Escala de grises", "Blanco y Negro"))

        if tabs == "Escala de grises":
            # Convertir automáticamente a escala de grises
            gray_image = gray_scale_conversion(image)
            st.image(gray_image, caption='Imagen en Escala de Grises', use_column_width=True)

        elif tabs == "Blanco y Negro":
            # Convertir automáticamente a blanco y negro
            bw_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            _, bw_image = cv2.threshold(bw_image, 127, 255, cv2.THRESH_BINARY)
            st.image(bw_image, caption='Imagen en Blanco y Negro', use_column_width=True)

if __name__ == '__main__':
    main()
