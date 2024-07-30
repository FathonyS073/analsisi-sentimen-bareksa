# inisiasi library
import streamlit as st
import pandas as pd


# judul
st.set_page_config(
    page_title="Pre-Proses Data",
    page_icon="💮",
)
st.title('Preproses Data')
st.write('')

# Data Asli
st.markdown('<h3>Data Asli </h3>', unsafe_allow_html=True)
st.write('Berikut merupakan data asli yang digunakan dalam penelitian ini: ')
data = pd.read_csv('data/labellingfix.csv')
data = data[['text asli', 'Sentimen']]
st.write(data.head(10))


# Tokenizing data
st.markdown('<h3>Tokenizing Data </h3>', unsafe_allow_html=True)
st.markdown('<p style="text-align: justify;">Tokenizing data adalah proses memecah teks menjadi unit-unit yang lebih kecil, yang disebut token. Token bisa berupa kata, frasa, simbol, atau elemen lain yang signifikan dalam konteks analisis teks. Berikut merupakan hasil tokenizing data: </p>', unsafe_allow_html=True)
data_token = pd.read_csv('data/hasilstopword.csv')
data_token1 = data_token[['content']]
data_token1.columns = ['Sebelum di Tokenizing']

data_token2 = data_token[['text_token']]
data_token2.columns = ['Sesudah di Tokenizing']

colom1, colom2 = st.columns(2)
colom1.write('Sebelum di Tokenizing')
colom1.write(data_token1.head(10))

colom2.write('Sesudah di Tokenizing')
colom2.write(data_token2.head(10))





# Case Folding
st.markdown('<h3>Cleaning Data & Case Folding </h3>', unsafe_allow_html=True)
st.markdown('<p style="text-align: justify;">Cleaning data adalah Proses menghapus tanda baca, mention, link, dan karakter khusus lainnya.Kemudian Case folding adalah proses mengubah semua huruf dalam sebuah teks menjadi huruf kecil (lowercase). Berikut merupakan hasil Cleaning Data & Case Folding : </p>', unsafe_allow_html=True)
data_casefolding = pd.read_csv('data/hasilstopword.csv')
data_casefolding1 = data_casefolding[['text_token']]
data_casefolding1.columns = ['Sebelum di Cleaning Data & Case Folding']
data_casefolding2 = data_casefolding[['text_clean']]
data_casefolding2.columns = ['Sesudah di Cleaning Data & Case Folding']

colom3, colom4 = st.columns(2)
colom3.write('Sebelum di Cleaning Data & Case Folding')
colom3.write(data_casefolding1.head(10))

colom4.write('Sesudah di Cleaning Data & Case Folding')
colom4.write(data_casefolding2.head(10))


# normalisasi data
st.markdown('<h3>Normalisasi Data </h3>', unsafe_allow_html=True)
st.markdown('<p style="text-align: justify;">Normalisasi data dengan kamus leksikon adalah proses mengubah bentuk kata dalam teks agar lebih konsisten dan seragam berdasarkan kamus leksikon yang telah ditentukan. Kamus leksikon berisi pasangan kata tidak baku dan kata baku atau bentuk standar. Normalisasi ini berguna untuk menyatukan variasi penulisan kata yang berbeda menjadi satu bentuk yang konsisten sehingga analisis data menjadi lebih akurat. Misalnya, kata "gk", "ga", dan "tidak" bisa dinormalisasi menjadi "tidak". Berikut merupakan hasil normalisasi data: </p>', unsafe_allow_html=True)
data_normalisasi = pd.read_csv('data/hasilstopword.csv')
data_normalisasi1 = data_normalisasi[['text_clean']]
data_normalisasi1.columns = ['Sebelum di Normalisasi Data']

data_normalisasi2 = data_normalisasi[['content_norm']]
data_normalisasi2.columns = ['Sesudah di Normalisasi Data']

colom5, colom6 = st.columns(2)
colom5.write('Sebelum di Normalisasi Data')
colom5.write(data_normalisasi1.head(10))

colom6.write('Sesudah di Normalisasi Data')
colom6.write(data_normalisasi2.head(10))



# stopword removal 
st.markdown('<h3>Stopword Removal </h3>', unsafe_allow_html=True)
st.markdown('<p style="text-align: justify;">Stopword removal adalah proses menghapus kata-kata umum yang tidak memiliki makna atau kontribusi signifikan dalam analisis teks. Kata-kata tersebut disebut stopword. Penghapusan stopword berguna untuk mempercepat proses analisis teks dan mengurangi noise dalam data. Berikut merupakan hasil stopword removal: </p>', unsafe_allow_html=True)
data_stopword = pd.read_csv('data/hasilstopword.csv')
data_stopword1 = data_stopword[['content_norm']]
data_stopword1.columns = ['Sebelum di Stopword Removal']

data_stopword2 = data_stopword[['text_stopword']]
data_stopword2.columns = ['Sesudah di Stopword Removal']

colom7, colom8 = st.columns(2)
colom7.write('Sebelum di Stopword Removal')
colom7.write(data_stopword1.head(10))

colom8.write('Sesudah di Stopword Removal')
colom8.write(data_stopword2.head(10))



