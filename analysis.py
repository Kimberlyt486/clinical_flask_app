import pandas as pd

def run_clinical_analysis(input_file):
    try:
        # 1. Load the raw data (15 patients x 5 readings = 75 rows)
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: {input_file} not found. Please run your data_gen.py first.")
        return

    # 2. Perform Clinical Calculations
    # PF Ratio = PaO2 / (FiO2 as a decimal)
    df['PF_Ratio'] = df['PaO2'] / (df['FiO2'] / 100)
    
    # Static Compliance = Vt / (P_Plat - PEEP)
    # .clip(lower=1) prevents division by zero errors
    df['Compliance'] = df['V_t'] / (df['P_Plat'] - df['PEEP']).clip(lower=1)

    # 3. Apply Triage Status Logic
    def get_status(ratio):
        if ratio < 100: return "SEVERE (ARDS)"
        if ratio < 200: return "MODERATE (ARDS)"
        if ratio < 300: return "MILD (ARDS)"
        return "STABLE"

    df['Status'] = df['PF_Ratio'].apply(get_status)

    # 4. Sorting for the Dashboard
    # This ensures that Bed-101 comes before Bed-102, 
    # and the 2:00 PM reading comes before the 12:00 PM reading.
    df = df.sort_values(by=['Patient_ID', 'Timestamp'], ascending=[True, False])

    # 5. Export to the Flask-ready CSV
    df.to_csv('analyzed_alerts.csv', index=False)
    
    print("--- ANALYSIS SUCCESSFUL ---")
    print(f"Total Readings Processed: {len(df)}")
    print(f"Unique Beds Analyzed: {df['Patient_ID'].nunique()}")
    print("File 'analyzed_alerts.csv' is ready for the dashboard.")

if __name__ == "__main__":
    run_clinical_analysis('clinical_data.csv')