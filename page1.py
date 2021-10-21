import spacy_streamlit
import streamlit as st
from utils import load_data, load_model
import random


def app():
    model_name = "en_core_web_sm"
    df = load_data("reviewSamples20.json")
    reviews = df["text"].to_list()
    random.seed(420)
    random.shuffle(reviews)

    nlp = load_model(model_name)

    st.title("Named Entity Recognition")
    review_text = st.selectbox("Choose review to analyze:", reviews)
    doc = spacy_streamlit.process_text(model_name, review_text)

    spacy_streamlit.visualize_ner(
        doc,
        labels=nlp.get_pipe("ner").labels,
    )
