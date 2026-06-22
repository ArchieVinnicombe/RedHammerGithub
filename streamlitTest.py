import streamlit as st

st.title("RedHammer File Renaming Tool")
st.write("Please fill out the information below.")

#Create the form container
with st.form(key="file_info_form"):
    
    #Add input widgets inside the form
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=18, max_value=100, value=25)
    role = st.selectbox("Job Role", ["Developer", "Data Scientist", "Manager", "Other"])
    
    submit_button = st.form_submit_button(label="Submit Form")

#Handle the action outside or after the form block
##if submit_button:
    