# ATM PIN VERIFICATION SYSTEM USING DFA

def atm_pin_dfa(pin):
    state = "Q0"

    for char in pin:
        if '0' <= char <= '9':
            if state == "Q0":
                state = "Q1"
            elif state == "Q1":
                state = "Q2"
            elif state == "Q2":
                state = "Q3"
            elif state == "Q3":
                state = "Q4"
            else:
                state = "Qdead"
        else:
            state = "Qdead"

    return state == "Q4"


def run_atm():
    print("\n===== ATM PIN VERIFICATION SYSTEM =====")
    print("Enter exactly four numeric digits.")

    pin = input("\nEnter your ATM PIN: ")

    print("PIN:", "*" * len(pin))

    if atm_pin_dfa(pin):
        print("\nRESULT: ACCEPTED")
        print("PIN satisfies the DFA rules.")
    else:
        print("\nRESULT: REJECTED")
        print("PIN must contain exactly four digits.")


def test_atm():
    accepted = ["1234", "5678", "9087", "2468", "1357"]
    rejected = ["123", "12345", "12AB", "1@34", "123456"]

    print("\nATM PIN DFA TEST RESULTS")

    for pin in accepted:
        print(pin, ":", "Accepted" if atm_pin_dfa(pin) else "FAILED")

    for pin in rejected:
        print(pin, ":", "Rejected" if not atm_pin_dfa(pin) else "FAILED")