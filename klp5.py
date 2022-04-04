from tkinter import Frame
from nbformat import read
import pandas as pd
import streamlit as st
import numpy as np
from pandas import DataFrame as df

st.header('Dashboard Data Pengidap Covid-19')
data_covid = pd.read_csv("covid_19_indonesia_time_series_all.csv")
st.write(data_covid)
jumlah = data_covid.iloc[:, 7:10]

st.header('Jumlah Kasus Penderita Covid-19')
jumlah_kasus = data_covid.iloc[:, 7]
total_kasus = jumlah_kasus.sum()
jumlah_kasus
st.write(total_kasus)

st.header('Jumlah Kasus Positif Covid-19')
jumlah_positif = data_covid.iloc[:, 10]
total_positif = jumlah_positif.sum()
jumlah_positif
st.write(total_positif)

st.header('Jumlah Kasus yang Pulih')
jumlah_pulih = data_covid.iloc[:, 9]
total_pulih = jumlah_pulih.sum()
jumlah_pulih
st.write(total_pulih)

st.header('Jumlah Kasus yang Meninggal')
jumlah_mati = data_covid.iloc[:, 8]
total_mati = jumlah_mati.sum()
jumlah_mati
st.write(total_mati)