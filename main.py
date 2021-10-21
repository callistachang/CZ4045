import streamlit as st
from src import ner_visualizer, dependency_visualizer, home_page

pages = {
    "Introduction": home_page,
    "Named Entity Recognition": ner_visualizer,
    "Token & Dependency Visualizer": dependency_visualizer,
}

st.sidebar.title("Navigation")
page_selection = st.sidebar.radio("Go to", list(pages.keys()))
page = pages[page_selection]
page.app()
