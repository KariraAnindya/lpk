import streamlit as st
from sttreamlit_option_menu import option_menu

if navbar == 'Home' :
    st._title('Menghitung Kadar COD')
    st.subheader('Kelompok 5')
    st.write('''
    Agina Zahara \n
    Arya Dhemas Pambudhi \n
    Ghaniyyuh Halmar Indrahani \n
    Karira Anindya \n
    Sekar Laras''')

def cod_calculator(app_mode):
    if app_mode == "Calculate COD":
        st.header("Calculate Chemical Oxygen Demand (COD)")
        st.write("Enter the values below to calculate the Chemical Oxygen Demand (COD)")

        volume = st.number_input("Enter the volume of the sample (in mL)", min_value=0.1, step=1.0)
        acid = st.number_input("Enter the volume of the acid used (in mL)", min_value=0.1, step=1.0)
        blank = st.number_input("Enter the volume of the blank (in mL)", min_value=0.1, step=1.0)
        factor = st.number_input("Enter the factor used for the calculation", min_value=0.1, step=0.01)

        cod = (factor * (acid - blank)) / volume

        st.write(f"The Chemical Oxygen Demand (COD) is {cod:.2f} mg/L")

    elif app_mode == "COD Analysis":
        st.header("COD Analysis")
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