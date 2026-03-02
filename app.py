from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    # 1. Load the data generated
    df = pd.read_csv('clinical_data.csv')
    
    # 2. Convert the table into a format the web can read
    # 'records' turns rows into a list of patient dictionaries
    patient_data = df.to_dict(orient='records')
    
    # 3. Send that data to our HTML file
    return render_template('index.html', patients=patient_data)

if __name__ == '__main__':
    app.run(debug=True)