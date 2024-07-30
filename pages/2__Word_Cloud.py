import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Word Cloud",
    page_icon="💮",
)
st.title('Word Cloud')

st.markdown('<p style="text-align: justify;">Word Cloud adalah representasi visual dari teks yang menyoroti kata-kata yang sering muncul dalam dokumen atau kumpulan dokumen. Dalam Word Cloud, kata-kata yang lebih sering muncul ditampilkan dengan ukuran font yang lebih besar atau warna yang lebih menonjol, sehingga memudahkan untuk mengidentifikasi kata-kata kunci atau tema utama dari teks. Berikut merupakan hasil word cloud: </p>', unsafe_allow_html=True)

gambar1, gambar2 = st.columns(2)
gambar1.markdown('<h3>Visualisasi Kata Positif</h3>', unsafe_allow_html=True)
gambar1.markdown('<img src="https://pbs.twimg.com/media/GTldquubIAAmdwR?format=png&name=900x900" style="max-width: 100%; display: block; margin-left: auto; margin-right: auto;">', unsafe_allow_html=True)

gambar2.markdown('<h3>Visualisasi Kata Negatif</h3>', unsafe_allow_html=True)
gambar2.markdown('<img src="https://pbs.twimg.com/media/GTldsFhbUAAUBdH?format=png&name=900x900" style="max-width: 100%; display: block; margin-left: auto; margin-right: auto;">', unsafe_allow_html=True)