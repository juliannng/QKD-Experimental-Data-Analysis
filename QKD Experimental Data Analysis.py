import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Experimental Data
# Replace these filenames with your actual dataset files
qued_data = pd.read_csv("quED_data.csv")        # columns: angle_diff, coincidences
cerberus_data = pd.read_csv("cerberus_data.csv") # columns: trial, qber_with_attack, qber_without_attack

# 2. Process Correlation Data (from quED)
# Normalize coincidences to get correlation values between 0 and 1
max_coincidences = qued_data["coincidences"].max()
qued_data["correlation"] = qued_data["coincidences"] / max_coincidences

# Visibility is a measure of how sharp the correlation curve is
max_corr = qued_data["correlation"].max()
min_corr = qued_data["correlation"].min()
visibility = (max_corr - min_corr) / (max_corr + min_corr)

# 3. Process QBER Data (from Cerberus)
# Average values across multiple trials
qber_no_attack = cerberus_data["qber_without_attack"].mean()
qber_attack = cerberus_data["qber_with_attack"].mean()

# 4. Print Key Metrics
print("=== Key QKD Metrics ===")
print(f"Visibility: {visibility:.3f}")
print(f"QBER (no attack): {qber_no_attack:.2%}")
print(f"QBER (with attack): {qber_attack:.2%}")
print("========================")

# 5. Visualization

#Polarization Correlation Curve
plt.figure(figsize=(8,5))
plt.plot(qued_data["angle_diff"], qued_data["correlation"], "o-", color="blue", label="Correlation")
plt.xlabel("Analyzer Angle Difference (°)")
plt.ylabel("Normalized Correlation")
plt.title("Polarization Correlation Curve")
plt.legend()
plt.grid(True)
plt.show()

#QBER Comparison
plt.figure(figsize=(6,4))
plt.bar(["No Attack", "With Attack"],
        [qber_no_attack, qber_attack],
        color=["green","red"])
plt.ylabel("Quantum Bit Error Rate (QBER)")
plt.title("Effect of Eavesdropping on QBER")
plt.show()