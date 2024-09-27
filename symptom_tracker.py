import streamlit as st

# Dictionary to store user symptom history
symptom_history = {}

# Function to track user symptoms over time
def track_symptoms(symptoms, disease):
    if disease not in symptom_history:
        symptom_history[disease] = []
    symptom_history[disease].append(symptoms)
    
    # Display the symptom history
    st.write(f"Symptom history for {disease}:")
    for entry in symptom_history[disease]:
        st.write(f"- {entry}")

# Function to analyze symptom trends and send alerts
def analyze_symptom_trends():
    for disease, symptoms in symptom_history.items():
        if len(symptoms) > 5:  # If symptoms persist or worsen, send an alert
            st.warning(f"Alert: Persistent or worsening symptoms detected for {disease}. Please consider consulting a healthcare provider.")

# Save this file as 'symptom_tracker.py'
