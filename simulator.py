print("=== Cyber Awareness Training Simulator ===")
print()

print("Scenario:")
print("You receive an email saying:")
print("'Your bank account is compromised! Click this link immediately.'")
print()

print("What should you do?")
print("1. Click the link")
print("2. Report the email as phishing")
print()

choice = input("Enter your choice (1 or 2): ")

print()

if choice == "2":
    print("✅ Correct!")
    print("This is a phishing attempt. Reporting it keeps you safe.")
elif choice == "1":
    print("❌ Wrong!")
    print("Clicking unknown links can steal your data.")
else:
    print("⚠️ Invalid input. Please choose 1 or 2.")
