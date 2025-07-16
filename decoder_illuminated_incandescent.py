import pandas as pd

# Load reference data
catalog_df = pd.read_csv("EveryProductNumber.csv")
lens_df = pd.read_csv("IlluminatedPushPullIncandescentLens.csv")
light_unit_df = pd.read_csv("IlluminatedPushPullIncandescentLightUnit.csv")
operator_df = pd.read_csv("PushPullOperator.csv")
circuit_df = pd.read_csv("Circuit.csv")

# Create lookup dictionaries
lens_lookup = dict(zip(lens_df["Code"], lens_df["Label"]))
light_unit_lookup = dict(zip(light_unit_df["Code"].astype(str), light_unit_df["Label"]))
operator_lookup = dict(zip(operator_df["Code"].astype(str), operator_df["Label"]))
circuit_lookup = dict(zip(circuit_df["Code"].astype(str), circuit_df["Label"]))
product_lookup = dict(zip(catalog_df["Catalog Number"], catalog_df["Product Name"]))

# Sort codes by length descending to match longest possible codes first
known_operator_codes = sorted(operator_lookup.keys(), key=lambda x: -len(x))
known_light_unit_codes = sorted(light_unit_lookup.keys(), key=lambda x: -len(x))
known_lens_codes = sorted(lens_lookup.keys(), key=lambda x: -len(x))
known_circuit_codes = sorted(circuit_lookup.keys(), key=lambda x: -len(x))

def decode_illuminated_pushpull_incandescent(part_number):
    if not part_number.startswith("10250T"):
        return {"error": "Invalid catalog number prefix"}

    base = part_number[6:]
    circuit_code = ""
    if "-" in base:
        base, circuit_code = base.split("-")

    # Identify operator code
    operator_code = next((code for code in known_operator_codes if base.startswith(code)), None)
    if not operator_code:
        return {"error": "Unknown operator code"}
    remaining = base[len(operator_code):]

    # Identify light unit code
    light_unit_code = next((code for code in known_light_unit_codes if remaining.startswith(code)), None)
    if not light_unit_code:
        return {"error": "Unknown light unit code"}
    remaining = remaining[len(light_unit_code):]

    # Identify lens code
    lens_code = next((code for code in known_lens_codes if remaining.startswith(code)), None)
    if not lens_code:
        return {"error": "Unknown lens code"}

    return {
        "Catalog Number": part_number,
        "Product Name": product_lookup.get(part_number, "Unknown"),
        "Operator Code": operator_code,
        "Operator Description": operator_lookup.get(operator_code, "Unknown"),
        "Operator Catalog": f"10250T{operator_code}",
        "Light Unit Code": light_unit_code,
        "Light Unit Description": light_unit_lookup.get(light_unit_code, "Unknown"),
        "Light Unit Catalog": f"10250T{light_unit_code}",
        "Lens Code": lens_code,
        "Lens Description": lens_lookup.get(lens_code, "Unknown"),
        "Lens Catalog": f"10250T{lens_code}",
        "Circuit Code": circuit_code,
        "Circuit Description": circuit_lookup.get(circuit_code, "Unknown") if circuit_code else "N/A",
        "Circuit Catalog": f"10250T{circuit_code}" if circuit_code else "N/A"
    }
