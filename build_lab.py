import os
import csv
import math

os.makedirs(".github/workflows", exist_ok=True)
os.makedirs("scripts", exist_ok=True)
os.makedirs("students", exist_ok=True)

yml_lines = [
    "name: Live Student Progress Tracker",
    "on:",
    "  push:",
    "    branches: [ main ]",
    "    paths:",
    "      - 'students/**'",
    "permissions:",
    "  contents: write",
    "jobs:",
    "  update-dashboard:",
    "    runs-on: ubuntu-latest",
    "    steps:",
    "      - uses: actions/checkout@v4",
    "      - uses: actions/setup-python@v5",
    "        with:",
    "          python-version: '3.11'",
    "      - run: python scripts/update_board.py",
    "      - run: |",
    "          git config --local user.email 'github-actions[bot]@users.noreply.github.com'",
    "          git config --local user.name 'Live Lab Monitor'",
    "          git add README.md",
    "          git diff --quiet && git diff --staged --quiet || git commit -m 'Auto-update live class status'",
    "          git push"
]
with open(".github/workflows/live_tracker.yml", "w", encoding="utf-8") as f:
    f.write("\n".join(yml_lines) + "\n")

board_lines = [
    "import os",
    "import subprocess",
    "from datetime import datetime, timezone, timedelta",
    "",
    "IST = timezone(timedelta(hours=5, minutes=30))",
    "now_ist = datetime.now(IST).strftime('%d %b %Y, %I:%M:%S %p IST')",
    "rows = []",
    "",
    "if os.path.exists('students'):",
    "    for folder in sorted(os.listdir('students')):",
    "        path = os.path.join('students', folder)",
    "        if not os.path.isdir(path):",
    "            continue",
    "        p1 = '✅' if os.path.exists(os.path.join(path, 'P1_Worked.pdf')) else '⬜'",
    "        p2 = '✅' if os.path.exists(os.path.join(path, 'P2_Worked.pdf')) else '⬜'",
    "        p3 = '✅' if os.path.exists(os.path.join(path, 'P3_Worked.pdf')) else '⬜'",
    "        try:",
    "            last_time = subprocess.check_output(['git', 'log', '-1', '--format=%cd', '--date=format:%H:%M:%S', '--', path]).decode('utf-8').strip() or 'No commits yet'",
    "        except Exception:",
    "            last_time = 'Initialized'",
    "        done = [p1, p2, p3].count('✅')",
    "        status = ['Not Started', 'In Progress (1/3)', 'In Progress (2/3)', '🟢 Completed'][done]",
    "        rows.append(f'| `{folder}` | {p1} | {p2} | {p3} | **{status}** | `{last_time}` |')",
    "",
    "header = f'# Live Differential Calculus Lab Dashboard\\n**Last Auto-Updated:** `{now_ist}`\\n\\n| Student ID & Name | Period 1 (Curvature/Evolute) | Period 2 (Partials/Jacobian) | Period 3 (Taylor/Extrema) | Overall Status | Last Push |\\n| :--- | :---: | :---: | :---: | :--- | :---: |\\n'",
    "with open('README.md', 'w', encoding='utf-8') as f:",
    "    f.write(header + ('\\n'.join(rows) if rows else '| *Awaiting student folders...* | ⬜ | ⬜ | ⬜ | Pending | - |') + '\\n')"
]
with open("scripts/update_board.py", "w", encoding="utf-8") as f:
    f.write("\n".join(board_lines) + "\n")

