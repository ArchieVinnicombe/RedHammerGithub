import streamlit as st

st.title("RedHammer File Renaming Tool")
st.write("Please fill out the information below.")

#Create the form container
with st.form(key="file_info_form"):
    
    #Add input widgets inside the form
    invNum = st.text_input("Supplier Invoice Number")
    jobRef = st.text_input("Job Reference Number")
    date = st.date_input("Date of Invoice")
    
    submit_button = st.form_submit_button(label="Submit Form")

if submit_button:
    #format date variable
    date = date[2].replace('-', '')

    st.write("Form submitted successfully!")
    st.write(f"Supplier Invoice Number: {invNum}")
    st.write(f"Job Reference Number: {jobRef}")
    st.write(f"Date of Invoice: {date} ")
    