import tkinter as tk
from tkinter import ttk, messagebox

# Define normal ranges for vital signs
NORMAL_RANGES = {
    "weight": (30, 200),  # kg
    "height": (100, 220),  # cm
    "bp_systolic": (90, 140),  # mmHg
    "bp_diastolic": (60, 90),  # mmHg
    "hr": (60, 100),  # bpm
    "rr": (12, 20),  # breaths/min
    "temp": (36.5, 37.5),  # °C
    "spo2": (95, 100)  # %
}

# Define a list of anesthesia drugs with their respective dosages
anesthesia_drugs = [
    # Intravenous Induction Agents
    {"drug_name": "Propofol", "dosage": "1.5-2.5 mg/kg"},
    {"drug_name": "Etomidate", "dosage": "0.2-0.3 mg/kg"},
    {"drug_name": "Thiopental", "dosage": "3-5 mg/kg"},
    {"drug_name": "Ketamine", "dosage": "1-2 mg/kg"},

    # Opioids (Analgesics)
    {"drug_name": "Fentanyl", "dosage": "1-2 mcg/kg"},
    {"drug_name": "Morphine", "dosage": "0.1-0.2 mg/kg"},
    {"drug_name": "Remifentanil", "dosage": "0.05-2 mcg/kg/min (infusion)"},
    {"drug_name": "Sufentanil", "dosage": "0.1-0.4 mcg/kg"},
    {"drug_name": "Hydromorphone", "dosage": "0.015 mg/kg"},

    # Benzodiazepines (Anxiolytics and Amnestics)
    {"drug_name": "Midazolam", "dosage": "0.025-0.1 mg/kg"},
    {"drug_name": "Lorazepam", "dosage": "0.02-0.06 mg/kg"},
    {"drug_name": "Diazepam", "dosage": "0.1-0.2 mg/kg"},

    # Neuromuscular Blocking Agents (Paralytics)
    {"drug_name": "Succinylcholine", "dosage": "1-1.5 mg/kg"},
    {"drug_name": "Rocuronium", "dosage": "0.6-1.2 mg/kg"},
    {"drug_name": "Vecuronium", "dosage": "0.1 mg/kg"},
    {"drug_name": "Cisatracurium", "dosage": "0.1-0.2 mg/kg"},
    {"drug_name": "Atracurium", "dosage": "0.4-0.5 mg/kg"},

    # Reversal Agents
    {"drug_name": "Neostigmine", "dosage": "0.04-0.08 mg/kg (with glycopyrrolate)"},
    {"drug_name": "Sugammadex", "dosage": "2-16 mg/kg (depending on the level of blockade)"},
    {"drug_name": "Flumazenil", "dosage": "0.2 mg (may repeat up to 1 mg)"},
    {"drug_name": "Naloxone", "dosage": "0.04-0.4 mg (titrate to effect)"},

    # Inhalational Anesthetics
    {"drug_name": "Sevoflurane", "dosage": "0.5-3% (inhalational)"},
    {"drug_name": "Isoflurane", "dosage": "0.5-2% (inhalational)"},
    {"drug_name": "Desflurane", "dosage": "3-9% (inhalational)"},
    {"drug_name": "Nitrous Oxide", "dosage": "25-70% (as an adjunct)"},

    # Local Anesthetics
    {"drug_name": "Lidocaine", "dosage": "1-2 mg/kg (max dose without epinephrine: 4 mg/kg, with epinephrine: 7 mg/kg)"},
    {"drug_name": "Bupivacaine", "dosage": "1.5-2.5 mg/kg (max dose: 2.5 mg/kg without epinephrine)"},
    {"drug_name": "Ropivacaine", "dosage": "0.2-0.5 mg/kg (max dose: 3 mg/kg)"},
    {"drug_name": "Mepivacaine", "dosage": "1-2 mg/kg (max dose: 5 mg/kg without epinephrine)"},

    # Sedatives and Hypnotics
    {"drug_name": "Dexmedetomidine", "dosage": "0.2-1 mcg/kg/hr (infusion)"},
    {"drug_name": "Propofol (sedative dose)", "dosage": "25-75 mcg/kg/min (infusion)"}
]

def open_table_window():
    table_window = tk.Toplevel(root)
    table_window.title("Anesthesia Drugs and Dosages")
    
    columns = ("Drug Name", "Dosage")
    table = ttk.Treeview(table_window, columns=columns, show="headings")
    table.heading("Drug Name", text="Drug Name")
    table.heading("Dosage", text="Dosage")
    
    for drug in anesthesia_drugs:
        table.insert("", tk.END, values=(drug["drug_name"], drug["dosage"]))
    
    table.pack(fill=tk.BOTH, expand=True)

