import pickle
import streamlit as st 

parkinsons_model = pickle.load(open('C:/Users/shree/Desktop/Parkinsons Web/Saved model/trained_model.sav', 'rb'))

st.title("Parkinson's Disease Prediction with ML")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    fo = st.text_input(r"MDVP:Fo(Hz)")
    
with col2:
    fhi = st.text_input(r"MDVP:Fhi(Hz)")

with col3:
    flo = st.text_input(r"MDVP:Flo(Hz)")

with col4:
    Jitter_percent = st.text_input(r"MDVP:Jitter(%)")

with col5:
    Jitter_Abs = st.text_input(r"MDVP:Jitter(Abs)")

with col1:
    RAP = st.text_input(r"MDVP:RAP")
    
with col2:
    PPQ = st.text_input(r"MDVP:PPQ")

with col3:
    DDP = st.text_input(r"Jitter:DDP")

with col4:
    Shimmer = st.text_input(r"MDVP:Shimmer")

with col5:
    Shimmer_dB = st.text_input(r"MDVP:Shimmer(dB)")

with col1:
    APQ3 = st.text_input(r"Shimmer:APQ3")

with col2:
    APQ5 = st.text_input(r"Shimmer:APQ5")
    
with col3:
    APQ = st.text_input(r"MDVP:APQ")

with col4:
    DDA = st.text_input(r"Shimmer:DDA")

with col5:
    NHR = st.text_input(r"NHR")

with col1:
    HNR = st.text_input(r"HNR")

with col2:
    RPDE = st.text_input(r"RPDE")

with col3:
    DFA = st.text_input(r"DFA")
    
with col4:
    spread1 = st.text_input(r"spread1")
    
with col5:
    spread2 = st.text_input(r"spread2")

with col1:
    D2 = st.text_input(r"D2")

with col2:
    PPE = st.text_input(r"PPE")
    

parkinsons_diagnosis = ''

if st.button("Parkinson's Disease Test Result"):
    parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
    
    if (parkinsons_prediction[0] == 1):
       parkinsons_diagnosis = "The patient has Parkinson's Disease"
    else:
       parkinsons_diagnosis = "The patient does not have Parkinson's Disease"
    
    st.success(parkinsons_diagnosis)

