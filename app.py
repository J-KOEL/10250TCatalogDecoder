import streamlit as st
from decoder_nonilluminated import decode_non_illuminated_pushpull

st.title("🔍 10250T Product Decoder")

part_number = st.text_input("Enter Catalog Number", placeholder="e.g., 10250T10B63-1")

if part_number:
    result = decode_non_illuminated_pushpull(part_number)
    if "error" in result:
        st.error(result["error"])
    else:
        st.subheader("Decoded Components")
        for key, value in result.items():
            st.write(f"**{key}**: {value}")
