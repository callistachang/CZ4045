import spacy_streamlit
import streamlit as st
from utils import load_data
import random


def app():
    model_name = "en_core_web_sm"
    df = load_data("reviewSelected100.json")
    reviews = list(sorted(df["text"].to_list(), key=len))[20:40]
    random.seed(420)
    random.shuffle(reviews)

    st.title("Token Analysis")
    review_text = st.selectbox("Choose review to analyze:", reviews)
    doc = spacy_streamlit.process_text(model_name, review_text)

    spacy_streamlit.visualize_tokens(doc, title="Token Analysis")
    spacy_streamlit.visualize_parser(doc, title="Dependency Visualizer")
