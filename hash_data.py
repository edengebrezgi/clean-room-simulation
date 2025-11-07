import pandas as pd
import hashlib
import hashlib

# Function to hash emails
def hash_email(email):
    return hashlib.sha256(email.lower().encode()).hexdigest()

import pandas as pd

# Load Company A CSV
company_a = pd.read_csv("company_A_customers.csv")
# Load Company B CSV
company_b = pd.read_csv("company_B_customers.csv")

# Hash the emails
company_a['hashed_email'] = company_a['email'].apply(hash_email)
company_b['hashed_email'] = company_b['email'].apply(hash_email)

# Load Company A CSV
company_a = pd.read_csv("company_A_customers.csv")
# Load Company B CSV
company_b = pd.read_csv("company_B_customers.csv")

# Hash the emails
company_a['hashed_email'] = company_a['email'].apply(hash_email)
company_b['hashed_email'] = company_b['email'].apply(hash_email)

# Drop original emails for privacy
company_a_hashed = company_a.drop(columns=['email'])
company_b_hashed = company_b.drop(columns=['email'])

# Save the hashed datasets
company_a_hashed.to_csv("company_A_customers_hashed.csv", index=False)
company_b_hashed.to_csv("company_B_customers_hashed.csv", index=False)

print("Hashing complete. Hashed CSVs saved!")


# Load the hashed CSVs
company_a_hashed = pd.read_csv("company_A_customers_hashed.csv")
company_b_hashed = pd.read_csv("company_B_customers_hashed.csv")

# Perform inner join on hashed_email
overlap = pd.merge(company_a_hashed, company_b_hashed, on="hashed_email", how="inner")

# Show number of overlapping users
print(f"Number of overlapping users: {len(overlap)}")

# Show some sample overlapping data
print("\nSample overlapping users:")
print(overlap.head())

# Optional: Save the overlap table
overlap.to_csv("overlapping_users.csv", index=False)
print("\nOverlap CSV saved!")

