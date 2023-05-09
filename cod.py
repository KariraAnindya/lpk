import streamlit as st
import pandas as pd

st.set_page_config(page_title='Perhitungan Kadar COD', page_icon=':memo:', layout='wide')

st.title('Perhitungan Kadar COD')

st.write('''
    Hallo! Website ini dibuat untuk memudahkan kamu dalam menghitung kadar COD sebelum melakukan analisa. Website ini sangat membantu dalam pengolahan data jika menjadi sebuah alat yang sangat berkembang pesat. Perkembangan ini membawa dampak positif bagi kampus yang berkembang''')

st.header('Pengertian COD')
st.write('''
    Chemical Oxygen Demand (COD) adalah metode analisis kimia yang digunakan untuk mengukur jumlah bahan organik yang teroksidasi dalam sampel air atau limbah cair. Metode ini digunakan sebagai indikator kualitas air untuk menentukan sejauh mana air tersebut tercemar oleh bahan-bahan organik terlarut.

Pada metode COD, bahan organik dalam sampel dioksidasi dengan menggunakan larutan oksidator kuat seperti kalium dikromat (K2Cr2O7) dalam kondisi asam. Proses oksidasi ini akan menghasilkan senyawa-senyawa seperti karbon dioksida, air, dan senyawa-senyawa anorganik lainnya.

Kemudian, jumlah oksigen yang dibutuhkan untuk proses oksidasi ini diukur dan dinyatakan dalam satuan ppm (part per million) atau mg/L (miligram per liter). Semakin tinggi nilai COD dalam sampel, semakin banyak bahan organik teroksidasi, yang menunjukkan bahwa kualitas air semakin buruk atau tercemar.

Metode COD sering digunakan dalam pengujian kualitas air limbah, industri, dan lingkungan. Nilai COD dapat digunakan sebagai indikator awal untuk menentukan proses pengolahan air yang dibutuhkan sebelum dibuang ke lingkungan atau digunakan kembali.
''')

st.subheader('Kelompok 5')
st.write ('''
    Agnia Zahara (2230424) \n
    Arya Dhemas Pambudhi (2230435) \n
    Ghaniyyu Halmar Indrahani (2230442) \n
    Karira Anindya (2230447) \n
    Sekar Laras (2230470) \n''')

def cod_calculator(app_mode):
    if app_mode == "Calculate COD":
        st.header("Calculate Chemical Oxygen Demand (COD)")
        st.write("Masukkan nilai untuk menghitung Kadar COD")

        volume_blanko = st.number_input("Masukkan volume blanko (mL)")
        volume_pereaksi = st.number_input("Masukkan volume pereaksi (mL)")
        normalitas = st.number_input("Masukkan nilai normalitas (grek/mL)")
        berat_ekivalen_oksigen = st.number_input("Masukkan berat ekivalen oksigen (mL) (Tetapan dalam SNI 8000)")
        volume_sampel = st.number_input("Masukkan nilai volume sampel (mL)")

        if volume_sampel !=0:
            cod = (volume_blanko - volume_pereaksi) * normalitas * berat_ekivalen_oksigen / volume_sampel
            st.write(f"Kadar COD adalah {cod:.2f} mg/L") # add this line

def ph_calculator(app_mode):
    if app_mode == "Calculate pH":
        st.header("Calculate pH")
        st.write("Masukkan nilai untuk menghitung pH")

        # Add your input fields and calculations for pH here

app_mode = st.sidebar.selectbox("Pilih mode", ["Calculate COD", "Calculate pH"])
if app_mode == "Calculate COD":
    cod_calculator(app_mode)
elif app_mode == "Calculate pH":
    ph_calculator(app_mode)
