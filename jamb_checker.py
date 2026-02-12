# JAMB REGISTRATION SYSTEM 2026
# Structured Version

def collect_candidate_data():
    print("=== JAMB REGISTRATION SYSTEM ===")

    name = input("Enter your full name: ")
    age = int(input("Enter your age: "))
    e_pin = input("Do you have E-PIN? (yes/no): ").lower()
    nin = input("Enter your NIN: ")
    waec = input("Do you have O'level result? (yes/no): ").lower()

    return name, age, e_pin, nin, waec


def validate_candidate(age, e_pin, nin, waec):
    if age < 17:
        return "Not eligible: Age below 17"

    if len(nin) != 11:
        return "Invalid NIN"

    if e_pin != "yes":
        return "E-PIN required"

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
    name, age, e_pin, nin, waec = collect_candidate_data()
    result = validate_candidate(age, e_pin, nin, waec)
    display_result(name, result)


# Run the program
main()
