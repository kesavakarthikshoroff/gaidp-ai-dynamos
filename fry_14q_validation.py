import pandas as pd
import numpy as np

# Load FR Y-14Q dataset
file_path = "FR_Y-14Q_data.csv"  # Update with actual file path
df = pd.read_csv(file_path)

# Define validation rules
REQUIRED_FIELDS = ["BHC_NAME", "RSSD_ID", "REPORTING_MONTH", "PORTFOLIO_ID", "SEGMENT_ID"]
NUMERIC_CONSTRAINTS = {
    "PD": (0, 1),   # Probability of Default must be between 0 and 1
    "LGD": (0, 1),  # Loss Given Default must be between 0 and 1
    "ELGD": (0, 1),  # Expected Loss Given Default must be between 0 and 1
    "Gross_Charge_Offs": (0, np.inf),
    "Net_Charge_Offs": (0, np.inf),
}

VALID_DELINQUENCY_CODES = ["01", "02", "03", "04", "05", "06"]  # Example: Current, 120+ DPD

# Function to validate data row-wise
def validate_row(row):
    errors = []

    # Check for missing required fields
    for field in REQUIRED_FIELDS:
        if pd.isnull(row[field]) or row[field] == "":
            errors.append(f"Missing value in {field}")

    # Check numeric constraints
    for field, (min_val, max_val) in NUMERIC_CONSTRAINTS.items():
        if field in row and not pd.isnull(row[field]):
            if not (min_val <= row[field] <= max_val):
                errors.append(f"{field} out of range [{min_val}, {max_val}]")

    # Validate delinquency status
    if "DELINQUENCY_STATUS" in row and str(row["DELINQUENCY_STATUS"]) not in VALID_DELINQUENCY_CODES:
        errors.append(f"Invalid DELINQUENCY_STATUS: {row['DELINQUENCY_STATUS']}")

    # Check cross-field consistency
    if "Gross_Charge_Offs" in row and "Net_Charge_Offs" in row:
        if row["Net_Charge_Offs"] > row["Gross_Charge_Offs"]:
            errors.append("Net Charge-offs cannot exceed Gross Charge-offs")

    return errors

# Apply validation to each row
df["ANOMALIES"] = df.apply(validate_row, axis=1)

# Filter records with anomalies
anomalies_df = df[df["ANOMALIES"].apply(len) > 0]

# Save anomalies report
anomalies_df.to_csv("FR_Y-14Q_anomalies_report.csv", index=False)

# Display anomalies
print("Validation completed. Anomalies found:")
print(anomalies_df[["BHC_NAME", "REPORTING_MONTH", "PORTFOLIO_ID", "ANOMALIES"]])