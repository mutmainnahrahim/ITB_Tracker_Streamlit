

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class DataframeTracerInitializer:
    def __init__(self, df2018, df2019, df2020, df2021, df2022, prodi,fakultas):
        self.df2018 = df2018
        self.df2019 = df2019
        self.df2020 = df2020
        self.df2021 = df2021
        self.df2022 = df2022
        # self.dfUser2018 = dfUser2018
        # self.dfUser2019 = dfUser2019
        # self.dfUser2020 = dfUser2020
        # self.dfUser2021 = dfUser2021
        # self.dfUser2022 = dfUser2022
        self.prodi = prodi
        self.fakultas = fakultas

    def __lookup_faculty_from_major(self, _prodi):
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
        if _prodi in prodiFITB:
            return fakultas[0]
        elif _prodi in prodiFMIPA:
            return fakultas[1]
        elif _prodi in prodiFSRD:
            return fakultas[2]
        elif _prodi in prodiFTI:
            return fakultas[3]
        elif _prodi in prodiFTSL:
            return fakultas[4]
        elif _prodi in prodiFTMD:
            return fakultas[5]
        elif _prodi in prodiFTTM:
            return fakultas[6]
        elif _prodi in prodiSAPPK:
            return fakultas[7]
        elif _prodi in prodiSBM:
            return fakultas[8]
        elif _prodi in prodiSF:
            return fakultas[9]
        elif _prodi in prodiSITH:
            return fakultas[10]
        elif _prodi in prodiSTEI:
            return fakultas[11]
        
    def cleanse_tracer_data(self):
        # Adding Faculty Column
        self.df2018['Fakultas/Sekolah'] = self.df2018['4. Program Studi'].apply(
            self.__lookup_faculty_from_major)
        self.df2019['Fakultas/Sekolah'] = self.df2019['4. Program Studi'].apply(
            self.__lookup_faculty_from_major)
        self.df2020['Fakultas/Sekolah'] = self.df2020['4. Program Studi'].apply(
            self.__lookup_faculty_from_major)
        
        # Competence A -> penguasaan kompetensi, B-> peran perguruan tinggi,C-> peran kompetensi
        # Check Space-Valued Data, and replaced by NULL
        self.df2018_competenceA = (
            self.df2018.iloc[:, 6:29].replace(' ', np.nan))
        self.df2018_competenceA.fillna(
            self.df2018_competenceA.mean(), inplace=True)
        self.df2018_competenceB = (self.df2018.iloc[:, 29:52].replace(
            ' ', np.nan))
        self.df2018_competenceB.fillna(
            self.df2018_competenceB.mean(), inplace=True)
        self.df2018_competenceC = (self.df2018.iloc[:, 52:75].replace(
            ' ', np.nan))
        self.df2018_competenceC.fillna(
            self.df2018_competenceC.mean(), inplace=True)
        self.df2019_competenceA = (self.df2019.iloc[:, 7:30].replace(
            ' ', np.nan))
        self.df2019_competenceA.fillna(
            self.df2019_competenceA.mean(), inplace=True)
        self.df2019_competenceB = (self.df2019.iloc[:, 30:53].replace(
            ' ', np.nan))
        self.df2019_competenceB.fillna(
            self.df2019_competenceB.mean(), inplace=True)
        self.df2019_competenceC = (self.df2019.iloc[:, 53:76].replace(
            ' ', np.nan))
        self.df2019_competenceC.fillna(
            self.df2019_competenceC.mean(), inplace=True)
        self.df2020_competenceA = (self.df2020.iloc[:, 7:30].replace(
            ' ', np.nan))
        self.df2020_competenceA.fillna(
            self.df2020_competenceA.mean(), inplace=True)
        self.df2020_competenceB = (self.df2020.iloc[:, 30:53].replace(
            ' ', np.nan))
        self.df2020_competenceB.fillna(
            self.df2020_competenceB.mean(), inplace=True)
        self.df2020_competenceC = (self.df2020.iloc[:, 53:76].replace(
            ' ', np.nan))
        self.df2020_competenceC.fillna(
            self.df2020_competenceC.mean(), inplace=True)
        self.df2021_competenceA = (self.df2021.iloc[:, 8:31].replace(
            ' ', np.nan))
        self.df2021_competenceA.fillna(
            self.df2021_competenceA.mean(), inplace=True)
        self.df2021_competenceB = (self.df2021.iloc[:, 31:54].replace(
            ' ', np.nan))
        self.df2021_competenceB.fillna(
            self.df2021_competenceB.mean(), inplace=True)
        self.df2021_competenceC = (self.df2021.iloc[:, 54:77].replace(
            ' ', np.nan))
        self.df2021_competenceC.fillna(
            self.df2021_competenceC.mean(), inplace=True)
        self.df2022_competenceA = (self.df2022.iloc[:, 8:31].replace(
            ' ', np.nan))
        self.df2022_competenceA.fillna(
            self.df2022_competenceA.mean(), inplace=True)
        self.df2022_competenceB = (self.df2022.iloc[:, 31:54].replace(
            ' ', np.nan))
        self.df2022_competenceB.fillna(
            self.df2022_competenceB.mean(), inplace=True)
        self.df2022_competenceC = (self.df2022.iloc[:, 54:77].replace(
            ' ', np.nan))
        self.df2022_competenceC.fillna(
            self.df2022_competenceC.mean(), inplace=True)

    def init_respondent_data(self):
        if self.prodi != "All":
            self.df2018_competenceA_Prodi = self.df2018_competenceA[
                self.df2018['4. Program Studi'] == self.prodi]
            self.df2018_competenceB_Prodi = self.df2018_competenceB[
                self.df2018['4. Program Studi'] == self.prodi]
            self.df2018_competenceC_Prodi = self.df2018_competenceC[
                self.df2018['4. Program Studi'] == self.prodi]
            self.df2019_competenceA_Prodi = self.df2019_competenceA[
                self.df2019['4. Program Studi'] == self.prodi]
            self.df2019_competenceB_Prodi = self.df2019_competenceB[
                self.df2019['4. Program Studi'] == self.prodi]
            self.df2019_competenceC_Prodi = self.df2019_competenceC[
                self.df2019['4. Program Studi'] == self.prodi]
            self.df2020_competenceA_Prodi = self.df2020_competenceA[
                self.df2020['4. Program Studi'] == self.prodi]
            self.df2020_competenceB_Prodi = self.df2020_competenceB[
                self.df2020['4. Program Studi'] == self.prodi]
            self.df2020_competenceC_Prodi = self.df2020_competenceC[
                self.df2020['4. Program Studi'] == self.prodi]
            self.df2021_competenceA_Prodi = self.df2021_competenceA[
                self.df2021['Program Studi'] == self.prodi]
            self.df2021_competenceB_Prodi = self.df2021_competenceB[
                self.df2021['Program Studi'] == self.prodi]
            self.df2021_competenceC_Prodi = self.df2021_competenceC[
                self.df2021['Program Studi'] == self.prodi]
            self.df2022_competenceA_Prodi = self.df2022_competenceA[
                self.df2022['Program Studi'] == self.prodi]
            self.df2022_competenceB_Prodi = self.df2022_competenceB[
                self.df2022['Program Studi'] == self.prodi]
            self.df2022_competenceC_Prodi = self.df2022_competenceC[
                self.df2022['Program Studi'] == self.prodi]

        # Filter Fakultas
        else:
            self.df2018_competenceA_fakultas = self.df2018_competenceA[
                self.df2018['Fakultas/Sekolah'] == self.fakultas]
            self.df2018_competenceB_fakultas = self.df2018_competenceB[
                self.df2018['Fakultas/Sekolah'] == self.fakultas]
            self.df2018_competenceC_fakultas = self.df2018_competenceC[
                self.df2018['Fakultas/Sekolah'] == self.fakultas]
            self.df2019_competenceA_fakultas = self.df2019_competenceA[
                self.df2019['Fakultas/Sekolah'] == self.fakultas]
            self.df2019_competenceB_fakultas = self.df2019_competenceB[
                self.df2019['Fakultas/Sekolah'] == self.fakultas]
            self.df2019_competenceC_fakultas = self.df2019_competenceC[
                self.df2019['Fakultas/Sekolah'] == self.fakultas]
            self.df2020_competenceA_fakultas = self.df2020_competenceA[
                self.df2020['Fakultas/Sekolah'] == self.fakultas]
            self.df2020_competenceB_fakultas = self.df2020_competenceB[
                self.df2020['Fakultas/Sekolah'] == self.fakultas]
            self.df2020_competenceC_fakultas = self.df2020_competenceC[
                self.df2020['Fakultas/Sekolah'] == self.fakultas]
            self.df2021_competenceA_fakultas = self.df2021_competenceA[
                self.df2021['Fakultas/Sekolah'] == self.fakultas]
            self.df2021_competenceB_fakultas = self.df2021_competenceB[
                self.df2021['Fakultas/Sekolah'] == self.fakultas]
            self.df2021_competenceC_fakultas = self.df2021_competenceC[
                self.df2021['Fakultas/Sekolah'] == self.fakultas]
            self.df2022_competenceA_fakultas = self.df2022_competenceA[
                self.df2022['Fakultas/Sekolah'] == self.fakultas]
            self.df2022_competenceB_fakultas = self.df2022_competenceB[
                self.df2022['Fakultas/Sekolah'] == self.fakultas]
            self.df2022_competenceC_fakultas = self.df2022_competenceC[
                self.df2022['Fakultas/Sekolah'] == self.fakultas]

    def init_competence_data(self):
        if self.prodi != "All":
            self.df2018_competenceA_Prodi = self.df2018_competenceA[
                self.df2018['4. Program Studi'] == self.prodi]
            self.df2018_competenceB_Prodi = self.df2018_competenceB[
                self.df2018['4. Program Studi'] == self.prodi]
            self.df2018_competenceC_Prodi = self.df2018_competenceC[
                self.df2018['4. Program Studi'] == self.prodi]
            self.df2019_competenceA_Prodi = self.df2019_competenceA[
                self.df2019['4. Program Studi'] == self.prodi]
            self.df2019_competenceB_Prodi = self.df2019_competenceB[
                self.df2019['4. Program Studi'] == self.prodi]
            self.df2019_competenceC_Prodi = self.df2019_competenceC[
                self.df2019['4. Program Studi'] == self.prodi]
            self.df2020_competenceA_Prodi = self.df2020_competenceA[
                self.df2020['4. Program Studi'] == self.prodi]
            self.df2020_competenceB_Prodi = self.df2020_competenceB[
                self.df2020['4. Program Studi'] == self.prodi]
            self.df2020_competenceC_Prodi = self.df2020_competenceC[
                self.df2020['4. Program Studi'] == self.prodi]
            self.df2021_competenceA_Prodi = self.df2021_competenceA[
                self.df2021['Program Studi'] == self.prodi]
            self.df2021_competenceB_Prodi = self.df2021_competenceB[
                self.df2021['Program Studi'] == self.prodi]
            self.df2021_competenceC_Prodi = self.df2021_competenceC[
                self.df2021['Program Studi'] == self.prodi]
            self.df2022_competenceA_Prodi = self.df2022_competenceA[
                self.df2022['Program Studi'] == self.prodi]
            self.df2022_competenceB_Prodi = self.df2022_competenceB[
                self.df2022['Program Studi'] == self.prodi]
            self.df2022_competenceC_Prodi = self.df2022_competenceC[
                self.df2022['Program Studi'] == self.prodi]

            self.means2018 = np.array([self.df2018_competenceA_Prodi.mean()[21], self.df2018_competenceA_Prodi.mean()[15], self.df2018_competenceA_Prodi.mean()[14],
                                       self.df2018_competenceA_Prodi.mean()[10], self.df2018_competenceA_Prodi.mean()[
                4], self.df2018_competenceA_Prodi.mean()[19],
                self.df2018_competenceA_Prodi.mean()[19]])

            self.means2019 = np.array([self.df2019_competenceA_Prodi.mean()[22], self.df2019_competenceA_Prodi.mean()[16], self.df2019_competenceA_Prodi.mean()[14],
                                       self.df2019_competenceA_Prodi.mean()[10], self.df2019_competenceA_Prodi.mean()[
                4], self.df2019_competenceA_Prodi.mean()[15],
                self.df2019_competenceA_Prodi.mean()[20]])

            self.means2020 = np.array([self.df2020_competenceA_Prodi.mean()[22], self.df2020_competenceA_Prodi.mean()[16], self.df2020_competenceA_Prodi.mean()[14],
                                       self.df2020_competenceA_Prodi.mean()[10], self.df2020_competenceA_Prodi.mean()[
                4], self.df2020_competenceA_Prodi.mean()[15],
                self.df2020_competenceA_Prodi.mean()[20]])
            self.means2021 = np.array([self.df2021_competenceA_Prodi.mean()[22], self.df2021_competenceA_Prodi.mean()[16], self.df2021_competenceA_Prodi.mean()[14],
                                       self.df2021_competenceA_Prodi.mean()[10], self.df2021_competenceA_Prodi.mean()[
                4], self.df2021_competenceA_Prodi.mean()[15],
                self.df2021_competenceA_Prodi.mean()[20]])
            self.means2022 = np.array([self.df2022_competenceA_Prodi.mean()[22], self.df2022_competenceA_Prodi.mean()[16], self.df2022_competenceA_Prodi.mean()[14],
                                       self.df2022_competenceA_Prodi.mean()[10], self.df2022_competenceA_Prodi.mean()[
                4], self.df2022_competenceA_Prodi.mean()[15],
                self.df2022_competenceA_Prodi.mean()[20]])

        # Filter Fakultas
        else:
            self.df2018_competenceA_fakultas = self.df2018_competenceA[
                self.df2018['Fakultas/Sekolah'] == self.fakultas]
            self.df2018_competenceB_fakultas = self.df2018_competenceB[
                self.df2018['Fakultas/Sekolah'] == self.fakultas]
            self.df2018_competenceC_fakultas = self.df2018_competenceC[
                self.df2018['Fakultas/Sekolah'] == self.fakultas]
            self.df2019_competenceA_fakultas = self.df2019_competenceA[
                self.df2019['Fakultas/Sekolah'] == self.fakultas]
            self.df2019_competenceB_fakultas = self.df2019_competenceB[
                self.df2019['Fakultas/Sekolah'] == self.fakultas]
            self.df2019_competenceC_fakultas = self.df2019_competenceC[
                self.df2019['Fakultas/Sekolah'] == self.fakultas]
            self.df2020_competenceA_fakultas = self.df2020_competenceA[
                self.df2020['Fakultas/Sekolah'] == self.fakultas]
            self.df2020_competenceB_fakultas = self.df2020_competenceB[
                self.df2020['Fakultas/Sekolah'] == self.fakultas]
            self.df2020_competenceC_fakultas = self.df2020_competenceC[
                self.df2020['Fakultas/Sekolah'] == self.fakultas]
            self.df2021_competenceA_fakultas = self.df2021_competenceA[
                self.df2021['Fakultas/Sekolah'] == self.fakultas]
            self.df2021_competenceB_fakultas = self.df2021_competenceB[
                self.df2021['Fakultas/Sekolah'] == self.fakultas]
            self.df2021_competenceC_fakultas = self.df2021_competenceC[
                self.df2021['Fakultas/Sekolah'] == self.fakultas]
            self.df2022_competenceA_fakultas = self.df2022_competenceA[
                self.df2022['Fakultas/Sekolah'] == self.fakultas]
            self.df2022_competenceB_fakultas = self.df2022_competenceB[
                self.df2022['Fakultas/Sekolah'] == self.fakultas]
            self.df2022_competenceC_fakultas = self.df2022_competenceC[
                self.df2022['Fakultas/Sekolah'] == self.fakultas]
            
            self.means2018 = np.array([self.df2018_competenceA_fakultas.mean()[21], self.df2018_competenceA_fakultas.mean()[15], self.df2018_competenceA_fakultas.mean()[14],
                                       self.df2018_competenceA_fakultas.mean()[10], self.df2018_competenceA_fakultas.mean()[
                4], self.df2018_competenceA_fakultas.mean()[19],
                self.df2018_competenceA_fakultas.mean()[19]])

            self.means2019 = np.array([self.df2019_competenceA_fakultas.mean()[22], self.df2019_competenceA_fakultas.mean()[16], self.df2019_competenceA_fakultas.mean()[14],
                                       self.df2019_competenceA_fakultas.mean()[10], self.df2019_competenceA_fakultas.mean()[
                4], self.df2019_competenceA_fakultas.mean()[15],
                self.df2019_competenceA_fakultas.mean()[20]])

            self.means2020 = np.array([self.df2020_competenceA_fakultas.mean()[22], self.df2020_competenceA_fakultas.mean()[16], self.df2020_competenceA_fakultas.mean()[14],
                                       self.df2020_competenceA_fakultas.mean()[10], self.df2020_competenceA_fakultas.mean()[
                4], self.df2020_competenceA_fakultas.mean()[15],
                self.df2020_competenceA_fakultas.mean()[20]])
            self.means2021 = np.array([self.df2021_competenceA_fakultas.mean()[22], self.df2021_competenceA_fakultas.mean()[16], self.df2021_competenceA_fakultas.mean()[14],
                                       self.df2021_competenceA_fakultas.mean()[10], self.df2021_competenceA_fakultas.mean()[
                4], self.df2021_competenceA_fakultas.mean()[15],
                self.df2021_competenceA_fakultas.mean()[20]])
            self.means2022 = np.array([self.df2022_competenceA_fakultas.mean()[22], self.df2022_competenceA_fakultas.mean()[16], self.df2022_competenceA_fakultas.mean()[14],
                                       self.df2022_competenceA_fakultas.mean()[10], self.df2022_competenceA_fakultas.mean()[
                4], self.df2022_competenceA_fakultas.mean()[15],
                self.df2022_competenceA_fakultas.mean()[20]])
            
        self.competencies2018 = ['memecahkan\nmasalah\nkompleks', 'berpikir\nkritis', 'inovasi\ndan/atau\nkreativitas', 'manajemen diri\ndan orang lain',
                                 'bekerja\ntim', 'bekerja\nindividu', 'kecerdasan\nemosional', 'penilaian dan\npengambilan\nkeputusan',
                                 'negosiasi', 'kecerdasan\ndalam\nbertindak', 'kemampuan\nbelajar', 'adaptasi\ndengan\nlingkungan',
                                 'kejujuran\n,loyalitas\n,integritas', 'bekerja dalam\ntekanan', 'etika',
                                 'pengetahuan\n dan penerapan\nbidang/disiplin\nilmu', 'pengetahuan\ndi luar \nbidang/displin\nilmu',
                                 'kemampuan\nanalisis', 'kemampuan \nadministrasi,\nmenuliskan\nlaporan\ndokumen', 'keterampilan\nteknologi\ninformasi dan\nkomunikasi',
                                 'merancang dan atau\nmendesain suatu\nkomponen,sistem\natau proses', 'berkomunikasi\ndengan\nbahasa asing', 'orientasi\nlayanan'
                                 ]

        self.competencies2019 = ['memecahkan\nmasalah\nkompleks', 'berpikir\nkritis', 'inovasi\ndan/atau\nkreativitas', 'manajemen diri\ndan orang lain',
                                 'bekerja\ntim', 'bekerja\nindividu', 'kecerdasan\nemosional', 'penilaian dan\npengambilan\nkeputusan',
                                 'negosiasi', 'kecerdasan\ndalam\nbertindak', 'kemampuan\nbelajar\nsepanjang\nhayat', 'adaptasi\ndengan\nlingkungan',
                                 'kejujuran\n,loyalitas\ndan integritas', 'bekerja dalam\ntekanan', 'etika dan\ntanggung jawab\nkeprofesian', 'kemampuan\nberkomunikasi',
                                 'pengetahuan\n dan penerapan\nbidang/disiplin\nilmu', 'pengetahuan\ndi luar \nbidang/displin\nilmu',
                                 'kemampuan\nanalisis dan\ninterpretasi data', 'kemampuan \nadministrasi,\nmenuliskan\nlaporan\ndokumen', 'keterampilan\nmenggunakan\nteknologi\ninformasi',
                                 'merancang\ndan atau\nmendesain suatu\nkomponen,sistem\natau\nproses', 'kemampuan\nbahasa\nasing'
                                 ]

        self.competencies2020 = self.competencies2019
        self.competencies2021 = self.competencies2019
        self.competencies2022 = self.competencies2019

        self.categoriesTrend = ["Bahasa\nAsing", "pengetahuan dan\npenerapan bidang/\ndisiplin ilmu", "etika dan tanggung\njawab keprofesian",
                                "kemampuan belajar\nsepanjang hayat", "bekerja tim", "kemampuan\nberkomunikasi", "keterampilan\nmenggunakan\nteknologi informasi"]

    def __filter_zero_workstatus_data(self, arr_workstatus_raw):
        workstatus_filtered = np.array([0, 0, 0, 0, 0])
        if "bekerja" in arr_workstatus_raw:
            workstatus_filtered[0] = arr_workstatus_raw['bekerja']
        if "bekerja dan wiraswasta" in arr_workstatus_raw:
            workstatus_filtered[1] = arr_workstatus_raw['bekerja dan wiraswasta']
        if "wirausaha" in arr_workstatus_raw:
            workstatus_filtered[2] = arr_workstatus_raw['wirausaha']
        if "melanjutkan studi" in arr_workstatus_raw:
            workstatus_filtered[3] = arr_workstatus_raw['melanjutkan studi']
        if "tidak bekerja" in arr_workstatus_raw:
            workstatus_filtered[4] = arr_workstatus_raw['tidak bekerja']

        return workstatus_filtered

    def __filter_zero_workstatus_data_v2(self, arr_workstatus_raw):
        workstatus_filtered = np.array([0, 0, 0, 0, 0])
        if "Bekerja" in arr_workstatus_raw:
            workstatus_filtered[0] = arr_workstatus_raw['Bekerja']
        if "Bekerja dan wiraswasta" in arr_workstatus_raw:
            workstatus_filtered[1] = arr_workstatus_raw['Bekerja dan wiraswasta']
        if "Wirausaha" in arr_workstatus_raw:
            workstatus_filtered[2] = arr_workstatus_raw['Wirausaha']
        if "Melanjutkan studi" in arr_workstatus_raw:
            workstatus_filtered[3] = arr_workstatus_raw['Melanjutkan studi']
        if "Tidak bekerja" in arr_workstatus_raw:
            workstatus_filtered[4] = arr_workstatus_raw['Tidak bekerja']

        return workstatus_filtered

    def init_jobstatus_data(self):
        if self.prodi != "All":
            arr_workstatus_2018 = self.df2018[self.df2018['4. Program Studi']
                                            == self.prodi].iloc[:, 75].value_counts(sort=False)
            arr_workstatus_2019 = self.df2019[self.df2019['4. Program Studi']
                                            == self.prodi].iloc[:, 76].value_counts(sort=False)
            arr_workstatus_2020 = self.df2020[self.df2020['4. Program Studi']
                                            == self.prodi].iloc[:, 76].value_counts(sort=False)
            arr_workstatus_2021 = self.df2021[self.df2021['Program Studi']
                                            == self.prodi].iloc[:, 77].value_counts(sort=False)
            arr_workstatus_2022 = self.df2022[self.df2022['Program Studi']
                                            == self.prodi].iloc[:, 77].value_counts(sort=False)
        else:
            arr_workstatus_2018 = self.df2018[self.df2018['Fakultas/Sekolah']
                                            == self.fakultas].iloc[:, 75].value_counts(sort=False)
            arr_workstatus_2019 = self.df2019[self.df2019['Fakultas/Sekolah']
                                            == self.fakultas].iloc[:, 76].value_counts(sort=False)
            arr_workstatus_2020 = self.df2020[self.df2020['Fakultas/Sekolah']
                                            == self.fakultas].iloc[:, 76].value_counts(sort=False)
            arr_workstatus_2021 = self.df2021[self.df2021['Fakultas/Sekolah']
                                            == self.fakultas].iloc[:, 77].value_counts(sort=False)
            arr_workstatus_2022 = self.df2022[self.df2022['Fakultas/Sekolah']
                                            == self.fakultas].iloc[:, 77].value_counts(sort=False)

        # try:
        workstatus_2018 = self.__filter_zero_workstatus_data(
            arr_workstatus_2018)
        workstatus_2019 = self.__filter_zero_workstatus_data(
            arr_workstatus_2019)
        workstatus_2020 = self.__filter_zero_workstatus_data(
            arr_workstatus_2020)
        workstatus_2021 = self.__filter_zero_workstatus_data_v2(
            arr_workstatus_2021)
        workstatus_2022 = self.__filter_zero_workstatus_data_v2(
            arr_workstatus_2022)

        self.workstatus_num = np.array([workstatus_2018,
                                        workstatus_2019,
                                        workstatus_2020,
                                        workstatus_2021,
                                        workstatus_2022])

        self.workstatus_perc = np.array([workstatus_2018/153,
                                         workstatus_2019/141,
                                         workstatus_2020/136,
                                         workstatus_2021/145,
                                         workstatus_2022/94])

    def init_timetogetwork_data(self):
        # Drop the data points that contains no value - 2018
        dfTTGWork2018_raw = self.df2018[["4. Program Studi", "37x. Kapankah Anda memperoleh pekerjaan pertama?",
                                         "37ax. Berapa bulan waktu yang digunakan (sebelum kelulusan) untuk memperoleh pekerjaan pertama?", "37bx. Berapa bulan waktu yang digunakan (sesudah kelulusan) untuk memperoleh pekerjaan pertama?"]]
        # If tidak bekerja, wirausaha,melanjutkan studi/bekerja but contains no value sesudah lulus atua sebelum lulus
        dfTTGWork2018 = dfTTGWork2018_raw.dropna(
            subset=['37x. Kapankah Anda memperoleh pekerjaan pertama?'])

        # Drop the data points that contains no value - 2019
        dfTTGWork2019_raw = self.df2019[["4. Program Studi", "37x. Kapankah Anda memperoleh pekerjaan pertama?",
                                         "37ax. Berapa bulan waktu yang digunakan (sebelum kelulusan) untuk memperoleh pekerjaan pertama?", "37bx. Berapa bulan waktu yang digunakan (sesudah kelulusan) untuk memperoleh pekerjaan pertama?"]]
        # If tidak bekerja, wirausaha,melanjutkan studi/bekerja but contains no value sesudah lulus atua sebelum lulus
        dfTTGWork2019 = dfTTGWork2019_raw.dropna(
            subset=['37x. Kapankah Anda memperoleh pekerjaan pertama?'])

        # Drop the data points that contains no value - 2019
        dfTTGWork2020_raw = self.df2020[["4. Program Studi", "37x. Kapankah Anda memperoleh pekerjaan pertama?",
                                         "37ax. Berapa bulan waktu yang digunakan (sebelum kelulusan) untuk memperoleh pekerjaan pertama?", "37bx. Berapa bulan waktu yang digunakan (sesudah kelulusan) untuk memperoleh pekerjaan pertama?"]]
        # If tidak bekerja, wirausaha,melanjutkan studi/bekerja but contains no value sesudah lulus atua sebelum lulus
        dfTTGWork2020 = dfTTGWork2020_raw.dropna(
            subset=['37x. Kapankah Anda memperoleh pekerjaan pertama?'])

        # Drop the data points that contains no value - 2019
        dfTTGWork2021_raw = self.df2021[["Program Studi", "Kapankah Anda memperoleh pekerjaan pertama?",
                                         "Berapa bulan waktu yang digunakan (sebelum kelulusan) untuk memperoleh pekerjaan pertama?", "Berapa bulan waktu yang digunakan (sesudah kelulusan) untuk memperoleh pekerjaan pertama?"]]
        # If tidak bekerja, wirausaha,melanjutkan studi/bekerja but contains no value sesudah lulus atua sebelum lulus
        dfTTGWork2021 = dfTTGWork2021_raw.dropna(
            subset=['Kapankah Anda memperoleh pekerjaan pertama?'])

        # Drop the data points that contains no value - 2019
        dfTTGWork2022_raw = self.df2022[["Program Studi", "Kapankah Anda memperoleh pekerjaan pertama?",
                                         "Berapa bulan waktu yang digunakan (sebelum kelulusan) untuk memperoleh pekerjaan pertama?", "Berapa bulan waktu yang digunakan (sesudah kelulusan) untuk memperoleh pekerjaan pertama?"]]

        # If tidak bekerja, wirausaha,melanjutkan studi/bekerja but contains no value sesudah lulus atua sebelum lulus
        dfTTGWork2022 = dfTTGWork2022_raw.dropna(
            subset=['Kapankah Anda memperoleh pekerjaan pertama?'])
        # dfTTGWork2018.iloc[230:330]

        # GET PRODI DATAFRAME
        dfTTGWork2018_Prodi = dfTTGWork2018[dfTTGWork2018['4. Program Studi'] == self.prodi]
        self.dfTTGWork2018_Prodi_BeforeGrad = dfTTGWork2018_Prodi[dfTTGWork2018_Prodi[
            "37x. Kapankah Anda memperoleh pekerjaan pertama?"] == "sebelum lulus"]
        self.dfTTGWork2018_Prodi_AfterGrad = dfTTGWork2018_Prodi[dfTTGWork2018_Prodi[
            "37x. Kapankah Anda memperoleh pekerjaan pertama?"] == "sesudah lulus"]

        dfTTGWork2019_Prodi = dfTTGWork2019[dfTTGWork2019['4. Program Studi'] == self.prodi]
        self.dfTTGWork2019_Prodi_BeforeGrad = dfTTGWork2019_Prodi[dfTTGWork2019_Prodi[
            "37x. Kapankah Anda memperoleh pekerjaan pertama?"] == "sebelum lulus"]
        self.dfTTGWork2019_Prodi_AfterGrad = dfTTGWork2019_Prodi[dfTTGWork2019_Prodi[
            "37x. Kapankah Anda memperoleh pekerjaan pertama?"] == "sesudah lulus"]

        dfTTGWork2020_Prodi = dfTTGWork2020[dfTTGWork2020['4. Program Studi'] == self.prodi]
        self.dfTTGWork2020_Prodi_BeforeGrad = dfTTGWork2020_Prodi[dfTTGWork2020_Prodi[
            "37x. Kapankah Anda memperoleh pekerjaan pertama?"] == "sebelum lulus"]
        self.dfTTGWork2020_Prodi_AfterGrad = dfTTGWork2020_Prodi[dfTTGWork2020_Prodi[
            "37x. Kapankah Anda memperoleh pekerjaan pertama?"] == "sesudah lulus"]

        dfTTGWork2021_Prodi = dfTTGWork2021[dfTTGWork2021['Program Studi'] == self.prodi]
        self.dfTTGWork2021_Prodi_BeforeGrad = dfTTGWork2021_Prodi[dfTTGWork2021_Prodi[
            "Kapankah Anda memperoleh pekerjaan pertama?"] == "Sebelum lulus"]
        self.dfTTGWork2021_Prodi_AfterGrad = dfTTGWork2021_Prodi[dfTTGWork2021_Prodi[
            "Kapankah Anda memperoleh pekerjaan pertama?"] == "Sesudah lulus"]

        dfTTGWork2022_Prodi = dfTTGWork2022[dfTTGWork2022['Program Studi'] == self.prodi]
        self.dfTTGWork2022_Prodi_BeforeGrad = dfTTGWork2022_Prodi[dfTTGWork2022_Prodi[
            "Kapankah Anda memperoleh pekerjaan pertama?"] == "Sebelum lulus"]
        self.dfTTGWork2022_Prodi_AfterGrad = dfTTGWork2022_Prodi[dfTTGWork2022_Prodi[
            "Kapankah Anda memperoleh pekerjaan pertama?"] == "Sesudah lulus"]

    def __filter_company_category_data(self, company_category_raw):
        companycat_filtered = np.array([0, 0, 0])
        if "lokal" in company_category_raw:
            companycat_filtered[0] = company_category_raw['lokal']
        if "multinasional" in company_category_raw:
            companycat_filtered[1] = company_category_raw['multinasional']
        if "nasional" in company_category_raw:
            companycat_filtered[2] = company_category_raw['nasional']

        return companycat_filtered

    def __filter_company_category_datav2(self, company_category_raw):
        companycat_filtered = np.array([0, 0, 0])
        if "Lokal" in company_category_raw:
            companycat_filtered[0] = company_category_raw['Lokal']
        if "Multinasional" in company_category_raw:
            companycat_filtered[1] = company_category_raw['Multinasional']
        if "Nasional" in company_category_raw:
            companycat_filtered[2] = company_category_raw['Nasional']

    def init_company_category_data(self):

        self.df2018['Fakultas/Sekolah'] = self.df2018['4. Program Studi'].apply(
            self.__lookup_faculty_from_major)
        self.df2019['Fakultas/Sekolah'] = self.df2019['4. Program Studi'].apply(
            self.__lookup_faculty_from_major)
        self.df2020['Fakultas/Sekolah'] = self.df2020['4. Program Studi'].apply(
            self.__lookup_faculty_from_major)
        
        dfCompanyCat2018_raw = self.df2018[[
            "4. Program Studi","Fakultas/Sekolah","A10. Apa kategori perusahaan tempat Anda bekerja?"]]
        dfCompanyCat2018 = dfCompanyCat2018_raw.dropna(
            subset=["A10. Apa kategori perusahaan tempat Anda bekerja?"])

        dfCompanyCat2019_raw = self.df2019[[
            "4. Program Studi","Fakultas/Sekolah","A10. Apa kategori perusahaan tempat Anda bekerja?"]]
        dfCompanyCat2019 = dfCompanyCat2019_raw.dropna(
            subset=["A10. Apa kategori perusahaan tempat Anda bekerja?"])

        dfCompanyCat2020_raw = self.df2020[[
            "4. Program Studi","Fakultas/Sekolah", "A10. Apa kategori perusahaan tempat Anda bekerja?"]]
        dfCompanyCat2020 = dfCompanyCat2020_raw.dropna(
            subset=["A10. Apa kategori perusahaan tempat Anda bekerja?"])

        dfCompanyCat2021_raw = self.df2021[[
            "Program Studi","Fakultas/Sekolah", "Apa kategori perusahaan tempat Anda bekerja?"]]
        dfCompanyCat2021 = dfCompanyCat2021_raw.dropna(
            subset=["Apa kategori perusahaan tempat Anda bekerja?"])

        dfCompanyCat2022_raw = self.df2022[[
            "Program Studi","Fakultas/Sekolah", "Apa kategori perusahaan tempat Anda bekerja?"]]
        dfCompanyCat2022 = dfCompanyCat2022_raw.dropna(
            subset=["Apa kategori perusahaan tempat Anda bekerja?"])

        if self.prodi != "All":
            dfCompanyCat2018_Prodi = dfCompanyCat2018[dfCompanyCat2018["4. Program Studi"] == self.prodi]
            dfCompanyCat2019_Prodi = dfCompanyCat2019[dfCompanyCat2019["4. Program Studi"] == self.prodi]
            dfCompanyCat2020_Prodi = dfCompanyCat2020[dfCompanyCat2020["4. Program Studi"] == self.prodi]
            dfCompanyCat2021_Prodi = dfCompanyCat2021[dfCompanyCat2021["Program Studi"] == self.prodi]
            dfCompanyCat2022_Prodi = dfCompanyCat2022[dfCompanyCat2022["Program Studi"] == self.prodi]
            
            valueCompanyCat2018_Prodi = self.__filter_company_category_data(dfCompanyCat2018_Prodi["A10. Apa kategori perusahaan tempat Anda bekerja?"].value_counts().sort_index())
            valueCompanyCat2019_Prodi = self.__filter_company_category_data(dfCompanyCat2019_Prodi["A10. Apa kategori perusahaan tempat Anda bekerja?"].value_counts().sort_index())
            valueCompanyCat2020_Prodi = self.__filter_company_category_data(dfCompanyCat2020_Prodi["A10. Apa kategori perusahaan tempat Anda bekerja?"].value_counts().sort_index())
            valueCompanyCat2021_Prodi = self.__filter_company_category_datav2(dfCompanyCat2021_Prodi["Apa kategori perusahaan tempat Anda bekerja?"].value_counts().sort_index())
            valueCompanyCat2022_Prodi = self.__filter_company_category_datav2(dfCompanyCat2022_Prodi["Apa kategori perusahaan tempat Anda bekerja?"].value_counts().sort_index())
            self.valueCompanyCat_Prodi = np.array([valueCompanyCat2018_Prodi, valueCompanyCat2019_Prodi,
                                                valueCompanyCat2020_Prodi, valueCompanyCat2021_Prodi,
                                                valueCompanyCat2022_Prodi])
        else:
            print(dfCompanyCat2018)
            dfCompanyCat2018_fakultas = dfCompanyCat2018[dfCompanyCat2018["Fakultas/Sekolah"] == self.fakultas]
            dfCompanyCat2019_fakultas = dfCompanyCat2019[dfCompanyCat2019["Fakultas/Sekolah"] == self.fakultas]
            dfCompanyCat2020_fakultas = dfCompanyCat2020[dfCompanyCat2020["Fakultas/Sekolah"] == self.fakultas]
            dfCompanyCat2021_fakultas = dfCompanyCat2021[dfCompanyCat2021["Fakultas/Sekolah"] == self.fakultas]
            dfCompanyCat2022_fakultas = dfCompanyCat2022[dfCompanyCat2022["Fakultas/Sekolah"] == self.fakultas]
            
            valueCompanyCat2018_fakultas = self.__filter_company_category_data(dfCompanyCat2018_fakultas["A10. Apa kategori perusahaan tempat Anda bekerja?"].value_counts().sort_index())
            valueCompanyCat2019_fakultas = self.__filter_company_category_data(dfCompanyCat2019_fakultas["A10. Apa kategori perusahaan tempat Anda bekerja?"].value_counts().sort_index())
            valueCompanyCat2020_fakultas = self.__filter_company_category_data(dfCompanyCat2020_fakultas["A10. Apa kategori perusahaan tempat Anda bekerja?"].value_counts().sort_index())
            valueCompanyCat2021_fakultas = self.__filter_company_category_datav2(dfCompanyCat2021_fakultas["Apa kategori perusahaan tempat Anda bekerja?"].value_counts().sort_index())
            valueCompanyCat2022_fakultas = self.__filter_company_category_datav2(dfCompanyCat2022_fakultas["Apa kategori perusahaan tempat Anda bekerja?"].value_counts().sort_index())
            self.valueCompanyCat_fakultas = np.array([valueCompanyCat2018_fakultas, valueCompanyCat2019_fakultas,
                                                valueCompanyCat2020_fakultas, valueCompanyCat2021_fakultas,
                                                valueCompanyCat2022_fakultas])

        
    def __insert_missing_index (self,missingdf):
        field =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U']
        zeros = [0]*len(field)
        alphabet =pd.DataFrame(zeros, index = field)
        z =pd.DataFrame(missingdf)
        missing_index = alphabet.index.difference(z.index)
        result = pd.concat([z,alphabet.loc[missing_index, :]]).sort_index(ascending=True).fillna(0)
        result.pop(0)
        return result

    def init_company_field_data(self, status="Bekerja"):
        #KARENA DATA 2018-2020 MEMISAHKAN ANTARA KATEGORI A (BEKERJA) DAN B (BEKERJA DAN WIRAUSAHA), MAKA HARUS DIGABUNGKAN
        if status == "Bekerja":
            dfCompanyField2018_rawA = self.df2018[[
                "4. Program Studi", "A2. Bidang Usaha"]]
            dfCompanyField2018A = dfCompanyField2018_rawA.dropna(
                subset=["A2. Bidang Usaha"])
            dfCompanyField2018_rawB = self.df2018[[
                "4. Program Studi", "B2. Bidang Usaha"]]
            dfCompanyField2018B = dfCompanyField2018_rawB.dropna(
                subset=["B2. Bidang Usaha"])
            
            dfCompanyField2019_rawA = self.df2019[[
                "4. Program Studi", "A2. Bidang Usaha"]]
            dfCompanyField2019A = dfCompanyField2019_rawA.dropna(
                subset=["A2. Bidang Usaha"])
            dfCompanyField2019_rawB = self.df2019[[
                "4. Program Studi", "B2. Bidang Usaha"]]
            dfCompanyField2019B= dfCompanyField2019_rawB.dropna(
                subset=["B2. Bidang Usaha"])        

            dfCompanyField2020_rawA = self.df2020[[
                "4. Program Studi", "A2. Bidang Usaha"]]
            dfCompanyField2020A = dfCompanyField2020_rawA.dropna(
                subset=["A2. Bidang Usaha"])
            dfCompanyField2020_rawB = self.df2020[[
                "4. Program Studi", "B2. Bidang Usaha"]]
            dfCompanyField2020B = dfCompanyField2020_rawB.dropna(
                subset= ["B2. Bidang Usaha"])
            
            dfCompanyField2021_raw = self.df2021[[
                "Program Studi", "Bidang usaha bekerja"]]
            dfCompanyField2021 = dfCompanyField2021_raw.dropna(
                subset=["Bidang usaha bekerja"])

            dfCompanyField2022_raw = self.df2022[[
                "Program Studi", "Bidang usaha bekerja"]]
            dfCompanyField2022 = dfCompanyField2022_raw.dropna(
                subset=["Bidang usaha bekerja"])

            dfCompanyField2018A_Prodi = dfCompanyField2018A[dfCompanyField2018A["4. Program Studi"] == self.prodi]
            dfCompanyField2018B_Prodi = dfCompanyField2018B[dfCompanyField2018B["4. Program Studi"] == self.prodi]
            dfCompanyField2019A_Prodi = dfCompanyField2019A[dfCompanyField2019A["4. Program Studi"] == self.prodi]
            dfCompanyField2019B_Prodi = dfCompanyField2019B[dfCompanyField2019B["4. Program Studi"] == self.prodi]
            dfCompanyField2020A_Prodi = dfCompanyField2020A[dfCompanyField2020A["4. Program Studi"] == self.prodi]
            dfCompanyField2020B_Prodi = dfCompanyField2020B[dfCompanyField2020B["4. Program Studi"] == self.prodi]
            dfCompanyField2021_Prodi = dfCompanyField2021[dfCompanyField2021["Program Studi"] == self.prodi]
            dfCompanyField2022_Prodi = dfCompanyField2022[dfCompanyField2022["Program Studi"] == self.prodi]

            valueCompanyField2018A_Prodi = dfCompanyField2018A_Prodi["A2. Bidang Usaha"].value_counts(ascending= True).sort_index(ascending= True)
            valueCompanyField2018B_Prodi = dfCompanyField2018B_Prodi["B2. Bidang Usaha"].value_counts(ascending= True).sort_index(ascending= True)
            valueCompanyField2019A_Prodi = dfCompanyField2019A_Prodi["A2. Bidang Usaha"].value_counts(ascending= True).sort_index(ascending= True)
            valueCompanyField2019B_Prodi = dfCompanyField2019B_Prodi["B2. Bidang Usaha"].value_counts(ascending= True).sort_index(ascending= True)
            valueCompanyField2020A_Prodi = dfCompanyField2020A_Prodi["A2. Bidang Usaha"].value_counts(ascending= True).sort_index(ascending= True)
            valueCompanyField2020B_Prodi = dfCompanyField2020B_Prodi["B2. Bidang Usaha"].value_counts(ascending= True).sort_index(ascending= True)

            valueCompanyField2018_Prodi = valueCompanyField2018A_Prodi.add(valueCompanyField2018B_Prodi, fill_value = 0 )
            valueCompanyField2019_Prodi = valueCompanyField2019A_Prodi.add(valueCompanyField2019B_Prodi, fill_value = 0 )
            valueCompanyField2020_Prodi = valueCompanyField2020A_Prodi.add(valueCompanyField2020B_Prodi, fill_value = 0 )

            valueCompanyField2021_Prodi = dfCompanyField2021_Prodi["Bidang usaha bekerja"].value_counts(
            ).sort_index()
            valueCompanyField2022_Prodi = dfCompanyField2022_Prodi["Bidang usaha bekerja"].value_counts(
            ).sort_index()

            valueCompanyField2018A_Prodi = self.__insert_missing_index(valueCompanyField2018A_Prodi.astype(np.int64))
            valueCompanyField2019A_Prodi = self.__insert_missing_index(valueCompanyField2019A_Prodi.astype(np.int64))
            valueCompanyField202A_Prodi = self.__insert_missing_index(valueCompanyField2020A_Prodi.astype(np.int64))
            valueCompanyField2021_Prodi = self.__insert_missing_index(valueCompanyField2021_Prodi.astype(np.int64))
            valueCompanyField2022_Prodi = self.__insert_missing_index(valueCompanyField2022_Prodi.astype(np.int64))

            self.valueCompanyField_Prodi = pd.concat ([valueCompanyField2018_Prodi,valueCompanyField2019_Prodi,valueCompanyField2020_Prodi, valueCompanyField2021_Prodi, valueCompanyField2022_Prodi], axis =1)
            self.valueCompanyField_Prodi.columns = ['2018', '2019', '2020', '2021', '2022']
            
    def init_revenue_data(self):
        # Get the raw data
        dfrevenue2018_raw = self.df2018[['4. Program Studi', '33. Pekerjaan utama saat ini?', 
                                         'A8. Berapa gaji per bulan saat ini di luar bonus? (dalam Rupiah)',
                                              'A9. Berapa bonus rata-rata per tahun (Jika ada)? (dalam Rupiah)', 
                                         'B8. Berapa rata-rata penghasilan per bulan saat ini di luar bonus? (dalam Rupiah)',
                                              'B9. Berapa bonus rata-rata per tahun (Jika ada)? (dalam Rupiah)', 
                                         'C8. Berapa rata-rata penghasilan per bulan saat ini di luar bonus? (dalam Rupiah)',
                                              'C9. Berapa bonus rata-rata per tahun (Jika ada)? (dalam Rupiah)',
                                         'C13. Berapa omset rata-rata perbulan? (dalam Rupiah)']]
        dfrevenue2019_raw = self.df2019[['4. Program Studi', '33. Pekerjaan utama saat ini?', 
                                         'A8. Berapa gaji per bulan saat ini di luar bonus? (dalam Rupiah)',
                                              'A9. Berapa bonus rata-rata per tahun (Jika ada)? (dalam Rupiah)',
                                         'B8. Berapa rata-rata penghasilan per bulan saat ini di luar bonus? (dalam Rupiah)',
                                              'B9. Berapa bonus rata-rata per tahun (Jika ada)? (dalam Rupiah)',
                                         'C7. Berapa rata-rata penghasilan per bulan saat ini di luar bonus? (dalam Rupiah)',
                                              'C8. Berapa bonus rata-rata per tahun (Jika ada)? (dalam Rupiah)',
                                         'C12. Berapa omset rata-rata perbulan? (dalam Rupiah)']]
        dfrevenue2020_raw = self.df2020[['4. Program Studi', '33. Pekerjaan utama saat ini?', 
                                         'A8. Berapa gaji per bulan saat ini di luar bonus? (dalam Rupiah)',
                                              'A9. Berapa bonus rata-rata per tahun (Jika ada)? (dalam Rupiah)',
                                         'B8. Berapa rata-rata penghasilan per bulan saat ini di luar bonus? (dalam Rupiah)',
                                              'B9. Berapa bonus rata-rata per tahun (Jika ada)? (dalam Rupiah)',
                                         'C7. Berapa rata-rata penghasilan per bulan saat ini di luar bonus? (dalam Rupiah)',
                                              'C8. Berapa bonus rata-rata per tahun (Jika ada)? (dalam Rupiah)',
                                         'C12. Berapa omset rata-rata perbulan? (dalam Rupiah)']]
        dfrevenue2021_raw = self.df2021[['Program Studi', 'Pekerjaan utama saat ini?', 
                                         'Berapa gaji per bulan saat ini di luar bonus? (dalam Rupiah)', 
                                         'Berapa bonus rata-rata per tahun (Jika ada)? (dalam Rupiah)',
                                         'Berapa omset rata-rata perbulan? (dalam Rupiah)']]
        dfrevenue2022_raw = self.df2022[['Program Studi', 'Pekerjaan utama saat ini?', 
                                         'Berapa gaji per bulan saat ini di luar bonus? (dalam Rupiah)', 
                                         'Berapa bonus rata-rata per tahun (Jika ada)? (dalam Rupiah)',
                                         'Berapa omset rata-rata perbulan? (dalam Rupiah)']]

        # GET PRODI DATAFRAME
        self.dfrevenue2018_Prodi = dfrevenue2018_raw[dfrevenue2018_raw['4. Program Studi'] == self.prodi]
        self.dfrevenue2019_Prodi = dfrevenue2019_raw[dfrevenue2019_raw['4. Program Studi'] == self.prodi]
        self.dfrevenue2020_Prodi = dfrevenue2020_raw[dfrevenue2020_raw['4. Program Studi'] == self.prodi]
        self.dfrevenue2021_Prodi = dfrevenue2021_raw[dfrevenue2021_raw['Program Studi'] == self.prodi]
        self.dfrevenue2022_Prodi = dfrevenue2022_raw[dfrevenue2022_raw['Program Studi'] == self.prodi]
        #pendapatan bekerja
        pb18 = []
        pb19 = []
        pb20 = []
        pb21 = []
        pb22 = []
        #pendapatan usaha
        pu18 = []
        pu19 = []
        pu20 = []
        pu21 = []
        pu22 = []

        #grouping for bekerja and wirausaha category
        #year 2018
        for i in range(len(self.dfrevenue2018_Prodi)):
            if self.dfrevenue2018_Prodi.iloc[i, 1] == 'bekerja':
                x = self.dfrevenue2018_Prodi.iloc[i, 2]
                pb18.append(x)
            elif self.dfrevenue2018_Prodi.iloc[i, 1] == 'wirausaha':
                x = self.dfrevenue2018_Prodi.iloc[i, 6]
                pu18.append(x)
            elif self.dfrevenue2018_Prodi.iloc[i, 1] == 'bekerja dan wiraswasta':
                x = self.dfrevenue2018_Prodi.iloc[i, 4]
                pb18.append(x)

        #year 2019
        for i in range(len(self.dfrevenue2019_Prodi)):
            if self.dfrevenue2019_Prodi.iloc[i, 1] == 'bekerja':
                x = self.dfrevenue2019_Prodi.iloc[i, 2]
                pb19.append(x)
            elif self.dfrevenue2019_Prodi.iloc[i, 1] == 'wirausaha':
                x = self.dfrevenue2019_Prodi.iloc[i, 6]
                pu19.append(x)
            elif self.dfrevenue2019_Prodi.iloc[i, 1] == 'bekerja dan wiraswasta':
                x = self.dfrevenue2019_Prodi.iloc[i, 4]
                pb19.append(x)

        #year 2020
        for i in range(len(self.dfrevenue2020_Prodi)):
            if self.dfrevenue2020_Prodi.iloc[i, 1] == 'bekerja':
                x = self.dfrevenue2020_Prodi.iloc[i, 2]
                pb20.append(x)
            elif self.dfrevenue2020_Prodi.iloc[i, 1] == 'wirausaha':
                x = self.dfrevenue2020_Prodi.iloc[i, 6]
                pu20.append(x)
            elif self.dfrevenue2020_Prodi.iloc[i, 1] == 'bekerja dan wiraswasta':
                x = self.dfrevenue2020_Prodi.iloc[i, 4]
                pb20.append(x)
                
        #year 2021
        for i in range(len(self.dfrevenue2021_Prodi)):
            if self.dfrevenue2021_Prodi.iloc[i, 1] == 'Bekerja':
                x = self.dfrevenue2021_Prodi.iloc[i, 2]
                pb21.append(x)
            elif self.dfrevenue2021_Prodi.iloc[i, 1] == 'Wirausaha':
                x = self.dfrevenue2021_Prodi.iloc[i, 2]
                pu21.append(x)
            elif self.dfrevenue2021_Prodi.iloc[i, 1] == 'Bekerja dan wiraswasta':
                x = self.dfrevenue2021_Prodi.iloc[i, 2]
                pb21.append(x)
                
        #year 2022
        for i in range(len(self.dfrevenue2022_Prodi)):
            if self.dfrevenue2022_Prodi.iloc[i, 1] == 'Bekerja':
                x = self.dfrevenue2022_Prodi.iloc[i, 2]
                pb22.append(x)
            elif self.dfrevenue2022_Prodi.iloc[i, 1] == 'Wirausaha':
                x = self.dfrevenue2022_Prodi.iloc[i, 2]
                pu22.append(x)
            elif self.dfrevenue2022_Prodi.iloc[i, 1] == 'Bekerja dan wiraswasta':
                x = self.dfrevenue2022_Prodi.iloc[i, 2]
                pb22.append(x)

        #make dataframe filled with 0 if the dataframe empty
        #bekerja
        if not pb18:
            pb18 = [0] * 1
        if not pb19:
            pb19 = [0] * len(pb18)
        if not pb20:
            pb20 = [0] * len(pb19)
        if not pb21:
            pb21 = [0] * len(pb20)
        if not pb22:
            pb22 = [0] * len(pb21)
        #wirausaha
        if not pu18:
            pu18 = [0] * len(pb22)
        if not pu19:
            pu19 = [0] * len(pu18)
        if not pu20:
            pu20 = [0] * len(pu19)
        if not pu21:
            pu21 = [0] * len(pu20)
        if not pu22:
            pu22 = [0] * len(pu21)
        #convert it
        self.pb18 = pb18
        self.pb19 = pb19
        self.pb20 = pb20
        self.pb21 = pb21
        self.pb22 = pb22

        self.pu18 = pu18
        self.pu19 = pu19
        self.pu20 = pu20
        self.pu21 = pu21
        self.pu22 = pu22
        
        #bonus dan omset
        #bonus bekerja
        bb18 = []
        bb19 = []
        bb20 = []
        bb21 = []
        bb22 = []
        #omset usaha
        ow18 = []
        ow19 = []
        ow20 = []
        ow21 = []
        ow22 = []

        #grouping for bekerja and wirausaha category
        #year 2018
        for i in range(len(self.dfrevenue2018_Prodi)):
            if self.dfrevenue2018_Prodi.iloc[i, 1] == 'bekerja':
                x = self.dfrevenue2018_Prodi.iloc[i, 3]
                bb18.append(x)
            elif self.dfrevenue2018_Prodi.iloc[i, 1] == 'wirausaha':
                x = self.dfrevenue2018_Prodi.iloc[i, 8]
                ow18.append(x)
            elif self.dfrevenue2018_Prodi.iloc[i, 1] == 'bekerja dan wiraswasta':
                x = self.dfrevenue2018_Prodi.iloc[i, 5]
                bb18.append(x)
                

        #year 2019
        for i in range(len(self.dfrevenue2019_Prodi)):
            if self.dfrevenue2019_Prodi.iloc[i, 1] == 'bekerja':
                x = self.dfrevenue2019_Prodi.iloc[i, 3]
                bb19.append(x)
            elif self.dfrevenue2019_Prodi.iloc[i, 1] == 'wirausaha':
                x = self.dfrevenue2019_Prodi.iloc[i, 8]
                ow19.append(x)
            elif self.dfrevenue2019_Prodi.iloc[i, 1] == 'bekerja dan wiraswasta':
                x = self.dfrevenue2019_Prodi.iloc[i, 5]
                bb19.append(x)

        #year 2020
        for i in range(len(self.dfrevenue2020_Prodi)):
            if self.dfrevenue2020_Prodi.iloc[i, 1] == 'bekerja':
                x = self.dfrevenue2020_Prodi.iloc[i, 3]
                bb20.append(x)
            elif self.dfrevenue2020_Prodi.iloc[i, 1] == 'wirausaha':
                x = self.dfrevenue2020_Prodi.iloc[i, 8]
                ow20.append(x)
            elif self.dfrevenue2020_Prodi.iloc[i, 1] == 'bekerja dan wiraswasta':
                x = self.dfrevenue2020_Prodi.iloc[i, 5]
                bb20.append(x)
                
        #year 2021
        for i in range(len(self.dfrevenue2021_Prodi)):
            if self.dfrevenue2021_Prodi.iloc[i, 1] == 'Bekerja':
                x = self.dfrevenue2021_Prodi.iloc[i, 3]
                bb21.append(x)
            elif self.dfrevenue2021_Prodi.iloc[i, 1] == 'Wirausaha':
                x = self.dfrevenue2021_Prodi.iloc[i, 4]
                ow21.append(x)
            elif self.dfrevenue2021_Prodi.iloc[i, 1] == 'Bekerja dan wiraswasta':
                x = self.dfrevenue2021_Prodi.iloc[i, 3]
                bb21.append(x)
                
        #year 2022
        for i in range(len(self.dfrevenue2022_Prodi)):
            if self.dfrevenue2022_Prodi.iloc[i, 1] == 'Bekerja':
                x = self.dfrevenue2022_Prodi.iloc[i, 3]
                bb22.append(x)
            elif self.dfrevenue2022_Prodi.iloc[i, 1] == 'Wirausaha':
                x = self.dfrevenue2022_Prodi.iloc[i, 4]
                ow22.append(x)
            elif self.dfrevenue2022_Prodi.iloc[i, 1] == 'Bekerja dan wiraswasta':
                x = self.dfrevenue2022_Prodi.iloc[i, 4]
                bb22.append(x)


        #make dataframe filled with 0 if the dataframe empty
        #bekerja
        if not bb18:
            bb18 = [0] * 10
        if not bb19:
            bb19 = [0] * len(bb18)
        if not bb20:
            bb20 = [0] * len(bb19)
        if not bb21:
            bb21 = [0] * len(bb20)
        if not bb22:
            bb22 = [0] * len(bb21)
        #wirausaha
        if not ow18:
            ow18 = [0] * len(bb22)
        if not ow19:
            ow19 = [0] * len(ow18)
        if not ow20:
            ow20 = [0] * len(ow19)
        if not ow21:
            ow21 = [0] * len(ow20)
        if not ow22:
            ow22 = [0] * len(ow21)
        #convert it
        self.bb18 = bb18
        self.bb19 = bb19
        self.bb20 = bb20
        self.bb21 = bb21
        self.bb22 = bb22

        self.ow18 = ow18
        self.ow19 = ow19
        self.ow20 = ow20
        self.ow21 = ow21
        self.ow22 = ow22
        
    def __filter_company_related_study(self, company_category_raw):
        companycat_filtered = np.array([0, 0])
        if "ya" in company_category_raw:
            companycat_filtered[0] = company_category_raw['ya']
        if "tidak" in company_category_raw:
            companycat_filtered[1] = company_category_raw['tidak']

        return companycat_filtered
            
    def init_company_related_study(self, status):
        if status == "Bekerja":
            dfCompanyRelated2018_rawA = self.df2018[[
                "4. Program Studi", "A11. Apakah pekerjaan Anda saat ini sesuai dengan bidang kuliah?"]]
            dfCompanyRelated2018A = dfCompanyRelated2018_rawA.dropna(
                subset=["A11. Apakah pekerjaan Anda saat ini sesuai dengan bidang kuliah?"])
            dfCompanyRelated2018_rawB = self.df2018[[
                "4. Program Studi", "B22. Apakah pekerjaan Anda saat ini sesuai dengan bidang kuliah?"]]
            dfCompanyRelated2018B = dfCompanyRelated2018_rawB.dropna(
                subset=["B22. Apakah pekerjaan Anda saat ini sesuai dengan bidang kuliah?"])
            
            dfCompanyRelated2019_rawA = self.df2019[[
                "4. Program Studi", "A11. Apakah pekerjaan Anda saat ini sesuai dengan bidang kuliah?"]]
            dfCompanyRelated2019A = dfCompanyRelated2019_rawA.dropna(
                subset=["A11. Apakah pekerjaan Anda saat ini sesuai dengan bidang kuliah?"])
            dfCompanyRelated2019_rawB = self.df2019[[
                "4. Program Studi", "B22. Apakah pekerjaan Anda saat ini sesuai dengan bidang kuliah?"]]
            dfCompanyRelated2019B= dfCompanyRelated2019_rawB.dropna(
                subset=["B22. Apakah pekerjaan Anda saat ini sesuai dengan bidang kuliah?"])

            dfCompanyRelated2020_rawA = self.df2020[[
                "4. Program Studi", "A11. Apakah pekerjaan Anda saat ini sesuai dengan bidang kuliah?"]]
            dfCompanyRelated2020A = dfCompanyRelated2020_rawA.dropna(
                subset=["A11. Apakah pekerjaan Anda saat ini sesuai dengan bidang kuliah?"])
            dfCompanyRelated2020_rawB = self.df2020[[
                "4. Program Studi", "B22. Apakah pekerjaan Anda saat ini sesuai dengan bidang kuliah?"]]
            dfCompanyRelated2020B = dfCompanyRelated2020_rawB.dropna(
                subset= ["B22. Apakah pekerjaan Anda saat ini sesuai dengan bidang kuliah?"])
            
            dfCompanyRelated2021_raw = self.df2021[[
                "Program Studi", "Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"]]
            dfCompanyRelated2021 = dfCompanyRelated2021_raw.dropna(
                subset=["Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"])

            dfCompanyRelated2022_raw = self.df2022[[
                "Program Studi", "Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"]]
            dfCompanyRelated2022 = dfCompanyRelated2022_raw.dropna(
                subset=["Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"])

            dfCompanyRelated2018A_Prodi = dfCompanyRelated2018A[dfCompanyRelated2018A["4. Program Studi"] == self.prodi]
            dfCompanyRelated2018B_Prodi = dfCompanyRelated2018B[dfCompanyRelated2018B["4. Program Studi"] == self.prodi]
            dfCompanyRelated2019A_Prodi = dfCompanyRelated2019A[dfCompanyRelated2019A["4. Program Studi"] == self.prodi]
            dfCompanyRelated2019B_Prodi = dfCompanyRelated2019B[dfCompanyRelated2019B["4. Program Studi"] == self.prodi]
            dfCompanyRelated2020A_Prodi = dfCompanyRelated2020A[dfCompanyRelated2020A["4. Program Studi"] == self.prodi]
            dfCompanyRelated2020B_Prodi = dfCompanyRelated2020B[dfCompanyRelated2020B["4. Program Studi"] == self.prodi]
            dfCompanyRelated2021_Prodi = dfCompanyRelated2021[dfCompanyRelated2021["Program Studi"] == self.prodi]
            dfCompanyRelated2022_Prodi = dfCompanyRelated2022[dfCompanyRelated2022["Program Studi"] == self.prodi]

            valueCompanyRelated2018A = self.__filter_company_related_study(dfCompanyRelated2018A_Prodi["A11. Apakah pekerjaan Anda saat ini sesuai dengan bidang kuliah?"].value_counts().sort_index())
            valueCompanyRelated2018B = self.__filter_company_related_study(dfCompanyRelated2018B_Prodi["B22. Apakah pekerjaan Anda saat ini sesuai dengan bidang kuliah?"].value_counts().sort_index())
            valueCompanyRelated2019A = self.__filter_company_related_study(dfCompanyRelated2019A_Prodi["A11. Apakah pekerjaan Anda saat ini sesuai dengan bidang kuliah?"].value_counts().sort_index())
            valueCompanyRelated2019B = self.__filter_company_related_study(dfCompanyRelated2019B_Prodi["B22. Apakah pekerjaan Anda saat ini sesuai dengan bidang kuliah?"].value_counts().sort_index())
            valueCompanyRelated2020A = self.__filter_company_related_study(dfCompanyRelated2020A_Prodi["A11. Apakah pekerjaan Anda saat ini sesuai dengan bidang kuliah?"].value_counts().sort_index())
            valueCompanyRelated2020B = self.__filter_company_related_study(dfCompanyRelated2020B_Prodi["B22. Apakah pekerjaan Anda saat ini sesuai dengan bidang kuliah?"].value_counts().sort_index())

            valueCompanyRelated2018 = valueCompanyRelated2018A + valueCompanyRelated2018B
            valueCompanyRelated2019 = valueCompanyRelated2019A + valueCompanyRelated2019B
            valueCompanyRelated2020 = valueCompanyRelated2020A + valueCompanyRelated2020B
            #valueCompanyField2018_Prodi = valueCompanyField2018A_Prodi.add(valueCompanyField2018B_Prodi, fill_value = 0 )
            #valueCompanyField2019_Prodi = valueCompanyField2019A_Prodi.add(valueCompanyField2019B_Prodi, fill_value = 0 )
            #valueCompanyField2020_Prodi = valueCompanyField2020A_Prodi.add(valueCompanyField2020B_Prodi, fill_value = 0 )

            valueCompanyRelated2021 = self.__filter_company_related_study(dfCompanyRelated2021_Prodi["Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"].value_counts(
            ).sort_index())
            valueCompanyRelated2022 = self.__filter_company_related_study(dfCompanyRelated2022_Prodi["Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"].value_counts(
            ).sort_index())

            self.valueCompanyRelated = np.array([valueCompanyRelated2018,valueCompanyRelated2019,valueCompanyRelated2020, valueCompanyRelated2021, valueCompanyRelated2022])

        elif status == "Wirausaha":
            dfCompanyRelated2018_rawC = self.df2018[[
                "4. Program Studi", "C14. Apakah pekerjaan/usaha Anda saat ini sesuai dengan bidang kuliah?"]]
            dfCompanyRelated2018C = dfCompanyRelated2018_rawC.dropna(
                subset=["C14. Apakah pekerjaan/usaha Anda saat ini sesuai dengan bidang kuliah?"])
            
            dfCompanyRelated2019_rawC = self.df2019[[
                "4. Program Studi", "C13. Apakah pekerjaan/usaha Anda saat ini sesuai dengan bidang kuliah?"]]
            dfCompanyRelated2019C = dfCompanyRelated2019_rawC.dropna(
                subset=["C13. Apakah pekerjaan/usaha Anda saat ini sesuai dengan bidang kuliah?"])

            dfCompanyRelated2020_rawC = self.df2020[[
                "4. Program Studi", "C13. Apakah pekerjaan/usaha Anda saat ini sesuai dengan bidang kuliah?"]]
            dfCompanyRelated2020C = dfCompanyRelated2020_rawC.dropna(
                subset=["C13. Apakah pekerjaan/usaha Anda saat ini sesuai dengan bidang kuliah?"])
            
            dfCompanyRelated2021_raw = self.df2021[[
                "Program Studi", "Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"]]
            dfCompanyRelated2021 = dfCompanyRelated2021_raw.dropna(
                subset=["Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"])

            dfCompanyRelated2022_raw = self.df2022[[
                "Program Studi", "Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"]]
            dfCompanyRelated2022 = dfCompanyRelated2022_raw.dropna(
                subset=["Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"])

            dfCompanyRelated2018_Prodi = dfCompanyRelated2018C[dfCompanyRelated2018C["4. Program Studi"] == self.prodi]
            dfCompanyRelated2019_Prodi = dfCompanyRelated2019C[dfCompanyRelated2019C["4. Program Studi"] == self.prodi]
            dfCompanyRelated2020_Prodi = dfCompanyRelated2020C[dfCompanyRelated2020C["4. Program Studi"] == self.prodi]
            dfCompanyRelated2021_Prodi = dfCompanyRelated2021[dfCompanyRelated2021["Program Studi"] == self.prodi]
            dfCompanyRelated2022_Prodi = dfCompanyRelated2022[dfCompanyRelated2022["Program Studi"] == self.prodi]

            valueCompanyRelated2018 = self.__filter_company_related_study(dfCompanyRelated2018_Prodi["C14. Apakah pekerjaan/usaha Anda saat ini sesuai dengan bidang kuliah?"].value_counts().sort_index())
            valueCompanyRelated2019 = self.__filter_company_related_study(dfCompanyRelated2019_Prodi["C13. Apakah pekerjaan/usaha Anda saat ini sesuai dengan bidang kuliah?"].value_counts().sort_index())
            valueCompanyRelated2020 = self.__filter_company_related_study(dfCompanyRelated2020_Prodi["C13. Apakah pekerjaan/usaha Anda saat ini sesuai dengan bidang kuliah?"].value_counts().sort_index())
            valueCompanyRelated2021 = self.__filter_company_related_study(dfCompanyRelated2021_Prodi["Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"].value_counts(
            ).sort_index())
            valueCompanyRelated2022 = self.__filter_company_related_study(dfCompanyRelated2022_Prodi["Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"].value_counts(
            ).sort_index())

            self.valueCompanyRelated = np.array([valueCompanyRelated2018,valueCompanyRelated2019,valueCompanyRelated2020, valueCompanyRelated2021, valueCompanyRelated2022])
        

        

