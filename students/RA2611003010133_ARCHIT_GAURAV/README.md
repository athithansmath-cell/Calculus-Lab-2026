# Differential Calculus Lab Worksheet
* **Student Name:** ARCHIT GAURAV
* **Register Number:** `RA2611003010133`
* **Assigned Unique Constants:** $a = 9$, $b = 7$

> **Submission Instructions:** Upload your hand-worked step-by-step derivations inside this folder (`students/RA2611003010133_ARCHIT_GAURAV/`) using the exact filenames below so the live class dashboard tracks your progress automatically:
> * **Period 1:** `P1_Worked.pdf` and `P1_Visual.png`
> * **Period 2:** `P2_Worked.pdf`
> * **Period 3:** `P3_Worked.pdf` and `P3_Surface.png`

---

## Period 1 (50 Mins): Curvature, Evolutes, Envelopes & Pedal Equations
1. **Curve Tracing & Curvature:** Trace the ellipse $\frac{x^2}{81} + \frac{y^2}{49} = 1$ ($x = 9\cos t, \; y = 7\sin t$). Derive $\rho$ in Cartesian and Parametric forms, and evaluate $\rho$ at $t = \frac{\pi}{4}$.
2. **Polar Curvature & Pedal Equation:** For the cardioid $r = 9(1 + \cos\theta)$, derive its pedal equation ($p$-$r$ relation) and compute $\rho$ at $\theta = \frac{\pi}{3}$ using both polar and pedal formulas.
3. **Circle of Curvature, Evolute & Envelope:** For the parabola $y^2 = 36x$, find the equation of the Circle of Curvature at $(9, 18)$, derive its Evolute $27(9)y^2 = 4(x - 18)^3$, and prove that the **Envelope of Normals** $y + tx = 18t + 9t^3$ yields the exact same evolute.
4. **Involute:** Derive the parametric equations of the involute of the circle $x = 7\cos\theta, \; y = 7\sin\theta$ starting from $\theta = 0$.

---

## Period 2 (50 Mins): Multivariable Limits, Partials, Euler’s Theorem & Jacobians
1. **Limit, Continuity & Geometrical Meaning:** Examine $f(x, y) = \frac{63xy}{x^2 + y^2}$ for $(x,y) \neq (0,0)$ and $f(0,0) = 0$. Test continuity along $y = mx$ and $y = x^2$, compute $f_x(0,0)$ and $f_y(0,0)$ from first principles, and state their geometrical interpretation.
2. **Total Derivative & Implicit Function:**
   * Find $\frac{dz}{dt}$ at $t = 0$ for $z = 9x^2 y + 7xy^2$, where $x = e^{9t}$ and $y = \sin(7t)$.
   * Find $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$ for the implicit curve $x^3 + y^3 + 189xy - 1072 = 0$.
3. **Euler’s Theorem (2nd Degree):** Verify $x u_x + y u_y = 2u$ and $x^2 u_{xx} + 2xy u_{xy} + y^2 u_{yy} = 2u$ for $u(x, y) = \frac{9x^4 + 7y^4}{x^2 + y^2}$.
4. **3-Variable Jacobian:** For $x = 9r\sin\theta\cos\phi, \; y = 7r\sin\theta\sin\phi, \; z = 63r\cos\theta$, compute $J = \frac{\partial(x,y,z)}{\partial(r,\theta,\phi)}$ and verify $J \cdot J' = 1$.

---

## Period 3 (50 Mins): Taylor Series, Extrema & Lagrange Multipliers
1. **3rd-Order Taylor Series:** Expand $f(x, y) = e^{9x} \cos(7y)$ around $(0, 0)$ up to third-degree terms.
2. **Unconstrained Extrema:** Find all stationary points of $g(x, y) = 9x^3 + 7y^3 - 189xy$ and classify each using $rt - s^2$.
3. **Lagrange Multipliers:** Find the minimum value of $T(x, y, z) = 9x^2 + 7y^2 + 63z^2$ subject to $x + y + z = 16$.
