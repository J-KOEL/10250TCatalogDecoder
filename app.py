import streamlit as st
import pandas as pd

# Load catalog reference
catalog_df = pd.read_csv("EveryProductNumber.csv")
catalog_df.columns = catalog_df.columns.str.strip()
catalog_lookup = dict(zip(catalog_df["Catalog Number"], catalog_df["Product Name"]))

# Import decoders
from decoder_nonilluminated import decode_non_illuminated_pushpull
from decoder_illuminated_incandescent import decode_illuminated_pushpull_incandescent

# Streamlit UI
st.set_page_config(page_title="10250T Decoder", layout="centered")
st.title("🔍 10250T Product Decoder")

part_number = st.text_input("Enter Catalog Number", placeholder="e.g., 10250T10B63-1")

if part_number:
    part_number = part_number.strip()
    product_type = catalog_lookup.get(part_number)

    if not product_type:
        st.error("Catalog number not found in reference list.")
    else:
        # Route to appropriate decoder based on product name
        product_type_lower = product_type.lower()
        if "non-illuminated push-pull" in product_type_lower:
            result = decode_non_illuminated_pushpull(part_number)
        elif "incandescent push-pull" in product_type_lower:
            result = decode_illuminated_pushpull_incandescent(part_number)
        else:
            result = {"error": f"Decoder for product type '{product_type}' is not implemented yet."}

        # Display results
        if "error" in result:
            st.error(result["error"])
        else:
            st.subheader("Decoded Components")
            for key, value in result.items():
                st.markdown(f"**{key}**: {value}")

