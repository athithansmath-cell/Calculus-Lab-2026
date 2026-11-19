import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# ENTER YOUR ASSIGNED CONSTANTS (a, b) FROM YOUR README.md
a = 9   # Replace with your assigned 'a'
b = 5   # Replace with your assigned 'b'
# ==========================================================

# --- PERIOD 1 VISUAL: Ellipse, Osculating Circle at pi/4 & Evolute ---
t = np.linspace(0, 2 * np.pi, 500)
x = a * np.cos(t)
y = b * np.sin(t)
x_ev = ((a**2 - b**2) / a) * (np.cos(t)**3)
y_ev = ((b**2 - a**2) / b) * (np.sin(t)**3)

t0 = np.pi / 4
x0, y0 = a * np.cos(t0), b * np.sin(t0)
xc = ((a**2 - b**2) / a) * (np.cos(t0)**3)
yc = ((b**2 - a**2) / b) * (np.sin(t0)**3)
rho = ((a**2 * np.sin(t0)**2 + b**2 * np.cos(t0)**2)**1.5) / (a * b)

theta = np.linspace(0, 2 * np.pi, 300)
plt.figure(figsize=(7, 7))
plt.plot(x, y, 'b-', linewidth=2, label=f'Ellipse (a={a}, b={b})')
plt.plot(x_ev, y_ev, 'r--', linewidth=2, label='Evolute (Envelope of Normals)')
plt.plot(xc + rho * np.cos(theta), yc + rho * np.sin(theta), 'g:', linewidth=1.8, label=f'Osculating Circle (rho={rho:.2f})')
plt.plot([x0, xc], [y0, yc], 'ko-', label='Normal & Center of Curvature')
plt.gca().set_aspect('equal')
plt.title(f'Period 1 Live Demo | a={a}, b={b}')
plt.legend()
plt.grid(True, linestyle=':')
plt.savefig('P1_Visual.png', dpi=200)
plt.close()

# --- PERIOD 2 VISUAL: Jacobian Grid Warping (u,v) -> (x,y) ---
u = np.linspace(0.2, 1.5, 12)
v = np.linspace(0.2, 1.5, 12)
U, V = np.meshgrid(u, v)
X_map = a * (U**2) - b * (V**2)
Y_map = 2 * np.sqrt(a * b) * U * V

plt.figure(figsize=(7, 6))
for i in range(len(u)):
    plt.plot(X_map[i, :], Y_map[i, :], 'b-', alpha=0.7)
    plt.plot(X_map[:, i], Y_map[:, i], 'r--', alpha=0.7)
plt.title(f'Period 2 Jacobian Grid Warping | a={a}, b={b}')
plt.xlabel('x = a·u² - b·v²')
plt.ylabel('y = 2√(ab)·u·v')
plt.grid(True, linestyle=':')
plt.savefig('P2_Visual.png', dpi=200)
plt.close()

# --- PERIOD 3 VISUAL: 3D Contour Terrain (Saddle vs Extremum) ---
x_val = np.linspace(-2, max(a, b) * 1.5, 300)
y_val = np.linspace(-2, max(a, b) * 1.5, 300)
X, Y = np.meshgrid(x_val, y_val)
G = a * (X**3) + b * (Y**3) - 3 * a * b * X * Y

x_stat = (a * (b**2))**(1/3)
y_stat = ((a**2) * b)**(1/3)

plt.figure(figsize=(7, 6))
cp = plt.contourf(X, Y, G, levels=35, cmap='viridis')
plt.colorbar(cp, label='g(x, y)')
plt.plot(0, 0, 'rx', markersize=10, markeredgewidth=2, label='Saddle Point (0, 0)')
plt.plot(x_stat, y_stat, 'wo', markersize=8, markeredgecolor='black', label=f'Local Minimum ({x_stat:.2f}, {y_stat:.2f})')
plt.title(f'Period 3 Extrema Contour Map | g(x,y) = {a}x³ + {b}y³ - {3*a*b}xy')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('P3_Visual.png', dpi=200)
plt.close()

print("Generated P1_Visual.png, P2_Visual.png, and P3_Visual.png!")
