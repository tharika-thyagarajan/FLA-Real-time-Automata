# PASSWORD VERIFICATION SYSTEM USING DFA

def password_dfa(password):
    state = "Q0"

    for char in password:
        if char.isascii() and char.isalpha():
            symbol = "L"
        elif char.isascii() and char.isdigit():
            symbol = "D"
        else:
            symbol = "X"

        if state == "Q0":
            if symbol == "L":
                state = "Q1"
            else:
                state = "Qdead"

        elif state == "Q1":
            if symbol == "L":
                state = "Q1"
            elif symbol == "D":
                state = "Q2"
            else:
                state = "Qdead"

        elif state == "Q2":
            if symbol == "L":
                state = "Q1"
            elif symbol == "D":
                state = "Q2"
            else:
                state = "Qdead"

        else:
            state = "Qdead"

    return state == "Q2"


def run_password():
    print("\n===== PASSWORD VERIFICATION SYSTEM =====")
    print("Rules: Start with a letter, use only letters")
    print("and digits, and end with a digit.")

    password = input("\nEnter your password: ")

    if password_dfa(password):
        print("\nRESULT: ACCEPTED")
        print("Password satisfies the DFA rules.")
    else:
        print("\nRESULT: REJECTED")
        print("Password does not satisfy the DFA rules.")


def test_password():
    accepted = ["Hello5", "ABC123", "A1", "Python9", "Z0"]
    rejected = ["123ABC", "@abc1", "A", "Abc", "Ab@123"]

    print("\nPASSWORD DFA TEST RESULTS")

    for pwd in accepted:
        print(pwd, ":", "Accepted" if password_dfa(pwd) else "FAILED")

    for pwd in rejected:
        print(pwd, ":", "Rejected" if not password_dfa(pwd) else "FAILED")