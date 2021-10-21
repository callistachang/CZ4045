import streamlit as st
from src import ner_visualizer, dependency_visualizer, home_page, dataset_analysis

pages = {
    "Introduction": home_page,
    "Dataset Analysis": dataset_analysis,
    "Named Entity Recognition": ner_visualizer,
    "Token & Dependency Visualizer": dependency_visualizer,
}

st.sidebar.title("Navigation")
page_selection = st.sidebar.radio("Go to", list(pages.keys()))
page = pages[page_selection]
page.app()
