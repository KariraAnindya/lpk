import streamlit as st

st.title('Perhitungan Kadar COD')
st.write('''
    "Hallo! Website ini dibuat untuk memudahkan kamu dalam menghitung kadar COD sebelum melakukan analisa. Website ini sangat membantu dalam pengolahan data jika menjadi sebuah alat yang sangat berkembang pesat. Perkembangan ini membawa dampak positif bagi kampus yang berkembang"''')

st.write('''
    "Chemical Oxygen Demand (COD) adalah metode analisis kimia yang digunakan untuk mengukur jumlah bahan organik yang teroksidasi dalam sampel air atau limbah cair. Metode ini digunakan sebagai indikator kualitas air untuk menentukan sejauh mana air tersebut tercemar oleh bahan-bahan organik terlarut.

Pada metode COD, bahan organik dalam sampel dioksidasi dengan menggunakan larutan oksidator kuat seperti kalium dikromat (K2Cr2O7) dalam kondisi asam. Proses oksidasi ini akan menghasilkan senyawa-senyawa seperti karbon dioksida, air, dan senyawa-senyawa anorganik lainnya.

Kemudian, jumlah oksigen yang dibutuhkan untuk proses oksidasi ini diukur dan dinyatakan dalam satuan ppm (part per million) atau mg/L (miligram per liter). Semakin tinggi nilai COD dalam sampel, semakin banyak bahan organik teroksidasi, yang menunjukkan bahwa kualitas air semakin buruk atau tercemar.

Metode COD sering digunakan dalam pengujian kualitas air limbah, industri, dan lingkungan. Nilai COD dapat digunakan sebagai indikator awal untuk menentukan proses pengolahan air yang dibutuhkan sebelum dibuang ke lingkungan atau digunakan kembali.
"''')

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
        berat_ekivalen_oksigen = st.number_input("Masukkan berat ekivalen oksigen (mL) (Tetapan dalam SNI 8*1000)")
        volume_sampel = st.number_input("Masukkan nilai volume sampel (mL)")

        return (volume_blanko - volume_pereaksi) * normalitas * berat_ekivalen_oksigen / volume_sampel

        st.write(f"The Chemical Oxygen Demand (COD) is {cod:.2f} mg/L")

    elif app_mode == "Analysis COD":
        st.header("Analysis COD")
        st.write("Upload your COD analysis data in CSV format below")

        uploaded_file = st.file_uploader("Choose a file")

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            fig, ax = plt.subplots()
            ax.plot(df["Sample"], df["COD"], marker="o")
            ax.set_xlabel("Sample")
            ax.set_ylabel("COD (mg/L)")
            ax.set_title("COD Analysis")
            st.pyplot(fig)

app_mode = st.sidebar.selectbox("Select an option", ["Calculate COD", "COD Analysis"])
cod_calculator(app_mode)