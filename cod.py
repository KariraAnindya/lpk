import streamlit as st
from sttreamlit_option_menu import option_menu

st.set_page_config(layout='wide')
st.write('''
    "Hallo! Website ini dibuat untuk memudahkan kamu dalam menghitung kadar COD sebelum melakukan analisa"''')

navbar = option_menu(menu_title=None, options=['Home'], icons=['0'])
if navbar == 'Home':
    st.title('Perhitungan Kadar COD')
    st.subheader('Kelompok 5')
    st.write ('''
        Agnia Zahara (2230424) \n
        Arya Dhemas Pambudhi (2230435) \n
        Ghaniyyu Halmar Indrahani (2230442) \n
        Karira Anindya (2230447) \n
        Sekar Laras (2230470) \n''')

def cod_calculator(app_mode):
    if app_mode == "Calculate COD":
        st.header("Kalkulasi Chemical Oxygen Demand (COD)")
        st.write("Masukkan nilai untuk menghitung Kadar COD")

        volume blanko = st.number_input("Masukkan volume blanko (mL)")
        volume pereaksi = st.number_input("Maasukkan volume pereaksi (mL)")
        normalitas = st.number_input("Masukkan nilai normalitas (grek/mL)")
        berat ekivalen oksigen = st.number_input("Masukkan berat ekivalen oksigen (mL) (Tetapan dalam SNI 8*1000)")
        volume sampel = st.number_input("Masukkan nilai volume sampel")

        cod = (volume blanko - volume pereaksi) * normalitas * berat ekivalen oksigen / volume sampel

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