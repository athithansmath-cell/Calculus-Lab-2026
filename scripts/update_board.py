import os
import subprocess
from datetime import datetime, timezone, timedelta

IST = timezone(timedelta(hours=5, minutes=30))
now_ist = datetime.now(IST).strftime('%d %b %Y, %I:%M:%S %p IST')
rows = []

if os.path.exists('students'):
    for folder in sorted(os.listdir('students')):
        path = os.path.join('students', folder)
        if not os.path.isdir(path):
            continue
        p1 = '✅' if os.path.exists(os.path.join(path, 'P1_Worked.pdf')) else '⬜'
        p2 = '✅' if os.path.exists(os.path.join(path, 'P2_Worked.pdf')) else '⬜'
        p3 = '✅' if os.path.exists(os.path.join(path, 'P3_Worked.pdf')) else '⬜'
        vis = '✅' if (os.path.exists(os.path.join(path, 'P1_Visual.png')) or os.path.exists(os.path.join(path, 'P2_Visual.png')) or os.path.exists(os.path.join(path, 'P3_Visual.png'))) else '⬜'
        obs_path = os.path.join(path, 'OBSERVATIONS.md')
        obs_done = False
        if os.path.exists(obs_path):
            with open(obs_path, 'r', encoding='utf-8') as of:
                obs_done = '*(write your' not in of.read()
        obs = '✅' if obs_done else '⬜'
        try:
            last_time = subprocess.check_output(['git', 'log', '-1', '--format=%cd', '--date=format:%H:%M:%S', '--', path]).decode('utf-8').strip() or 'No commits yet'
        except Exception:
            last_time = 'Initialized'
        score = [p1, p2, p3, vis, obs].count('✅')
        status = f'{score}/5 Completed' if score < 5 else '🟢 Fully Verified'
        rows.append(f'| `{folder}` | {p1} | {p2} | {p3} | {vis} | {obs} | **{status}** | `{last_time}` |')

header = f'# Live Differential Calculus Lab & Discovery Dashboard\n**Last Auto-Updated:** `{now_ist}`\n\n| Student ID & Name | P1 Math | P2 Math | P3 Math | Live Visuals | Learning Log | Overall Progress | Last Push |\n| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :---: |\n'
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(header + ('\n'.join(rows) if rows else '| *Awaiting student folders...* | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | Pending | - |') + '\n')
