import streamlit as st

st.title("Streamlit text input")

name=st.text_input("Enter your name")

age=st.slider("Selct your age",0,100,25)
st.write(f"Your age is {age}")

options=['python','java','c++','javascript']
choice=st.selectbox("Select your language",options=options)
st.write(f"You Selected {choice}")

if name:
    st.write(f"Hello, {name}!")