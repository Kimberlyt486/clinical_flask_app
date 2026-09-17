import pandas as pd

def run_clinical_analysis(input_file):
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: {input_file} not found. Please run your data_gen.py first.")
        return

    # FiO2 is recorded as a percentage; P/F ratio expects a decimal
    df['PF_Ratio'] = df['PaO2'] / (df['FiO2'] / 100)
    
    # Static Compliance = Vt / (P_Plat - PEEP)
    driving_pressure = df['P_Plat'] - df['PEEP']
    df['Valid_Reading'] = driving_pressure > 0
    df['Compliance'] = (df['V_t'] / driving_pressure).where(df['Valid_Reading'])

  
    def get_status(ratio):
        if ratio <= 100: return "SEVERE (ARDS)"
        if ratio <= 200: return "MODERATE (ARDS)"
        if ratio <= 300: return "MILD (ARDS)"
        return "STABLE"

    df['Status'] = df['PF_Ratio'].apply(get_status)

   # Newest reading first within each bed, so the dashboard shows current state
    df = df.sort_values(by=['Patient_ID', 'Timestamp'], ascending=[True, False])


    df.to_csv('analyzed_alerts.csv', index=False)
    
    print("--- ANALYSIS SUCCESSFUL ---")
    print(f"Total Readings Processed: {len(df)}")
    invalid_count = (~df['Valid_Reading']).sum()
    if invalid_count:
        print(f"WARNING: {invalid_count} reading(s) had invalid pressures — compliance not calculated.")
    print(f"Unique Beds Analyzed: {df['Patient_ID'].nunique()}")
    print("File 'analyzed_alerts.csv' is ready for the dashboard.")

if __name__ == "__main__":
    run_clinical_analysis('clinical_data.csv')
