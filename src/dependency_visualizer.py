import spacy_streamlit
import streamlit as st
from .utils import load_data_pandas, load_data_json
import random


def app():
    model_name = "en_core_web_sm"
    filepath = "src/reviewSelected100.json"
    df = load_data_pandas(filepath)
    reviews = list(sorted(df["text"].to_list(), key=len))[20:40]
    random.seed(420)
    random.shuffle(reviews)

    st.title("Token Analysis")
    st.markdown(
        "20 reviews are used as samples for token analysis and dependency parsing."
    )
    review_text = st.selectbox("Choose a review from the following dropdown:", reviews)
    st.markdown("---")
    doc = spacy_streamlit.process_text(model_name, review_text)
    review_data = load_data_json(filepath, review_text)
    st.markdown("JSON object:")
    st.json(review_data)

    spacy_streamlit.visualize_tokens(doc, title="Token Analysis")
    spacy_streamlit.visualize_parser(doc, title="Dependency Visualizer")
