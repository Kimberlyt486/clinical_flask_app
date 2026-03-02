from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    file_path = 'analyzed_alerts.csv'
    
    if not os.path.exists(file_path):
        return f"Error: {file_path} not found. Run analysis.py first!"

    # Read the CSV
    df = pd.read_csv(file_path)
    
    # Clean up column names (removes hidden spaces)
    df.columns = df.columns.str.strip()
    
    # Convert to list of dictionaries
    patient_data = df.to_dict(orient='records')
    
    # DEBUG: See the first row in your terminal
    if patient_data:
        print("--- SERVER DATA CHECK ---")
        print(f"First Patient Keys: {list(patient_data[0].keys())}")
    
    return render_template('index.html', patients=patient_data)

if __name__ == '__main__':
    app.run(debug=True)