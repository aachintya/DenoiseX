import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import io
from io import BytesIO

# Load the model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("denoising_model.h5", compile=False)
    return model

# Preprocess the input image
def preprocess_image(image):
    original_size = image.size
    
    # Compress input image slightly to reduce noise
    buffer = BytesIO()
    image.save(buffer, format="JPEG", quality=95)
    buffer.seek(0)
    compressed_image = Image.open(buffer)
    
    # Resize for model input
    resized_img = compressed_image.resize((256, 256))
    img_array = np.array(resized_img) / 255.0  # Normalize to [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array, original_size

# Postprocess the model output
def postprocess_output(output, original_size):
    output = np.squeeze(output)  # Remove batch dimension
    output = np.clip(output * 255, 0, 255).astype(np.uint8)
    output_image = Image.fromarray(output)
    
    # Resize back to original dimensions with high quality
    output_image = output_image.resize(original_size, Image.LANCZOS)
    
    # Apply moderate compression for clarity (reduces noise)
    buffer = BytesIO()
    output_image.save(buffer, format="JPEG", quality=92)
    buffer.seek(0)
    final_image = Image.open(buffer).convert("RGB")
    
    return final_image

# Streamlit UI
st.set_page_config(page_title="Low-Light Image Enhancer", layout="centered")

st.title("🔆 Low-Light Image Enhancer")
st.markdown("Upload a low-light image and enhance it using the trained model.")

uploaded_file = st.file_uploader("Choose a low-light image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    input_image = Image.open(uploaded_file).convert("RGB")
    
    # Display original with slight compression for comparison
    buffer = BytesIO()
    input_image.save(buffer, format="JPEG", quality=95)
    buffer.seek(0)
    display_original = Image.open(buffer).convert("RGB")
    st.image(display_original, caption="Original Low-Light Image", use_container_width=True)

    if st.button("✨ Enhance Image"):
        with st.spinner("Enhancing your image..."):
            model = load_model()
            preprocessed, original_size = preprocess_image(input_image)
            prediction = model.predict(preprocessed)
            enhanced_image = postprocess_output(prediction, original_size)

            st.image(enhanced_image, caption="Enhanced Image", use_container_width=True)
            st.success("Image enhanced successfully!")

            # Download button
            buf = io.BytesIO()
            enhanced_image.save(buf, format="PNG")
            byte_im = buf.getvalue()

            st.download_button(
                label="📥 Download Enhanced Image",
                data=byte_im,
                file_name="enhanced_image.png",
                mime="image/png"
            )