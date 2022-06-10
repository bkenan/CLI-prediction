import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Fill-Mask")

st.title("Fill-Mask tool")
st.write("Write a sentence and put <mask> in place of any word. The model will predict that word!")
st.write("Example: Machine learning is an application of <mask>.")



def load_model():
    model = pipeline("fill-mask", model="roberta-base")
    return model


model_load_state = st.text('Loading Model...')
model = load_model()

model_load_state.text('Model is ready!')


st.write("##  Your Sentence:")
input = st.text_input(" ")


button = st.button("Predict")
if button and not input:
    st.warning("No sentence was provided!")


with st.spinner("Finding suitable Words"):
    if button and input:
        answers = model(input)
        i = 1
        for a in answers:
            st.write(f"Prediction {i}:",
                        a["sequence"], "\n", "Score:", str(round(a["score"], 2)))
            i = i+1