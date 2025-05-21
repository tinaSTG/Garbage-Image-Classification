# import streamlit_app
# import eda
# import streamlit as st

# # define pages
# PAGES = {
#     #  format :"Judul Menu": nama_file
#     "EDA": eda,
#     "Inference": streamlit_app
# }

# # set sidebar title
# st.sidebar.title('Navigation')

# # set sidebar selection
# selection = st.sidebar.radio("Go to", list(PAGES.keys()))
# page = PAGES[selection]

# page.run()

import streamlit as st
import streamlit_app
import eda

# Define pages
PAGES = {
    "EDA": eda,
    "Inference": streamlit_app
}

# Sidebar title
st.sidebar.title("Navigation")

# Sidebar navigation
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]

# Jalankan fungsi run() di masing-masing modul
if hasattr(page, "run") and callable(page.run):
    page.run()
else:
    st.error(f"Halaman '{selection}' tidak memiliki fungsi run().")

