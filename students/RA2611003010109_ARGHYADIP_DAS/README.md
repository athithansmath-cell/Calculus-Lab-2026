# Differential Calculus Lab Worksheet
* **Student Name:** ARGHYADIP DAS
* **Register Number:** `RA2611003010109`
* **Assigned Unique Constants:** $a = 6$, $b = 4$

> **Submission Instructions:** Upload your hand-worked step-by-step derivations inside this folder (`students/RA2611003010109_ARGHYADIP_DAS/`) using the exact filenames below so the live class dashboard tracks your progress automatically:
> * **Period 1:** `P1_Worked.pdf` and `P1_Visual.png`
> * **Period 2:** `P2_Worked.pdf`
> * **Period 3:** `P3_Worked.pdf` and `P3_Surface.png`

---

## Period 1 (50 Mins): Curvature, Evolutes, Envelopes & Pedal Equations
1. **Curve Tracing & Curvature:** Trace the ellipse $\frac{x^2}{36} + \frac{y^2}{16} = 1$ ($x = 6\cos t, \; y = 4\sin t$). Derive $\rho$ in Cartesian and Parametric forms, and evaluate $\rho$ at $t = \frac{\pi}{4}$.
2. **Polar Curvature & Pedal Equation:** For the cardioid $r = 6(1 + \cos\theta)$, derive its pedal equation ($p$-$r$ relation) and compute $\rho$ at $\theta = \frac{\pi}{3}$ using both polar and pedal formulas.
3. **Circle of Curvature, Evolute & Envelope:** For the parabola $y^2 = 24x$, find the equation of the Circle of Curvature at $(6, 12)$, derive its Evolute $27(6)y^2 = 4(x - 12)^3$, and prove that the **Envelope of Normals** $y + tx = 12t + 6t^3$ yields the exact same evolute.
4. **Involute:** Derive the parametric equations of the involute of the circle $x = 4\cos\theta, \; y = 4\sin\theta$ starting from $\theta = 0$.

---

## Period 2 (50 Mins): Multivariable Limits, Partials, Euler’s Theorem & Jacobians
1. **Limit, Continuity & Geometrical Meaning:** Examine $f(x, y) = \frac{24xy}{x^2 + y^2}$ for $(x,y) \neq (0,0)$ and $f(0,0) = 0$. Test continuity along $y = mx$ and $y = x^2$, compute $f_x(0,0)$ and $f_y(0,0)$ from first principles, and state their geometrical interpretation.
2. **Total Derivative & Implicit Function:**
   * Find $\frac{dz}{dt}$ at $t = 0$ for $z = 6x^2 y + 4xy^2$, where $x = e^{6t}$ and $y = \sin(4t)$.
   * Find $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$ for the implicit curve $x^3 + y^3 + 72xy - 280 = 0$.
3. **Euler’s Theorem (2nd Degree):** Verify $x u_x + y u_y = 2u$ and $x^2 u_{xx} + 2xy u_{xy} + y^2 u_{yy} = 2u$ for $u(x, y) = \frac{6x^4 + 4y^4}{x^2 + y^2}$.
4. **3-Variable Jacobian:** For $x = 6r\sin\theta\cos\phi, \; y = 4r\sin\theta\sin\phi, \; z = 24r\cos\theta$, compute $J = \frac{\partial(x,y,z)}{\partial(r,\theta,\phi)}$ and verify $J \cdot J' = 1$.

---

## Period 3 (50 Mins): Taylor Series, Extrema & Lagrange Multipliers
1. **3rd-Order Taylor Series:** Expand $f(x, y) = e^{6x} \cos(4y)$ around $(0, 0)$ up to third-degree terms.
2. **Unconstrained Extrema:** Find all stationary points of $g(x, y) = 6x^3 + 4y^3 - 72xy$ and classify each using $rt - s^2$.
3. **Lagrange Multipliers:** Find the minimum value of $T(x, y, z) = 6x^2 + 4y^2 + 24z^2$ subject to $x + y + z = 10$.
