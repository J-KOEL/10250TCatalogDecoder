import streamlit as st
from decoder_nonilluminated import decode_non_illuminated_pushpull
from decoder_illuminated_incandescent import decode_illuminated_pushpull_incandescent

st.set_page_config(page_title="10250T Decoder", layout="centered")
st.title("🔍 10250T Product Decoder")

# Product type selector
product_type = st.selectbox(
    "Select Product Type",
    ["Non-Illuminated Push-Pull", "Illuminated Push-Pull (Incandescent)"]
)

# Catalog number input
part_number = st.text_input("Enter Catalog Number", placeholder="e.g., 10250T10B63-1")

# Decode based on selected product type
if part_number:
    if product_type == "Non-Illuminated Push-Pull":
        result = decode_non_illuminated_pushpull(part_number)
    elif product_type == "Illuminated Push-Pull (Incandescent)":
        result = decode_illuminated_pushpull_incandescent(part_number)
    else:
        result = {"error": "Unsupported product type"}

    # Display results
    if "error" in result:
        st.error(result["error"])
    else:
        st.subheader("Decoded Components")
        for key, value in result.items():
            st.markdown(f"**{key}**: {value}")
