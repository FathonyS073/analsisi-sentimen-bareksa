# inisialisasi library
import streamlit as st
import matplotlib.pyplot as mp
import pandas as pd
import seaborn as sb

# judul
st.set_page_config(
    page_title="Feature Extraction",
    page_icon="💮",
)
st.title('Feature Extraction')
st.markdown('<p style="text-align: justify;">Feature Extraction dengan TF-IDF (Term Frequency-Inverse Document Frequency) adalah metode yang digunakan untuk menilai pentingnya suatu kata dalam sebuah dokumen relatif terhadap kumpulan dokumen lainnya. Metode ini sering digunakan dalam penambangan teks dan pemrosesan bahasa alami untuk mengidentifikasi kata-kata yang lebih signifikan dalam suatu dokumen. Berikut merupakan hasil feature extraction: </p>', unsafe_allow_html=True)
# memanggil data
data = pd.read_csv('data/hasilstopword.csv')
data = data[['text_stopword']]

# tf-idf
datatfidf = pd.read_csv('data/tfidffix.csv')


data1, data2 = st.columns(2)

# menampilkan data
data1.write('Data Sebelum Feature Extraction')
data1.write(data.head(10))

data2.write('Data Sesudah Feature Extraction')
data2.write(datatfidf.head(10))
