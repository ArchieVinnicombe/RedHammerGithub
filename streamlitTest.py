import streamlit as st

st.title("User Onboarding Form")
st.write("Please fill out the information below.")

# 1. Create the form container
with st.form(key="user_info_form"):
    
    # 2. Add input widgets inside the form
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=18, max_value=100, value=25)
    role = st.selectbox("Job Role", ["Developer", "Data Scientist", "Manager", "Other"])
    
    # Toggle switch inside the form
    receive_updates = st.checkbox("Subscribe to newsletter")
    
    # 3. Every form MUST have a submit button inside the block
    submit_button = st.form_submit_button(label="Submit Form")

# 4. Handle the action outside or after the form block
if submit_button:
    if name:
        st.success(f"Thank you, {name}! Your information has been submitted.")
        
        # Display the collected data neatly using metrics or columns
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Selected Role", role)
        with col2:
            st.metric("Newsletter", "Subscribed" if receive_updates else "No")
    else:
        st.error("Please enter your name before submitting.")