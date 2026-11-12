import os

# Folder to save all DFA diagrams
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIAGRAM_DIR = os.path.join(BASE_DIR, "diagrams")
os.makedirs(DIAGRAM_DIR, exist_ok=True)


def create_svg(filename, title, description, nodes, edges):
    width, height = 1100, 650

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
    width="{width}" height="{height}" viewBox="0 0 {width} {height}">

    <defs>
      <marker id="arrow" markerWidth="10" markerHeight="10"
      refX="9" refY="3" orient="auto">
        <path d="M0,0 L0,6 L9,3 z" fill="#263746"/>
      </marker>
    </defs>

    <rect width="100%" height="100%" fill="white"/>
    <text x="550" y="48" text-anchor="middle"
    font-size="27" font-weight="bold" fill="#172B4D">{title}</text>

    <text x="550" y="82" text-anchor="middle"
    font-size="16" fill="#444">{description}</text>
    '''

    # Draw transitions
    for edge in edges:
        x1, y1, x2, y2, label = edge

        svg += f'''
        <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"
        stroke="#263746" stroke-width="2.5"
        marker-end="url(#arrow)"/>

        <text x="{(x1+x2)/2}" y="{(y1+y2)/2-12}"
        text-anchor="middle" font-size="16"
        fill="#C0392B">{label}</text>
        '''

    # Draw states
    for state in nodes:
        x, y, name, accepting = state

        svg += f'''
        <circle cx="{x}" cy="{y}" r="39"
        fill="#EAF2F8" stroke="#1F618D" stroke-width="3"/>
        '''

        if accepting:
            svg += f'''
            <circle cx="{x}" cy="{y}" r="33"
            fill="none" stroke="#1F618D" stroke-width="2"/>
            '''

        svg += f'''
        <text x="{x}" y="{y+6}" text-anchor="middle"
        font-size="18" font-weight="bold"
        fill="#172B4D">{name}</text>
        '''

    svg += '''
    <text x="550" y="610" text-anchor="middle"
    font-size="17" fill="#172B4D">
    Initial State: Q0 | Double Circle: Final State
    </text>
    </svg>
    '''

    path = os.path.join(DIAGRAM_DIR, filename)

    with open(path, "w", encoding="utf-8") as file:
        file.write(svg)

    print("Created:", filename)


# -------------------------------------------------
# 1. PASSWORD VERIFICATION DFA
# -------------------------------------------------

password_nodes = [
    (130, 300, "Q0", False),
    (400, 300, "Q1", False),
    (700, 300, "Q2", True),
    (950, 500, "Qdead", False)
]

password_edges = [
    (170, 300, 360, 300, "Letter"),
    (440, 300, 660, 300, "Digit"),
    (680, 340, 420, 340, "Letter"),
    (740, 340, 740, 340, "Digit"),
    (430, 340, 430, 340, "Letter"),
    (730, 340, 730, 340, "Digit"),
    (170, 330, 920, 480, "Invalid input")
]

create_svg(
    "01_password_verification_dfa.svg",
    "PASSWORD VERIFICATION - DFA",
    "Starts with a letter and ends with a digit",
    password_nodes,
    password_edges
)


# -------------------------------------------------
# 2. EMAIL VALIDATION DFA
# -------------------------------------------------

email_nodes = [
    (100, 300, "Q0", False),
    (300, 300, "Q1", False),
    (500, 300, "Q2", False),
    (700, 300, "Q3", False),
    (950, 300, "Q4", True),
    (550, 510, "Qdead", False)
]

email_edges = [
    (140, 300, 260, 300, "Username"),
    (340, 300, 460, 300, "@"),
    (540, 300, 660, 300, "Domain"),
    (740, 300, 910, 300, ". + extension"),
    (300, 340, 500, 470, "Invalid"),
    (500, 340, 550, 470, "Invalid"),
    (700, 340, 550, 470, "Invalid")
]

create_svg(
    "02_email_validation_dfa.svg",
    "EMAIL FORMAT VALIDATION - DFA",
    "Username -> @ -> Domain -> . -> Extension",
    email_nodes,
    email_edges
)


# -------------------------------------------------
# 3. ATM PIN VERIFICATION DFA
# -------------------------------------------------

atm_nodes = [
    (100, 300, "Q0", False),
    (300, 300, "Q1", False),
    (500, 300, "Q2", False),
    (700, 300, "Q3", False),
    (950, 300, "Q4", True),
    (550, 520, "Qdead", False)
]

atm_edges = [
    (140, 300, 260, 300, "Digit"),
    (340, 300, 460, 300, "Digit"),
    (540, 300, 660, 300, "Digit"),
    (740, 300, 910, 300, "Digit"),
    (300, 340, 500, 480, "Invalid input"),
    (500, 340, 550, 480, "Invalid input"),
    (700, 340, 550, 480, "Invalid input"),
    (950, 340, 550, 480, "Extra digit")
]

create_svg(
    "03_atm_pin_verification_dfa.svg",
    "ATM PIN VERIFICATION - DFA",
    "Exactly four numeric digits are accepted",
    atm_nodes,
    atm_edges
)


print("\n====================================")
print("ALL THREE DFA DIAGRAMS GENERATED!")
print("====================================")
print("Saved inside:", DIAGRAM_DIR)