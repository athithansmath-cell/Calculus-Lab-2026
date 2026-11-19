# Differential Calculus Lab & Live Discovery Worksheet
* **Student Name:** KRISHNA JHA
* **Register Number:** `RA2611003010142`
* **Assigned Unique Constants:** $a = 6$, $b = 13$

> **Deliverables to Upload Inside This Folder (`students/RA2611003010142_KRISHNA_JHA/`):**
> 1. **Hand-Worked Derivations:** `P1_Worked.pdf`, `P2_Worked.pdf`, `P3_Worked.pdf`
> 2. **Live Demonstration Visuals:** `P1_Visual.png`, `P2_Visual.png`, `P3_Visual.png` (generated via `live_visualizer.py` or GeoGebra/Desmos using $a=6, b=13$)
> 3. **Individual Learning Log:** Edit `OBSERVATIONS.md` in this folder to record your visual observations and mathematical takeaways.

---

## Period 1 (50 Mins): Curvature, Evolutes, Envelopes & Pedal Equations
1. **Curve Tracing & Curvature:** Trace the ellipse $\frac{x^2}{36} + \frac{y^2}{169} = 1$ ($x = 6\cos t, \; y = 13\sin t$). Derive $\rho$ in Cartesian and Parametric forms, and evaluate $\rho$ at $t = \frac{\pi}{4}$.
2. **Polar Curvature & Pedal Equation:** For the cardioid $r = 6(1 + \cos\theta)$, derive its pedal equation ($p$-$r$) and compute $\rho$ at $\theta = \frac{\pi}{3}$ using both polar and pedal formulas.
3. **Circle of Curvature, Evolute & Envelope:** For the parabola $y^2 = 24x$, find the equation of the Circle of Curvature at $(6, 12)$, derive its Evolute $27(6)y^2 = 4(x - 12)^3$, and prove that the **Envelope of Normals** $y + tx = 12t + 6t^3$ yields the exact same evolute.
4. **Involute:** Derive the parametric equations of the involute of the circle $x = 13\cos\theta, \; y = 13\sin\theta$ starting from $\theta = 0$.

---

## Period 2 (50 Mins): Multivariable Limits, Partials, Euler’s Theorem & Jacobians
1. **Limit, Continuity & Geometrical Meaning:** Examine $f(x, y) = \frac{78xy}{x^2 + y^2}$ for $(x,y) \neq (0,0)$ and $f(0,0) = 0$. Test continuity along $y = mx$ and $y = x^2$, compute $f_x(0,0)$ and $f_y(0,0)$ from first principles, and state their geometrical interpretation.
2. **Total Derivative & Implicit Function:**
   * Find $\frac{dz}{dt}$ at $t = 0$ for $z = 6x^2 y + 13xy^2$, where $x = e^{6t}$ and $y = \sin(13t)$.
   * Find $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$ for the implicit curve $x^3 + y^3 + 234xy - 2413 = 0$.
3. **Euler’s Theorem (2nd Degree):** Verify $x u_x + y u_y = 2u$ and $x^2 u_{xx} + 2xy u_{xy} + y^2 u_{yy} = 2u$ for $u(x, y) = \frac{6x^4 + 13y^4}{x^2 + y^2}$.
4. **3-Variable Jacobian:** For $x = 6r\sin\theta\cos\phi, \; y = 13r\sin\theta\sin\phi, \; z = 78r\cos\theta$, compute $J = \frac{\partial(x,y,z)}{\partial(r,\theta,\phi)}$ and verify $J \cdot J' = 1$.

---

## Period 3 (50 Mins): Taylor Series, Extrema & Lagrange Multipliers
1. **3rd-Order Taylor Series:** Expand $f(x, y) = e^{6x} \cos(13y)$ around $(0, 0)$ up to third-degree terms.
2. **Unconstrained Extrema:** Find all stationary points of $g(x, y) = 6x^3 + 13y^3 - 234xy$ and classify each using $rt - s^2$.
3. **Lagrange Multipliers:** Find the minimum value of $T(x, y, z) = 6x^2 + 13y^2 + 78z^2$ subject to $x + y + z = 19$.
