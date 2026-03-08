import streamlit as st
from PIL import Image
from damage_detector import detect_damage
from cost_estimator import estimate_cost

st.set_page_config(page_title="Car Damage Detection", layout="centered")

st.title("🚗 Car Damage Detection & Repair Cost Estimation")

st.write("Upload an image of a damaged car and get an estimated repair cost.")

uploaded_file = st.file_uploader(
    "Upload Car Damage Image",
    type=["jpg","jpeg","png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.write("🔍 Detecting damage...")

    damages = detect_damage(image)

    if len(damages) == 0:

        st.success("No damage detected.")

    else:

        st.subheader("Detected Damages")

        for d in damages:
            st.write("•", d)

        cost = estimate_cost(damages)

        st.subheader("Estimated Repair Cost")

        st.success(f"₹ {cost}")
