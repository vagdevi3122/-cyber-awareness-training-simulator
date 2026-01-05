print("Cyber Awareness Training Simulator")

print("1. Phishing Awareness")
print("2. Password Safety")
print("3. Safe Internet Practices")

choice = input("Enter your choice: ")

if choice == "1":
    print("Do not click on unknown links or emails.")
elif choice == "2":
    print("Use strong passwords with symbols, numbers, and uppercase letters.")
elif choice == "3":
    print("Avoid sharing personal information on untrusted websites.")
else:
    print("Invalid choice. Please try again.")
score = 0

print("Cyber Security Quiz")

print("Q1: Is it safe to share OTP with anyone?")
ans = input("Yes / No: ")

if ans.lower() == "no":
    print("Correct!")
    score += 1
else:
    print("Wrong! Never share OTP.")

print("Your score:", score)
password = input("Enter your password: ")

if len(password) >= 8:
    print("Good length password")
else:
    print("Password too short")

if any(char.isdigit() for char in password):
    print("Contains number")
else:
    print("Add numbers to strengthen password")
import streamlit as st

st.title("Cyber Awareness Training Simulator")

option = st.selectbox(
    "Choose a topic",
    ("Phishing", "Password Safety", "Safe Browsing")
)

if option == "Phishing":
    st.warning("Never click suspicious links.")
elif option == "Password Safety":
    st.success("Use strong passwords with symbols.")
else:
    st.info("Avoid public Wi-Fi for sensitive work.")
