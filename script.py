import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from grapher import GrapherTracer, GrapherUser

# List Fakultas
fakultas = ["Fakultas Ilmu dan Teknologi Kebumian",
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
prodiFITB = ["Teknik Geologi", "Teknik Geodesi dan Geomatika",
             "Meteorologi", "Oseanografi", "Semua Prodi"]
prodiFMIPA = ["Matematika", "Fisika", "Astronomi", "Kimia", "Semua Prodi"]
prodiFSRD = ["Seni Rupa", "Desain Interior",
             "Desain Komunikasi Visual", "Desain Produk", "Semua Prodi"]
prodiFTI = ["Teknik Kimia", "Teknik Industri",
            "Teknik Fisika", "Manajemen Rekayasa Industri", "Semua Prodi"]
prodiFTSL = ["Teknik Sipil", "Teknik Lingkungan",
             "Teknik Kelautan", "Semua Prodi"]
prodiFTMD = ["Teknik Mesin", "Teknik Dirgantara",
             "Teknik Material", "Semua Prodi"]
prodiFTTM = ["Teknik Pertambangan", "Teknik Perminyakan",
             "Teknik Geofisika", "Teknik Metalurgi", "Semua Prodi"]
prodiSAPPK = ["Arsitektur", "Perencanaan Wilayah dan Kota", "Semua Prodi"]
prodiSBM = ["Manajemen", "Kewirausahaan", "Semua Prodi"]
prodiSF = [
    "Sains dan Teknologi Farmasi, Farmasi Klinik dan Komunitas", "Semua Prodi"]
prodiSITH = ["Biologi", "Mikrobiologi", "Rekayasa Hayati",
             "Rekayasa Pertanian", "Rekayasa Kehutanan", "Teknologi Pasca Panen", "Semua Prodi"]
prodiSTEI = ["Teknik Elektro", "Teknik Tenaga Listrik", "Teknik Telekomunikasi",
             "Teknik Biomedis", "Teknik Informatika", "Sistem dan Teknologi Informasi", "Semua Prodi"]

# List Grafik
listGraph = ["-", "Status Pekerjaan", "Data Responden",
             "Kompetensi Alumni", "7 Kompetensi Alumni (Tren)", "Waktu Tunggu Mendapatkan Pekerjaan (Sebelum Lulus)",
             "Waktu Tunggu Mendapatkan Pekerjaan (Sesudah Lulus)", "Kategori Perusahaan", "Kompetensi Alumni (User)"]

################################################################################################

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

requestGraph = st.selectbox('Grafik yang ingin ditampilkan', listGraph)

inputTahunDummy = st.empty()
if requestGraph == "Kompetensi Alumni" or requestGraph == "Kompetensi Alumni (User)":
    inputTahun = inputTahunDummy.selectbox(
        'Tahun', [2018, 2019, 2020, 2021, 2022])
else:
    inputTahunDummy.selectbox('Tahun', [], index=0)

######################################################################################################################

# Display the selected values
st.write('Fakultas:', inputFakultas)
st.write('Prodi:', inputProdi)
# st.write('Selected Option 3:', selected_option_3)
# st.write('Selected Option 4:', option_1+2)

######################################################################################################################
# Init Pandas dataframe, execute onetime only


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


##################################################################################################################################

# How to Use Grapher Class
gt = GrapherTracer(df2018, df2019, df2020, df2021,
                   df2022, inputProdi, inputFakultas)
gu = GrapherUser(dfUser2018, dfUser2019, dfUser2020,
                 dfUser2021, dfUser2022, inputProdi)
gt.cleanse_tracer_data()
gu.cleanse_user_data()

if requestGraph == "Data Responden":
    gt.init_respondent_data()
    gt.draw_respondent_data()
elif requestGraph == "Kompetensi Alumni":
    gt.init_competence_data()
    gt.draw_competence_data(year=inputTahun)
elif requestGraph == "Status Pekerjaan":
    gt.init_jobstatus_data()
    gt.draw_jobstatus_data()
elif requestGraph == "7 Kompetensi Alumni (Tren)":
    gt.init_competence_data()
    gt.draw_competence_trend_data()
elif requestGraph == "Waktu Tunggu Mendapatkan Pekerjaan (Sebelum Lulus)":
    gt.init_timetogetwork_data()
    gt.draw_timetogetwork_data(beforegrad=True)
elif requestGraph == "Waktu Tunggu Mendapatkan Pekerjaan (Sesudah Lulus)":
    gt.init_timetogetwork_data()
    gt.draw_timetogetwork_data()
elif requestGraph == "Kategori Perusahaan":
    gt.init_company_category_data()
    gt.draw_company_category_data()
elif requestGraph == "Kompetensi Alumni (User)":
    gu.init_competence_data()
    gu.draw_competence_data(year=inputTahun)
# if requestGraph == "Kompetensi Alumni":
#     gp.init_competence_data()
#     gp.draw_respondent_data()

# st.write("Hellows")
# def draw_respondent_data(dfcom18,dfcom19,dfcom20,dfcom21,dfcom22):

# year = np.array(['2018','2019','2020','2021','2022'])
# # df2019_competenceA_EL.shape[0] # To search The num Of Rows.
# RespondentEL= np.array([dfcom18.shape[0],
#                         dfcom19.shape[0],
#                         dfcom20.shape[0],
#                         dfcom21.shape[0],
#                         dfcom22.shape[0]])

# # Manually Inputted from Data responden 2018-2022.xlsx
# PercentageRespondentEL = np.array([dfcom18.shape[0]/153,
#                                     dfcom19.shape[0]/141,
#                                     dfcom20.shape[0]/136,
#                                     dfcom21.shape[0]/145,
#                                     dfcom22.shape[0]/94])

# # convert to pandas
# dfPercentage = pd.DataFrame(PercentageRespondentEL,index=year)

# fig,ax = plt.subplots(figsize=(20,10))
# rects1 = ax.bar(year,PercentageRespondentEL*100,color=['blue','orange','green','purple','red'],width=0.3)

# # Make description/annotation in above bar plots:
# i=0
# for rect in rects1:
#     height = rect.get_height()
#     ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
#             "[{}]; {}%".format(RespondentEL[i],int(round(height,0))), size=18,
#             ha='center', va='bottom')
#     i += 1

# ax.set_ylabel('Persentase Mahasiswa\nMengisi Kuesioner (%)\n',size=20)
# ax.set_xlabel('Tahun',size=20)

# # ax.set_title('Data Jumlah Responden Tracer Study \n (Prodi Teknik Elektro)\n',size=40)
# ax.set_yticks(range(0,110,10))
# ax.tick_params(axis='y', labelsize=20,labelcolor="black")
# ax.tick_params(axis='x',labelsize=20,pad=20)
# plt.show()
