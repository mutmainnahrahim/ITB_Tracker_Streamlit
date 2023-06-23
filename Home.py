import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Dashboard",page_icon="🌍",layout="wide")
st.subheader("📊  Data")
st.markdown("##")

#side bar
st.sidebar.image("logo.jpeg",caption="ITB Tracer Study")

# List Fakultas
fakultas = ["All", "Fakultas Ilmu dan Teknologi Kebumian",
            "Fakultas Matematika dan Ilmu Pengetahuan Alam",
            "Fakultas Seni Rupa dan Desain",
            "Fakultas Teknologi Industri",
            "Fakultas Teknik Sipil dan Lingkungan",
            "Fakultas Teknik Mesin dan Dirgantara",
            "Fakultas Teknik Pertambangan dan Perminyakan",
            "Sekolah Arsitektur, Perencanaan dan Pengembangan Kebijakan",
            "Sekolah Bisnis dan Manajemen",
            "Sekolah Farmasi",
            "Sekolah Ilmu dan Teknologi Hayati",
            "Sekolah Teknik Elektro dan Informatika"]

# List Prodi
prodiAll = ["All", "Teknik Geologi", "Teknik Geodesi dan Geomatika",
             "Meteorologi", "Oseanografi","Matematika", "Fisika", "Astronomi", "Kimia","Seni Rupa", "Desain Interior",
             "Desain Komunikasi Visual", "Desain Produk","Teknik Kimia", "Teknik Industri",
            "Teknik Fisika", "Manajemen Rekayasa Industri","Teknik Sipil", "Teknik Lingkungan", "Teknik Kelautan","Teknik Mesin", "Teknik Dirgantara", "Teknik Material","Teknik Pertambangan", "Teknik Perminyakan",
             "Teknik Geofisika", "Teknik Metalurgi","Arsitektur", "Perencanaan Wilayah dan Kota","Manajemen", "Kewirausahaan","Sains dan Teknologi Farmasi, Farmasi Klinik dan Komunitas","Biologi", "Mikrobiologi", "Rekayasa Hayati",
             "Rekayasa Pertanian", "Rekayasa Kehutanan", "Teknologi Pasca Panen","Teknik Elektro", "Teknik Tenaga Listrik", "Teknik Telekomunikasi",
             "Teknik Biomedis", "Teknik Informatika", "Sistem dan Teknologi Informasi"]
prodiFITB = ["All", "Teknik Geologi", "Teknik Geodesi dan Geomatika",
             "Meteorologi", "Oseanografi"]
prodiFMIPA = ["All","Matematika", "Fisika", "Astronomi", "Kimia"]
prodiFSRD = ["All","Seni Rupa", "Desain Interior",
             "Desain Komunikasi Visual", "Desain Produk"]
prodiFTI = ["All","Teknik Kimia", "Teknik Industri",
            "Teknik Fisika", "Manajemen Rekayasa Industri"]
prodiFTSL = ["All","Teknik Sipil", "Teknik Lingkungan", "Teknik Kelautan"]
prodiFTMD = ["All","Teknik Mesin", "Teknik Dirgantara", "Teknik Material"]
prodiFTTM = ["All","Teknik Pertambangan", "Teknik Perminyakan",
             "Teknik Geofisika", "Teknik Metalurgi"]
prodiSAPPK = ["All","Arsitektur", "Perencanaan Wilayah dan Kota"]
prodiSBM = ["All","Manajemen", "Kewirausahaan"]
prodiSF = ["All","Sains dan Teknologi Farmasi, Farmasi Klinik dan Komunitas"]
prodiSITH = ["All","Biologi", "Mikrobiologi", "Rekayasa Hayati",
             "Rekayasa Pertanian", "Rekayasa Kehutanan", "Teknologi Pasca Panen"]
prodiSTEI = ["All","Teknik Elektro", "Teknik Tenaga Listrik", "Teknik Telekomunikasi",
             "Teknik Biomedis", "Teknik Informatika", "Sistem dan Teknologi Informasi"]

#switcher
st.sidebar.header("Please filter")
inputFakultas=st.sidebar.selectbox(
    "Pilih Fakultas",
    options=fakultas
)

if inputFakultas == fakultas[0]:
    inputProdi = st.sidebar.selectbox('Program Studi', prodiAll)
elif inputFakultas == fakultas[1]:
    inputProdi = st.sidebar.selectbox('Program Studi', prodiFITB)
elif inputFakultas == fakultas[2]:
    inputProdi = st.sidebar.selectbox('Program Studi', prodiFMIPA)
elif inputFakultas == fakultas[3]:
    inputProdi = st.sidebar.selectbox('Program Studi', prodiFSRD)
elif inputFakultas == fakultas[4]:
    inputProdi = st.sidebar.selectbox('Program Studi', prodiFTI)
elif inputFakultas == fakultas[5]:
    inputProdi = st.sidebar.selectbox('Program Studi', prodiFTSL)
elif inputFakultas == fakultas[6]:
    inputProdi = st.sidebar.selectbox('Program Studi', prodiFTMD)
elif inputFakultas == fakultas[7]:
    inputProdi = st.sidebar.selectbox('Program Studi', prodiFTTM)
elif inputFakultas == fakultas[8]:
    inputProdi = st.sidebar.selectbox('Program Studi', prodiSAPPK)
elif inputFakultas == fakultas[9]:
    inputProdi = st.sidebar.selectbox('Program Studi', prodiSBM)
elif inputFakultas == fakultas[10]:
    inputProdi = st.sidebar.selectbox('Program Studi', prodiSF)
elif inputFakultas == fakultas[11]:
    inputProdi = st.sidebar.selectbox('Program Studi', prodiSITH)
elif inputFakultas == fakultas[12]:
    inputProdi = st.sidebar.selectbox('Program Studi', prodiSTEI)

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
        options=["Data Responden","Status Pekerjaan", "Kompetensi Alumni", "Tren Kompetensi Alumni", "Tingkat Kepentingan dan Kepuasan User", "Tren Penilaian Tingkat Kepentingan dan Kepuasan User", "Waktu Tunggu", "Jenis Perusahaan", "Kategori Perusahaan", "Kategori Bidang Usaha", "Kesesuaian Kuliah dengan Pekerjaan", "Penghasilan"],
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




