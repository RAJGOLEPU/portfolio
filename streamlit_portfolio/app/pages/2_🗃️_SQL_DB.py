import streamlit as st
import pandas as pd
import sys, os

# Fix Python path to import from utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from app.utils.db import get_engine
from sqlalchemy import text

st.title("🗃️ SQLite Database Example")

engine = get_engine()

# --- Input field ---
user_note = st.text_input("Enter a message to save into the database:")

# --- Insert into database ---
if st.button("Insert Record"):
    if user_note.strip() == "":
        st.warning("Please enter some text before inserting.")
    else:
        with engine.begin() as conn:
            conn.execute(text("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, note TEXT);"))
            conn.execute(text("INSERT INTO messages (note) VALUES (:note);"), {"note": user_note})
            st.success("Your message has been saved!")

# --- Fetch and show records ---
if st.button("Fetch Records"):
    with engine.connect() as conn:
        result = pd.read_sql("SELECT * FROM messages;", conn)
        st.dataframe(result)
