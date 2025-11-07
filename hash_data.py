# ----------------------------
# Imports
# ----------------------------
import pandas as pd
import hashlib
import matplotlib.pyplot as plt

# ----------------------------
# Hashing function
# ----------------------------
def hash_email(email):
    return hashlib.sha256(email.lower().encode()).hexdigest()

# ----------------------------
# Load CSVs and hash emails
# ----------------------------
company_a = pd.read_csv("company_A_customers.csv")
company_b = pd.read_csv("company_B_customers.csv")

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
company_a_hashed = pd.read_csv("company_A_customers_hashed.csv")
company_b_hashed = pd.read_csv("company_B_customers_hashed.csv")

overlap = pd.merge(company_a_hashed, company_b_hashed, on="hashed_email", how="inner")

# ----------------------------
# Display sample overlapping users and save CSV
# ----------------------------
print(f"Number of overlapping users: {len(overlap)}")
print("\nSample overlapping users:")
print(overlap.head())

overlap.to_csv("overlapping_users.csv", index=False)
print("\nOverlap CSV saved!")

# ----------------------------
# Visualization (optional)
# ----------------------------
plt.bar(['Overlapping Users'], [len(overlap)], color='skyblue')
plt.title('Number of Overlapping Users')
plt.ylabel('Count')
plt.show()



