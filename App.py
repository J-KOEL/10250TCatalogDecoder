
import streamlit as st
from decoder import decode_catalog_number
st.set_page_config(page_title="10250T Decoder", layout="centered")

st.title("🔍 10250T Product Decoder")
st.markdown("Enter a catalog number to decode its product line.")

# Input field
part_number = st.text_input("Catalog Number", placeholder="e.g., 10250T589C47-1")

# Decode and display result
if part_number:
    result = decode_catalog_number(part_number)
    st.success(f"**Decoded Product:** {result}")
