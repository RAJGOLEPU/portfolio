import streamlit as st
from utils.db import get_engine
import pandas as pd

st.title("📦 SQL Database Example")

engine = get_engine()

if st.button("Insert Test Record"):
    with engine.connect() as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, note TEXT);")
        conn.execute("INSERT INTO test_table (note) VALUES ('Hello from Streamlit');")
        st.success("Inserted test record.")

if st.button("Fetch Records"):
    df = pd.read_sql("SELECT * FROM test_table;", engine)
    st.dataframe(df)
