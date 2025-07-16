import pandas as pd

# Load reference data
catalog_df = pd.read_csv("EveryProductNumber.csv")
circuit_df = pd.read_csv("Circuit.csv")
button_df = pd.read_csv("NonIlluminatedPushPullButton.csv")
operator_df = pd.read_csv("NonIlluminatedPushPullOperator.csv")

# Create lookup dictionaries
circuit_lookup = dict(zip(circuit_df["Code"].astype(str), circuit_df["Label"]))
button_lookup = dict(zip(button_df["Code"], button_df["Label"]))
operator_lookup = dict(zip(operator_df["Code"].astype(str), operator_df["Label"]))
product_lookup = dict(zip(catalog_df["Catalog Number"], catalog_df["Product Name"]))

def decode_non_illuminated_pushpull(part_number):
    if not part_number.startswith("10250T"):
        return {"error": "Invalid catalog number prefix"}

    base = part_number[6:]
    variant = ""
    if "-" in base:
        base, variant = base.split("-")

    operator_code = ''.join(filter(str.isdigit, base[:2]))
    button_code = base[2:5]
    circuit_code = variant

    return {
        "Catalog Number": part_number,
        "Product Name": product_lookup.get(part_number, "Unknown"),
        "Operator Code": operator_code,
        "Operator Description": operator_lookup.get(operator_code, "Unknown"),
        "Operator Catalog": f"10250T{operator_code}",
        "Button Code": button_code,
        "Button Description": button_lookup.get(button_code, "Unknown"),
        "Button Catalog": f"10250T{button_code}",
        "Circuit Code": circuit_code,
        "Circuit Description": circuit_lookup.get(circuit_code, "Unknown"),
        "Circuit Catalog": f"10250T{circuit_code}" if circuit_code else "N/A"
    }
