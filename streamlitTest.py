import streamlit as st

st.title("RedHammer File Renaming Tool")
st.write("Please fill out the information below.")

#Create the form container
with st.form(key="file_info_form"):
    #Add input widgets inside the form
    uploaded_file = st.file_uploader("Upload File", type=["pdf", "docx", "xlsx"])
    invNum = st.text_input("Supplier Invoice Number")
    jobRef = st.text_input("Job Reference Number")
    date = st.date_input("Date of Invoice")
    
    submit_button = st.form_submit_button(label="Submit Form")

if submit_button:
    #format date variable
    formatted_date = date.strftime("%y%m%d")
    st.write(f"Inv_{invNum}_{jobRef}_{formatted_date}")
    