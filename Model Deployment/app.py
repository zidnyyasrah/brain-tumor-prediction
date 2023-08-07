import streamlit as st
import eda
import prediction

navigation = st.sidebar.selectbox('Pilih Halaman: ', ('Brain Tumor Analysis', 'Predict Tumor'))

if navigation == 'Brain Tumor Analysis':
    eda.run()
elif navigation == 'Predict Tumor':
    prediction.run()