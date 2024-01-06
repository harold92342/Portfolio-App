import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Timothée Kabwe")
    content = """
    Hi, I am Timothy Kabwe, a systems and Network Administration Engineer from Salama
    Higher Institute of Computer Science(ESISALAMA - DON BOSCO University, Democratic Republic of Congo).
    Python is my programming language of choice, and I'm fueled by a strong passion for data analysis.
    Presently, I'm immersed in the dynamic world of IT as an IT Support Technician at Kamoa Copper SA, part of the Ivanohemines Group. 
    My role involves providing robust technical support and solutions to ensure smooth operations.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me! 
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")





