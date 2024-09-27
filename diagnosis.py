import torch
from transformers import BertTokenizer, BertForSequenceClassification
from voice_assistant import speak, listen

# Load BioBERT from your local environment path
MODEL_PATH = r"C:\Users\CEMI\Documents\Arduino\RAG&GPT\hack\saved_biobert\biobert"
tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
model = BertForSequenceClassification.from_pretrained(MODEL_PATH)

# Function to query BioBERT for symptom classification into disease categories
def query_biobert_classification(symptoms, candidate_labels):
    inputs = tokenizer(symptoms, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    
    # Get the predicted class label (the index of the maximum score)
    predicted_index = torch.argmax(outputs.logits, dim=1).item()
    
    # Map the predicted index to the corresponding disease in the candidate labels
    predicted_disease = candidate_labels[predicted_index]
    
    return predicted_disease

# Function to ask follow-up questions and confirm diagnosis
def confirm_diagnosis(questions):
    for question in questions:
        speak(question)
        answer = listen()
        if answer.lower() not in ["yes", "no"]:
            speak("Please answer with yes or no.")
        if answer.lower() == "no":
            speak("Diagnosis confirmed.")
            return questions[0]  # The first question refers to the disease directly
    return questions[0]  # Default confirmed disease

# Save this file as 'diagnosis.py'
