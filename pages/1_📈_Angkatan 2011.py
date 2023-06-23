import streamlit as st
from grapher import GrapherTracer, GrapherUser


st.title("Angkatan 2011")

# st.write("Data Angkatan Tahun 2011 (Tahun Survey 2018)", st.session_state["Fakultas"], "Prodi", st.session_state["Jurusan"])

gt = GrapherTracer(st.session_state["df2018"], 
                   st.session_state["df2019"], 
                   st.session_state["df2020"], 
                   st.session_state["df2021"], 
                   st.session_state["df2022"], 
                   st.session_state["Jurusan"])

gt.cleanse_tracer_data()
gt.init_competence_data()
gt.draw_competence_data(year=2018)