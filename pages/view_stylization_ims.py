import streamlit as st

st.set_page_config(layout='wide')

with open('models.txt') as f:
    models = f.read().splitlines()

with st.sidebar:
    m_name = st.selectbox('m_name', options=models)
    styl = st.selectbox('styl', options=['orig', 'merged', 'smoothed', 'stylized'])
    toggle_1 = st.selectbox('t1', options=['orig', 'simplified-manual-index)', 'simplified-auto-index)', 'max-simplified'])
    toggle_2 = st.selectbox('t2', options=['orig', 'simplified-manual-index)', 'simplified-auto-index)', 'max-simplified'])

im1 = f'stylization_ims/{m_name}_35_{toggle_1}_{styl}.png'
im2 = f'stylization_ims/{m_name}_35_{toggle_2}_{styl}.png'
im_paths = [im1, im2]

idx = st.slider('idx', 0, 1)

st.image(im_paths[idx])
