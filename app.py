from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    file_path = 'analyzed_alerts.csv'
    if not os.path.exists(file_path):
        return f"Error: {file_path} not found. Run analysis.py first!", 500
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    patient_data = df.to_dict(orient='records')
    
    return render_template('index.html', patients=patient_data)

if __name__ == '__main__':
    app.run(debug=os.environ.get('FLASK_DEBUG') =='1')
