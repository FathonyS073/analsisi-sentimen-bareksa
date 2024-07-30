import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Performa Kinerja Model ",
    page_icon="💮",
)
st.title('Performa Kinerja Model ')

# berikan dropdown untuk memilih model 
st.write("Pilih model yang ingin dilihat performanya: ")
model = st.selectbox(
    'Pilih Model',
    ('SVM', 'SVM+CHISQUARE','SVM+SMOTE' ,'SVM+CHISQUARE+SMOTE')
)

submit = st.button('Submit')

if submit:
    if(model == 'SVM'):
        st.write("Performa Model SVM")
        # tampilkan foto performa model
        gambar1, gambar2 = st.columns(2)
        gambar1.markdown('<h3>SVM dengan K = 5</h3>', unsafe_allow_html=True)
        # ambil gambar dari folder data
        gambar1.image('data/svm_K5.png', use_column_width=True)
        #     [89.28, 89.25, 89.28],
        gambar2.markdown('<table><tr><th>Accuracy</th><th>Precision</th><th>Recall</th></tr><tr><td>89.28%</td><td>89.25%</td><td>89.28%</td></tr></table>', unsafe_allow_html=True)
        
        # k = 7
        gambar3, gambar4 = st.columns(2)
        gambar3.markdown('<h3>SVM dengan K = 7</h3>', unsafe_allow_html=True)
        # ambil gambar dari folder data
        gambar3.image('data/svm_K7.png', use_column_width=True)
        # [90.15, 90.13, 90.15],
        gambar4.markdown('<table><tr><th>Accuracy</th><th>Precision</th><th>Recall</th></tr><tr><td>90.15%</td><td>90.13%</td><td>90.15%</td></tr></table>', unsafe_allow_html=True)
        
        # k = 9
        gambar5, gambar6 = st.columns(2)
        gambar5.markdown('<h3>SVM dengan K = 9</h3>', unsafe_allow_html=True)
        # ambil gambar dari folder data
        gambar5.image('data/svm_K9.png', use_column_width=True)
        # [90.15, 90.13, 90.15],
        gambar6.markdown('<table><tr><th>Accuracy</th><th>Precision</th><th>Recall</th></tr><tr><td>90.15%</td><td>90.13%</td><td>90.15%</td></tr></table>', unsafe_allow_html=True)
        
        # full 
        st.write("Performa Model SVM dengan K = 5, 7, 9")
        st.image('data/svm_FULL.png', use_column_width=True)
        # ambil akurasi dari semua k
        # [89.28, 90.15, 90.15],
        
        st.markdown('<table><tr><th>Accuracy K=5</th><th>Accuracy K=7</th><th>Accuracy K=9</th></tr><tr><td>89.28%</td><td>90.15%</td><td>90.15%</td></tr></table>', unsafe_allow_html=True)    
        
        
    elif (model == 'SVM+CHISQUARE'):
        st.write("Performa Model SVM + CHISQUARE")
    
        chi1, chi2 = st.columns(2)
        # gambar dari link
        chi1.markdown("<img src='https://pbs.twimg.com/media/GTlt5JiaoAAbpeS?format=png&name=small' style='max-width: 100%; display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
        chi2.markdown("<img src='https://pbs.twimg.com/media/GTlt9sCbIAA73wR?format=png&name=small' style='max-width: 100%; display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
        
        st.write("Perbandingan Performa Model SVM + CHISQUARE")
        st.image('https://pbs.twimg.com/media/GTltm7zbgAAM4Qe?format=png&name=900x900', use_column_width=True)
        
        
    elif (model == 'SVM+SMOTE'):
        st.write("Performa Model SVM + SMOTE")
        
        st.write("SVM + SMOTE dengan K = 5")
        smote1, smote2 = st.columns(2)
        # gambar dari folder data
        smote1.image('data/smote_K5.png', use_column_width=True)
        smote2.markdown('<table><tr><th>Accuracy</th><th>Precision</th><th>Recall</th></tr><tr><td>92.79%</td><td>92.85%</td><td>92.79%</td></tr></table>', unsafe_allow_html=True)
        
        st.write("SVM + SMOTE dengan K = 7")
        smote3, smote4 = st.columns(2)
        # gambar dari folder data
        smote3.image('data/smote_K7.png', use_column_width=True)
        # akurasi berikut     [93.41, 93.45, 93.41],
        smote4.markdown('<table><tr><th>Accuracy</th><th>Precision</th><th>Recall</th></tr><tr><td>93.41%</td><td>93.45%</td><td>93.41%</td></tr></table>', unsafe_allow_html=True)
        
        st.write("SVM + SMOTE dengan K = 9")
        smote5, smote6 = st.columns(2)
        # gambar dari folder data
        smote5.image('data/smote_K9.png', use_column_width=True)
        # akurasi berikut         [93.15, 93.19, 93.15]
        smote6.markdown('<table><tr><th>Accuracy</th><th>Precision</th><th>Recall</th></tr><tr><td>93.15%</td><td>93.19%</td><td>93.15%</td></tr></table>', unsafe_allow_html=True)
        
        st.write("Perbandingan Performa Model SVM + SMOTE")
        st.image('https://pbs.twimg.com/media/GTlyIEUbYAA02J9?format=jpg&name=medium', use_column_width=True)
        
        
    elif (model == 'SVM+CHISQUARE+SMOTE'):
        st.write("Performa Model SVM + CHISQUARE + SMOTE")
    
        chis1, chis2 = st.columns(2)
        # gambar dari link
        chis1.markdown("<img src='https://pbs.twimg.com/media/GTndv_ObsAACH3b?format=png&name=small' style='max-width: 100%; display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
        chis2.markdown("<img src='https://pbs.twimg.com/media/GTnd3Boa8AAtlQ0?format=png&name=small' style='max-width: 100%; display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
        
        st.write("Perbandingan Performa Model SVM + CHISQUARE + SMOTE")
        st.image('https://pbs.twimg.com/media/GTne7ZBbsAAvqqz?format=png&name=900x900', use_column_width=True)

else:
    st.warning("Pilih model terlebih dahulu")
        
    