roster = [
    ("RA2611003010078", "PARAMITA RAKSHIT"), ("RA2611003010079", "SATTWIK DAS"),
    ("RA2611003010080", "SAMEEKSHA"), ("RA2611003010081", "KONATHAM JAGATH ANIRUDH"),
    ("RA2611003010082", "BANDI AISHWARYA"), ("RA2611003010083", "BORAPAREDDY KRISHNA SANDEEP"),
    ("RA2611003010084", "ABHIGYAN HAZRA"), ("RA2611003010085", "UPADHYE SAKSHAM KISHOR"),
    ("RA2611003010087", "SYED ARHAM HAMEED"), ("RA2611003010088", "GOPAVARAM KOUSHIK PREETHAM REDDY"),
    ("RA2611003010089", "BHASITH VENKATA MANI SAI PARDHU CHAKKA"), ("RA2611003010090", "AASIM M A"),
    ("RA2611003010091", "RAJA VIKRAM M P"), ("RA2611003010092", "PRATHISHNA K"),
    ("RA2611003010093", "HARISH R"), ("RA2611003010094", "ANANT SINGH"),
    ("RA2611003010095", "MADDELA AKHIL"), ("RA2611003010096", "MUKTESH REDDY PALLE"),
    ("RA2611003010097", "PRIYANSH MAURYA"), ("RA2611003010098", "PRANIT AMARTYA BANERJEE"),
    ("RA2611003010099", "PUGHAZ RAAGHAVAN S Y"), ("RA2611003010100", "NAMBI RAM V"),
    ("RA2611003010101", "VISHWAS GARG"), ("RA2611003010102", "SAMBHAAVYA GHOSH"),
    ("RA2611003010104", "ANUSHKA MITRA"), ("RA2611003010105", "TRISHLA BISWAL"),
    ("RA2611003010106", "SHREYAS R NAIR"), ("RA2611003010107", "DIVYA RANJAN SINGH"),
    ("RA2611003010108", "NIHAL AGARWAL"), ("RA2611003010109", "ARGHYADIP DAS"),
    ("RA2611003010110", "YASASWI BANDARU"), ("RA2611003010111", "RUDRANIL GHOSH"),
    ("RA2611003010112", "ADITYA PRASAD KUSHWAHA"), ("RA2611003010113", "ANSH GARG"),
    ("RA2611003010114", "MADDALI PRISHA"), ("RA2611003010116", "SAKSHAM TOMAR"),
    ("RA2611003010117", "M MONITH KRISHNA"), ("RA2611003010118", "AISHWARY KUSHWAHA"),
    ("RA2611003010119", "AYUSH MISHRA"), ("RA2611003010120", "GORTY SIDHI AKSHARA"),
    ("RA2611003010121", "MEENAKSHI KUMARI"), ("RA2611003010122", "VASHU GAUTAM"),
    ("RA2611003010123", "PARAMVEER SINGH BHOGAL"), ("RA2611003010124", "MEDIPALLI CHARAN SIVA"),
    ("RA2611003010125", "SHIVAM SHASHANK"), ("RA2611003010126", "AYUSH CHANDRA"),
    ("RA2611003010127", "AKASH SHARMA"), ("RA2611003010128", "SOHAN CHOWDHURY"),
    ("RA2611003010129", "VISHNUVARDHANA JANITH SAI"), ("RA2611003010130", "ABINAV THANGARAJ"),
    ("RA2611003010131", "ANKUR KUMAR"), ("RA2611003010132", "SUHANI"),
    ("RA2611003010133", "ARCHIT GAURAV"), ("RA2611003010134", "SHOUNAK BHAUMIK"),
    ("RA2611003010135", "NAISHA JAISWAL"), ("RA2611003010136", "RISHIPARN SINGH"),
    ("RA2611003010137", "PALLAVI ROY"), ("RA2611003010138", "CHARANJOT SINGH GILL"),
    ("RA2611003010139", "SIVA GOKUL S"), ("RA2611003010140", "DRISHAYAN MAJUMDER"),
    ("RA2611003010141", "ARYA CHANDRA"), ("RA2611003010142", "KRISHNA JHA"),
    ("RA2611003010143", "YASH RAJ"), ("RA2611003010144", "VANSH GOEL"),
    ("RA2611003010145", "ANSHUL LAIJU SAM"), ("RA2611003010146", "GOURAV CHAKRABORTY"),
    ("RA2611003010147", "RITURAJ BHAKUNI"), ("RA2611003010148", "AMSURI GOWTHAM"),
    ("RA2611003010149", "BALAJI P"), ("RA2611003010150", "CHILAMALA PURUSHOTHAM"),
    ("RA2611003010151", "STEPHEN RAJ A"),
]

