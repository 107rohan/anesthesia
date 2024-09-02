import tkinter as tk
from tkinter import ttk, messagebox
import csv
import json
import os

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

# List of anesthesia drugs with their respective dosages
anesthesia_drugs = [
    {"drug_name": "Propofol", "dosage": "1.5-2.5 mg/kg"},
    {"drug_name": "Etomidate", "dosage": "0.2-0.3 mg/kg"},
    {"drug_name": "Thiopental", "dosage": "3-5 mg/kg"},
    {"drug_name": "Ketamine", "dosage": "1-2 mg/kg"},
    {"drug_name": "Fentanyl", "dosage": "1-2 mcg/kg"},
    {"drug_name": "Morphine", "dosage": "0.1-0.2 mg/kg"},
    {"drug_name": "Remifentanil", "dosage": "0.05-2 mcg/kg/min (infusion)"},
    {"drug_name": "Sufentanil", "dosage": "0.1-0.4 mcg/kg"},
    {"drug_name": "Hydromorphone", "dosage": "0.015 mg/kg"},
    {"drug_name": "Midazolam", "dosage": "0.025-0.1 mg/kg"},
    {"drug_name": "Lorazepam", "dosage": "0.02-0.06 mg/kg"},
    {"drug_name": "Diazepam", "dosage": "0.1-0.2 mg/kg"},
    {"drug_name": "Succinylcholine", "dosage": "1-1.5 mg/kg"},
    {"drug_name": "Rocuronium", "dosage": "0.6-1.2 mg/kg"},
    {"drug_name": "Vecuronium", "dosage": "0.1 mg/kg"},
    {"drug_name": "Cisatracurium", "dosage": "0.1-0.2 mg/kg"},
    {"drug_name": "Atracurium", "dosage": "0.4-0.5 mg/kg"},
    {"drug_name": "Neostigmine", "dosage": "0.04-0.08 mg/kg (with glycopyrrolate)"},
    {"drug_name": "Sugammadex", "dosage": "2-16 mg/kg (depending on the level of blockade)"},
    {"drug_name": "Flumazenil", "dosage": "0.2 mg (may repeat up to 1 mg)"},
    {"drug_name": "Naloxone", "dosage": "0.04-0.4 mg (titrate to effect)"},
    {"drug_name": "Sevoflurane", "dosage": "0.5-3% (inhalational)"},
    {"drug_name": "Isoflurane", "dosage": "0.5-2% (inhalational)"},
    {"drug_name": "Desflurane", "dosage": "3-9% (inhalational)"},
    {"drug_name": "Nitrous Oxide", "dosage": "25-70% (as an adjunct)"},
    {"drug_name": "Lidocaine", "dosage": "1-2 mg/kg (max dose without epinephrine: 4 mg/kg, with epinephrine: 7 mg/kg)"},
    {"drug_name": "Bupivacaine", "dosage": "1.5-2.5 mg/kg (max dose: 2.5 mg/kg without epinephrine)"},
    {"drug_name": "Ropivacaine", "dosage": "0.2-0.5 mg/kg (max dose: 3 mg/kg)"},
    {"drug_name": "Mepivacaine", "dosage": "1-2 mg/kg (max dose: 5 mg/kg without epinephrine)"},
    {"drug_name": "Dexmedetomidine", "dosage": "0.2-1 mcg/kg/hr (infusion)"},
    {"drug_name": "Propofol (sedative dose)", "dosage": "25-75 mcg/kg/min (infusion)"}
]

patients_list = []

def submit_patient_info():
    name = name_entry.get()
    age = age_entry.get()
    weight = weight_entry.get()
    height = height_entry.get()
    bp_systolic = bp_systolic_entry.get()
    bp_diastolic = bp_diastolic_entry.get()
    hr = hr_entry.get()
    rr = rr_entry.get()
    temp = temp_entry.get()
    spo2 = spo2_entry.get()
    asa = asa_entry.get()
    
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
        messagebox.showwarning("Patient Information Warning", "\n".join(abnormalities))
    
    # Store patient data
    patient_record = {
        "name": name,
        "age": age,
        "weight": weight,
        "height": height,
        "bp_systolic": bp_systolic,
        "bp_diastolic": bp_diastolic,
        "hr": hr,
        "rr": rr,
        "temp": temp,
        "spo2": spo2,
        "asa": asa,
        "abnormalities": abnormalities
    }
    
    patients_list.append(patient_record)
    save_patient_data()
    messagebox.showinfo("Success", "Patient information submitted successfully.")
    update_patient_list()

