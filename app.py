import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Alfabetismo en México")

df = pd.read_excel('datos_completos.xlsx')

lista_estados = df['Entidad federativa'].unique().tolist()

estado = st.selectbox("Seleccione el estado", lista_estados)

fig, ax = plt.subplots(1, 1, figsize=(14,8))

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.set_yticklabels([])


(df[df['Entidad federativa'] == estado].groupby('Edad')[['Población total', 'SLE', 'NSLE', 'NE']]
 .sum()
 .reset_index()
 .assign(tasa_alf=lambda x:x['SLE'] / x['Población total'],
         tasa_nalf=lambda x:x['NSLE'] / x['Población total'],
         tasa_ne=lambda x:x['NE'] / x['Población total'])
 .set_index('Edad')[['tasa_alf', 'tasa_nalf', 'tasa_ne']].plot(kind='area', cmap='viridis', ax=ax))

st.pyplot(fig)
