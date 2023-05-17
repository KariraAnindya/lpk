import streamlit as st
from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title="APLIKASI CHEMICAL OXYGEN DEMAND", #required
    options=["Home", "Pengertian", "Rumus", "Kalkulator"], #required
    orientation="horizontal"
)

if selected == "Home":
    st.title(f"Selamat Datang di Website Kami")
    st.header ("KELOMPOK 5")
        
    daftar_nama = ["Agnia Zahara (2230424)", "Arya Dhemas Pambudhi (2230435)", "Ghaniyyu Halmar Indrahani (2230442)", "Karira Anindya (2230447)", "Sekar Laras (2230470)"]
    cols = st.columns(len(daftar_nama))
    for i, col in enumerate(cols):
     col.write(daftar_nama[i])

if selected == "Pengertian":
    st.title(f"Pengertian COD")
    st.header("Apa itu COD?")
    st.write ("COD ( Chemical Oxygen Demand ) adalah ukuran oksigen yang dikonsumsi selama dekomposisi bahan organik dan oksidasi bahan kimia anorganik seperti amonia dan nitrit. Chemical Oxygen Demand merupakan parameter kualitas air yang penting karena, dapat menilai dampak effluen air limbah yang akan dibuang pada lingkungan penerima (badan air). Tingkat COD tinggi menandakan banyaknya jumlah bahan organik yang teroksidasi pada sampel, yang akan mengurangi tingkat oksigen terlarut (DO). Penurunan DO dapat menyebabkan kondisi anaerob, yang dapat merusak kehidupan air. Tes COD sering digunakan sebagai alternatif untuk BOD karena waktu analisa yang lebih singkat.")
    st.header ("Sampel Apa Saja yang Biasa diuji Kadar COD-nya?")
    st.write ('''
    1. Influen air limbah di unit pengolahan (untuk mengetahui nilai COD awal)
    2. Effluen air limbah di unit pengolahan (untuk mengetahui nilai COD akhir, dan untuk mengetahui efisiensi pengolahan suatu unit)
    3. Effluen air limbah ke badan air (untuk kesesuaian terhadap baku mutu)
    4. Badan air (untuk mengetahui nilai COD dan dapat memperkirakan dampak yang ditimbulkan)''')

if selected  == "Rumus":
    st.title (f"Rumus Mencari Kadar COD Dalam Sampel")
    st.write ("Berdasarkan kalkulator yang kami buat, berikut adalah rumus dari hasil yang didapat :")
    st.image ('rumus cod.jpeg')
    st.write (''' Keterangan :
    1. A adalah volume blanko (mL)
    2. B adalah volume pereaksi (mL)
    3. N adalah normalitas (grek/mL)
    4. F adalah berat ekivalen menggunakan tetapan SNI yaitu 8000 grek
    5. V adalah volume sampel (mL)''')

if selected  == "Kalkulator":
    st.title (f"Kalkulator Kadar COD")
    st.write("Masukkan nilai untuk menghitung Kadar COD")

    volume_blanko = st.number_input("Masukkan volume blanko (mL)", 00.00)
    volume_pereaksi = st.number_input("Masukkan volume pereaksi (mL)", 00.00)
    normalitas = st.number_input("Masukkan nilai normalitas (grek/mL)", 00.000)
    berat_ekivalen_oksigen = st.number_input("Masukkan berat ekivalen oksigen (grek) (Tetapan dalam SNI 8000 grek)", 8000)
    volume_sampel = st.number_input("Masukkan nilai volume sampel (mL)", 00.00)
    st.button("HITUNG")
    if volume_sampel != 0:
            cod = (volume_blanko - volume_pereaksi) * normalitas * berat_ekivalen_oksigen / volume_sampel
            st.success(f"Kadar COD adalah {cod:.2f} mg/L") # add this line