answer_rows = []
for reg, name in roster:
    n = int(reg[-3:])
    a = ((n * 7) % 11) + 2
    b = ((n * 5 + 3) % 13) + 2
    if a == b:
        b += 1

    folder_name = f"{reg}_{name.replace(' ', '_')}"
    folder_path = os.path.join("students", folder_name)
    os.makedirs(folder_path, exist_ok=True)

    rho_ellipse_pi4 = round(((a**2 + b**2) / 2)**1.5 / (a * b), 4)
    rho_cardioid_pi3 = round((4 * a / 3) * math.cos(math.pi / 6), 4)
    stat_x = round((a * (b**2))**(1/3), 4)
    stat_y = round(((a**2) * b)**(1/3), 4)
    extremum_val = round(-(a**2) * (b**2), 4)
    lagrange_min = round(((a + b)**2) / ((1/a) + (1/b) + (1/(a*b))), 4)

    answer_rows.append([reg, name, a, b, rho_ellipse_pi4, rho_cardioid_pi3, f"({stat_x}, {stat_y})", extremum_val, lagrange_min])

    worksheet = (
        f"# Differential Calculus Lab Worksheet\n"
        f"* **Student Name:** {name}\n"
        f"* **Register Number:** `{reg}`\n"
        f"* **Assigned Unique Constants:** $a = {a}$, $b = {b}$\n\n"
        f"> **Submission Instructions:** Upload your hand-worked step-by-step derivations inside this folder (`students/{folder_name}/`) using the exact filenames below:\n"
        f"> * **Period 1:** `P1_Worked.pdf`\n"
        f"> * **Period 2:** `P2_Worked.pdf`\n"
        f"> * **Period 3:** `P3_Worked.pdf`\n\n"
        f"---\n\n"
        f"## Period 1 (50 Mins): Curvature, Evolutes, Envelopes & Pedal Equations\n"
        f"1. **Curve Tracing & Curvature:** Trace the ellipse $\\frac{{x^2}}{{{a**2}}} + \\frac{{y^2}}{{{b**2}}} = 1$ ($x = {a}\\cos t, \\; y = {b}\\sin t$). Derive $\\rho$ in Cartesian and Parametric forms, and evaluate $\\rho$ at $t = \\frac{{\\pi}}{{4}}$.\n"
        f"2. **Polar Curvature & Pedal Equation:** For the cardioid $r = {a}(1 + \\cos\\theta)$, derive its pedal equation ($p$-$r$) and compute $\\rho$ at $\\theta = \\frac{{\\pi}}{{3}}$ using both polar and pedal formulas.\n"
        f"3. **Circle of Curvature, Evolute & Envelope:** For the parabola $y^2 = {4*a}x$, find the equation of the Circle of Curvature at $({a}, {2*a})$, derive its Evolute $27({a})y^2 = 4(x - {2*a})^3$, and prove that the **Envelope of Normals** $y + tx = {2*a}t + {a}t^3$ yields the exact same evolute.\n"
        f"4. **Involute:** Derive the parametric equations of the involute of the circle $x = {b}\\cos\\theta, \\; y = {b}\\sin\\theta$ starting from $\\theta = 0$.\n\n"
        f"---\n\n"
        f"## Period 2 (50 Mins): Multivariable Limits, Partials, Euler’s Theorem & Jacobians\n"
        f"1. **Limit, Continuity & Geometrical Meaning:** Examine $f(x, y) = \\frac{{{a*b}xy}}{{x^2 + y^2}}$ for $(x,y) \\neq (0,0)$ and $f(0,0) = 0$. Test continuity along $y = mx$ and $y = x^2$, compute $f_x(0,0)$ and $f_y(0,0)$ from first principles, and state their geometrical interpretation.\n"
        f"2. **Total Derivative & Implicit Function:**\n"
        f"   * Find $\\frac{{dz}}{{dt}}$ at $t = 0$ for $z = {a}x^2 y + {b}xy^2$, where $x = e^{{{a}t}}$ and $y = \\sin({b}t)$.\n"
        f"   * Find $\\frac{{dy}}{{dx}}$ and $\\frac{{d^2y}}{{dx^2}}$ for the implicit curve $x^3 + y^3 + {3*a*b}xy - {a**3 + b**3} = 0$.\n"
        f"3. **Euler’s Theorem (2nd Degree):** Verify $x u_x + y u_y = 2u$ and $x^2 u_{{xx}} + 2xy u_{{xy}} + y^2 u_{{yy}} = 2u$ for $u(x, y) = \\frac{{{a}x^4 + {b}y^4}}{{x^2 + y^2}}$.\n"
        f"4. **3-Variable Jacobian:** For $x = {a}r\\sin\\theta\\cos\\phi, \\; y = {b}r\\sin\\theta\\sin\\phi, \\; z = {a*b}r\\cos\\theta$, compute $J = \\frac{{\\partial(x,y,z)}}{{\\partial(r,\\theta,\\phi)}}$ and verify $J \\cdot J' = 1$.\n\n"
        f"---\n\n"
        f"## Period 3 (50 Mins): Taylor Series, Extrema & Lagrange Multipliers\n"
        f"1. **3rd-Order Taylor Series:** Expand $f(x, y) = e^{{{a}x}} \\cos({b}y)$ around $(0, 0)$ up to third-degree terms.\n"
        f"2. **Unconstrained Extrema:** Find all stationary points of $g(x, y) = {a}x^3 + {b}y^3 - {3*a*b}xy$ and classify each using $rt - s^2$.\n"
        f"3. **Lagrange Multipliers:** Find the minimum value of $T(x, y, z) = {a}x^2 + {b}y^2 + {a*b}z^2$ subject to $x + y + z = {a + b}$.\n"
    )
    with open(os.path.join(folder_path, "README.md"), "w", encoding="utf-8") as f:
        f.write(worksheet)

desktop_key = os.path.join(os.path.expanduser("~"), "Desktop", "INSTRUCTOR_ANSWER_KEY.csv")
with open(desktop_key, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Register No.", "Student Name", "a", "b", "P1: Ellipse rho(pi/4)", "P1: Cardioid rho(pi/3)", "P3: Stationary Pt", "P3: Extremum", "P3: Lagrange Min"])
    writer.writerows(answer_rows)

print("SUCCESS: All 71 student folders and Answer Key generated!")