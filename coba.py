# inisialisasi library
import streamlit as st
import pandas as pd

# Judul website
st.set_page_config(
    page_title="Analisis Sentimen Ulasan Aplikasi Bareksa dengan Pendekatan Lexicon-Based, Seleksi Fitur Chi-square, dan Support Vector Machine",
    page_icon="💮",
)
st.title('Website Analisis Sentimen Ulasan Aplikasi Bareksa dengan Pendekatan Lexicon-Based, Seleksi Fitur Chi-square, dan Support Vector Machine')

# Menu navigasi manual
menu = ["Home", "Pre-Proses Data", "Feature Extraction", "Word Cloud", "SMOTE Data", "Performa Kinerja Model", "Uji Coba"]
choice = st.sidebar.selectbox("Menu", menu)

# Halaman yang sesuai dengan pilihan menu
if choice == "Home":
    st.markdown('<div style="text-align: justify;"> <b>Website ini </b> adalah sebuah platform yang dirancang untuk menganalisis sentimen ulasan pengguna terhadap aplikasi Bareksa. Pendekatan yang digunakan melibatkan analisis berbasis leksikon untuk mengidentifikasi sentimen positif atau negatif dalam teks ulasan. Seleksi fitur Chi-square digunakan untuk memilih fitur-fitur yang paling relevan dari data ulasan, sementara algoritma Support Vector Machine (SVM) diaplikasikan untuk melakukan klasifikasi sentimen secara akurat. Platform ini bertujuan untuk memberikan wawasan yang mendalam tentang persepsi pengguna terhadap aplikasi Bareksa, membantu pengembang dalam meningkatkan kualitas dan performa aplikasi tersebut.</div>', unsafe_allow_html=True)
    st.text("")

    # Data
    st.markdown('<h5>Beberapa sample terkait data yang digunakan dalam penelitian ini: </h5>', unsafe_allow_html=True)

    # Show data with dataframe table mengambil 10 data pertama
    data = pd.read_csv('data/labellingfix.csv')

    # Ambil kolom 'data asli' dan 'sentimen' ambil 10 data pertama
    data = data[['text asli', 'Sentimen']].head(10)

    # Tambahkan kolom 'At Date' pada data
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

    data.columns = ['Data', 'Sentimen', "At Date"]

    # Tampilkan data
    st.write(data.head(10))

elif choice == "Pre-Proses Data":
    st.subheader("Pre-Proses Data")
    # Tambahkan konten untuk halaman Pre-Proses Data

elif choice == "Feature Extraction":
    st.subheader("Feature Extraction")
    # Tambahkan konten untuk halaman Feature Extraction

elif choice == "Word Cloud":
    st.subheader("Word Cloud")
    # Tambahkan konten untuk halaman Word Cloud

elif choice == "SMOTE Data":
    st.subheader("SMOTE Data")
    # Tambahkan konten untuk halaman SMOTE Data

elif choice == "Performa Kinerja Model":
    st.subheader("Performa Kinerja Model")
    # Tambahkan konten untuk halaman Performa Kinerja Model

elif choice == "Uji Coba":
    st.subheader("Uji Coba")
    # Tambahkan konten untuk halaman Uji Coba