def open_patient_info_window():
    patient_info_window = tk.Toplevel(root)
    patient_info_window.title("Enter Patient Information")
    
    tk.Label(patient_info_window, text="Patient Name:").grid(row=0, column=0, padx=10, pady=5)
    name_entry = tk.Entry(patient_info_window)
    name_entry.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(patient_info_window, text="Age:").grid(row=1, column=0, padx=10, pady=5)
    age_entry = tk.Entry(patient_info_window)
    age_entry.grid(row=1, column=1, padx=10, pady=5)
    
    tk.Label(patient_info_window, text="Weight (kg):").grid(row=2, column=0, padx=10, pady=5)
    weight_entry = tk.Entry(patient_info_window)
    weight_entry.grid(row=2, column=1, padx=10, pady=5)
    
    tk.Label(patient_info_window, text="Height (cm):").grid(row=3, column=0, padx=10, pady=5)
    height_entry = tk.Entry(patient_info_window)
    height_entry.grid(row=3, column=1, padx=10, pady=5)
    
    tk.Label(patient_info_window, text="Blood Pressure Systolic (mmHg):").grid(row=4, column=0, padx=10, pady=5)
    bp_systolic_entry = tk.Entry(patient_info_window)
    bp_systolic_entry.grid(row=4, column=1, padx=10, pady=5)
    
    tk.Label(patient_info_window, text="Blood Pressure Diastolic (mmHg):").grid(row=5, column=0, padx=10, pady=5)
    bp_diastolic_entry = tk.Entry(patient_info_window)
    bp_diastolic_entry.grid(row=5, column=1, padx=10, pady=5)
    
    tk.Label(patient_info_window, text="Heart Rate (bpm):").grid(row=6, column=0, padx=10, pady=5)
    hr_entry = tk.Entry(patient_info_window)
    hr_entry.grid(row=6, column=1, padx=10, pady=5)
    
    tk.Label(patient_info_window, text="Respiratory Rate (breaths/min):").grid(row=7, column=0, padx=10, pady=5)
    rr_entry = tk.Entry(patient_info_window)
    rr_entry.grid(row=7, column=1, padx=10, pady=5)
    
    tk.Label(patient_info_window, text="Temperature (°C):").grid(row=8, column=0, padx=10, pady=5)
    temp_entry = tk.Entry(patient_info_window)
    temp_entry.grid(row=8, column=1, padx=10, pady=5)
    
    tk.Label(patient_info_window, text="Oxygen Saturation (%):").grid(row=9, column=0, padx=10, pady=5)
    spo2_entry = tk.Entry(patient_info_window)
    spo2_entry.grid(row=9, column=1, padx=10, pady=5)
    
    tk.Label(patient_info_window, text="ASA Classification (1-5):").grid(row=10, column=0, padx=10, pady=5)
    asa_entry = tk.Entry(patient_info_window)
    asa_entry.grid(row=10, column=1, padx=10, pady=5)
    
    submit_button = tk.Button(patient_info_window, text="Submit", command=lambda: submit_patient_info(
        name_entry.get(),
        age_entry.get(),
               weight_entry.get(),
        height_entry.get(),
        bp_systolic_entry.get(),
        bp_diastolic_entry.get(),
        hr_entry.get(),
        rr_entry.get(),
        temp_entry.get(),
        spo2_entry.get(),
        asa_entry.get()
    ))
    submit_button.grid(row=11, columnspan=2, pady=20)

