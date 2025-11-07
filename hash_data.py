# ----------------------------
# Imports
# ----------------------------
import pandas as pd
import hashlib

# ----------------------------
# Hashing function
# ----------------------------
def hash_email(email):
    return hashlib.sha256(email.lower().encode()).hexdigest()

# ----------------------------
# Load CSVs and hash emails
# ----------------------------
# Load Company A CSV
company_a = pd.read_csv("company_A_customers.csv")
# Load Company B CSV
company_b = pd.read_csv("company_B_customers.csv")

# Hash the emails
company_a['hashed_email'] = company_a['email'].apply(hash_email)
company_b['hashed_email'] = company_b['email'].apply(hash_email)

# ----------------------------
# Drop raw emails and save hashed CSVs
# ----------------------------
company_a_hashed = company_a.drop(columns=['email'])
company_b_hashed = company_b.drop(columns=['email'])

company_a_hashed.to_csv("company_A_customers_hashed.csv", index=False)
company_b_hashed.to_csv("company_B_customers_hashed.csv", index=False)

print("Hashing complete. Hashed CSVs saved!")

# ----------------------------
# Privacy-safe inner join
# ----------------------------
# Load hashed CSVs (optional if re-running)
company_a_hashed = pd.read_csv("company_A_customers_hashed.csv")
company_b_hashed = pd.rea

