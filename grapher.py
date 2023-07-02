
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from dataframeinitializer import DataframeTracerInitializer, DataframeUserInitializer
import matplotlib.ticker as mtick
import plotly.express as px
# matplotlib.use('TkAgg')  # or any other GUI backend of your choice

class GrapherTracer(DataframeTracerInitializer):
    def __init__(self, df2018, df2019, df2020, df2021, df2022, prodi, fakultas):
        super().__init__(df2018, df2019, df2020, df2021, df2022, prodi, fakultas)
        self.prodi = prodi
        self.fakultas = fakultas
        self.modeProdi = True
        if prodi == "All":
            self.modeProdi = False
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

        if self.prodi != "All":
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
        elif self.prodi == "All" and self.fakultas != "All":
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
        else:
            if year == 2018:
                competenceA = self.df2018_competenceA
                competenceB = self.df2018_competenceB
                competenceC = self.df2018_competenceC
                competenciesLabel = self.competencies2018
            elif year == 2019:
                competenceA = self.df2019_competenceA
                competenceB = self.df2019_competenceB
                competenceC = self.df2019_competenceC
                competenciesLabel = self.competencies2019
            elif year == 2020:
                competenceA = self.df2020_competenceA
                competenceB = self.df2020_competenceB
                competenceC = self.df2020_competenceC
                competenciesLabel = self.competencies2020
            elif year == 2021:
                competenceA = self.df2021_competenceA
                competenceB = self.df2021_competenceB
                competenceC = self.df2021_competenceC
                competenciesLabel = self.competencies2021
            elif year == 2022:
                competenceA = self.df2022_competenceA
                competenceB = self.df2022_competenceB
                competenceC = self.df2022_competenceC
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
            valuesLokal, valuesNasional, valuesInternasional = valuesLokal[::-1], valuesNasional[::-1], valuesInternasional[::-1]
        else:
            valuesLokal = self.valueCompanyCat_fakultas.T[0]
            valuesInternasional = self.valueCompanyCat_fakultas.T[1]
            valuesNasional = self.valueCompanyCat_fakultas.T[2]
            valuesLokal, valuesNasional, valuesInternasional = valuesLokal[::-1], valuesNasional[::-1], valuesInternasional[::-1]

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

    
    def draw_revenue(self):
        def curr(a, b, c, d, e):
            if a is None:
                a = 0
            else:
                a = "Rp {:,.2f}".format(float(a))
            if b is None:
                b = 0
            else:
                b = "Rp {:,.2f}".format(float(b))
            if c is None:
                c = 0
            else:
                c = "Rp {:,.2f}".format(float(c))
            if d is None:
                d = 0
            else:
                d = "Rp {:,.2f}".format(float(d))
            if e is None:
                e = 0
            else:
                e = "Rp {:,.2f}".format(float(e))
            x = [a, b, c, d, e]
            return x
        def curr2(a, b, c, d, e):
            if a is None:
                a = 0
            else:
                a = "Rp {:,.2f}".format(float(a))
            if b is None:
                b = 0
            else:
                b = "Rp {:,.2f}".format(float(b))
            if c is None:
                c = 0
            else:
                c = "Rp {:,.2f}".format(float(c))
            if d is None:
                d = 0
            else:
                d = "Rp {:,.2f}".format(float(d))
            if e is None:
                e = 0
            else:
                e = "Rp {:,.2f}".format(float(e))
            x = [a, b, c, d, e]
            return x
        def org(a, b, c, d, e):
            if a is None:
                a = 0
                a = "{} orang".format(a)
            else:
                a = "{} orang".format(int(a))
            if b is None:
                b = 0
            else:
                b = "{} orang".format(int(b))
            if c is None:
                c = 0
            else:
                c = "{} orang".format(int(c))
            if d is None:
                d = 0
            else:
                d = "{} orang".format(int(d))
            if e is None:
                e = 0
            else:
                e = "{} orang".format(int(e))
            x = [a, b, c, d, e]
            return x
        
        self.pb18 = pd.DataFrame(self.pb18)
        self.pb19 = pd.DataFrame(self.pb19)
        self.pb20 = pd.DataFrame(self.pb20)
        self.pb21 = pd.DataFrame(self.pb21)
        self.pb22 = pd.DataFrame(self.pb22)

        pbd18 = self.pb18.describe()
        pbd19 = self.pb19.describe()
        pbd20 = self.pb20.describe()
        pbd21 = self.pb21.describe()
        pbd22 = self.pb22.describe()

        bc_18 = pbd18.loc['count', :]
        bc_19 = pbd19.loc['count', :]
        bc_20 = pbd20.loc['count', :]
        bc_21 = pbd21.loc['count', :]
        bc_22 = pbd22.loc['count', :]

            # calculate mean
        mean_pb18 = pbd18.loc['mean', :]
        mean_pb19 = pbd19.loc['mean', :]
        mean_pb20 = pbd20.loc['mean', :]
        mean_pb21 = pbd21.loc['mean', :]
        mean_pb22 = pbd22.loc['mean', :]

            # calculate the lowest value
        min_pb18 = pbd18.loc['min', :]
        min_pb19 = pbd19.loc['min', :]
        min_pb20 = pbd20.loc['min', :]
        min_pb21 = pbd21.loc['min', :]
        min_pb22 = pbd22.loc['min', :]

            # calculate the highest value
        max_pb18 = pbd18.loc['max', :]
        max_pb19 = pbd19.loc['max', :]
        max_pb20 = pbd20.loc['max', :]
        max_pb21 = pbd21.loc['max', :]
        max_pb22 = pbd22.loc['max', :]

            # calculate the median
        med_b18 = pbd18.loc['50%', :]
        med_b19 = pbd19.loc['50%', :]
        med_b20 = pbd20.loc['50%', :]
        med_b21 = pbd21.loc['50%', :]
        med_b22 = pbd22.loc['50%', :]

            # calculate standard deviation
        std_b18 = pbd18.loc['std', :]
        std_b19 = pbd19.loc['std', :]
        std_b20 = pbd20.loc['std', :]
        std_b21 = pbd21.loc['std', :]
        std_b22 = pbd22.loc['std', :]    

        self.pu18 = pd.DataFrame(self.pu18)
        self.pu19 = pd.DataFrame(self.pu19)
        self.pu20 = pd.DataFrame(self.pu20)
        self.pu21 = pd.DataFrame(self.pu21)
        self.pu22 = pd.DataFrame(self.pu22)

        pud18 = self.pu18.describe()
        pud19 = self.pu19.describe()
        pud20 = self.pu20.describe()
        pud21 = self.pu21.describe()
        pud22 = self.pu22.describe()

        bu_18 = pud18.loc['count', :]
        bu_19 = pud19.loc['count', :]
        bu_20 = pud20.loc['count', :]
        bu_21 = pud21.loc['count', :]
        bu_22 = pud22.loc['count', :]

            # calculate mean
        mean_pu18 = pud18.loc['mean', :]
        mean_pu19 = pud19.loc['mean', :]
        mean_pu20 = pud20.loc['mean', :]
        mean_pu21 = pud21.loc['mean', :]
        mean_pu22 = pud22.loc['mean', :]

            # calculate the lowest value
        min_pu18 = pud18.loc['min', :]
        min_pu19 = pud19.loc['min', :]
        min_pu20 = pud20.loc['min', :]
        min_pu21 = pud21.loc['min', :]
        min_pu22 = pud22.loc['min', :]

            # calculate the highest value
        max_pu18 = pud18.loc['max', :]
        max_pu19 = pud19.loc['max', :]
        max_pu20 = pud20.loc['max', :]
        max_pu21 = pud21.loc['max', :]
        max_pu22 = pud22.loc['max', :]

            # calculate the median
        med_u18 = pud18.loc['50%', :]
        med_u19 = pud19.loc['50%', :]
        med_u20 = pud20.loc['50%', :]
        med_u21 = pud21.loc['50%', :]
        med_u22 = pud22.loc['50%', :]

            # calculate standard deviation
        std_u18 = pud18.loc['std', :]
        std_u19 = pud19.loc['std', :]
        std_u20 = pud20.loc['std', :]
        std_u21 = pud21.loc['std', :]
        std_u22 = pud22.loc['std', :]

        countb = org(bc_18, bc_19, bc_20, bc_21, bc_22)
        minb = curr(min_pb18, min_pb19, min_pb20, min_pb21, min_pb22)
        maxb = curr(max_pb18, max_pb19, max_pb20, max_pb21, max_pb22)
        medb = curr(med_b18, med_b19, med_b20, med_b21, med_b22)
        meanb = curr(mean_pb18, mean_pb19, mean_pb20, mean_pb21, mean_pb22)
        stdb = curr(std_b18, std_b19, std_b20, std_b21, std_b22)
        #make the table
        df1 = pd.DataFrame(
        [countb, minb, maxb, medb, meanb, stdb],
        columns=('2018', '2019', '2020', '2021', '2022'), 
        index=['Count', 'Min', 'Max', 'Median', 'Mean', 'Standard Deviation'])

        st.table(df1)  


        #plot bekerja
        year = ['2018', '2019', '2020','2021','2022']
        categories = ['Median','Mean']
        med_pb = (med_b18,med_b19,med_b20,med_b21,med_b22)
        mean_pb = (mean_pb18, mean_pb19, mean_pb20, mean_pb21, mean_pb22)
        fig3,ax3 = plt.subplots(figsize=(11,6))
        #set the grid and plot background color
        ax3.set_facecolor("white")

        # Set the border properties
        ax3.spines['left'].set_visible(True)    # Show left border
        ax3.spines['bottom'].set_visible(True)  # Show bottom border
        ax3.spines['right'].set_visible(True)   # Show right border
        ax3.spines['top'].set_visible(True)     # Show top border

        # Customize the border style
        border_style = {'linewidth': 0.5, 'edgecolor': 'black'}
        for spine in ax3.spines.values():
            spine.set(**border_style)
            
        plt.grid(color='black',axis='y',alpha=0.2)
        #plot the bar
        plt.plot(year, med_pb, '#4F81BD', marker='o',linewidth=2.0,label = "median")
        plt.plot(year, mean_pb, '#C0504D', marker='o',linewidth=2.0,label = "mean")
        plt.grid(color='black',axis='y',alpha=0.2)


        
        #set the y limit
        val = 2000000
        plt.ylim((0, 15*val))

        #formatting the y ticks
        current_values = plt.gca().get_yticks()
        plt.gca().set_yticklabels(['Rp {:,.2f}'.format(x) for x in current_values])

        #set the data label
        for i in range(len(med_pb)):
                plt.text(i+0.1,med_pb[i]-400000,'Rp {:,.2f}'.format(float(med_pb[i])),ha = 'center')
        for i in range(len(mean_pb)):
                plt.text(i+0.1,mean_pb[i]+300000,'Rp {:,.2f}'.format(float(mean_pb[i])),ha = 'center')


        #setting the legend
        ax3.legend(categories,fontsize="14",loc='lower left', bbox_to_anchor=(0.25, -0.25),facecolor="white",edgecolor="white",ncol=2)

        plt.title('Pendapatan Bekerja')
        st.pyplot(fig3)

        countu = org(bu_18, bu_19, bu_20, bu_21, bu_22)
        minu = curr2(min_pu18, min_pu19, min_pu20, min_pu21, min_pu22)
        maxu = curr2(max_pu18, max_pu19, max_pu20, max_pu21, max_pu22)
        medu = curr2(med_u18, med_u19, med_u20, med_u21, med_u22)
        meanu = curr2(mean_pu18, mean_pu19, mean_pu20, mean_pu21, mean_pu22)
        stdu = curr2(std_u18, std_u19, std_u20, std_u21, std_u22)

        df2 = pd.DataFrame(
        [countu, minu, maxu, medu, meanu, stdu],
        columns=('2018', '2019', '2020', '2021', '2022'), 
        index=['Count', 'Min', 'Max', 'Median', 'Mean', 'Standard Deviation'])

        st.table(df2)

        #plot wirausaha
        med_pu = (med_u18, med_u19, med_u20, med_u21, med_u22)
        mean_pu = (mean_pu18, mean_pu19, mean_pu20, mean_pu21, mean_pu22)

        fig4,ax4 = plt.subplots(figsize=(11,6))
        #set the grid and plot background color
        ax4.set_facecolor("white")

        # Set the border properties
        ax4.spines['left'].set_visible(True)    # Show left border
        ax4.spines['bottom'].set_visible(True)  # Show bottom border
        ax4.spines['right'].set_visible(True)   # Show right border
        ax4.spines['top'].set_visible(True)     # Show top border

        # Customize the border style
        border_style = {'linewidth': 0.5, 'edgecolor': 'black'}
        for spine in ax4.spines.values():
            spine.set(**border_style)
            
        plt.grid(color='black',axis='y',alpha=0.2)
        #plot the bar
        plt.plot(year, med_pu, '#4F81BD', marker='o',linewidth=2.0,label = "median")
        plt.plot(year, mean_pu, '#C0504D', marker='o',linewidth=2.0,label = "mean")
        plt.grid(color='black',axis='y',alpha=0.2)

        #set the y limit
        val = 2000000
        max_value = max(meanu)
        # ax4.set_yticks((0, val, 2*val, 3*val, 4*val, 5*val, 6*val,
        #             7*val, 8*val, 9*val, 10*val))
        plt.ylim((0, 15*val))

        #formatting the y ticks
        current_values = plt.gca().get_yticks()
        plt.gca().set_yticklabels(['Rp {:,.2f}'.format(x) for x in current_values])

        #set the data label
        for i in range(len(med_pu)):
                plt.text(i+0.1,med_pu[i]-500000,'Rp {:,.2f}'.format(float(med_pu[i])),ha = 'center')
        for i in range(len(mean_pu)):
                plt.text(i+0.1,mean_pu[i]+500000,'Rp {:,.2f}'.format(float(mean_pu[i])),ha = 'center')


        #setting the legend
        ax4.legend(categories,fontsize="14",loc='lower left', bbox_to_anchor=(0.25, -0.25),facecolor="white",edgecolor="white",ncol=2)
        plt.title('Pendapatan Wirausaha')

        st.pyplot(fig4)
        

        #bonus bekerja

        #convert into dataframe
        self.bb18 = pd.DataFrame(self.bb18)
        self.bb19 = pd.DataFrame(self.bb19)
        self.bb20 = pd.DataFrame(self.bb20)
        self.bb21 = pd.DataFrame(self.bb21)
        self.bb22 = pd.DataFrame(self.bb22)

        #calculate the statistics descriptive
        bbd18 = self.bb18.describe()
        bbd19 = self.bb19.describe()
        bbd20 = self.bb20.describe()
        bbd21 = self.bb21.describe()
        bbd22 = self.bb22.describe()

        #calculation for the table (bekerja)
        #calculate the count
        bb_18 = bbd18.loc['count', :]
        bb_19 = bbd19.loc['count', :]
        bb_20 = bbd20.loc['count', :]
        bb_21 = bbd21.loc['count', :]
        bb_22 = bbd22.loc['count', :]

        #calculate mean
        mean_bb18 = bbd18.loc['mean', :]
        mean_bb19 = bbd19.loc['mean', :]
        mean_bb20 = bbd20.loc['mean', :]
        mean_bb21 = bbd21.loc['mean', :]
        mean_bb22 = bbd22.loc['mean', :]
        #calculate the lbbdest value
        min_bb18 = bbd18.loc['min', :]
        min_bb19 = bbd19.loc['min', :]
        min_bb20 = bbd20.loc['min', :]
        min_bb21 = bbd21.loc['min', :]
        min_bb22 = bbd22.loc['min', :]

        #calculate the highest value
        max_bb18 = bbd18.loc['max', :]
        max_bb19 = bbd19.loc['max', :]
        max_bb20 = bbd20.loc['max', :]
        max_bb21 = bbd21.loc['max', :]
        max_bb22 = bbd22.loc['max', :]

        #calculate the median
        med_bb18 = bbd18.loc['50%', :]
        med_bb19 = bbd19.loc['50%', :]
        med_bb20 = bbd20.loc['50%', :]
        med_bb21 = bbd21.loc['50%', :]
        med_bb22 = bbd22.loc['50%', :]
        #calculate standard deviation
        std_bb18 = bbd18.loc['std', :]
        std_bb19 = bbd19.loc['std', :]
        std_bb20 = bbd20.loc['std', :]
        std_bb21 = bbd21.loc['std', :]
        std_bb22 = bbd22.loc['std', :]


        countbb = org(bb_18, bb_19, bb_20, bb_21, bb_22)
        minbb = curr(min_bb18, min_bb19, min_bb20, min_bb21, min_bb22)
        maxbb = curr(max_bb18, max_bb19, max_bb20, max_bb21, max_bb22)
        medbb = curr(med_bb18, med_bb19, med_bb20, med_bb21, med_bb22)
        meanbb = curr(mean_bb18, mean_bb19, mean_bb20, mean_bb21, mean_bb22)
        stdbb = curr(std_bb18, std_bb19, std_bb20, std_bb21, std_bb22)


        df4 = pd.DataFrame(
            [countbb, minbb, maxbb, medbb, meanbb, stdbb],
            columns=('2018', '2019', '2020', '2021', '2022'), 
            index=['Count', 'Min', 'Max', 'Median', 'Mean', 'Standard Deviation'])

        st.table(df4)

        med_bbb = (med_bb18,med_bb19,med_bb20,med_bb21,med_bb22)
        mean_bbb = (mean_bb18, mean_bb19, mean_bb20, mean_bb21, mean_bb22)


        #plot bekerja
        fig5,ax5 = plt.subplots(figsize=(11,6))
        #set the grid and plot background color
        ax5.set_facecolor("white")

        # Set the border properties
        ax5.spines['left'].set_visible(True)    # Show left border
        ax5.spines['bottom'].set_visible(True)  # Show bottom border
        ax5.spines['right'].set_visible(True)   # Show right border
        ax5.spines['top'].set_visible(True)     # Show top border

        # Customize the border style
        border_style = {'linewidth': 0.5, 'edgecolor': 'black'}
        for spine in ax5.spines.values():
            spine.set(**border_style)
            
        plt.grid(color='black',axis='y',alpha=0.2)
        #plot the bar
        plt.plot(year, med_bbb, '#4F81BD', marker='o',linewidth=2.0,label = "median")
        plt.plot(year, mean_bbb, '#C0504D', marker='o',linewidth=2.0,label = "mean")
        plt.grid(color='black',axis='y',alpha=0.2)

        #set the y limit
        val = 2000000
        plt.ylim((0, 10*val))

        #formatting the y ticks
        current_values = plt.gca().get_yticks()
        plt.gca().set_yticklabels(['Rp {:,.2f}'.format(x) for x in current_values])

        #set the data label
        for i in range(len(med_bbb)):
                plt.text(i+0.1,med_bbb[i]-400000,'Rp {:,.2f}'.format(float(med_bbb[i])),ha = 'center')
        for i in range(len(mean_bbb)):
                plt.text(i+0.1,mean_bbb[i]+300000,'Rp {:,.2f}'.format(float(mean_bbb[i])),ha = 'center')

        #setting the legend
        ax5.legend(categories,fontsize="14",loc='lower left', bbox_to_anchor=(0.25, -0.25),facecolor="white",edgecolor="white",ncol=2)

        plt.title('Bonus Bekerja')
        st.pyplot(fig5)

        #calculation for the table (omset)
        #calculate the count
        
        #convert into dataframe
        self.ow18 = pd.DataFrame(self.ow18)
        self.ow19 = pd.DataFrame(self.ow19)
        self.ow20 = pd.DataFrame(self.ow20)
        self.ow21 = pd.DataFrame(self.ow21)
        self.ow22 = pd.DataFrame(self.ow22)

        #calculate the statistics descriptive
        owd18 = self.ow18.describe()
        owd19 = self.ow19.describe()
        owd20 = self.ow20.describe()
        owd21 = self.ow21.describe()
        owd22 = self.ow22.describe()
        
        cow_18 = owd18.loc['count', :]
        cow_19 = owd19.loc['count', :]
        cow_20 = owd20.loc['count', :]
        cow_21 = owd21.loc['count', :]
        cow_22 = owd22.loc['count', :]

        #calculate mean
        mean_ow18 = owd18.loc['mean', :]
        mean_ow19 = owd19.loc['mean', :]
        mean_ow20 = owd20.loc['mean', :]
        mean_ow21 = owd21.loc['mean', :]
        mean_ow22 = owd22.loc['mean', :]
        #calculate the lowdest value
        min_ow18 = owd18.loc['min', :]
        min_ow19 = owd19.loc['min', :]
        min_ow20 = owd20.loc['min', :]
        min_ow21 = owd21.loc['min', :]
        min_ow22 = owd22.loc['min', :]

        #calculate the highest value
        max_ow18 = owd18.loc['max', :]
        max_ow19 = owd19.loc['max', :]
        max_ow20 = owd20.loc['max', :]
        max_ow21 = owd21.loc['max', :]
        max_ow22 = owd22.loc['max', :]

        #calculate the median
        med_ow18 = owd18.loc['50%', :]
        med_ow19 = owd19.loc['50%', :]
        med_ow20 = owd20.loc['50%', :]
        med_ow21 = owd21.loc['50%', :]
        med_ow22 = owd22.loc['50%', :]
        #calculate standard deviation
        std_ow18 = owd18.loc['std', :]
        std_ow19 = owd19.loc['std', :]
        std_ow20 = owd20.loc['std', :]
        std_ow21 = owd21.loc['std', :]
        std_ow22 = owd22.loc['std', :]

        countow = org(cow_18, cow_19, cow_20,cow_21, cow_22)
        minow = curr2(min_ow18, min_ow19, min_ow20, min_ow21, min_ow22)
        maxow = curr2(max_ow18, max_ow19, max_ow20, max_ow21, max_ow22)
        medow = curr2(med_ow18, med_ow19, med_ow20, med_ow21, med_ow22)
        meanow = curr2(mean_ow18, mean_ow19, mean_ow20, mean_ow21, mean_ow22)
        stdow = curr2(std_ow18, std_ow19, std_ow20, std_ow21, std_ow22)


        df5 = pd.DataFrame(
            [countow, minow, maxow, medow, meanow, stdow],
            columns=('2018', '2019', '2020', '2021', '2022'), 
            index=['Count', 'Min', 'Max', 'Median', 'Mean', 'Standard Deviation'])

        st.table(df5)

        med_ow = (med_ow18, med_ow19, med_ow20, med_ow21, med_ow22)
        mean_ow = (mean_ow18, mean_ow19, mean_ow20, mean_ow21, mean_ow22)

        #plot bekerja
        fig6,ax6 = plt.subplots(figsize=(11,6))
        #set the grid and plot background color
        ax6.set_facecolor("white")

        # Set the border properties
        ax6.spines['left'].set_visible(True)    # Show left border
        ax6.spines['bottom'].set_visible(True)  # Show bottom border
        ax6.spines['right'].set_visible(True)   # Show right border
        ax6.spines['top'].set_visible(True)     # Show top border

        # Customize the border style
        border_style = {'linewidth': 0.5, 'edgecolor': 'black'}
        for spine in ax6.spines.values():
            spine.set(**border_style)
            
        plt.grid(color='black',axis='y',alpha=0.2)
        #plot the bar
        plt.plot(year, med_ow, '#4F81BD', marker='o',linewidth=2.0,label = "median")
        plt.plot(year, mean_ow, '#C0504D', marker='o',linewidth=2.0,label = "mean")
        plt.grid(color='black',axis='y',alpha=0.2)

        #set the y limit
        val = 2000000
        plt.ylim((0, 20*val))

        #formatting the y ticks
        current_values = plt.gca().get_yticks()
        plt.gca().set_yticklabels(['Rp {:,.2f}'.format(x) for x in current_values])

        #set the data label
        for i in range(len(med_ow)):
                plt.text(i+0.1,med_ow[i]-400000,'Rp {:,.2f}'.format(float(med_ow[i])),ha = 'center')
        for i in range(len(mean_ow)):
                plt.text(i+0.1,mean_ow[i]+300000,'Rp {:,.2f}'.format(float(mean_ow[i])),ha = 'center')

        #setting the legend
        ax6.legend(categories,fontsize="14",loc='lower left', bbox_to_anchor=(0.25, -0.25),facecolor="white",edgecolor="white",ncol=2)

        plt.title('Omset Wirausaha')
        st.pyplot(fig6)
        
    def draw_company_related_study(self):
        # create sample data
        categoryCompany = ['Sesuai', 'Tidak Sesuai']
        years = ['2018', '2019', '2020', '2021', '2022']

    
        valuesSesuai = self.valueCompanyRelated.T[0]
        valuesTidakSesuai = self.valueCompanyRelated.T[1]
        valuesSesuai, valuesTidakSesuai = valuesSesuai[::-1], valuesTidakSesuai[::-1]

        # Calculate Percentage Relative to ALL CATEGORIES
        pvaluesSesuai = []
        pvaluesTidakSesuai = []
        for i, (vs, vn) in enumerate(zip(valuesSesuai, valuesTidakSesuai)):
            total = vs+vn
            pvaluesSesuai.append(round(100*vs/total))
            pvaluesTidakSesuai.append(round(100*vn/total))

        fig, ax = plt.subplots(figsize=(10,4))
        ax.plot(years, pvaluesSesuai, label="Sesuai", color='#4e81bd')
        ax.plot(years, pvaluesTidakSesuai, label="Tidak Sesuai", color='#b94a48')


        for i, year in enumerate(years):
            ax.text(year, pvaluesSesuai[i], '[{:,.0f}];'.format(valuesSesuai[i])+'{}%'.format(pvaluesSesuai[i]), ha='center')
            ax.text(year, pvaluesTidakSesuai[i], '[{:,.0f}];'.format(valuesTidakSesuai[i])+'{}%'.format(pvaluesTidakSesuai[i]), ha='center')



        # add legend
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)
        ax.grid(axis='y', linestyle='-', linewidth=0.3, color='gray', alpha=0.5)
        ax.yaxis.set_major_formatter(mtick.PercentFormatter())

        # show the plot
        st.pyplot(fig)
    
    def draw_bussiness_field_data(self):

        dfbusfield = self.valueBussinessField_Prodi
        dfbusfieldt = dfbusfield.T
        dfbusfieldt["sum"] =dfbusfieldt.sum(axis =1)
        #HITUNG PERSEN
        percentbusfield = dfbusfieldt.div(dfbusfieldt["sum"], axis=0)*100 
        percentbusfield.pop("sum")
        figb = px.bar(percentbusfield, barmode='stack', title="Kategori Perusahaan (Wirausaha)")
        fig2b = px.line(percentbusfield, title="Kategori Perusahaan (Wirausaha)")
        st.plotly_chart(figb, use_container_width=True) 
        st.plotly_chart(fig2b, use_container_width=True) 
        print("bussiness field data drawn")
        
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
        print("company field data drawn")



