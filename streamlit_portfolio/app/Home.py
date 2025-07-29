import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="📁", layout="centered")

st.title("👋 Welcome to My Data Science Portfolio")

st.markdown("""
Hi, I'm **Raj Kumar Golepu**. I'm passionate about data, machine learning, and real-world problem-solving.

Choose a project below to explore:
""")

col1, col2 = st.columns(2)

with col1:
    if st.button("🌸 ML Demo"):
        st.switch_page("pages/1_📊_ML_Demo.py")

with col2:
    if st.button("🗃️ SQL DB Example"):
        st.switch_page("pages/2_🗃️_SQL_DB.py")

st.markdown("---\nMade with ❤️ using Streamlit")
