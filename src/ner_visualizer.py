import spacy_streamlit
import streamlit as st
from .utils import load_data_pandas, load_model, load_data_json
import random


def app():
    model_name = "en_core_web_sm"
    filepath = "src/reviewSamples20.json"
    df = load_data_pandas(filepath)
    reviews = df["text"].to_list()
    random.seed(420)
    random.shuffle(reviews)

    nlp = load_model(model_name)

    st.title("Named Entity Recognition")
    review_text = st.selectbox("Choose a review from the following dropdown:", reviews)
    doc = spacy_streamlit.process_text(model_name, review_text)
    review_data = load_data_json(filepath, review_text)
    st.markdown("JSON object:")
    st.json(review_data)

    spacy_streamlit.visualize_ner(
        doc,
        labels=nlp.get_pipe("ner").labels,
        title="Named Entity Recognition Visualizer",
    )
