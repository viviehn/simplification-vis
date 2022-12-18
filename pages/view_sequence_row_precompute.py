import streamlit as st

st.set_page_config(layout='wide')

st.text('Each row shows a different model and scale [5, 35, 65].')
st.text('The density function is computed using a gaussian blur with width=scale.')
st.text('If you are trying to delete a stroke with length L, the maximum region area to be merged is L*(scale/2)')
st.text('The first image in each row shows the original drawing, and the final image shows the result after performing all valid deletions (validity determined by regions)')


cols = st.columns(6)
rows = 141

for r in range(rows):
    for c in range(6):
        cols[c].image(f'view_sequence_row/{r}_{c}.png')
