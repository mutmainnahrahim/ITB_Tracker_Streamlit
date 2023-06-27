import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from dataframeinitializer import DataframeTracerInitializer, DataframeUserInitializer
import plotly.express as px
# matplotlib.use('TkAgg')  # or any other GUI backend of your choice


class GrapherTracer(DataframeTracerInitializer):
    def __init__(self, df2018, df2019, df2020, df2021, df2022, prodi,fakultas):
        super().__init__(df2018, df2019, df2020, df2021, df2022, prodi,fakultas)
        # self.graph = graph
        self.modeProdi = True
        if prodi == "All":
            self.modeProdi = False

    def draw_respondent_data(self):
        year = np.array(['2018', '2019', '2020', '2021', '2022'])
        # df2019_competenceA_EL.shape[0] # To search The num Of Rows.
        Respondent_Prodi = np.array([self.df2018_competenceA_Prodi.shape[0],
                                     self.df2019_competenceA_Prodi.shape[0],
                                     self.df2020_competenceA_Prodi.shape[0],
                                     self.df2021_competenceA_Prodi.shape[0],
                                     self.df2022_competenceA_Prodi.shape[0]])

        # Manually Inputted from Data responden 2018-2022.xlsx
        PercentageRespondent_Prodi = np.array([self.df2018_competenceA_Prodi.shape[0]/153,
                                               self.df2019_competenceA_Prodi.shape[0]/141,
                                               self.df2020_competenceA_Prodi.shape[0]/136,
                                               self.df2021_competenceA_Prodi.shape[0]/145,
                                               self.df2022_competenceA_Prodi.shape[0]/94])

        # convert to pandas
        dfPercentage = pd.DataFrame(PercentageRespondent_Prodi, index=year)

        fig, ax = plt.subplots(figsize=(20, 10))
        rects1 = ax.bar(year, PercentageRespondent_Prodi*100,
                        color=['blue', 'orange', 'green', 'purple', 'red'], width=0.3)

        # Make description/annotation in above bar plots:
        i = 0
        for rect in rects1:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                    "[{}]; {}%".format(Respondent_Prodi[i], int(round(height, 0))), size=18,
                    ha='center', va='bottom')
            i += 1

        ax.set_ylabel('Persentase Mahasiswa\nMengisi Kuesioner (%)\n', size=20)
        ax.set_xlabel('Tahun', size=20)

        # ax.set_title('Data Jumlah Responden Tracer Study \n (Prodi Teknik Elektro)\n',size=40)
        ax.set_yticks(range(0, 110, 10))
        ax.tick_params(axis='y', labelsize=20, labelcolor="black")
        ax.tick_params(axis='x', labelsize=20, pad=20)
        st.pyplot(fig)

    def draw_competence_data(self, year):

        if self.modeProdi:
            if year == 2018:
                competenceA = self.df2018_competenceA_Prodi
                competenceB = self.df2018_competenceB_Prodi
                competenceC = self.df2018_competenceC_Prodi
                competenciesLabel = self.competencies2018
            elif year == 2019:
                competenceA = self.df2019_competenceA_Prodi
                competenceB = self.df2019_competenceB_Prodi
                competenceC = self.df2019_competenceC_Prodi
                competenciesLabel = self.competencies2019
            elif year == 2020:
                competenceA = self.df2020_competenceA_Prodi
                competenceB = self.df2020_competenceB_Prodi
                competenceC = self.df2020_competenceC_Prodi
                competenciesLabel = self.competencies2020
            elif year == 2021:
                competenceA = self.df2021_competenceA_Prodi
                competenceB = self.df2021_competenceB_Prodi
                competenceC = self.df2021_competenceC_Prodi
                competenciesLabel = self.competencies2021
            elif year == 2022:
                competenceA = self.df2022_competenceA_Prodi
                competenceB = self.df2022_competenceB_Prodi
                competenceC = self.df2022_competenceC_Prodi
                competenciesLabel = self.competencies2022
        else:
            if year == 2018:
                competenceA = self.df2018_competenceA_fakultas
                competenceB = self.df2018_competenceB_fakultas
                competenceC = self.df2018_competenceC_fakultas
                competenciesLabel = self.competencies2018
            elif year == 2019:
                competenceA = self.df2019_competenceA_fakultas
                competenceB = self.df2019_competenceB_fakultas
                competenceC = self.df2019_competenceC_fakultas
                competenciesLabel = self.competencies2019
            elif year == 2020:
                competenceA = self.df2020_competenceA_fakultas
                competenceB = self.df2020_competenceB_fakultas
                competenceC = self.df2020_competenceC_fakultas
                competenciesLabel = self.competencies2020
            elif year == 2021:
                competenceA = self.df2021_competenceA_fakultas
                competenceB = self.df2021_competenceB_fakultas
                competenceC = self.df2021_competenceC_fakultas
                competenciesLabel = self.competencies2021
            elif year == 2022:
                competenceA = self.df2022_competenceA_fakultas
                competenceB = self.df2022_competenceB_fakultas
                competenceC = self.df2022_competenceC_fakultas
                competenciesLabel = self.competencies2022

        # Extract Mean Of Competence Values
        arr_meanA = np.array(competenceA.mean())
        arr_meanB = np.array(competenceB.mean())
        arr_meanC = np.array(competenceC.mean())

        # Plotting
        plt.style.use('ggplot')

        # Create Polar Axis
        fig = plt.figure(figsize=(30, 15))
        ax = fig.add_subplot(111, polar=True)
        ax.set_theta_zero_location("N", offset=15)

        # Set the number of angles/coordinates to be used for the radar plot
        angles = np.linspace(
            0, 2*np.pi, len(competenciesLabel[::-1]), endpoint=False)
        angles = np.concatenate((angles, [angles[0]]))

        # Plot the data
        arr_meanA = np.concatenate((arr_meanA[::-1], [arr_meanA[::-1][0]]))
        arr_meanB = np.concatenate((arr_meanB[::-1], [arr_meanB[::-1][0]]))
        arr_meanC = np.concatenate((arr_meanC[::-1], [arr_meanC[::-1][0]]))

        ax.plot(angles, arr_meanA, 'o-', linewidth=4,
                label="Kompetensi\nyang\nDikuasai", color="blue", markersize=12)
        ax.plot(angles, arr_meanB, 'o-', linewidth=4,
                label="Kontribusi\nPerguruan\nTinggi", color="red", markersize=12)
        ax.plot(angles, arr_meanC, 'o-', linewidth=4,
                label="Peran\nKompetensi", color="green", markersize=12)

        # Fill the area inside the plot (optional)
        # ax.fill(angles, values, alpha=0.25)

        # Set Grids, and other parameters to make graph more neat
        ax.set_thetagrids(angles[:-1] * 180/np.pi, competenciesLabel[::-1])
        ax.set_xticks(angles[:-1], competenciesLabel[::-1],
                      color='black', size=20)
        ax.tick_params(axis='y', labelcolor='black', labelsize=25, grid_linestyle='--',
                       grid_color='black', grid_alpha=0.5, grid_linewidth=1.5)
        plt.yticks([0.0, 1.0, 2.0, 3.0, 4.0, 5.0],)
        ax.tick_params(axis='x', grid_color='black', grid_alpha=0.4,
                       grid_linestyle='-.', top=True, direction='out', pad=65)

        # Set the plot title, and its margin y
        plt.title("Kompetensi Alumni - {} (N=124)".format(year),
                  loc='center', y=1.3, fontsize=30)

        # Add a legend, bbox_to_anchor to make custom position
        plt.legend(bbox_to_anchor=([0.125, 0.75, 0.5, 0.5]),
                   loc='upper left', fontsize=20, ncol=3)

        # Show the plot
        st.pyplot(fig)

    def draw_jobstatus_data(self):
        # Datasets
        year = np.array(['2018', '2019', '2020', '2021', '2022'])
        bekerja = self.workstatus_perc.T[0]
        bekerja2 = self.workstatus_perc.T[1]
        studi = self.workstatus_perc.T[3]
        not_bekerja = self.workstatus_perc.T[4]
        wirausaha = self.workstatus_perc.T[2]

        # create a figure with 5 subplots
        fig, axes = plt.subplots(nrows=1, ncols=5, figsize=(25, 8))

        """
        ========================================================
        axes[0] : bekerja
        =========================================================
        """
        rects_bekerja = axes[0].bar(
            year, bekerja*100, color=['blue', 'orange', 'green', 'purple', 'red'], width=0.3)

        # Make description/annotation in abova bar plots:
        i = 0
        for rect in rects_bekerja:
            height = rect.get_height()
            axes[0].text(rect.get_x() + rect.get_width()/2., 1.05*height,
                         "[{:.0f}];\n {:.0f}%".format(self.workstatus_num.T[0][i], height), size=12,
                         ha='center', va='bottom')
            i += 1

        # axes[0].set_ylabel('Persentase Mahasiswa\nMengisi Kuesioner (%)\n',size=20)
        axes[0].set_xlabel('\nBekerja', size=20)

        # axes[0].set_title('Data Jumlah Responden Tracer Study \n (Prodi Teknik Elektro)\n',size=40)
        axes[0].set_yticks(range(0, 110, 10))
        axes[0].tick_params(axis='y', labelsize=20, labelcolor="black")
        axes[0].tick_params(axis='x', labelsize=20,
                            labelcolor="black", labelrotation=45, pad=20)

        """
        ========================================================
        axes[1] : bekerja dan wiraswasta
        =========================================================
        """
        rects_bekerja2 = axes[1].bar(
            year, bekerja2*100, color=['blue', 'orange', 'green', 'purple', 'red'], width=0.3)

        # Make description/annotation in abova bar plots:
        i = 0
        for rect in rects_bekerja2:
            height = rect.get_height()
            axes[1].text(rect.get_x() + rect.get_width()/2., 1.05*height,
                         "[{:.0f}];\n {:.0f}%".format(self.workstatus_num.T[1][i], height), size=12,
                         ha='center', va='bottom')
            i += 1

        axes[1].set_xlabel('\nBekerja dan \nwiraswasta', size=20)
        axes[1].set_yticks(range(0, 110, 10))
        axes[1].tick_params(axis='y', labelsize=20, labelcolor="black")
        axes[1].tick_params(axis='x', labelsize=20,
                            labelcolor="black", labelrotation=45, pad=20)

        """
        ========================================================
        axes[3] : studi
        =========================================================
        """
        rects_studi = axes[3].bar(
            year, studi*100, color=['blue', 'orange', 'green', 'purple', 'red'], width=0.3)

        # Make description/annotation in abova bar plots:
        i = 0
        for rect in rects_studi:
            height = rect.get_height()
            axes[3].text(rect.get_x() + rect.get_width()/2., 1.05*height,
                         "[{:.0f}];\n {:.0f}%".format(self.workstatus_num.T[3][i], height), size=12,
                         ha='center', va='bottom')
            i += 1

        axes[3].set_xlabel('\nMelanjutkan \nStudi', size=20)
        axes[3].set_yticks(range(0, 110, 10))
        axes[3].tick_params(axis='y', labelsize=20, labelcolor="black")
        axes[3].tick_params(axis='x', labelsize=20,
                            labelcolor="black", labelrotation=45, pad=20)

        """
        ========================================================
        axes[4] : not_bekerja
        =========================================================
        """
        rects_not_bekerja = axes[4].bar(
            year, not_bekerja*100, color=['blue', 'orange', 'green', 'purple', 'red'], width=0.3)

        # Make description/annotation in abova bar plots:
        i = 0
        for rect in rects_not_bekerja:
            height = rect.get_height()
            axes[4].text(rect.get_x() + rect.get_width()/2., 1.05*height,
                         "[{:.0f}];\n {:.0f}%".format(self.workstatus_num.T[4][i], height), size=12,
                         ha='center', va='bottom')
            i += 1

        axes[4].set_xlabel('\nTidak\nBekerja', size=20)
        axes[4].set_yticks(range(0, 110, 10))
        axes[4].tick_params(axis='y', labelsize=20, labelcolor="black")
        axes[4].tick_params(axis='x', labelsize=20,
                            labelcolor="black", labelrotation=45, pad=20)

        """
        ========================================================
        axes[2] : wirausaha
        =========================================================
        """
        rects_wirausaha = axes[2].bar(
            year, wirausaha*100, color=['blue', 'orange', 'green', 'purple', 'red'], width=0.3)

        # Make description/annotation in abova bar plots:
        i = 0
        for rect in rects_wirausaha:
            height = rect.get_height()
            axes[2].text(rect.get_x() + rect.get_width()/2., 1.05*height,
                         "[{:.0f}];\n {:.0f}%".format(self.workstatus_num.T[2][i], height), size=12,
                         ha='center', va='bottom')
            i += 1

        axes[2].set_xlabel('\nWirausaha', size=20)
        axes[2].set_yticks(range(0, 110, 10))
        axes[2].tick_params(axis='y', labelsize=20, labelcolor="black")
        axes[2].tick_params(axis='x', labelsize=20,
                            labelcolor="black", labelrotation=45, pad=20)

        # set the title for each subplot
        # fig.text(0.5,1,'Status Pekerjaan \nAlumni Teknik Elektro ITB',ha='center',rotation='horizontal',size=20)

        # set the common y-axis label
        fig.text(0.08, 0.4, 'Jumlah Alumni Bekerja (%)',
                 va='center', rotation='vertical', size=20)

        # adjust the layout
        # fig.tight_layout()

        # display the plot
        st.pyplot(fig)

    def draw_competence_trend_data(self):
        fig = plt.figure(figsize=(15, 15))
        ax = fig.add_subplot(111, polar=True)
        ax.set_theta_zero_location('S', offset=77)
        # Set the number of angles/coordinates to be used for the radar plot
        angles = np.linspace(
            0, 2*np.pi, len(self.categoriesTrend), endpoint=False)
        # angles = angles - 1.57
        angles = np.concatenate((angles, [angles[0]]))

        # Plot the data
        __means2018 = np.concatenate((self.means2018, [self.means2018[0]]))
        __means2019 = np.concatenate((self.means2019, [self.means2019[0]]))
        __means2020 = np.concatenate((self.means2020, [self.means2020[0]]))
        __means2021 = np.concatenate((self.means2021, [self.means2021[0]]))
        __means2022 = np.concatenate((self.means2022, [self.means2022[0]]))

        ax.plot(angles, __means2018, 'o-', linewidth=4,
                label="2018", color='blue', markersize=12)
        ax.plot(angles, __means2019, 'o-', linewidth=4,
                label="2019", color='orange', markersize=12)
        ax.plot(angles, __means2020, 'o-', linewidth=4,
                label="2020", color='green', markersize=12)
        ax.plot(angles, __means2021, 'o-', linewidth=4,
                label="2021", color='purple', markersize=12)
        ax.plot(angles, __means2022, 'o-', linewidth=4,
                label="2022", color='red', markersize=12)

        # Fill the area inside the plot (optional)
        # ax.fill(angles, values, alpha=0.25)

        # Set Grids, and other parameters to make graph more neat
        ax.set_thetagrids(angles[:-1] * 180/np.pi, self.categoriesTrend)
        ax.set_xticks(angles[:-1], self.categoriesTrend,
                      color='black', size=20)
        ax.tick_params(axis='y', labelcolor='black', labelsize=25, grid_linestyle='--',
                       grid_color='black', grid_alpha=0.5, grid_linewidth=1.5)
        plt.yticks([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        ax.tick_params(axis='x', grid_color='black', grid_alpha=0.4,
                       grid_linestyle='-.', top=True, direction='out', pad=65)

        # Set the plot title, and its margin y
        plt.title("Tren Kompetensi Alumni Tahun 2018-2022: \nPenguasaan Kompetensi ",
                  loc='center', y=1.3, fontsize=30)

        # Add a legend, bbox_to_anchor to make custom position
        plt.legend(bbox_to_anchor=([0.2, 0.75, 0.5, 0.5]),
                   loc='upper left', fontsize=20, ncol=3)

        # Show the plot
        st.pyplot(fig)

    def draw_timetogetwork_data(self, beforegrad=False):

        if beforegrad:
            __medians = np.array([
                self.dfTTGWork2018_Prodi_BeforeGrad.describe().T["50%"][0],
                self.dfTTGWork2019_Prodi_BeforeGrad.describe().T["50%"][0],
                self.dfTTGWork2020_Prodi_BeforeGrad.describe().T["50%"][0],
                self.dfTTGWork2021_Prodi_BeforeGrad.describe().T["50%"][0],
                self.dfTTGWork2022_Prodi_BeforeGrad.describe().T["50%"][0]
            ])
            __string = "Sebelum"
        else:
            __medians = np.array([
                self.dfTTGWork2018_Prodi_AfterGrad.describe().T["50%"][1],
                self.dfTTGWork2019_Prodi_AfterGrad.describe().T["50%"][1],
                self.dfTTGWork2020_Prodi_AfterGrad.describe().T["50%"][1],
                self.dfTTGWork2021_Prodi_AfterGrad.describe().T["50%"][1],
                self.dfTTGWork2022_Prodi_AfterGrad.describe().T["50%"][1]
            ])
            __string = "Sesudah"

        year = np.array(["2018", "2019", "2020", "2021", "2022"])

        fig, ax = plt.subplots(figsize=(12, 6))

        ax.plot(year, __medians, 'o-', linewidth=3,
                label="Median", color="blue", markersize=10)
        ax.tick_params(axis='y', labelcolor='black', labelsize=25,
                       grid_color='black', grid_alpha=0.4)
        ax.set_xlabel("Tahun", size=25, labelpad=20, color="black")
        ax.set_ylabel("Median (Bulan)", size=25, labelpad=20, color="black")
        ax.tick_params(axis='x', grid_color='black', labelsize=25,
                       grid_alpha=0.4, top=True, direction='out', labelcolor='black')
        plt.title("Waktu Tunggu Kerja ({} Lulus), dalam Median".format(
            __string), loc='center', y=1.1, size=25)
        st.pyplot(fig)

    def draw_company_category_data(self):
    
        # create sample data
        categoryCompany = ['Lokal', 'Nasional', 'Internasional']
        years = ['2018', '2019', '2020', '2021', '2022']

        # Still manually  for value_counts
        if self.prodi != "All":
            valuesLokal = self.valueCompanyCat_Prodi.T[0]
            valuesInternasional = self.valueCompanyCat_Prodi.T[1]
            valuesNasional = self.valueCompanyCat_Prodi.T[2]
            valuesLokal, valuesNasional, valuesInternasional = valuesLokal[::-
                                                                        1], valuesNasional[::-1], valuesInternasional[::-1]
        else:
            valuesLokal = self.valueCompanyCat_fakultas.T[0]
            valuesInternasional = self.valueCompanyCat_fakultas.T[1]
            valuesNasional = self.valueCompanyCat_fakultas.T[2]
            valuesLokal, valuesNasional, valuesInternasional = valuesLokal[::-
                                                                        1], valuesNasional[::-1], valuesInternasional[::-1]


        # Calculate Percentage Relative to ALL CATEGORIES
        pvaluesLokal = []
        pvaluesInternasional = []
        pvaluesNasional = []
        for i, (vl, vn, vi) in enumerate(zip(valuesLokal, valuesNasional, valuesInternasional)):
            total = vl+vn+vi
            pvaluesLokal.append(round(1000*vl/total))
            pvaluesNasional.append(round(1000*vn/total))
            pvaluesInternasional.append(round(1000*vi/total))

        # create horizontal stacked bar chart
        fig, ax = plt.subplots(figsize=(40/2, 20/2))
        con1 = ax.barh(years[::-1], pvaluesLokal,
                       label=categoryCompany[0], height=0.3, color='#2F79C3')
        con2 = ax.barh(years[::-1], pvaluesNasional, left=pvaluesLokal,
                       label=categoryCompany[1], height=0.3, color='#EC2D2D')
        con3 = ax.barh(years[::-1], pvaluesInternasional, left=np.array(pvaluesLokal) +
                       np.array(pvaluesNasional), label=categoryCompany[2], height=0.3, color='#6EC740')
        # add text descriptions on bars
        for i, (v1, v2, v3, pv1, pv2, pv3) in enumerate(zip(valuesLokal, valuesNasional, valuesInternasional,
                                                            pvaluesLokal, pvaluesNasional, pvaluesInternasional)):
            # ax.bar_label(ax.containers[0], fmt=("[{}];{}".format(v1,(str(round(pv1*100))+"%%"))), label_type='center', fontsize=12)
            # ax.bar_label(ax.containers[1], fmt=("[{}];{}".format(v2,(str(round(pv2*100))+"%%"))) , label_type='center', fontsize=12)
            # ax.bar_label(ax.containers[2], fmt=("[{}];{}".format(v3,(str(round(pv3*100))+"%%"))), label_type='center', fontsize=12)
            ax.text(pv1/2, i, "[{}];{}".format(v1, (str(round(pv1/10))+"%")),
                    ha='center', va='center', color='white', fontsize=16)
            ax.text(pv1+pv2/2, i, "[{}];{}".format(v2, (str(round(pv2/10))+"%")),
                    ha='center', va='center', color='white', fontsize=16)
            ax.text(pv1+pv2+pv3/2, i, "[{}];{}".format(v3, (str(round(pv3/10))+"%")),
                    ha='center', va='center', color='white', fontsize=16)

        # set legend and axis
        ax.set_xticks([])
        ax.set_xticklabels([])
        ax.set_ylabel('Tahun', size=20)
        ax.tick_params(axis='y', labelsize=20, labelcolor="black")
        ax.tick_params(axis='x', labelsize=20, pad=20)
        plt.legend(categoryCompany, bbox_to_anchor=(
            [0.0, -0.2, 0.9, 0]), loc='lower center', fontsize=20, ncol=3)

        st.pyplot(fig)
    
    def draw_company_field_data(self):
        
        dfcomfield = self.valueCompanyField_Prodi
        dfcomfieldt = dfcomfield.T
        dfcomfieldt["sum"] =dfcomfieldt.sum(axis =1)
        #HITUNG PERSEN
        percentcomfield = dfcomfieldt.div(dfcomfieldt["sum"], axis=0)*100
        percentcomfield.pop("sum")
        fig = px.bar(percentcomfield, barmode='stack', title="Kategori Perusahaan (Bekerja)")
        fig2 = px.line(percentcomfield, title="Kategori Perusahaan (Bekerja)")
        st.plotly_chart(fig, use_container_width=True) 
        st.plotly_chart(fig2, use_container_width=True) 
        
        
class GrapherUser(DataframeUserInitializer):
    def __init__(self, dfUser2018, dfUser2019, dfUser2020, dfUser2021, dfUser2022, prodi):
        super().__init__(dfUser2018=dfUser2018,
                         dfUser2019=dfUser2019,
                         dfUser2020=dfUser2020,
                         dfUser2021=dfUser2021,
                         dfUser2022=dfUser2022,
                         prodi=prodi)
        # self.graph = graph

    def draw_competence_data(self, year):
        # Extract Mean Of Competence Values
        if year == 2018:
            kepentingan = self.dfUser2018_Kepentingan_Prodi
            kepuasan = self.dfUser2018_Kepuasan_Prodi
            competencies = self.competencies2018
        elif year == 2019:
            kepentingan = self.dfUser2019_Kepentingan_Prodi
            kepuasan = self.dfUser2019_Kepuasan_Prodi
            competencies = self.competencies2019
        elif year == 2020:
            kepentingan = self.dfUser2020_Kepentingan_Prodi
            kepuasan = self.dfUser2020_Kepuasan_Prodi
            competencies = self.competencies2020
        elif year == 2021:
            kepentingan = self.dfUser2021_Kepentingan_Prodi
            kepuasan = self.dfUser2021_Kepuasan_Prodi
            competencies = self.competencies2021
        elif year == 2022:
            kepentingan = self.dfUser2021_Kepentingan_Prodi
            kepuasan = self.dfUser2021_Kepuasan_Prodi
            competencies = self.competencies2022

        arr_meanA = np.array(kepentingan.mean())
        arr_meanB = np.array(kepuasan.mean())

        # Plotting
        plt.style.use('ggplot')

        # Create Polar Axis
        fig = plt.figure(figsize=(30, 15))
        ax = fig.add_subplot(111, polar=True)
        ax.set_theta_zero_location("N", offset=15)

        # Set the number of angles/coordinates to be used for the radar plot
        angles = np.linspace(
            0, 2*np.pi, len(self.competencies2018[::-1]), endpoint=False)
        angles = np.concatenate((angles, [angles[0]]))

        # Plot the data
        arr_meanA = np.concatenate((arr_meanA[::-1], [arr_meanA[::-1][0]]))
        arr_meanB = np.concatenate((arr_meanB[::-1], [arr_meanB[::-1][0]]))

        ax.plot(angles, arr_meanA, 'o-', linewidth=4,
                label="Kepentingan", color="blue", markersize=12)
        ax.plot(angles, arr_meanB, 'o-', linewidth=4,
                label="Kepuasan", color="red", markersize=12)

        # Fill the area inside the plot (optional)
        # ax.fill(angles, values, alpha=0.25)

        # Set Grids, and other parameters to make graph more neat
        ax.set_thetagrids(angles[:-1] * 180/np.pi, competencies[::-1])
        ax.set_xticks(
            angles[:-1], competencies[::-1], color='black', size=20)
        ax.tick_params(axis='y', labelcolor='black', labelsize=25, grid_linestyle='--',
                       grid_color='black', grid_alpha=0.5, grid_linewidth=1.5)
        plt.yticks([0.0, 1.0, 2.0, 3.0, 4.0, 5.0],)
        ax.tick_params(axis='x', grid_color='black', grid_alpha=0.4,
                       grid_linestyle='-.', top=True, direction='out', pad=65)

        # Set the plot title, and its margin y
        plt.title("Kepentingan dan Kepuasan User - {}\n(N=20)".format(year),
                  loc='center', y=1.3, fontsize=30)

        # Add a legend, bbox_to_anchor to make custom position
        plt.legend(bbox_to_anchor=([0.25, 0.75, 0.5, 0.5]),
                   loc='upper left', fontsize=20, ncol=3)

        # Show the plot
        st.pyplot(fig)