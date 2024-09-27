import streamlit as st
from voice_assistant import voice_assistant_intro, listen, speak
from diagnosis import query_biobert_classification, confirm_diagnosis
from disease_data import get_disease_info, get_follow_up_questions
from symptom_tracker import track_symptoms, analyze_symptom_trends

# Main Streamlit Web Interface
st.title("Comprehensive Healthcare Diagnosis System")

# Voice Assistant introduction
voice_assistant_intro()

# Display a pop-up with instructions
st.info("""
    **Instructions:**
    1. Describe your symptoms in the chatbox or use the voice assistant.
    2. The system will diagnose the condition using BioBERT and may ask follow-up questions for confirmation.
    3. You will receive detailed information about the disease.
    4. Symptoms will be tracked over time for better health monitoring.
    5. Alerts will notify you if there are dangerous patterns in your symptoms.
    6. You can also schedule an appointment with a healthcare provider if needed.
""")

# Get symptoms from user (either text input or voice assistant)
user_symptoms = st.text_input("Enter your symptoms or use the voice assistant.")

# Broad range of disease labels (500 diseases across categories)
candidate_labels = [
    "flu", "diabetes", "hypertension", "asthma", "pneumonia", "COVID-19", 
    "bronchitis", "arthritis", "anemia", "migraine", "depression", "anxiety", 
    "heart attack", "stroke", "cardiac arrest", "kidney failure", "HIV", "hepatitis B", 
    "hepatitis C", "chickenpox", "measles", "tuberculosis", "cholera", "diphtheria", 
    "typhoid", "strep throat", "candidiasis", "ringworm", "aspergillosis", "malaria", 
    "toxoplasmosis", "giardiasis", "lung cancer", "breast cancer", "colorectal cancer", 
    "prostate cancer", "leukemia", "lymphoma", "melanoma", "pancreatitis", "gastritis", 
    "atherosclerosis", "tumor", "cyst", "appendicitis", "brain tumor", "inflammation of the liver", 
    "intestinal blockage", "arterial blockages", "bone tumor",
    # More diseases up to 500 labels
]

# If user clicks the "Diagnose" button
if st.button("Diagnose"):
    if user_symptoms:
        # Use BioBERT to classify the disease
        result = query_biobert_classification(user_symptoms, candidate_labels)
        predicted_disease = result  # Get the top predicted disease
        
        # Display the predicted disease
        st.write(f"Initial Predicted Disease: {predicted_disease}")
        speak(f"Based on your symptoms, you may have {predicted_disease}. Let me confirm.")

        # Follow-up questions to confirm diagnosis
        follow_up_questions = get_follow_up_questions(predicted_disease)
        confirmed_disease = confirm_diagnosis(follow_up_questions)

        # Show confirmed disease and provide detailed information
        st.write(f"Confirmed Disease: {confirmed_disease}")
        speak(f"After additional questions, you may have {confirmed_disease}.")
        get_disease_info(confirmed_disease)
        
        # Track symptoms over time and analyze trends
        track_symptoms(user_symptoms, confirmed_disease)
        analyze_symptom_trends()

    else:
        # Use voice assistant to listen for symptoms
        speak("Please tell me your symptoms.")
        symptoms = listen()
        result = query_biobert_classification(symptoms, candidate_labels)
        predicted_disease = result
        
        # Display the predicted disease
        st.write(f"Initial Predicted Disease: {predicted_disease}")
        speak(f"Based on your symptoms, you may have {predicted_disease}. Let me confirm.")
        
        # Follow-up questions to confirm diagnosis
        follow_up_questions = get_follow_up_questions(predicted_disease)
        confirmed_disease = confirm_diagnosis(follow_up_questions)

        # Show confirmed disease and provide detailed information
        st.write(f"Confirmed Disease: {confirmed_disease}")
        speak(f"After additional questions, you may have {confirmed_disease}.")
        get_disease_info(confirmed_disease)
        
        # Track symptoms over time and analyze trends
        track_symptoms(symptoms, confirmed_disease)
        analyze_symptom_trends()

# Save this file as 'app.py'
