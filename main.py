import streamlit as st
from driver import read_query




st.title("DENTUXO")

st.write(read_query('MATCH (cat:Treatment {code: $code}) RETURN cat',params={'code':'HBGD475'}))

st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
# st.markdown("![Alt Text](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNG9uMm5kOWVrbnpjZHF3NXNjNGNvYnozbGhuOXJtdHBnOGF0OTZmNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qmoggo2eQMYY8/giphy.gif")
