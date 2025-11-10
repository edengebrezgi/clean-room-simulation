import pandas as pd

# Load the overlapping users dataset from Project 1
overlap = pd.read_csv("overlapping_users.csv")
import numpy as np

# If age columns do not exist, generate demo ages
if 'age_x' not in overlap.columns and 'age_y' not in overlap.columns:
    overlap['age_x'] = np.random.randint(18, 65, size=len(overlap))
    overlap['age_y'] = np.random.randint(18, 65, size=len(overlap))


# Show the first few rows to confirm the file loaded
print("Loaded overlapping users:")
print(overlap.head())

from diffprivlib.mechanisms import Laplace

# Choose the privacy budget (epsilon)
epsilon = 1.0  # Lower = more privacy, Higher = more accuracy

# Option 1: Use Company A ages
true_avg_age = overlap['age_x'].mean()

# or Option 2: Use Company B ages
# true_avg_age = overlap['age_y'].mean()

# or Option 3: Take the average between both companies per user
# true_avg_age = ((overlap['age_x'] + overlap['age_y']) / 2).mean()


# Apply Differential Privacy using Laplace mechanism
# Sensitivity for mean of ages (assuming ages range ~0-100) is about 1
mechanism = Laplace(epsilon=epsilon, sensitivity=1)
private_avg_age = mechanism.randomise(true_avg_age)

print("\nTrue Average Age:", round(true_avg_age, 2))
print("Private Average Age (with noise):", round(private_avg_age, 2))
