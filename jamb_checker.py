# JAMB REGISTRATION SYSTEM 2026
# Structured Version

def collect_candidate_data():
    print("=== JAMB REGISTRATION SYSTEM ===")

    name = input("Enter your full name: ")
    age = int(input("Enter your age: "))
    e_mail = input("Enter your E-mail: ")
    e_pin = input("Do you have E-PIN? (yes/no): ").lower()
    nin = input("Enter your NIN: ")
    profile_code = input("Enter your Profile code: ")
    waec = input("Do you have O'level result? (yes/no): ").lower()

    return name, age, e_mail, e_pin, nin, profile_code, waec


def validate_candidate(name, age, e_mail, e_pin, nin, profile_code, waec):

    if name.strip() == "":
        return "Name cannot be empty"

    if age < 17:
        return "Not eligible: Age below 17"

    if age > 60:
        return "Invalid age: Above 60 not allowed"
   
    if e_mail.strip() == "":
        return "E-mail cannot be empty"

    if e_pin != "yes":
        return "E-PIN not provided"

    if len(nin) != 11:
        return "Invalid NIN"

    if len(profile_code) != 12:
        return "Invalid Profile code"

    if waec != "yes":
        return "O'level result required"

    return "Eligible"


def display_result(name, result):
    print("\n=== REGISTRATION STATUS ===")

    if result == "Eligible":
        print("Candidate:", name)
        print("Status: ✅ Eligible")
    else:
        print("Candidate:", name)
        print("Status: ❌", result)


def main():
    name, age, e_mail, e_pin, nin, profile_code, waec = collect_candidate_data()
    result = validate_candidate(name, age, e_mail, e_pin, nin, profile_code, waec)
    display_result(name, result)


# Run the program
main()
