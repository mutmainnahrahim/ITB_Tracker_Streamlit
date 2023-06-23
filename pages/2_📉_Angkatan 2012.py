import streamlit as st

#title
st.title("Angkatan 2012")

st.write("Data Angkatan Tahun 2012 (Tahun Survey 2019)", st.session_state["Fakultas"], "Prodi", st.session_state["Jurusan"])


gt.cleanse_tracer_data()
gt.init_competence_data()
gt.draw_competence_data(year=2019)