class DataframeUserInitializer():
    def __init__(self, dfUser2018, dfUser2019, dfUser2020, dfUser2021, dfUser2022, prodi):
        self.dfUser2018 = dfUser2018
        self.dfUser2019 = dfUser2019
        self.dfUser2020 = dfUser2020
        self.dfUser2021 = dfUser2021
        self.dfUser2022 = dfUser2022
        self.prodi = prodi

    def cleanse_user_data(self):

        self.dfUser2018_Kepuasan = self.dfUser2018.iloc[:, 6:29]
        self.dfUser2018_Kepentingan = self.dfUser2018.iloc[:, 29:53]

        # Replace - data with null values
        self.dfUser2018_Kepentingan.replace('-', np.nan, inplace=True)
        self.dfUser2018_Kepuasan.replace('-', np.nan, inplace=True)

        # Fill Null Data if contains null values, filling with mean values
        self.dfUser2018_Kepuasan.fillna(
            self.dfUser2018_Kepuasan.mean(), inplace=True)
        self.dfUser2018_Kepentingan.fillna(
            self.dfUser2018_Kepentingan.mean(), inplace=True)

        self.dfUser2019_Kepuasan = self.dfUser2019.iloc[:, 7:30]
        self.dfUser2019_Kepentingan = self.dfUser2019.iloc[:, 30:54]

        # Replace - data with null values
        self.dfUser2019_Kepentingan.replace('-', np.nan, inplace=True)
        self.dfUser2019_Kepuasan.replace('-', np.nan, inplace=True)

        # Fill Null Data if contains null values, filling with mean values
        self.dfUser2019_Kepuasan.fillna(
            self.dfUser2019_Kepuasan.mean(), inplace=True)
        self.dfUser2019_Kepentingan.fillna(
            self.dfUser2019_Kepentingan.mean(), inplace=True)

        dfUser2020_Dropped = self.dfUser2020.dropna()
        self.dfUser2020_Kepuasan = dfUser2020_Dropped.iloc[:, 6:29]
        self.dfUser2020_Kepentingan = dfUser2020_Dropped.iloc[:, 29:53]

        # Filter Electrical Engineering
        # dfUser2021_EL = dfUser2021[dfUser2021["Program Studi"]=="Teknik Elektro"]
        # # dfUser2021_EL
        # If User (Labelled by 1 in Staff Column), Save to Importance Data Data
        # dfUser2021_EL_Kepentingan = dfUser2021_EL[dfUser2021_EL["Staff"]==1] # N=
        # dfUser2021_EL_KepentinganF=dfUser2021_EL_Kepentingan.iloc[:,6:29]

        # # If Students (Labelled by Name in Staff Column), Save to Satisfaction Data
        # dfUser2021_EL_Kepuasan = dfUser2021_EL[dfUser2021_EL["Staff"]!=1]
        # dfUser2021_EL_KepuasanF = dfUser2021_EL_Kepuasan.iloc[:,29:53]
        dfUser2021_Dropped = self.dfUser2021.dropna()
        self.dfUser2021_Kepentingan = dfUser2021_Dropped.iloc[:, 6:29]
        self.dfUser2021_Kepuasan = dfUser2021_Dropped.iloc[:, 29:53]

        # Fill Null Data if contains null values, filling with mean values
        self.dfUser2021_Kepuasan.fillna(
            self.dfUser2021_Kepuasan.mean(), inplace=True)
        self.dfUser2021_Kepentingan.fillna(
            self.dfUser2021_Kepentingan.mean(), inplace=True)

        dfUser2022_Dropped = self.dfUser2022.dropna()
        self.dfUser2022_Kepentingan = dfUser2022_Dropped.iloc[:, 6:29]
        self.dfUser2022_Kepuasan = dfUser2022_Dropped.iloc[:, 29:53]

        # Fill Null Data if contains null values, filling with mean values
        self.dfUser2022_Kepuasan.fillna(
            self.dfUser2022_Kepuasan.mean(), inplace=True)
        self.dfUser2022_Kepentingan.fillna(
            self.dfUser2022_Kepentingan.mean(), inplace=True)

    def init_competence_data(self):

        self.competencies2018 = ['memecahkan\nmasalah\nkompleks', 'berpikir\nkritis', 'inovasi\ndan/atau\nkreativitas', 'manajemen diri\ndan orang lain',
                                 'bekerja\ntim', 'bekerja\nindividu', 'kecerdasan\nemosional', 'penilaian dan\npengambilan\nkeputusan',
                                 'negosiasi', 'kecerdasan\ndalam\nbertindak', 'kemampuan\nbelajar', 'adaptasi\ndengan\nlingkungan',
                                 'kejujuran\n,loyalitas\n,integritas', 'bekerja dalam\ntekanan', 'etika',
                                 'pengetahuan\n dan penerapan\nbidang/disiplin\nilmu', 'pengetahuan\ndi luar \nbidang/displin\nilmu',
                                 'kemampuan\nanalisis', 'kemampuan \nadministrasi,\nmenuliskan\nlaporan\ndokumen', 'keterampilan\nteknologi\ninformasi dan\nkomunikasi',
                                 'merancang dan atau\nmendesain suatu\nkomponen,sistem\natau proses', 'berkomunikasi\ndengan\nbahasa asing', 'orientasi\nlayanan'
                                 ]

        self.competencies2019 = ['memecahkan\nmasalah\nkompleks', 'berpikir\nkritis', 'inovasi\ndan/atau\nkreativitas', 'manajemen diri\ndan orang lain',
                                 'bekerja\ntim', 'bekerja\nindividu', 'kecerdasan\nemosional', 'penilaian dan\npengambilan\nkeputusan',
                                 'negosiasi', 'kecerdasan\ndalam\nbertindak', 'kemampuan\nbelajar\nsepanjang\nhayat', 'adaptasi\ndengan\nlingkungan',
                                 'kejujuran\n,loyalitas\ndan integritas', 'bekerja dalam\ntekanan', 'etika dan\ntanggung jawab\nkeprofesian', 'kemampuan\nberkomunikasi',
                                 'pengetahuan\n dan penerapan\nbidang/disiplin\nilmu', 'pengetahuan\ndi luar \nbidang/displin\nilmu',
                                 'kemampuan\nanalisis dan\ninterpretasi data', 'kemampuan \nadministrasi,\nmenuliskan\nlaporan\ndokumen', 'keterampilan\nmenggunakan\nteknologi\ninformasi',
                                 'merancang\ndan atau\nmendesain suatu\nkomponen,sistem\natau\nproses', 'kemampuan\nbahasa\nasing'
                                 ]

        self.competencies2020 = self.competencies2019
        self.competencies2021 = self.competencies2019
        self.competencies2022 = self.competencies2019

        self.dfUser2018_Kepuasan_Prodi = self.dfUser2018_Kepuasan[
            self.dfUser2018['Prodi'] == self.prodi]

        self.dfUser2018_Kepentingan_Prodi = self.dfUser2018_Kepentingan[
            self.dfUser2018['Prodi'] == self.prodi]

        # self.dfUser2018_Kepuasan_Prodi_N = self.dfUser2018_Kepuasan_Prodi
        # self.dfUser2018_Kepentingan_Prodi_N = self.dfUser2018_Kepentingan_Prodi

        # current_indices = self.dfUser2018_Kepuasan_Prodi.columns.tolist() #check column

        # 2018 dataframe order should be changed as for column orientasi layanan and bekerja individu is changed in the format
        # new_indices = [0,1,2,3,4,11,5,6,8,9,10,12,13,14,15,16,17,18,19,20,21,22,7]
        # self.dfUser2018_Kepuasan_Prodi= self.dfUser2018_Kepuasan_Prodi.iloc[:,new_indices]
        # self.dfUser2018_Kepentingan_Prodi= self.dfUser2018_Kepentingan_Prodi.iloc[:,new_indices]

        """
        2019-2022 -> Competences Order Is Same as Raw Data
        """
        self.dfUser2019_Kepuasan_Prodi = self.dfUser2019_Kepuasan[
            self.dfUser2019['Program Studi'] == self.prodi]
        self.dfUser2019_Kepentingan_Prodi = self.dfUser2019_Kepentingan[
            self.dfUser2019['Program Studi'] == self.prodi]

        self.dfUser2020_Kepuasan_Prodi = self.dfUser2020_Kepuasan[
            self.dfUser2020['Program Studi'] == self.prodi]
        self.dfUser2020_Kepentingan_Prodi = self.dfUser2020_Kepentingan[
            self.dfUser2020['Program Studi'] == self.prodi]

        self.dfUser2021_Kepuasan_Prodi = self.dfUser2021_Kepuasan[
            self.dfUser2021['Program Studi'] == self.prodi]
        self.dfUser2021_Kepentingan_Prodi = self.dfUser2021_Kepentingan[
            self.dfUser2021['Program Studi'] == self.prodi]

        self.dfUser2022_Kepuasan_Prodi = self.dfUser2022_Kepuasan[
            self.dfUser2022['Program Studi'] == self.prodi]
        self.dfUser2022_Kepentingan_Prodi = self.dfUser2022_Kepentingan[
            self.dfUser2022['Program Studi'] == self.prodi]

        print("Dijalankan")        

      
