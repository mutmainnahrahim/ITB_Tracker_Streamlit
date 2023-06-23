import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

#title
st.title("Angkatan 2011")
st.write("Data Angkatan Tahun 2011 (Tahun Survey 2018)", st.session_state["Fakultas"], "Prodi", st.session_state["Jurusan"])

#read data responden
df = pd.read_excel(
    io= "Data responden 2018-2022.xlsx",
    engine="openpyxl",
    sheet_name="sarjana_2018_ ang.2011",
    usecols="A:I",
    nrows=50,
)

#filter dataframe
selected_major = st.session_state["Jurusan"]
filtered_data = df[df['PRODI'] == selected_major]
row = df[df['PRODI'] == selected_major].index[0]
N = df["Status Pengisian Kuesioner"][row]
Total = df["Total Alumni (N)"][row]
N_persen = round(df["%"][row]*100)

#show
st.subheader("Data Responden")
st.write("Yang telah mengisi kuisioner: ", N)
st.write("Total alumni: ", Total)
st.write("Persentase data responden: ", N_persen,"%")
st.dataframe(filtered_data)

#---------------------------------STATUS PEKERJAAN-------------------------------------------#
dm = pd.read_excel(
    io= "Data Mentah Sortir_Analisis Tren_v3.xlsx",
    engine="openpyxl",
    sheet_name="2018",
    usecols="A:CP",
    nrows=3000,
)

#filter based on major
dm_filtered = dm[(dm['4. Program Studi']==selected_major)]

#calculate each status
bekerja_count = (dm_filtered['33. Pekerjaan utama saat ini?'] == 'bekerja').sum()
bnw_count = (dm_filtered['33. Pekerjaan utama saat ini?'] == 'bekerja dan wiraswasta').sum()
wir_count = (dm_filtered['33. Pekerjaan utama saat ini?'] == 'wirausaha').sum()
ms_count = (dm_filtered['33. Pekerjaan utama saat ini?'] == 'melanjutkan studi').sum()
tb_count = (dm_filtered['33. Pekerjaan utama saat ini?'] == 'tidak bekerja').sum()

#total
total = len(dm_filtered)

#persentase
bekerja_per = round(bekerja_count/total*100,2)
bnw_per = round(bnw_count/total*100,2)
wir_per = round(wir_count/total*100,2)
ms_per = round(ms_count/total*100,2)
tb_per = round(tb_count/total*100,2)

y_axis = ["Bekerja","Bekerja dan Wiraswasta","Wirausaha","Melanjutkan Studi","Tidak Bekerja"]
responden=[bekerja_count,bnw_count,wir_count,ms_count,tb_count]
x_axis = [bekerja_per,bnw_per,wir_per,ms_per,tb_per]
colors = ['#4e81bd', '#f79645', '#95b554', '#7e629f', '#b94a48']

st.subheader("Status Pekerjaan")

fig, ax = plt.subplots()
ax.bar(y_axis, x_axis, color=colors)
ax.yaxis.set_major_formatter(mtick.PercentFormatter())

#tambahkan label ke bar
for i,p in enumerate(x_axis):
    label= f"{[responden[i]]}; {p:.0f}%"
    ax.text(y_axis[i], p+1.5, label, ha='center')

st.pyplot(fig)

#--------------------------------------KOMPETENSI ALUMNI-----------------------------------#
st.subheader("Kompetensi Alumni")

#buat fungsi terlebih dahulu

def user_survey(year_file,i,year,categories):
    count = len(year_file)
    count_str = str(count)
    kompetensi = year_file.iloc[:,i:i+23]

    kompetensi_avg = []
    for coloumn in kompetensi:
        kompetensi_avg.append(kompetensi[coloumn].mean().round(2))
    kompetensi_avg.append(kompetensi_avg[0])

    #Average kontribusi tahun 2018
    kontribusi = year_file.iloc[:,i+23:i+46]

    kontribusi_avg = []
    for coloumn in kontribusi:
        kontribusi_avg.append(kontribusi[coloumn].mean().round(2))
    kontribusi_avg.append(kontribusi_avg[0])

    #Average peran tahun 2018
    peran = year_file.iloc[:,i+46:i+69]

    peran_avg = []
    for coloumn in peran:
        peran_avg.append(peran[coloumn].mean().round(2))
    peran_avg.append(peran_avg[0])

    # define nilai
    categories_new = categories[::-1]
    # Set the number of data points
    N = len(categories_new)

    # Calculate the angles for each data point
    angles = np.linspace(0, 2*np.pi, N, endpoint=False)

    # Close the polygon by repeating the first angle
    angles = np.concatenate((angles, [angles[0]]))

    # Set the colors for each line
    colors = ['#b94a48', '#95b554', '#4e81bd']

    # Create a figure and axis objects
    fig, ax = plt.subplots(1, 1, figsize=(20, 10), subplot_kw=dict(polar=True))
    #ax.set_thetagrids(angles * 180/np.pi, categories18)

    # Plot the data for each line
    ax.plot(angles, kompetensi_avg, 'o-', linewidth=1, linestyle='solid', color=colors[0], label='Kompetensi yang Dikuasai')
    ax.plot(angles, kontribusi_avg,'o-', linewidth=1, linestyle='solid', color=colors[1], label='Kontribusi Perguruan Tinggi')
    ax.plot(angles, peran_avg,'o-', linewidth=1, linestyle='solid', color=colors[2], label='Peran Kompetensi')

    # Set the labels for each data point
    ax.set_thetagrids(angles[:-1] * 180/np.pi, categories, ha='center')
    ax.set_rlim(0, 5)
    ax.set_title(year, pad='80', fontweight='bold', fontsize='30')


    # Add a legend for the lines
    ax.legend(loc='upper right', bbox_to_anchor=(1, 1.11), ncol=3)
    plt.figtext(0.72, 0.9, 'N = '+ count_str, ha='right', fontsize='15', fontweight='bold')


    # Show the plot
    #plt.show()
    st.pyplot(fig)

user_survey(dm_filtered,6,'Tahun 2018',['penilaian dan \npengambilan keputusan','negosiasi', 'kecerdasan dalam bertindak','kemampuan belajar','adaptasi \ndengan \nlingkungan','kejujuran, loyalitas \ndan integrasi','bekerja dalam tekanan','etika','orientasi layanan','pengetahuan dan \n penerapan\n bidang/\ndisiplin ilmu','pengetahuan di \n luar bidang/\ndisiplin ilmu','kemampuan \n analisis','kemampuan \n administrasi, \nmenuliskan \nlaporan/\ndokumen','keterampilan teknologi \ninformasi \ndan \nkomunikasi', 'merancang dan/atau mendesain suatu komponen, sistem atau proses','berkomunikasi \nmenggunakan \nbahasa asing','memecahkan\n masalah\n kompleks', 'berpikir kritis', 'kreativitas', 'manajemen \ndiri dan\n orang lain', 'bekerja tim', 'bekerja \nindividu', 'kecerdasan\n emosional'])






