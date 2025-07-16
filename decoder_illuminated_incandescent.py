import pandas as pd

# Load reference data
catalog_df = pd.read_csv("EveryProductNumber.csv")
lens_df = pd.read_csv("IlluminatedPushPullIncandescentLens.csv")
light_unit_df = pd.read_csv("IlluminatedPushPullIncandescentLightUnit.csv")
operator_df = pd.read_csv("PushPullOperator.csv")

# Create lookup dictionaries
lens_lookup = dict(zip(lens_df["Code"], lens_df["Label"]))
light_unit_lookup = dict(zip(light_unit_df["Code"].astype(str), light_unit_df["Label"]))
operator_lookup = dict(zip(operator_df["Code"].astype(str), operator_df["Label"]))
product_lookup = dict(zip(catalog_df["Catalog Number"], catalog_df["Product Name"]))

# Sort operator codes by length (longest first) to match correctly
known_operator_codes = sorted(operator_lookup.keys(), key=lambda x: -len(x))

def decode_illuminated_pushpull_incandescent(part_number):
    if not part_number.startswith("10250T"):
        return {"error": "Invalid catalog number prefix"}

    base = part_number[6:]
    variant = ""
    if "-" in base:
        base, variant = base.split("-")

    # Identify operator code from known list
    operator_code = None
    for code in known_operator_codes:
        if base.startswith(code):
            operator_code = code
            break

    if not operator_code:
        return {"error": "Unknown operator code"}

    lens_code = base[len(operator_code):len(operator_code)+3]
    light_unit_code = base[len(operator_code)+3:]

    return {
        "Catalog Number": part_number,
        "Product Name": product_lookup.get(part_number, "Unknown"),
        "Operator Code": operator_code,
        "Operator Description": operator_lookup.get(operator_code, "Unknown"),
        "Operator Catalog": f"10250T{operator_code}",
        "Lens Code": lens_code,
        "Lens Description": lens_lookup.get(lens_code, "Unknown"),
        "Lens Catalog": f"10250T{lens_code}",
        "Light Unit Code": light_unit_code,
        "Light Unit Description": light_unit_lookup.get(light_unit_code, "Unknown"),
        "Light Unit Catalog": f"10250T{light_unit_code}" if light_unit_code else "N/A"
    }
