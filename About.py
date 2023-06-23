import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Multipage App",
)

with st.sidebar:
    st.title("ITB Tracker Study")
    st.image("logo.jpeg")

st.sidebar.success("Select a page above.")

################################################ LOAD DATASET ################################################


@st.cache_data
def load_dataset():
    df2018 = pd.read_excel(
        'Data Mentah Sortir_Analisis Tren_v3.xlsx', sheet_name="2018")
    df2019 = pd.read_excel(
        'Data Mentah Sortir_Analisis Tren_v3.xlsx', sheet_name="2019")
    df2020 = pd.read_excel(
        'Data Mentah Sortir_Analisis Tren_v3.xlsx', sheet_name="2020")
    df2021 = pd.read_excel(
        'Data Mentah Sortir_Analisis Tren_v3.xlsx', sheet_name="2021")
    df2022 = pd.read_excel(
        'Data Mentah Sortir_Analisis Tren_v3.xlsx', sheet_name="2022")

    dfUser2018 = pd.read_excel(
        'Data Mentah Kuesioner User Survey_Analisis Tren_v3.xlsx', sheet_name="User Survey 2018")
    dfUser2019 = pd.read_excel(
        'Data Mentah Kuesioner User Survey_Analisis Tren_v3.xlsx', sheet_name="User Survey 2019")
    dfUser2020 = pd.read_excel(
        'Data Mentah Kuesioner User Survey_Analisis Tren_v3.xlsx', sheet_name="User Survey 2020")
    dfUser2021 = pd.read_excel(
        'Data Mentah Kuesioner User Survey_Analisis Tren_v3.xlsx', sheet_name="User Survey 2021")
    dfUser2022 = pd.read_excel(
        'Data Mentah Kuesioner User Survey_Analisis Tren_v3.xlsx', sheet_name="User Survey 2022")
    return df2018, df2019, df2020, df2021, df2022, dfUser2018, dfUser2019, dfUser2020, dfUser2021, dfUser2022


df2018, df2019, df2020, df2021, df2022, dfUser2018, dfUser2019, dfUser2020, dfUser2021, dfUser2022 = load_dataset()
st.session_state["df2018"] = df2018
st.session_state["df2019"] = df2019
st.session_state["df2020"] = df2020
st.session_state["df2021"] = df2021
st.session_state["df2022"] = df2022

################################################ LOAD DATASET ################################################


fakultas = ["Fakultas Ilmu dan Teknologi Kebumian (FITB)",
            "Fakultas Matematika dan Ilmu Pengetahuan Alam (FMIPA)",
            "Fakultas Seni Rupa dan Desain (FSRD)",
            "Fakultas Teknologi Industri (FTI)",
            "Fakultas Teknik Sipil dan Lingkungan (FTSL)",
            "Fakultas Teknik Mesin dan Dirgantara (FTMD)",
            "Fakultas Teknik Pertambangan dan Perminyakan (FTTM)",
            "Sekolah Arsitektur, Perencanaan dan Pengembangan Kebijakan (SAPPK)",
            "Sekolah Bisnis dan Manajemen (SBM)",
            "Sekolah Farmasi (SF)",
            "Sekolah Ilmu dan Teknologi Hayati (SITH)",
            "Sekolah Teknik Elektro dan Informatika (STEI)"]

prodiFITB = ["Teknik Geologi", "Teknik Geodesi dan Geomatika",
             "Meteorologi", "Oseanografi"]
prodiFMIPA = ["Matematika", "Fisika", "Astronomi", "Kimia"]
prodiFSRD = ["Seni Rupa", "Desain Interior",
             "Desain Komunikasi Visual", "Desain Produk"]
prodiFTI = ["Teknik Kimia", "Teknik Industri",
            "Teknik Fisika", "Manajemen Rekayasa Industri"]
prodiFTSL = ["Teknik Sipil", "Teknik Lingkungan", "Teknik Kelautan"]
prodiFTMD = ["Teknik Mesin", "Teknik Dirgantara", "Teknik Material"]
prodiFTTM = ["Teknik Pertambangan", "Teknik Perminyakan",
             "Teknik Geofisika", "Teknik Metalurgi"]
prodiSAPPK = ["Arsitektur", "Perencanaan Wilayah dan Kota"]
prodiSBM = ["Manajemen", "Kewirausahaan"]
prodiSF = ["Sains dan Teknologi Farmasi, Farmasi Klinik dan Komunitas"]
prodiSITH = ["Biologi", "Mikrobiologi", "Rekayasa Hayati",
             "Rekayasa Pertanian", "Rekayasa Kehutanan", "Teknologi Pasca Panen"]
prodiSTEI = ["Teknik Elektro", "Teknik Tenaga Listrik", "Teknik Telekomunikasi",
             "Teknik Biomedis", "Teknik Informatika", "Sistem dan Teknologi Informasi"]

inputFakultas = st.selectbox('Fakultas', fakultas)
if inputFakultas == fakultas[0]:
    inputProdi = st.selectbox('Program Studi', prodiFITB)
elif inputFakultas == fakultas[1]:
    inputProdi = st.selectbox('Program Studi', prodiFMIPA)
elif inputFakultas == fakultas[2]:
    inputProdi = st.selectbox('Program Studi', prodiFSRD)
elif inputFakultas == fakultas[3]:
    inputProdi = st.selectbox('Program Studi', prodiFTI)
elif inputFakultas == fakultas[4]:
    inputProdi = st.selectbox('Program Studi', prodiFTSL)
elif inputFakultas == fakultas[5]:
    inputProdi = st.selectbox('Program Studi', prodiFTMD)
elif inputFakultas == fakultas[6]:
    inputProdi = st.selectbox('Program Studi', prodiFTTM)
elif inputFakultas == fakultas[7]:
    inputProdi = st.selectbox('Program Studi', prodiSAPPK)
elif inputFakultas == fakultas[8]:
    inputProdi = st.selectbox('Program Studi', prodiSBM)
elif inputFakultas == fakultas[9]:
    inputProdi = st.selectbox('Program Studi', prodiSF)
elif inputFakultas == fakultas[10]:
    inputProdi = st.selectbox('Program Studi', prodiSITH)
elif inputFakultas == fakultas[11]:
    inputProdi = st.selectbox('Program Studi', prodiSTEI)

search = st.button("Search")


if search:
    st.session_state["Fakultas"] = inputFakultas
    st.session_state["Jurusan"] = inputProdi
    st.write("You have entered: ", inputFakultas + " and ", inputProdi)
