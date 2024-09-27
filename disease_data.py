import streamlit as st

# Function to provide detailed information about a disease
def get_disease_info(disease):
    info = ""
    
    if disease == "diabetes":
        info = """
        **Diabetes** is a chronic condition where the body cannot regulate blood sugar levels. Treatment involves monitoring, diet, exercise, and insulin.
        """
    elif disease == "heart attack":
        info = """
        **Heart Attack** occurs when blood flow to the heart is blocked, causing damage to the heart muscle. Immediate medical attention is required.
        """
    elif disease == "lung cancer":
        info = """
        **Lung Cancer** involves abnormal cell growth in the lungs, often due to smoking. Treatment includes surgery, chemotherapy, and radiation.
        """
    elif disease == "pneumonia":
        info = """
        **Pneumonia** is a lung infection that causes inflammation and fluid buildup in the air sacs. Treatment includes antibiotics and rest.
        """
    # Add more diseases here up to 500
    else:
        info = "No detailed information is available for this disease."

    st.info(info)

# Function to get follow-up questions for a given disease
def get_follow_up_questions(disease):
    questions = []
    
    if disease == "diabetes":
        questions = ["Do you feel extreme hunger?", "Do you have frequent urination?", "Do you feel fatigued?"]
    elif disease == "heart attack":
        questions = ["Do you have chest pain?", "Do you feel pain in your left arm?", "Do you have difficulty breathing?"]
    elif disease == "pneumonia":
        questions = ["Do you have a fever?", "Do you have a cough?", "Are you experiencing chest pain?"]
    # Add follow-up questions for more diseases up to 500
    else:
        questions = ["Are you experiencing symptoms related to this condition?"]
    
    return questions

# Save this file as 'disease_data.py'
