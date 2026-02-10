# JAMB Registry Checker 2026

print("=== JAMB REGISTRATION SYSTEM ===")

name = input("Enter your full name: ")

age = int(input("Enter your age: "))

e_pin = input("Enter your E-PIN (yes/no): ").lower()

profile_code = input("Enter your profile code: ")

marital_status = input("Enter your marital status: ")

gsm = input("Enter your mobile number: ")

state = input("Enter your state: ")

email = input("Enter your email address: ")

nin = input("Enter your NIN: ")

waec = input("Do you have O'level result? (yes/no): ").lower()

# ---- VALIDATION LOGIC ----

if age < 17:
    print("❌ Not eligible: Age below 17")

elif len(nin) != 11:
    print("❌ Invalid NIN")

elif e_pin != "yes":
    print("❌ E-PIN not provided")

elif waec != "yes":
    print("❌ O'level result required")

else:
    print("✅ Candidate Eligible")
    print("Processing registration for", name)
