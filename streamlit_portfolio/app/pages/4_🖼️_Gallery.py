import streamlit as st

st.title("🖼️ Project Gallery")

projects = [
    {"name": "ML Demo", "page": "📊 ML Demo"},
    {"name": "SQL DB Example", "page": "🗃️ SQL DB"},
]

for project in projects:
    if st.button(project["name"]):
        st.switch_page(f"pages/{project['page']}.py")
