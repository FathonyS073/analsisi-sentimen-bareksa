# inisialisasi library
import streamlit as st
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

# judul
st.set_page_config(
    page_title="SMOTE Data",
    page_icon="💮",
    
)
st.title('SMOTE Data')
st.markdown('<p style="text-align: justify;">SMOTE (Synthetic Minority Over-sampling Technique) merupakan metode yang digunakan untuk menangani ketidakseimbangan kelas pada data, data yang di SMOTE adalah data training.  Berikut merupakan hasil SMOTE: </p>', unsafe_allow_html=True) 


dataytrainbefore = pd.read_csv('data/y_train.csv').values.ravel()
dataytrainafter = pd.read_csv('data/y_train_resampled.csv')

# show data dengan plot sebelum  smote
db = pd.DataFrame(Counter(dataytrainbefore).items(), columns=['Sentimen', 'JUMLAH'])


ax = db.plot.bar()
plt.title('Data Sebelum SMOTE')
plt.xlabel('Sentimen')
plt.ylabel('Jumlah')
# tampilkan keterangan jumlah data di setiap kelas

for i in ax.patches:
    ax.text(i.get_x() + 0.2, i.get_height() + 0.2, str(i.get_height()), fontsize=10, color='black')
st.set_option('deprecation.showPyplotGlobalUse', False)


st.pyplot()

# show data dengan plot setelah smote
da = pd.DataFrame(Counter(dataytrainafter['Sentimen']).items(), columns=['Sentimen', 'JUMLAH'])
ax = da.plot.bar()
plt.title('Data Setelah SMOTE')
plt.xlabel('Sentimen')
plt.ylabel('Jumlah')
# tampilkan keterangan jumlah data di setiap kelas

for i in ax.patches:
    ax.text(i.get_x() + 0.2, i.get_height() + 0.2, str(i.get_height()), fontsize=10, color='black')
st.set_option('deprecation.showPyplotGlobalUse', False)


st.pyplot()