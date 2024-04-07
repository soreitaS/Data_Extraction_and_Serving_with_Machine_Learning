# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 23:39:01 2023

@author: İBRAHİM
"""

import streamlit as st
import joblib
from sklearn.preprocessing import LabelEncoder

# Eğitilmiş modeli yükleyin
model = joblib.load('random_forest_model.pkl')

# Kullanıcıdan giriş al
dahili_hafiza = st.number_input("Dahili Hafıza (GB)", min_value=0.0, max_value=None, step=1.0)
ekran_boyutu = st.number_input("Ekran Boyutu (inç)", min_value=0.0, max_value=None, step=1.0)
ram_kapasitesi = st.number_input("RAM Kapasitesi (GB)", min_value=0.0, max_value=None, step=1.0)

# İşletim Sistemi seçimini al
isletim_sistemi_mapping = {'Android': 0, 'IOS': 1}
isletim_sistemi = st.selectbox("İşletim Sistemi", list(isletim_sistemi_mapping.keys()))

# 'Android' için 0, 'IOS' için 1 dönüşümü
label_encoder = LabelEncoder()
isletim_sistemi_numeric = label_encoder.fit_transform([isletim_sistemi])[0]

# Tahmin butonu
if st.button("Tahmin Et"):
    input_data = [[dahili_hafiza, ekran_boyutu, ram_kapasitesi, isletim_sistemi_numeric]]
    prediction = model.predict(input_data)
    st.success(f"Tahmini Fiyat: {prediction[0]:,.2f} TL")