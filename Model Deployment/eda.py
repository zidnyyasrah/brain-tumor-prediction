import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title='Brain Tumor Analysis',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    # Membuat Title
    st.title('Brain Tumor Analysis')
    # Menambahkan Deskripsi
    st.write('This page is created by _Zidny Yasrah Sallum_')
    st.markdown('---')
    st.write("<span style='font-size: 25px;'><b>What is Brain Tumor?</b></span>", unsafe_allow_html=True)
    braintumor = '''
    A brain tumor, known as an intracranial tumor, is an abnormal mass of tissue in which cells grow and multiply uncontrollably, 
    seemingly unchecked by the mechanisms that control normal cells. More than 150 different brain tumors have been documented, 
    but the two main groups of brain tumors are termed primary and metastatic.
    
    Primary brain tumors include tumors that originate from the tissues of the brain or the brain's immediate surroundings. 
    Primary tumors are categorized as glial (composed of glial cells) or non-glial (developed on or in the structures of the brain, 
    including nerves, blood vessels and glands) and benign or malignant.

    Metastatic brain tumors include tumors that arise elsewhere in the body (such as the breast or lungs) and migrate to the brain, 
    usually through the bloodstream. Metastatic tumors are considered cancer and are malignant.

    Source : _https://www.aans.org/en/Patients/Neurosurgical-Conditions-and-Treatments/Brain-Tumors_

    '''
    st.write(braintumor)

if __name__ == '__main__':
    run()