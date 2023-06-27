import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
import plotly.express as px
sys.path.append(r'C:\Users\muhru\OneDrive\Documents\Magang TracerStudy\SourceDataMei\streamlit\Tracer Study 2\pages\backend' )

from grapher import GrapherTracer, DataframeInitializer
st.set_page_config(page_title="Plotting Demo", page_icon="📈")
st.title("Data Tren User Survey")
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

# List Grafik
listGraph = ["-", "Status Pekerjaan", "Data Responden",
             "Kompetensi Alumni", "7 Kompetensi Alumni (Tren)", "Waktu Tunggu Mendapatkan Pekerjaan (Sebelum Lulus)",
             "Waktu Tunggu Mendapatkan Pekerjaan (Sesudah Lulus)", "Kategori Perusahaan"]

################################################################################################

######################################################################################################################

# Display the selected values
inputFakultas = st.session_state["Fakultas"]
inputProdi = st.session_state["Jurusan"]
st.write('Fakultas:', inputFakultas)
st.write('Prodi:', inputProdi )
# st.write('Selected Option 3:', selected_option_3)
# st.write('Selected Option 4:', option_1+2)

######################################################################################################################
# Init Pandas dataframe, execute onetime only


@st.cache_data
def load_dataset():
    df2018 = pd.read_excel(
        r"C:\Users\muhru\OneDrive\Documents\Magang TracerStudy\SourceDataMei\Data Mentah Sortir_Analisis Tren_v3.xlsx", sheet_name="2018")
    df2019 = pd.read_excel(
        r"C:\Users\muhru\OneDrive\Documents\Magang TracerStudy\SourceDataMei\Data Mentah Sortir_Analisis Tren_v3.xlsx", sheet_name="2019")
    df2020 = pd.read_excel(
        r"C:\Users\muhru\OneDrive\Documents\Magang TracerStudy\SourceDataMei\Data Mentah Sortir_Analisis Tren_v3.xlsx", sheet_name="2020")
    df2021 = pd.read_excel(
        r"C:\Users\muhru\OneDrive\Documents\Magang TracerStudy\SourceDataMei\Data Mentah Sortir_Analisis Tren_v3.xlsx", sheet_name="2021")
    df2022 = pd.read_excel(
        r"C:\Users\muhru\OneDrive\Documents\Magang TracerStudy\SourceDataMei\Data Mentah Sortir_Analisis Tren_v3.xlsx", sheet_name="2022")

    dfUser2018 = pd.read_excel(
        r"C:\Users\muhru\OneDrive\Documents\Magang TracerStudy\SourceDataMei\Data Mentah Kuesioner User Survey_Analisis Tren_v3.xlsx", sheet_name="User Survey 2018")
    dfUser2019 = pd.read_excel(
        r"C:\Users\muhru\OneDrive\Documents\Magang TracerStudy\SourceDataMei\Data Mentah Kuesioner User Survey_Analisis Tren_v3.xlsx", sheet_name="User Survey 2019")
    dfUser2020 = pd.read_excel(
        r"C:\Users\muhru\OneDrive\Documents\Magang TracerStudy\SourceDataMei\Data Mentah Kuesioner User Survey_Analisis Tren_v3.xlsx", sheet_name="User Survey 2020")
    dfUser2021 = pd.read_excel(
        r"C:\Users\muhru\OneDrive\Documents\Magang TracerStudy\SourceDataMei\Data Mentah Kuesioner User Survey_Analisis Tren_v3.xlsx", sheet_name="User Survey 2021")
    dfUser2022 = pd.read_excel(
        r"C:\Users\muhru\OneDrive\Documents\Magang TracerStudy\SourceDataMei\Data Mentah Kuesioner User Survey_Analisis Tren_v3.xlsx", sheet_name="User Survey 2022")
    return df2018, df2019, df2020, df2021, df2022, dfUser2018, dfUser2019, dfUser2020, dfUser2021, dfUser2022


df2018, df2019, df2020, df2021, df2022, dfUser2018, dfUser2019, dfUser2020, dfUser2021, dfUser2022 = load_dataset()


##################################################################################################################################

# How to Use Grapher Class
gt = GrapherTracer(df2018, df2019, df2020, df2021, df2022, inputProdi)
gt.init_company_field_data()
gt.draw_company_field_data()
gt.cleanse_tracer_data()
gt.init_respondent_data()
gt.draw_respondent_data()
gt.init_competence_data()
gt.draw_competence_data(year=2018)
gt.draw_competence_data(year=2019)
gt.draw_competence_data(year=2020)
gt.draw_competence_data(year=2021)
gt.draw_competence_data(year=2022)
gt.init_jobstatus_data()
gt.draw_jobstatus_data()
gt.init_competence_data()
gt.draw_competence_trend_data()
gt.init_timetogetwork_data()
gt.draw_timetogetwork_data(beforegrad=True)
gt.init_timetogetwork_data()
gt.draw_timetogetwork_data()
gt.init_company_category_data()
gt.draw_company_category_data()

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