def submit_procedure_info():
    procedure_name = procedure_name_entry.get()
    
    if not patients_list:
        messagebox.showerror("Data Error", "Please enter patient information first.")
        return
    
    # Example of how patient data can influence procedure planning
    if len(patients_list) > 0 and patients_list[-1]["asa"] > 2:
        messagebox.showwarning("Risk Warning", f"Patient ASA classification is {patients_list[-1]['asa']}. This patient might be at higher risk for the procedure: {procedure_name}.")
    else:
        messagebox.showinfo("Procedure Info", f"Procedure {procedure_name} can be performed with standard anesthesia protocols.")

def search_patients():
    query = search_entry.get()
    search_results.delete(*search_results.get_children())
    for patient in patients_list:
        if query.lower() in patient["name"].lower():
            search_results.insert("", tk.END, values=(
                patient["name"],
                patient["age"],
                patient["weight"],
                patient["height"],
                patient["bp_systolic"],
                patient["bp_diastolic"],
                patient["hr"],
                patient["rr"],
                patient["temp"],
                patient["spo2"],
                patient["asa"]
            ))

def update_patient_list():
    search_results.delete(*search_results.get_children())
    for patient in patients_list:
        search_results.insert("", tk.END, values=(
            patient["name"],
            patient["age"],
            patient["weight"],
            patient["height"],
            patient["bp_systolic"],
            patient["bp_diastolic"],
            patient["hr"],
            patient["rr"],
            patient["temp"],
            patient["spo2"],
            patient["asa"]
        ))

def save_patient_data():
    if not os.path.exists('patient_data'):
        os.makedirs('patient_data')

    with open('patient_data/patients_data.json', 'w') as file:
        json.dump(patients_list, file, indent=4)