def submit_patient_info(name, age, weight, height, bp_systolic, bp_diastolic, hr, rr, temp, spo2, asa):
    # Validate ASA Classification
    try:
        asa = int(asa)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid ASA classification.")
        return
    
    if asa < 1 or asa > 5:
        messagebox.showerror("ASA Classification Error", "ASA classification must be between 1 and 5.")
        return
    
    # Validate and flag abnormal values
    abnormalities = []
    
    try:
        weight = float(weight)
        if not (NORMAL_RANGES["weight"][0] <= weight <= NORMAL_RANGES["weight"][1]):
            abnormalities.append(f"Weight {weight} kg is outside normal range.")
    except ValueError:
        abnormalities.append("Weight must be a number.")
    
    try:
        height = float(height)
        if not (NORMAL_RANGES["height"][0] <= height <= NORMAL_RANGES["height"][1]):
            abnormalities.append(f"Height {height} cm is outside normal range.")
    except ValueError:
        abnormalities.append("Height must be a number.")
    
    try:
        bp_systolic = float(bp_systolic)
        bp_diastolic = float(bp_diastolic)
        if not (NORMAL_RANGES["bp_systolic"][0] <= bp_systolic <= NORMAL_RANGES["bp_systolic"][1]):
            abnormalities.append(f"Systolic Blood Pressure {bp_systolic} mmHg is outside normal range.")
        if not (NORMAL_RANGES["bp_diastolic"][0] <= bp_diastolic <= NORMAL_RANGES["bp_diastolic"][1]):
            abnormalities.append(f"Diastolic Blood Pressure {bp_diastolic} mmHg is outside normal range.")
    except ValueError:
        abnormalities.append("Blood Pressure must be numeric values.")
    
    try:
        hr = float(hr)
        if not (NORMAL_RANGES["hr"][0] <= hr <= NORMAL_RANGES["hr"][1]):
            abnormalities.append(f"Heart Rate {hr} bpm is outside normal range.")
    except ValueError:
        abnormalities.append("Heart Rate must be a number.")
    
    try:
        rr = float(rr)
        if not (NORMAL_RANGES["rr"][0] <= rr <= NORMAL_RANGES["rr"][1]):
            abnormalities.append(f"Respiratory Rate {rr} breaths/min is outside normal range.")
    except ValueError:
        abnormalities.append("Respiratory Rate must be a number.")
    
    try:
        temp = float(temp)
        if not (NORMAL_RANGES["temp"][0] <= temp <= NORMAL_RANGES["temp"][1]):
            abnormalities.append(f"Temperature {temp} °C is outside normal range.")
    except ValueError:
        abnormalities.append("Temperature must be a number.")
    
    try:
        spo2 = float(spo2)
        if not (NORMAL_RANGES["spo2"][0] <= spo2 <= NORMAL_RANGES["spo2"][1]):
            abnormalities.append(f"Oxygen Saturation {spo2} % is outside normal range.")
    except ValueError:
        abnormalities.append("Oxygen Saturation must be a number.")
    
    if abnormalities:
        messagebox.showwarning("Abnormal Values", "\n".join(abnormalities))
    else:
        messagebox.showinfo("Patient Information", "Patient information submitted successfully.")

def open_procedure_entry_window():
    procedure_window = tk.Toplevel(root)
    procedure_window.title("Enter Procedure Information")
    
    tk.Label(procedure_window, text="Procedure Name:").grid(row=0, column=0, padx=10, pady=5)
    procedure_name_entry = tk.Entry(procedure_window)
    procedure_name_entry.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(procedure_window, text="ASA Classification (1-5):").grid(row=1, column=0, padx=10, pady=5)
    asa_entry = tk.Entry(procedure_window)
    asa_entry.grid(row=1, column=1, padx=10, pady=5)
    
    submit_button = tk.Button(procedure_window, text="Submit", command=lambda: submit_procedure_info(
        procedure_name_entry.get(),
        asa_entry.get()
    ))
    submit_button.grid(row=2, columnspan=2, pady=20)

def submit_procedure_info(procedure_name, asa):
    try:
        asa = int(asa)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid ASA classification.")
        return

    if asa < 1 or asa > 5:
        messagebox.showerror("ASA Classification Error", "ASA classification must be between 1 and 5.")
        return

    if asa in (1, 2):
        risk_level = "Low Risk"
    elif asa in (3, 4):
        risk_level = "Moderate Risk"
    else:
        risk_level = "High Risk"

    # Generate anesthetic plan based on ASA classification
    plan = ""
    if asa == 1:
        plan = "General anesthesia with minimal monitoring."
    elif asa == 2:
        plan = "General anesthesia with standard monitoring."
    elif asa == 3:
        plan = "Regional or general anesthesia with close monitoring."
    elif asa == 4:
        plan = "Intensive monitoring and possible additional resources."
    elif asa == 5:
        plan = "Advanced preparation and possible additional support required."

    messagebox.showinfo("Procedure Details", f"Procedure Name: {procedure_name}\nRisk Level: {risk_level}\nAnesthetic Plan: {plan}")

# Main application window (landing page)
root = tk.Tk()
root.title("Anesthesia App")

# Create a label for the landing page
welcome_label = tk.Label(root, text="Welcome to the Anesthesia App", font=("Arial", 24))
welcome_label.pack(pady=20)

# Create a button to open the table window
open_table_button = tk.Button(root, text="View Anesthesia Drugs and Dosages", font=("Arial", 16), command=open_table_window)
open_table_button.pack(pady=20)

# Create a button to open the patient info window
open_patient_info_button = tk.Button(root, text="Enter Patient Information", font=("Arial", 16), command=open_patient_info_window)
open_patient_info_button.pack(pady=20)

# Create a button to open the procedure entry window
open_procedure_button = tk.Button(root, text="Enter Procedure Information", font=("Arial", 16), command=open_procedure_entry_window)
open_procedure_button.pack(pady=20)

# Start the main event loop
root.mainloop()