class GrapherUser(DataframeUserInitializer):
    def __init__(self, dfUser2018, dfUser2019, dfUser2020, dfUser2021, dfUser2022, prodi, fakultas):
        super().__init__(dfUser2018=dfUser2018,
                         dfUser2019=dfUser2019,
                         dfUser2020=dfUser2020,
                         dfUser2021=dfUser2021,
                         dfUser2022=dfUser2022,
                         prodi=prodi,
                         fakultas=fakultas)
        # self.graph = graph

    def draw_competence_data(self, year):
        # Extract Mean Of Competence Values
        if self.prodi != "All":
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

            
        elif self.prodi == "All" and self.fakultas != "All":
            if year == 2018:
                kepentingan = self.dfUser2018_Kepentingan_fakultas
                kepuasan = self.dfUser2018_Kepuasan_fakultas
                competencies = self.competencies2018
            elif year == 2019:
                kepentingan = self.dfUser2019_Kepentingan_fakultas
                kepuasan = self.dfUser2019_Kepuasan_fakultas
                competencies = self.competencies2019
            elif year == 2020:
                kepentingan = self.dfUser2020_Kepentingan_fakultas
                kepuasan = self.dfUser2020_Kepuasan_fakultas
                competencies = self.competencies2020
            elif year == 2021:
                kepentingan = self.dfUser2021_Kepentingan_fakultas
                kepuasan = self.dfUser2021_Kepuasan_fakultas
                competencies = self.competencies2021
            elif year == 2022:
                kepentingan = self.dfUser2021_Kepentingan_fakultas
                kepuasan = self.dfUser2021_Kepuasan_fakultas
                competencies = self.competencies2022
        
        else:
            if year == 2018:
                kepentingan = self.dfUser2018_Kepentingan
                kepuasan = self.dfUser2018_Kepuasan
                competencies = self.competencies2018
            elif year == 2019:
                kepentingan = self.dfUser2019_Kepentingan
                kepuasan = self.dfUser2019_Kepuasan
                competencies = self.competencies2019
            elif year == 2020:
                kepentingan = self.dfUser2020_Kepentingan
                kepuasan = self.dfUser2020_Kepuasan
                competencies = self.competencies2020
            elif year == 2021:
                kepentingan = self.dfUser2021_Kepentingan
                kepuasan = self.dfUser2021_Kepuasan
                competencies = self.competencies2021
            elif year == 2022:
                kepentingan = self.dfUser2021_Kepentingan
                kepuasan = self.dfUser2021_Kepuasan
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

    def draw_competence_trend_data(self, typeGraph):
        if typeGraph == "Kepuasan":
            categoriesTrend = ["Bahasa\nAsing", "pengetahuan dan\npenerapan bidang/\ndisiplin ilmu","etika dan tanggung\njawab keprofesian"
                ,"kemampuan belajar\nsepanjang hayat","bekerja tim", "kemampuan\nberkomunikasi", "keterampilan\nmenggunakan\nteknologi informasi"]
            # Plotting
            plt.style.use('ggplot')

            # Create Polar Axis
            fig = plt.figure(figsize=(15,15))
            ax = fig.add_subplot(111, polar=True)
            ax.set_theta_zero_location('S',offset=77)
            # Set the number of angles/coordinates to be used for the radar plot
            angles = np.linspace(0, 2*np.pi, len(categoriesTrend), endpoint=False)
            # angles = angles - 1.57
            angles = np.concatenate((angles,[angles[0]]))
            
            # Plot the data
            self.meansKepuasan2018 = np.concatenate((self.meansKepuasan2018,[self.meansKepuasan2018[0]]))
            self.meansKepuasan2019 = np.concatenate((self.meansKepuasan2019,[self.meansKepuasan2019[0]]))
            self.meansKepuasan2020 = np.concatenate((self.meansKepuasan2020,[self.meansKepuasan2020[0]]))
            self.meansKepuasan2021 = np.concatenate((self.meansKepuasan2021,[self.meansKepuasan2021[0]]))
            self.meansKepuasan2022 = np.concatenate((self.meansKepuasan2022,[self.meansKepuasan2022[0]]))

            ax.plot(angles, self.meansKepuasan2018, 'o-', linewidth=4, label="2018",color='blue',markersize=12)
            ax.plot(angles, self.meansKepuasan2019, 'o-', linewidth=4, label="2019",color='orange',markersize=12)
            ax.plot(angles, self.meansKepuasan2020, 'o-', linewidth=4, label="2020",color='green',markersize=12)
            ax.plot(angles, self.meansKepuasan2021, 'o-', linewidth=4, label="2021",color='purple',markersize=12)
            ax.plot(angles, self.meansKepuasan2022, 'o-', linewidth=4, label="2022",color='red',markersize=12)

            # Fill the area inside the plot (optional)
            # ax.fill(angles, values, alpha=0.25)
            
            # Set Grids, and other parameters to make graph more neat
            ax.set_thetagrids(angles[:-1] * 180/np.pi,categoriesTrend)
            ax.set_xticks(angles[:-1],categoriesTrend, color='black', size=20)
            ax.tick_params(axis='y',labelcolor='black',labelsize=25, grid_linestyle='--',grid_color='black', grid_alpha=0.5, grid_linewidth=1.5)
            plt.yticks([0.0,1.0,2.0,3.0,4.0,5.0])
            ax.tick_params(axis='x', grid_color='black',grid_alpha=0.4,grid_linestyle='-.',top=True,direction='out',pad=65)


            # Set the plot title, and its margin y
            plt.title("Tren Tingkat Kepuasan User\nTahun 2018-2022",loc='center',y=1.3,fontsize=30)

            # Add a legend, bbox_to_anchor to make custom position
            plt.legend(bbox_to_anchor=([0.2, 0.75,0.5,0.5]),loc='upper left',fontsize=20,ncol=3)

            # Show the plot
            st.pyplot(fig)
            
        
        else:
            categoriesTrend = ["Bahasa\nAsing", "pengetahuan dan\npenerapan bidang/\ndisiplin ilmu","etika dan tanggung\njawab keprofesian"
                ,"kemampuan belajar\nsepanjang hayat","bekerja tim", "kemampuan\nberkomunikasi", "keterampilan\nmenggunakan\nteknologi informasi"]
            # Plotting
            plt.style.use('ggplot')

            # Create Polar Axis
            fig = plt.figure(figsize=(15,15))
            ax = fig.add_subplot(111, polar=True)
            ax.set_theta_zero_location('S',offset=77)
            # Set the number of angles/coordinates to be used for the radar plot
            angles = np.linspace(0, 2*np.pi, len(categoriesTrend), endpoint=False)
            # angles = angles - 1.57
            angles = np.concatenate((angles,[angles[0]]))
            
            # Plot the data
            self.meansKepentingan2018 = np.concatenate((self.meansKepentingan2018,[self.meansKepentingan2018[0]]))
            self.meansKepentingan2019 = np.concatenate((self.meansKepentingan2019,[self.meansKepentingan2019[0]]))
            self.meansKepentingan2020 = np.concatenate((self.meansKepentingan2020,[self.meansKepentingan2020[0]]))
            self.meansKepentingan2021 = np.concatenate((self.meansKepentingan2021,[self.meansKepentingan2021[0]]))
            self.meansKepentingan2022 = np.concatenate((self.meansKepentingan2022,[self.meansKepentingan2022[0]]))

            ax.plot(angles, self.meansKepentingan2018, 'o-', linewidth=4, label="2018",color='blue',markersize=12)
            ax.plot(angles, self.meansKepentingan2019, 'o-', linewidth=4, label="2019",color='orange',markersize=12)
            ax.plot(angles, self.meansKepentingan2020, 'o-', linewidth=4, label="2020",color='green',markersize=12)
            ax.plot(angles, self.meansKepentingan2021, 'o-', linewidth=4, label="2021",color='purple',markersize=12)
            ax.plot(angles, self.meansKepentingan2022, 'o-', linewidth=4, label="2022",color='red',markersize=12)

            # Fill the area inside the plot (optional)
            # ax.fill(angles, values, alpha=0.25)
            
            # Set Grids, and other parameters to make graph more neat
            ax.set_thetagrids(angles[:-1] * 180/np.pi,categoriesTrend)
            ax.set_xticks(angles[:-1],categoriesTrend, color='black', size=20)
            ax.tick_params(axis='y',labelcolor='black',labelsize=25, grid_linestyle='--',grid_color='black', grid_alpha=0.5, grid_linewidth=1.5)
            plt.yticks([0.0,1.0,2.0,3.0,4.0,5.0])
            ax.tick_params(axis='x', grid_color='black',grid_alpha=0.4,grid_linestyle='-.',top=True,direction='out',pad=65)


            # Set the plot title, and its margin y
            plt.title("Tren Tingkat Kepentingan User\nTahun 2018-2022",loc='center',y=1.3,fontsize=30)

            # Add a legend, bbox_to_anchor to make custom position
            plt.legend(bbox_to_anchor=([0.2, 0.75,0.5,0.5]),loc='upper left',fontsize=20,ncol=3)

            # Show the plot
            st.pyplot(fig)
# class GrapherUser(DataframeInitializer):
#     def __init__(self, dfUser2018, dfUser2019, dfUser2020, dfUser2021, dfUser2022, prodi):
#         super().__init__(dfUser2018=dfUser2018,
#                          dfUser2019=dfUser2019,
#                          dfUser2020=dfUser2020,
#                          dfUser2021=dfUser2021,
#                          dfUser2022=dfUser2022,
#                          prodi=prodi)
#         # self.graph = graph
