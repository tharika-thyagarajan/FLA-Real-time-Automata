# EMAIL FORMAT VALIDATOR USING DFA

def email_dfa(email):
    state = "Q0"

    for char in email:
        if char.isascii() and char.isalpha():
            symbol = "L"
        elif char.isascii() and char.isdigit():
            symbol = "D"
        elif char == "@":
            symbol = "@"
        elif char == ".":
            symbol = "."
        else:
            symbol = "X"

        if state == "Q0":
            if symbol in ["L", "D"]:
                state = "Q1"
            else:
                state = "Qdead"

        elif state == "Q1":
            if symbol in ["L", "D"]:
                state = "Q1"
            elif symbol == "@":
                state = "Q2"
            else:
                state = "Qdead"

        elif state == "Q2":
            if symbol in ["L", "D"]:
                state = "Q3"
            else:
                state = "Qdead"

        elif state == "Q3":
            if symbol in ["L", "D"]:
                state = "Q3"
            elif symbol == ".":
                state = "Q4"
            else:
                state = "Qdead"

        elif state == "Q4":
            if symbol == "L":
                state = "Q4"
            else:
                state = "Qdead"

        else:
            state = "Qdead"

    return state == "Q4"


def run_email():
    print("\n===== EMAIL FORMAT VALIDATOR =====")
    print("Format: username@domain.extension")

    email = input("\nEnter your email ID: ")

    if email_dfa(email):
        print("\nRESULT: ACCEPTED")
        print("Email satisfies the DFA rules.")
    else:
        print("\nRESULT: REJECTED")
        print("Email does not satisfy the DFA rules.")


def test_email():
    accepted = [
        "abc@gmail.com",
        "user123@yahoo.com",
        "hello@outlook.in",
        "student@srm.edu",
        "test123@google.org"
    ]

    rejected = [
        "@gmail.com",
        "abc@gmail",
        "abc@@gmail.com",
        "abc@.com",
        "abc gmail.com"
    ]

    print("\nEMAIL DFA TEST RESULTS")

    for email in accepted:
        print(email, ":", "Accepted" if email_dfa(email) else "FAILED")

    for email in rejected:
        print(email, ":", "Rejected" if not email_dfa(email) else "FAILED")