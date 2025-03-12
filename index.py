import streamlit as st
import re
import string
import random

# Set the page config
st.set_page_config("ShieldPass: Secure Password Analyzer", page_icon="🛡️", layout="wide")

# Import custom css file
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Set the page title
st.title("🛡️ ShieldPass: Secure Password Analyzer")

st.subheader(
    "Shield Your Digital Life: Analyze, Optimize, and Strengthen Your Passwords for Smarter Security. 🔐✨"
)

# Sidebar with password tips
st.sidebar.title("⚡ Craft an Unbreakable Password!")

st.sidebar.subheader("Boost your digital security with these power-packed tips:")

st.sidebar.markdown(
    """  
🟢 **Make it Long:** Use at least **8+ characters** for enhanced security.  
🔠 **Mix Upper & Lowercase Letters:** Strengthen your password with a variety of letters.  
🔢 **Include Numbers:** Add **digits (0-9)** to increase complexity.  
💢 **Use Special Characters:** Symbols like [**! @ # * $ % ^ &**] make your password harder to crack.  
🚫 **Avoid Predictability:** Create a unique password that's hard to guess.
"""
)

st.sidebar.markdown("---")


# Function to generate a strong password
def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(12))


# initialize session state for password
if "password" not in st.session_state:
    st.session_state.password = ""

# Auto generate password button
if st.sidebar.button("🔄 Auto-Generate Password"):
    st.session_state.password = generate_strong_password()
    st.sidebar.success(f"✅ Generated Password: {st.session_state.password}")

# Set the password input
password = st.text_input(
    "Enter your password:", type="password", value=st.session_state.password
)

# Common passwords
common_passwords = [
    "password",
    "123456",
    "qwerty",
    "admin",
    "user",
    "test",
    "password123",
    "12345678",
    "123456789",
    "1234567890",
    "welcome",
    "hello",
]


# Function to check password strength
def check_password_strength(password):

    score = 0
    feedback = []

    # Check common passwords
    if password in common_passwords:
        feedback.append("❌ This password is too common! Choose a unique one.")

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append(
            "❌ Password is too short! It should be at least 8 characters long."
        )

    # Check uppercase and lowercase
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append(
            "❌ Password should contain both uppercase and lowercase letters."
        )

    # Check for digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")

    # Check for special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character.")

    return score, feedback


# Function to get progress bar color based on score
def get_progress_color(score):
    if score == 4:
        return "green"
    elif score == 3:
        return "yellow"
    else:
        return "red"


# Button to check password strength
if st.button("🔍 Check Password Strength"):
    if password:
        score, feedback = check_password_strength(password)

        # Convert score to percentage for progress bar
        strength_percentage = (score / 4) * 100
        progress_color = get_progress_color(score)

        st.header("🔒 Password Strength Analysis")

        # Custom color-coded progress bar 📊
        st.markdown(
            f"""
            <div style="width: {strength_percentage}%; background-color: {progress_color}; height: 7px; border-radius: 5px;"></div>
                """,
            unsafe_allow_html=True,
        )

        if score == 4:
            st.success(
                "✅ Strong Password! Your password is secure and meets all recommended criteria."
            )
        elif score >= 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features")
        else:
            st.error("❌ Weak Password - Improve it following the guidelines below")

        if feedback:
            st.subheader("💡Improvement Suggestions")
            for msg in feedback:
                st.markdown(
                    f"<div class='feedback-msg'>- {msg}</div>", unsafe_allow_html=True
                )
    else:
        st.warning("Please enter a password to check its strength.")

# Footer
st.markdown("---")
st.write("Made with ❤️ by Amna Shafiq")
