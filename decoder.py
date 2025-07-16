import pandas as pd

# Load the product data
df = pd.read_csv("EveryProductNumber.csv")
df.columns = df.columns.str.strip()

# Create a dictionary for decoding
decoder_dict = dict(zip(df["Catalog Number"], df["Product Name"]))

def decode_catalog_number(part_number):
    """
    Returns the product name for a given catalog number.
    """
    return decoder_dict.get(part_number.strip(), "Unknown catalog number")
