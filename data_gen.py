import pandas as pd
import random
from datetime import datetime, timedelta

def generate_icu_data(file_name='clinical_data.csv'):
    data = []
    # 1. Generate 15 Patient IDs 
    patients = [f"Bed-{i}" for i in range(101, 116)]
    
    now = datetime.now()
    
    for p_id in patients:
        
        for i in range(5):
            # Space out readings by 2 hours
            timestamp = (now - timedelta(hours=i*2)).strftime("%Y-%m-%d %H:%M")
            
            # Clinical randomization
            paO2 = random.randint(55, 120)
            fiO2 = random.choice([21, 30, 40, 50, 60, 80, 100])
            peep = random.randint(5, 15)
            p_plat = random.randint(18, 35)
            v_t = random.randint(350, 550)
            
            data.append([p_id, timestamp, paO2, fiO2, peep, p_plat, v_t])

    df = pd.DataFrame(data, columns=['Patient_ID', 'Timestamp', 'PaO2', 'FiO2', 'PEEP', 'P_Plat', 'V_t'])
    df.to_csv(file_name, index=False)
    print(f"Generated readings for {len(patients)} patients.")

if __name__ == "__main__":
    generate_icu_data()