import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

# Load the h5 model
model = load_model('brain_tumor.h5')

def preprocess_image(image):
        # Resize the image to the input shape of model
        image = image.resize((256, 256))
        # Convert the image to numpy array
        image_array = np.array(image)
        # scaling pixel values between 0 and 1
        image_array = image_array / 255.0
        # Add a batch dimension to the image array
        image_array = np.expand_dims(image_array, axis=0)
        return image_array

def run():
    # create the title
    st.title('Insert the MRI Scan Results')
    st.markdown('---')
    
    img = 'scan-type.png'
    st.image(img, caption='MRI Scan Type.', use_column_width=True, width=100)   

    st.write("<span style='font-size: 25px;'>Before Uploading the image, please make sure the MRI result is an **axial scan**</span>", unsafe_allow_html=True)
    st.markdown('---')

    uploaded = st.file_uploader("Input the Image...", type=["jpg", "jpeg", "png"])

    if uploaded is not None:
        # Show the uploaded image
        st.image(uploaded, caption='Uploaded Image.', use_column_width=True)

        # Preprocess the image
        img = Image.open(uploaded)
        processed_img = preprocess_image(img)

        # Predict using model
        prediction = model.predict(processed_img)
        class_label = "Positive Tumor" if prediction[0][0] >= 0.5 else "Normal Brain"
        st.markdown('---')
        st.write("Prediction :")
        st.write(f"# {class_label}")
        
if __name__ == '__main__':
   run()