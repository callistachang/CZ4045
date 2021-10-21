import streamlit as st
import page1
import page2

pages = {"Named Entity Recognition": page1, "Token & Dependency Visualizer": page2}

st.sidebar.title("Navigation")
page_selection = st.sidebar.radio("Go to", list(pages.keys()))
page = pages[page_selection]
page.app()
