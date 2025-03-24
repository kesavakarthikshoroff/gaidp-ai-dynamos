import pandas as pd
import numpy as np
import random
import uuid

# Number of synthetic records
num_records = 1000  

# Define lists for categorical fields
ratings = ["AAA", "AA", "A", "BBB", "BB", "B", "CCC", "D"]
countries = ["US", "CA", "UK", "DE", "FR", "JP", "CN", "IN"]
industries = ["Finance", "Technology", "Healthcare", "Energy", "Retail", "Manufacturing"]
currencies = ["USD", "EUR", "GBP", "JPY", "CNY"]
facilities = ["Term Loan", "Revolver", "Bridge Loan", "Syndicated Loan"]
collateral_types = ["Secured", "Unsecured", "Partially Secured"]
repayment_types = ["Bullet", "Amortizing", "Balloon", "Interest-Only"]
default_status = ["Current", "Past Due", "Defaulted"]
sectors = ["Public", "Private", "Government"]

# Define synthetic data generation functions
def generate_id():
    return str(uuid.uuid4())  # Unique identifier

def generate_amount():
    return round(np.random.uniform(1e6, 1e9), 2)  # Loan amount in millions/billions

def generate_rating():
    return random.choice(ratings)

def generate_country():
    return random.choice(countries)

def generate_industry():
    return random.choice(industries)

def generate_currency():
    return random.choice(currencies)

def generate_facility():
    return random.choice(facilities)

def generate_collateral():
    return random.choice(collateral_types)

def generate_repayment():
    return random.choice(repayment_types)

def generate_ltv():
    return round(np.random.uniform(0.2, 1.5), 2)  # Loan-to-value ratio

def generate_pd():
    return round(np.random.uniform(0.01, 0.3), 4)  # Probability of default

def generate_lgd():
    return round(np.random.uniform(0.2, 0.9), 4)  # Loss given default

def generate_ead():
    return round(np.random.uniform(1e6, 1e8), 2)  # Exposure at default

def generate_rwa():
    return round(np.random.uniform(1e6, 1e9), 2)  # Risk-weighted assets

def generate_interest_rate():
    return round(np.random.uniform(1, 15), 2)  # Interest rate in %

def generate_maturity():
    return random.randint(1, 30)  # Maturity in years

def generate_default_status():
    return random.choice(default_status)

def generate_sector():
    return random.choice(sectors)

def generate_date():
    return f"{random.randint(2015, 2025)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"  # Random date

# Define the 112 fields as per FR Y-14Q H1
fields = [
    "Customer_ID", "Internal_ID", "Original_Internal_ID", "Obligor_Name", "City", "Country",
    "Zip_Code", "Facility_ID", "Loan_Type", "Currency", "Commitment_Amount", "Outstanding_Balance",
    "Interest_Rate", "Maturity_Date", "PD", "LGD", "EAD", "RWA", "LTV", "Repayment_Type", "Collateral_Type",
    "Industry", "Sector", "Default_Status", "Loan_Purpose", "Facility_Type", "Origination_Date",
    "Internal_Rating", "Minimum_PD", "Maximum_PD", "Credit_Score", "Annual_Revenue", "Total_Assets",
    "EBITDA", "Net_Income", "Leverage_Ratio", "Debt_Service_Coverage_Ratio", "Guarantor_Name",
    "Guarantor_Assets", "Guarantor_Income", "Parent_Company", "Sub_Limit", "Covenant_Indicator",
    "Loan_Spread", "Syndication_Status", "Syndication_Percentage", "Underwriting_Agency", "Basel_Category",
    "Refinancing_Status", "Facility_Term", "Drawn_Amount", "Unused_Commitment", "Obligor_Risk_Rating",
    "Market_Valuation", "Total_Exposures", "Regulatory_Capital", "Primary_Collateral_Value",
    "Secondary_Collateral_Value", "Risk_Adjusted_Exposure", "Net_Charge_Offs", "Interest_Expense",
    "Fee_Income", "Internal_Loan_Grade", "Annual_Loss_Rate", "Credit_Enhancement_Type", "Regulatory_Limit",
    "Guarantee_Amount", "Synthetic_Loan_Flag", "Cross_Collateralization", "Loan_Securitization_Status",
    "Basel_PD", "Basel_LGD", "Basel_EAD", "Basel_RWA", "Supervisory_Review", "Portfolio_Name",
    "Economic_Region", "Risk_Rating_Agency", "Credit_Model_Type", "Internal_Model_Type",
    "Historical_Default_Indicator", "Workout_Status", "Credit_Event_Trigger", "Interest_Only_Period",
    "Non_Performing_Loan_Flag", "Special_Mention_Flag", "Watchlist_Flag", "Amortization_Type",
    "Loan_Adjustment_Factor", "Internal_Credit_Model", "Data_Quality_Score", "Regulatory_Compliance_Status",
    "Liquidity_Facility", "Credit_Substitution", "Final_Maturity_Term", "Payment_Structure",
    "Loan_Covenant_Status", "Loan_Aging_Category", "Underwriter_Name", "Loan_Recovery_Score",
    "Default_Probability_Score", "Portfolio_Segment", "Credit_Exposure_Type", "Regulatory_Capital_Adjustment",
    "Non_Performing_Exposures", "Loss_Given_Default", "Prepayment_Risk", "Loan_Modification_Status",
    "Borrower_Restructuring", "Historical_Default_Rate", "Loss_Severity", "Economic_Capital",
    "Expected_Credit_Loss", "Stress_Test_Scenario", "Recovery_Percentage", "Net_Loss_Given_Default"
]

# Generate synthetic data
data = {
    "Customer_ID": [generate_id() for _ in range(num_records)],
    "Internal_ID": [generate_id() for _ in range(num_records)],
    "Original_Internal_ID": [generate_id() for _ in range(num_records)],
    "Obligor_Name": [generate_id()[:8] for _ in range(num_records)],  # Simulated names
    "City": ["City_" + str(random.randint(1, 100)) for _ in range(num_records)],
    "Country": [generate_country() for _ in range(num_records)],
    "Zip_Code": [str(random.randint(10000, 99999)) for _ in range(num_records)],
    "Facility_ID": [generate_id() for _ in range(num_records)],
    "Loan_Type": [generate_facility() for _ in range(num_records)],
    "Currency": [generate_currency() for _ in range(num_records)],
    "Commitment_Amount": [generate_amount() for _ in range(num_records)],
    "Outstanding_Balance": [generate_amount() for _ in range(num_records)],
    "Interest_Rate": [generate_interest_rate() for _ in range(num_records)],
    "Maturity_Date": [generate_date() for _ in range(num_records)],
}

# Fill remaining fields with random values
for field in fields[len(data):]:
    data[field] = [round(np.random.uniform(0, 1000000), 2) for _ in range(num_records)]

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("synthetic_FRY14Q_H1.csv", index=False)

print("✅ Synthetic FR Y-14Q H1 data generated and saved as 'synthetic_FRY14Q_H1.csv'.")