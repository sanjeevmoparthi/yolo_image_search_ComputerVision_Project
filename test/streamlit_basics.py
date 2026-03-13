# python streamlit_basics.py Not Done .
# streamlit run test/streamlit_basics.py


import streamlit as st

# Basic element 
st.title("Streamlit Intro")
st.write("This is Where we will learn Streamlit")


# Getting User Input 
name = st.text_input("What's your name?")
if name:
    st.write(f"Welcome,{name} ! Ready to Build Something amazing")

# More interactive Elements
age = st.slider("Your age",0,100)
gender = st.radio("Gender",("Male","Female","other"))
interest = st.selectbox("Interested in",("CV","ML","Both"))

if st.button("Create profile"):
    st.write(f"Age: {age}, Gender : {gender},Interest :{interest}")

# Save user profile without session_state 

# all_profile = []
# new_profile = {"Name":name,
#                 "Age": age,
#                "Gender": gender,
#                "Interest": interest}

# all_profile.append(new_profile)

# if st.button("Show All Profile"):
#     st.write(all_profile)

# Reruns the whole page from top to bottom
# all the variables gets initialized again
# a.py --> a = 0, b = 0
# a+=1, b+= 1 
# print(a,b) --> python a.py: a = 1,b = 1 
# python a.py : a = 1 , b  =  1 


# because streamlit retials value of widget we see the previous value
# instead of python native variables we should use streamlit session_state 
# session_state is like a dictionary.
# Solution 
if "profiles" not in st.session_state:
    st.session_state.profiles = []

new_profile = {"Name": name,
               "Age":age,
               "Gender": gender,
               "Interest":interest}
if st.button("Save and Show Profiles"):
    st.session_state.profiles.append(new_profile)
    st.write(f"All Profiles : ",st.session_state.profiles)
