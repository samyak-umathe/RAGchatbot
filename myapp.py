import streamlit as st
import re

st.title("Login System")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

def login():
    username = st.session_state.username
    password = st.session_state.password
    email = st.session_state.email
    gender = st.session_state.gender
    phone = st.session_state.phone

    if not validate_email(email):
        st.error("Invalid email format")
        return
    
    if not phone.isdigit() or len(phone) < 7:
        st.error("Invalid phone number")
        return

    if username == "admin" and password == "1234":
        st.session_state.logged_in = True
        st.session_state.user_data = {
            "Username": username,
            "Email": email,
            "Gender": gender,
            "Phone": phone
        }
    else:
        st.error("Invalid credentials")

def logout():
    st.session_state.logged_in = False
    if "user_data" in st.session_state:
        del st.session_state.user_data

if not st.session_state.logged_in:
    st.text_input("Username", key="username")
    st.text_input("Password", type="password", key="password")
    st.text_input("Email", key="email")
    st.selectbox("Gender", ["Male", "Female", "Other"], key="gender")
    st.text_input("Phone Number", key="phone")
    st.button("Login", on_click=login)
else:
    st.success("Welcome! You are logged in.")
    
    st.subheader("User Details")
    for key, value in st.session_state.user_data.items():
        st.write(f"**{key}:** {value}")
    
    st.button("Logout", on_click=logout)