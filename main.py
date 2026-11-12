# FLA TASK 2
# DESIGNING AUTOMATA FOR REAL-TIME APPLICATIONS

from password_verification import run_password, test_password
from email_validator import run_email, test_email
from atm_pin_verification import run_atm, test_atm


def main():

    while True:

        print("\n" + "=" * 50)
        print("   REAL-TIME APPLICATIONS USING FINITE AUTOMATA")
        print("=" * 50)

        print("\n1. Password Verification System")
        print("2. Email Format Validator")
        print("3. ATM PIN Verification System")
        print("4. Run All DFA Test Cases")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            run_password()

        elif choice == "2":
            run_email()

        elif choice == "3":
            run_atm()

        elif choice == "4":
            test_password()
            test_email()
            test_atm()
            print("\nAll DFA test cases completed.")

        elif choice == "5":
            print("\nThank you for using our DFA application!")
            break

        else:
            print("\nInvalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()