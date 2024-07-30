# inisialisasi library
import streamlit as st
from st_pages import Page, show_pages, _hide_pages
import pandas as pd


# judul website
st.set_page_config(
    page_title="Analisis Sentimen Ulasan Aplikasi Bareksa dengan Pendekatan Lexicon-Based, Seleksi Fitur Chi-square, dan Support Vector Machine",
    page_icon="💮",
)
st.title('Website Analisis Sentimen Ulasan Aplikasi Bareksa dengan Pendekatan Lexicon-Based, Seleksi Fitur Chi-square, dan Support Vector Machine')


# menus 
show_pages(
    [
        Page("main.py", "Home", "🏠"),
        Page("pages/preproses.py", "Pre-Proses Data", "♻"),
        Page("pages/FeatureExtraction.py", "Feature Extraction", "📶"),
        Page("pages/WordCloud.py", "Word Cloud", "🧮"),
        Page("pages/smote.py", "SMOTE Data", "🔄"),
        Page("pages/klasifikasisvm.py", "Performa Kinerja Model", "🔬"),
        Page("pages/ujidata.py", "Uji Coba", "🔂"),
    ]
)

#penjelasan paru-paru

st.markdown('<div style="text-align: justify;"> <b>Website ini </b> adalah sebuah platform yang dirancang untuk menganalisis sentimen ulasan pengguna terhadap aplikasi Bareksa. Pendekatan yang digunakan melibatkan analisis berbasis leksikon untuk mengidentifikasi sentimen positif atau negatif dalam teks ulasan. Seleksi fitur Chi-square digunakan untuk memilih fitur-fitur yang paling relevan dari data ulasan, sementara algoritma Support Vector Machine (SVM) diaplikasikan untuk melakukan klasifikasi sentimen secara akurat. Platform ini bertujuan untuk memberikan wawasan yang mendalam tentang persepsi pengguna terhadap aplikasi Bareksa, membantu pengembang dalam meningkatkan kualitas dan performa aplikasi tersebut.</div>', unsafe_allow_html=True)

st.text("")


# data
st.markdown('<h5>Beberapa sample terkait data yang digunakan dalam penelitian ini: </h5>', unsafe_allow_html=True)

# show data with dataframe table mengambil 10 data pertama

data = pd.read_csv('data/labellingfix.csv')

# ambil kolom 'data asli' dan 'sentimen' ambil 10 data pertama
data = data[['text asli', 'Sentimen']].head(10)

# tambahkan kolom 'At Date' pada data
dates_list = [
    "2023-11-19 2:12:44",
    "2023-11-21 6:21:44",
    "2023-11-14 6:06:12",
    "2023-11-28 7:06:17",
    "2023-11-16 8:53:10",
    "2023-10-27 21:43:01",
    "2023-11-25 2:06:17",
    "2023-10-21 16:08:28",
    "2023-12-06 13:25:44",
    "2023-11-21 5:50:32"]

data['At Date'] = dates_list

data.columns = ['Data', 'Sentimen',"At Date"]



# tampilkan data
st.write(data.head(10))