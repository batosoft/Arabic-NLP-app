import awesome_streamlit as ast
import streamlit as st

from backend.utils import get_current_ram_usage, ga

import backend.aragpt
import backend.qa

st.set_page_config(
    page_title="RTA Services Search", page_icon="📖", initial_sidebar_state="expanded", layout="wide"
)

ga(st.__file__)

PAGES = {
    "Arabic Question Answering": backend.qa,
}


st.sidebar.title("Navigation")
selection = st.sidebar.radio("Pages", list(PAGES.keys()))

page = PAGES[selection]
# with st.spinner(f"Loading {selection} ..."):
ast.shared.components.write_page(page)

st.sidebar.header("Info")
st.sidebar.write("Made by [Ali Alhashimi](https://twitter.com/alilibx)")
st.sidebar.write(
    "Pre-trained models are available on [HF Hub](https://huggingface.co/aubmindlab)"
)
st.sidebar.write(
    "Models source code available on [GitHub](https://github.com/aub-mind/arabert)"
)
st.sidebar.write(
    "App source code available on [GitHub](https://github.com/alilibx/Arabic-NLP-app)"
)
if st.sidebar.checkbox("Show RAM usage"):
    ram = get_current_ram_usage()
    st.sidebar.write("Ram usage: {:.2f}/{:.2f} GB".format(ram[0], ram[1]))