def open_patient_info_tab():
    for widget in patient_info_frame.winfo_children():
        widget.destroy()
    
    tk.Label(patient_info_frame, text="Patient Name:").grid(row=0, column=0, padx=10, pady=5)
    global name_entry
    name_entry = tk.Entry(patient_info_frame)
    name_entry.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(patient_info_frame, text="Age:").grid(row=1, column=0, padx=10, pady=5)
    global age_entry
    age_entry = tk.Entry(patient_info_frame)
    age_entry.grid(row=1, column=1, padx=10, pady=5)
    
    tk.Label(patient_info_frame, text="Weight (kg):").grid(row=2, column=0, padx=10, pady=5)
    global weight_entry
    weight_entry = tk.Entry(patient_info_frame)
    weight_entry.grid(row=2, column=1, padx=10, pady=5)
    
    tk.Label(patient_info_frame, text="Height (cm):").grid(row=3, column=0, padx=10, pady=5)
    global height_entry
    height_entry = tk.Entry(patient_info_frame)
    height_entry.grid(row=3, column=1, padx=10, pady=5)
    
    tk.Label(patient_info_frame, text="Blood Pressure Systolic (mmHg):").grid(row=4, column=0, padx=10, pady=5)
    global bp_systolic_entry
    bp_systolic_entry = tk.Entry(patient_info_frame)
    bp_systolic_entry.grid(row=4, column=1, padx=10, pady=5)
    
    tk.Label(patient_info_frame, text="Blood Pressure Diastolic (mmHg):").grid(row=5, column=0, padx=10, pady=5)
    global bp_diastolic_entry
    bp_diastolic_entry = tk.Entry(patient_info_frame)
    bp_diastolic_entry.grid(row=5, column=1, padx=10, pady=5)
    
    tk.Label(patient_info_frame, text="Heart Rate (bpm):").grid(row=6, column=0, padx=10, pady=5)
    global hr_entry
    hr_entry = tk.Entry(patient_info_frame)
    hr_entry.grid(row=6, column=1, padx=10, pady=5)
    
    tk.Label(patient_info_frame, text="Respiratory Rate (breaths/min):").grid(row=7, column=0, padx=10, pady=5)
    global rr_entry
    rr_entry = tk.Entry(patient_info_frame)
    rr_entry.grid(row=7, column=1, padx=10, pady=5)
    
    tk.Label(patient_info_frame, text="Temperature (°C):").grid(row=8, column=0, padx=10, pady=5)
    global temp_entry
    temp_entry = tk.Entry(patient_info_frame)
    temp_entry.grid(row=8, column=1, padx=10, pady=5)
    
    tk.Label(patient_info_frame, text="Oxygen Saturation (%):").grid(row=9, column=0, padx=10, pady=5)
    global spo2_entry
    spo2_entry = tk.Entry(patient_info_frame)
    spo2_entry.grid(row=9, column=1, padx=10, pady=5)
    
    tk.Label(patient_info_frame, text="ASA Classification (1-5):").grid(row=10, column=0, padx=10, pady=5)
    global asa_entry
    asa_entry = tk.Entry(patient_info_frame)
    asa_entry.grid(row=10, column=1, padx=10, pady=5)
    
    submit_button = tk.Button(patient_info_frame, text="Submit", command=submit_patient_info)
    submit_button.grid(row=11, columnspan=2, pady=20)
    
    # Add Search Widgets
    tk.Label(patient_info_frame, text="Search Patient Data:").grid(row=12, column=0, padx=10, pady=5)
    global search_entry
    search_entry = tk.Entry(patient_info_frame)
    search_entry.grid(row=12, column=1, padx=10, pady=5)
    
    search_button = tk.Button(patient_info_frame, text="Search", command=search_patients)
    search_button.grid(row=12, column=2, padx=10, pady=5)
    
    # Patient List Treeview
    columns = ("Name", "Age", "Weight (kg)", "Height (cm)", "BP Systolic (mmHg)", "BP Diastolic (mmHg)", "Heart Rate (bpm)", "Respiratory Rate (breaths/min)", "Temperature (°C)", "Oxygen Saturation (%)", "ASA Classification")
    global search_results
    search_results = ttk.Treeview(patient_info_frame, columns=columns, show="headings")
    for col in columns:
        search_results.heading(col, text=col)
    search_results.grid(row=13, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")
    
    update_patient_list()

def open_procedure_info_tab():
    for widget in procedure_info_frame.winfo_children():
        widget.destroy()
    
    tk.Label(procedure_info_frame, text="Procedure Name:").grid(row=0, column=0, padx=10, pady=5)
    global procedure_name_entry
    procedure_name_entry = tk.Entry(procedure_info_frame)
    procedure_name_entry.grid(row=0, column=1, padx=10, pady=5)
    
    submit_button = tk.Button(procedure_info_frame, text="Submit", command=submit_procedure_info)
    submit_button.grid(row=1, columnspan=2, pady=20)

def open_anesthesia_drugs_tab():
    for widget in anesthesia_drugs_frame.winfo_children():
        widget.destroy()
    
    columns = ("Drug Name", "Dosage")
    table = ttk.Treeview(anesthesia_drugs_frame, columns=columns, show="headings")
    table.heading("Drug Name", text="Drug Name")
    table.heading("Dosage", text="Dosage")
    
    for drug in anesthesia_drugs:
        table.insert("", tk.END, values=(drug["drug_name"], drug["dosage"]))
    
    table.pack(fill=tk.BOTH, expand=True)

# Main application window
root = tk.Tk()
root.title("Anesthesia Management System")

# Create a Notebook (tabbed interface)
notebook = ttk.Notebook(root)

# Create frames for each tab
patient_info_frame = ttk.Frame(notebook)
procedure_info_frame = ttk.Frame(notebook)
anesthesia_drugs_frame = ttk.Frame(notebook)

# Add frames to the notebook
notebook.add(patient_info_frame, text="Patient Information")
notebook.add(procedure_info_frame, text="Procedure Information")
notebook.add(anesthesia_drugs_frame, text="Anesthesia Drugs and Dosages")
notebook.pack(expand=1, fill="both")

# Open tabs
open_patient_info_tab()
open_procedure_info_tab()
open_anesthesia_drugs_tab()

root.mainloop()
