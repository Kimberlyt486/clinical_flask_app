#  ICU Respiratory Triage Dashboard
### *Automating Clinical Math & ARDS Triage with Python*

## Project Overview
As a Respiratory Therapist with years of clinical experience, I recognized a "data silo" problem at the bedside: critical metrics like **P/F Ratios** and **Static Compliance** are often buried in ventilator sub-menus or require manual calculation.

This project is a **Full-Stack Data Pipeline** that simulates ICU ventilator data, performs automated clinical analysis using **Pandas**, and visualizes patient priority through a **Flask-based Web Dashboard**.

---

##  The Tech Stack
* **Language:** Python 3.x
* **Data Analysis:** Pandas (Vectorized clinical calculations)
* **Web Framework:** Flask (Backend routing & server)
* **Frontend:** HTML5, Jinja2 (Template logic), Bootstrap 5 (Responsive UI)
* **Data Storage:** CSV (Simulated EMR export)

---

## Clinical Logic & Features
The application processes a 15-bed ICU unit, providing a longitudinal view of lung function:

1.  **Automated Calculations:** * **P/F Ratio:** $PaO_2 / FiO_2$ (Standardized ARDS assessment)
    * **Compliance:** $V_t / (P_{plat} - PEEP)$ (Lung mechanics)
2.  **Color-Coded Triage:**
    * 🔴 **Severe (P/F < 100):** Immediate intervention required.
    * 🟡 **Moderate (P/F < 200):** High-risk monitoring.
    * ⚪ **Stable:** Routine care.
3.  **Accordion View:** Groups 75 individual readings into 15 "Patient Cards" to show trends over time without cluttering the UI.

---

##  How to Run the Project

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Kimberlyt486/clinical_flask_app.git](https://github.com/Kimberlyt486/clinical_flask_app.git)
   cd clinical_flask_app
2. **Create the environment:**
    ```bash
    python -m venv venv
3. **Activate it:**
    ```bash
    .\venv\Scripts\activate
4. **Install Dependencies:**
    ```bash
    pip install pandas flask
5. **Run the Clinical Pipeline:**
    ```bash
    python data_gen.py  (to create clinical_data.csv)
    python analysis.py (to create analyzed_alerts.csv)
    python app.py (to launch the dashboard)
6. **View the Dashboard:**

    Open your web browser and go to: http://127.0.0.1:5000
