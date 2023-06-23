import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Dashboard",page_icon="🌍",layout="wide")
st.subheader("📊  Data")
st.markdown("##")

#side bar
st.sidebar.image("data/logo.jpeg",caption="ITB Tracer Study")

# List Fakultas
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

# List Prodi
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

#switcher
st.sidebar.header("Please filter")
inputFakultas=st.sidebar.selectbox(
    "Pilih Fakultas",
    options=fakultas
)

if inputFakultas == fakultas[0]:
    inputProdi = st.sidebar.multiselect('Program Studi', prodiFITB)
elif inputFakultas == fakultas[1]:
    inputProdi = st.sidebar.multiselect('Program Studi', prodiFMIPA)
elif inputFakultas == fakultas[2]:
    inputProdi = st.sidebar.multiselect('Program Studi', prodiFSRD)
elif inputFakultas == fakultas[3]:
    inputProdi = st.sidebar.multiselect('Program Studi', prodiFTI)
elif inputFakultas == fakultas[4]:
    inputProdi = st.sidebar.multiselect('Program Studi', prodiFTSL)
elif inputFakultas == fakultas[5]:
    inputProdi = st.sidebar.multiselect('Program Studi', prodiFTMD)
elif inputFakultas == fakultas[6]:
    inputProdi = st.sidebar.multiselect('Program Studi', prodiFTTM)
elif inputFakultas == fakultas[7]:
    inputProdi = st.sidebar.multiselect('Program Studi', prodiSAPPK)
elif inputFakultas == fakultas[8]:
    inputProdi = st.sidebar.multiselect('Program Studi', prodiSBM)
elif inputFakultas == fakultas[9]:
    inputProdi = st.sidebar.multiselect('Program Studi', prodiSF)
elif inputFakultas == fakultas[10]:
    inputProdi = st.sidebar.multiselect('Program Studi', prodiSITH)
elif inputFakultas == fakultas[11]:
    inputProdi = st.sidebar.multiselect('Program Studi', prodiSTEI)

years_2018=st.sidebar.checkbox(
    "2018",
)
years_2019=st.sidebar.checkbox(
    "2019",
)
years_2020=st.sidebar.checkbox(
    "2020",
)
years_2021=st.sidebar.checkbox(
    "2021",
)
years_2022=st.sidebar.checkbox(
    "2022",
)

def sideBar():

 with st.sidebar:
    selected=option_menu(
        menu_title="Tampilan",
        options=["Data Responden","Status Pekerjaan"],
        icons=["house","eye"],
        menu_icon="cast",
        default_index=0
    )
 #if selected=="Home":
    #st.subheader(f"Page: {selected}")
    #Home()
    #graphs()
 #if selected=="Progress":
    #st.subheader(f"Page: {selected}")
    #Progressbar()
    #graphs()

sideBar()




