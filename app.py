import streamlit as st

# Page Title
st.title("Voting Eligibility Checker 🗳️")

# Inputs
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=120, value=18)

# State Dropdown
state = st.selectbox(
    "Select your State:",
    ["Uttarakhand (UK)", "Uttar Pradesh (UP)", "Madhya Pradesh (MP)"]
)

# Button to check
if st.button("Check Eligibility"):
    if name.strip() == "":
        st.warning("Please enter your name first!")
    elif age >= 18:
        st.success(f"🎉 Congratulations {name}! You are eligible to vote.")
        st.balloons()
        
        st.markdown("---")
        st.subheader("📌 Government Info:")
        
        # Display CM based on selected state
        if "Uttarakhand" in state:
            st.info(" Uttarakhand CM: **Dhruv**")
        elif "Uttar Pradesh" in state:
            st.info(" Uttar Pradesh CM: **Dilip**")
        elif "Madhya Pradesh" in state:
            st.info(" Madhya Pradesh CM: **Akash**")
            
        # Display PM
        st.info(" Prime Minister of India: **Narendra Modi (BJP)**")
        
    else:
        st.error(f" Sorry {name}, you are not eligible to vote yet. You need to be 18 or older.")

      
