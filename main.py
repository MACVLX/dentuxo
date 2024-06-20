import streamlit as st
from driver import read_query




st.title("DENTUXO")

st.write(read_query('MATCH (cat:Treatment {code: $code}) RETURN cat',params={'code':'HBGD475'}))
