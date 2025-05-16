import streamlit as st
import re

def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    # Remarks based on strength
    if strength == 5:
        remarks = "Very Strong 💪"
    elif strength >= 4:
        remarks = "Strong 👍"
    elif strength >= 3:
        remarks = "Moderate 🙂"
    elif strength >= 2:
        remarks = "Weak 😕"
    else:
        remarks = "Very Weak 🚫"

    return remarks

# Streamlit App
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password:")

if password:
    result = check_password_strength(password)
    st.success(f"Password Strength: {result}")

