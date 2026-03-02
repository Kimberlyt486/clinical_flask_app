import pandas as pd

data = {
    'Patient_ID': ['PT-101', 'PT-102', 'PT-103', 'PT-104'],
    'PaO2': [95, 62, 58, 110],
    'FiO2': [0.21, 0.50, 0.80, 0.40],
    'PEEP': [5, 10, 15, 8],
    'Vt': [450, 420, 400, 500],      # Tidal Volume in mL
    'Pplat': [20, 30, 35, 22]        # Plateau Pressure in cmH2O
}

df = pd.DataFrame(data)

# Calculation 1: P/F Ratio
df['PF_Ratio'] = df['PaO2'] / df['FiO2']

# Calculation 2: Static Compliance
df['Compliance'] = df['Vt'] / (df['Pplat'] - df['PEEP'])

# Save
df.to_csv('clinical_data.csv', index=False)
print("Updated CSV with Compliance data.")