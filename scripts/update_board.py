import os, subprocess
from datetime import datetime, timezone, timedelta
IST = timezone(timedelta(hours=5, minutes=30))
now_ist = datetime.now(IST).strftime('%d %b %Y, %I:%M:%S %p IST')
rows = []
if os.path.exists('students'):
    for folder in sorted(os.listdir('students')):
        path = os.path.join('students', folder)
        if not os.path.isdir(path): continue
        p1 = '✅' if os.path.exists(os.path.join(path, 'P1_Worked.pdf')) else '⬜'
        p2 = '✅' if os.path.exists(os.path.join(path, 'P2_Worked.pdf')) else '⬜'
        p3 = '✅' if os.path.exists(os.path.join(path, 'P3_Worked.pdf')) else '⬜'
        try:
            last_time = subprocess.check_output(['git', 'log', '-1', '--format=%cd', '--date=format:%H:%M:%S', '--', path]).decode().strip() or 'No commits yet'
        except Exception:
            last_time = 'Initialized'
        done = [p1, p2, p3].count('✅')
        status = ['Not Started', 'In Progress (1/3)', 'In Progress (2/3)', '🟢 Completed'][done]
        rows.append(f'| {folder} | {p1} | {p2} | {p3} | **{status}** | {last_time} |')
header = f'# Live Differential Calculus Lab Dashboard\n**Last Auto-Updated:** {now_ist}\n\n| Student ID & Name | Period 1 (Curvature/Evolute) | Period 2 (Partials/Jacobian) | Period 3 (Taylor/Extrema) | Overall Status | Last Push |\n| :--- | :---: | :---: | :---: | :--- | :---: |\n'
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(header + ('\n'.join(rows) if rows else '| *Awaiting student folders...* | ⬜ | ⬜ | ⬜ | Pending | - |') + '\n')
