import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="The Banana Clock",
    page_icon="🍌",
    layout="centered"
)

MODEL_PATH = 'banana_classifier_model.h5'
IMG_SIZE = (128, 128)

CLASS_NAMES = ['overripe', 'ripe', 'rotten', 'unripe'] 

CLASS_TO_DAYS = {
    "unripe": "≈ 5-6 days left",   
    "ripe": "≈ 2-3 days left",     
    "overripe": "≈ 1 day left", 
    "rotten": "0 days (already dead)" 
}

@st.cache_resource
def load_model():
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def predict_banana_stage(pil_image, model):
    img = pil_image.resize(IMG_SIZE)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0


    predictions = model.predict(img_array)
    class_idx = np.argmax(predictions[0])
    predicted_class = CLASS_NAMES[class_idx]
    days_left = CLASS_TO_DAYS.get(predicted_class, "Unknown")

    return predicted_class, days_left


model = load_model()

st.title("🍌 The Banana Clock ⏰")
st.write(
    "Curious about your banana's best-by date? I can help with that. Pop in a picture below."
)
st.write("Get started by dragging and dropping a banana photo below.")

uploaded_file = st.file_uploader(
    "Choose a banana image...",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None and model is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")

    with st.spinner('Classifying...'):
        predicted_stage, days_left = predict_banana_stage(image, model)

    st.success(f"**Predicted Stage:** {predicted_stage}")
    st.info(f"**Estimated Shelf Life:** {days_left}")

    msg = {
    "unripe": "My personality is still loading. Give it a week",
    "ripe": "Single, ready to mingle... with your cereal. Let's do this.",
    "overripe": "My sugar levels are over 9000. I'm basically a dessert ingredient now.",
    "rotten": "My therapist says I'm compost now. It's a journey."
}
    
    status = msg.get(predicted_stage)
    st.info(f"🍌 Banana says: \"{status}\"")

elif model is None:
    st.warning("Model could not be loaded. Please ensure the model file is correct.")