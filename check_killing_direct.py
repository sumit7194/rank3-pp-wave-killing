"""Two direct checks that the pp-wave has no Killing vector beyond d_t, d_s -- sympy only, no jet count.

    python check_killing_direct.py          (well under a minute)

Added 2026-10-19 after Prof. A. Galajinsky asked for (i) a proof that the original sigma = 0
Smorodinsky-Winternitz system has no additional integral linear in momenta, and (ii) questioned the jet-count bound
used in check_rank3.py (step 5). That bound is only an upper bound; this file adds explicit derivations that do not use it.

Same metric as check_rank3.py, coordinates (t, s, xi, eta), rho^2 = xi^2 + eta^2, a != 0, V = 2 a xi / rho^2:
    ds^2 = -2V dt^2 + 2 dt ds + 8 rho^2 (dxi^2 + deta^2)
The transverse metric h = 8 rho^2 |dz|^2 (z = xi + i eta) equals 2|dw|^2 with w = z^2 = x + i y, so it is flat.
Everything is local: the conclusions hold on every connected open set with rho > 0.

PART A. Integrals I = A p_xi + B p_eta + f of the original system H = (p_xi^2 + p_eta^2)/(16 rho^2) + V, with A, B, f
        allowed to depend on t. Conservation, dI/dt = d_t I + {I, H} = 0, splits by degree in momenta:
          degree 2:  (A, B) is a Killing field of h, i.e. locally c1(t), c2(t) w-translations plus omega(t) w-rotation
                     (a 2D flat metric has exactly this 3-dimensional Killing algebra);
          degree 1:  h(d_t X) = -df, so h(d_t X) must be closed: the rotation part is not, hence omega' = 0, and then
                     f = -2 (c1' x + c2' y) + k(t);
          degree 0:  the remaining conditions, extracted below by matching coefficients.
        Result: for a != 0, I is a constant.   control: a = 0 (free motion) must leave nonzero solutions.

PART B. The Killing equation L_X g = 0 for X = T d_t + S d_s + P d_xi + Q d_eta, solved explicitly in stages. Each
        stage substitutes the general solution of the equations solved so far, and sympy checks that those equations
        now vanish identically.
          B1  (s,s), (s,i), (s,t) components: T_s = 0, h(d_s X_perp) = -dT, S_s = -T_t. Integrating in s:
              T = T(t, x),  X_perp = -s grad_h T + Y(t, x),  S = -s T_t + Z(t, x).
          B2  (i,j), order s: L_{grad_h T} h = 2 Hess_h T = 0, so T is affine in the flat coordinates (x, y):
              T = alpha(t) + beta1(t) x + beta2(t) y.   (i,j), order 1: Y is a Killing field of h (as in Part A).
          B3  (t,i), order s, and (t,t), order s: give beta' = 0, then beta = 0 and alpha'' = 0.
          B4  (t,i), order 1: h(d_t Y) = -dZ: omega' = 0 and Z = z1(t) x + z2(t) y + k(t), with z fixed by sympy.
          B5  (t,t), order 1: the remaining conditions, extracted by matching coefficients.
        Result: X = alpha0 d_t + k0 d_s, a 2-dimensional algebra.   control: a = 0 must leave nonzero solutions.
"""
import sympy as sp

t, s, xi, eta = sp.symbols('t s xi eta', real=True)
a = sp.symbols('a', real=True)
pxi, peta = sp.symbols('p_xi p_eta')
rho2 = xi**2 + eta**2
V = 2*a*xi/rho2
x_w, y_w = xi**2 - eta**2, 2*xi*eta                     # w = z^2 = x + i y
co = [xi, eta]

def report(name, ok, detail=""):
    print(f"  {'PASS' if ok else 'FAIL'}  {name}{('   ' + detail) if detail else ''}"); return ok

def killing_h(c1, c2, om):
    """General local Killing field of h = 8 rho^2 |dz|^2: w-translation (c1 + i c2) plus w-rotation om, in z-coords."""
    z = xi + sp.I*eta
    Xz = sp.expand((c1 + sp.I*c2 + sp.I*om*z**2)/(2*z))
    return [sp.simplify(sp.re(sp.expand_complex(Xz))), sp.simplify(sp.im(sp.expand_complex(Xz)))]

def lie_h(Xv):
    """L_X h for h = 8 rho^2 delta (X may depend on t, s; only spatial derivatives enter)."""
    phi = 8*rho2
    return sp.Matrix(2, 2, lambda i, j: sp.simplify(phi*(sp.diff(Xv[j], co[i]) + sp.diff(Xv[i], co[j]))
                                                    + (1 if i == j else 0)*sum(Xv[k]*sp.diff(phi, co[k]) for k in range(2))))

def curl_hdual(Xv):
    """d of the h-dual 1-form of X (zero iff the 1-form is locally exact)."""
    return sp.simplify(sp.diff(8*rho2*Xv[1], xi) - sp.diff(8*rho2*Xv[0], eta))

def conditions(expr, vars_=(xi, eta)):
    """All coefficient conditions of a rational expression in (xi, eta) that must vanish identically."""
    num = sp.expand(sp.numer(sp.together(sp.expand(expr))))
    if num == 0:
        return []
    return sorted({sp.factor(c) for c in sp.Poly(num, *vars_).coeffs()}, key=str)

ok = True
fn = lambda n: sp.Function(n, real=True)(t)
c1, c2, om, k, al, b1, b2, z1, z2 = map(fn, ['c1', 'c2', 'om', 'k', 'alpha', 'beta1', 'beta2', 'z1', 'z2'])

# ---------------------------------------------------------------------------------------------------------------
print("0. Ingredients")
Kf = killing_h(*sp.symbols('C1 C2 Om', real=True))
ok &= report("3-parameter family is Killing for h", lie_h(Kf) == sp.zeros(2, 2))
ok &= report("h = 2|dw|^2 with w = (xi + i eta)^2",
             sp.simplify(2*((sp.diff(x_w, xi)**2 + sp.diff(y_w, xi)**2)) - 8*rho2) == 0
             and sp.simplify(sp.diff(x_w, xi)*sp.diff(x_w, eta) + sp.diff(y_w, xi)*sp.diff(y_w, eta)) == 0)
rot, tr1, tr2 = killing_h(0, 0, 1), killing_h(1, 0, 0), killing_h(0, 1, 0)
ok &= report("h-dual of the w-rotation is not closed", curl_hdual(rot) != 0, f"d(...) = {curl_hdual(rot)}")
ok &= report("h-duals of the w-translations are closed: d(2x), d(2y)",
             all(sp.simplify(8*rho2*v[i] - sp.diff(2*p, co[i])) == 0 for v, p in ((tr1, x_w), (tr2, y_w)) for i in range(2)))

# ---------------------------------------------------------------------------------------------------------------
print("A. Integrals linear in momenta of the original system (time dependence allowed)")
H2 = (pxi**2 + peta**2)/(16*rho2) + V
def pb(F_, G_):
    return sum(sp.diff(F_, q)*sp.diff(G_, p) - sp.diff(F_, p)*sp.diff(G_, q) for q, p in ((xi, pxi), (eta, peta)))
Xa = killing_h(c1, c2, om)
f = -2*(sp.diff(c1, t)*x_w + sp.diff(c2, t)*y_w) + k
I = Xa[0]*pxi + Xa[1]*peta + f
E = sp.expand(sp.diff(I, t) + pb(I, H2)).subs(sp.Derivative(om, t), 0)
Ep = sp.Poly(sp.numer(sp.together(E)), pxi, peta)
ok &= report("degree-2 and degree-1 parts vanish (Killing field; omega' = 0; f as stated)",
             all(m == (0, 0) for m in Ep.monoms()))
condA = conditions(E)
print("     degree-0 conditions:", condA)
solA = sp.solve([cc for cc in condA], [c1, c2, om, sp.Derivative(k, t), sp.Derivative(c1, (t, 2)), sp.Derivative(c2, (t, 2))], dict=True)
ok &= report("for a != 0 the only solution is c1 = c2 = omega = 0, k' = 0 (I = const)",
             len(solA) == 1 and all(v == 0 for v in solA[0].values()) and len(solA[0]) == 6, f"{solA}")
condA0 = [cc.subs(a, 0) for cc in condA]
free0 = [cc for cc in condA0 if cc != 0]
ok &= report("control: a = 0 leaves c1, c2, omega unconstrained (free motion has linear integrals)",
             not any(cc.has(c1) and not cc.has(sp.Derivative) for cc in free0) and not any(cc.has(om) for cc in free0),
             f"remaining: {free0}")

# ---------------------------------------------------------------------------------------------------------------
print("B. Explicit solution of the Killing equation L_X g = 0")
X4 = [t, s, xi, eta]
def metric(Vp):
    g = sp.zeros(4, 4); g[0, 0] = -2*Vp; g[0, 1] = g[1, 0] = 1; g[2, 2] = g[3, 3] = 8*rho2; return g
def lie_g(Xv, g):
    return sp.Matrix(4, 4, lambda i, j: sp.simplify(
        sum(Xv[c]*sp.diff(g[i, j], X4[c]) + g[c, j]*sp.diff(Xv[c], X4[i]) + g[i, c]*sp.diff(Xv[c], X4[j]) for c in range(4))))
G = metric(V)

# B1: general functions; the s-row of L_X g
Tg, Sg, Pg, Qg = [sp.Function(n)(t, s, xi, eta) for n in ('T', 'S', 'P', 'Q')]
L = lie_g([Tg, Sg, Pg, Qg], G)
ok &= report("B1 (s,s) = 2 T_s", sp.simplify(L[1, 1] - 2*sp.diff(Tg, s)) == 0)
ok &= report("B1 (s,xi) = 8 rho^2 P_s + T_xi, (s,eta) likewise",
             sp.simplify(L[1, 2] - (8*rho2*sp.diff(Pg, s) + sp.diff(Tg, xi))) == 0
             and sp.simplify(L[1, 3] - (8*rho2*sp.diff(Qg, s) + sp.diff(Tg, eta))) == 0)
ok &= report("B1 (s,t) = T_t + S_s - 2V T_s", sp.simplify(L[0, 1] - (sp.diff(Tg, t) + sp.diff(Sg, s) - 2*V*sp.diff(Tg, s))) == 0)
T1 = sp.Function('T')(t, xi, eta); Y1, Y2, Z1 = [sp.Function(n)(t, xi, eta) for n in ('Y1', 'Y2', 'Z')]
Xb = [T1, -s*sp.diff(T1, t) + Z1, -s*sp.diff(T1, xi)/(8*rho2) + Y1, -s*sp.diff(T1, eta)/(8*rho2) + Y2]
L = lie_g(Xb, G)
ok &= report("B1 general solution of the s-row: s-row of L_X g vanishes identically",
             all(sp.simplify(L[1, j]) == 0 for j in range(4)))
# B2: (i,j) block, order s, is -(L_{grad_h T} h) = -2 Hess_h T; general solution T affine in (x, y)
Tb = al + b1*x_w + b2*y_w
gradT = [sp.diff(Tb, xi)/(8*rho2), sp.diff(Tb, eta)/(8*rho2)]
ok &= report("B2 T = alpha + beta1 x + beta2 y makes grad_h T Killing (Hessian zero in flat x, y)", lie_h(gradT) == sp.zeros(2, 2))
# B3: substitute T affine and Y = general Killing field of h; Z still a general function
Ya = killing_h(c1, c2, om)
Xc = [Tb, -s*sp.diff(Tb, t) + Z1, -s*gradT[0] + Ya[0], -s*gradT[1] + Ya[1]]
L = lie_g(Xc, G)
ok &= report("B2 (i,j) block vanishes identically", all(sp.simplify(L[i, j]) == 0 for i in (2, 3) for j in (2, 3)))
ti_s = [sp.factor(sp.expand(L[0, i]).coeff(s, 1)) for i in (2, 3)]
print("     (t,xi), (t,eta) at order s:", ti_s)
ok &= report("B3 (t,i) order s forces beta1' = beta2' = 0",
             set(sp.solve(ti_s, [sp.Derivative(b1, t), sp.Derivative(b2, t)], dict=True)[0].values()) == {0})
tt_s = sp.expand(L[0, 0]).coeff(s, 1).subs({sp.Derivative(b1, (t, 2)): 0, sp.Derivative(b2, (t, 2)): 0})
condB3 = conditions(tt_s)
print("     (t,t) order s conditions:", condB3)
solB3 = sp.solve(condB3, [b1, b2, sp.Derivative(al, (t, 2))], dict=True)
ok &= report("B3 (t,t) order s forces beta1 = beta2 = 0 and alpha'' = 0 (a != 0)",
             len(solB3) == 1 and set(solB3[0].values()) == {0} and len(solB3[0]) == 3, f"{solB3}")
# B4: beta = 0, alpha = alpha0 + alpha1 t; (t,i) at order 1 is h(d_t Y) + dZ = 0
al0, al1, k0 = sp.symbols('alpha0 alpha1 k0', real=True)
Td = al0 + al1*t
Xd = [Td, -s*al1 + Z1, Ya[0], Ya[1]]
L = lie_g(Xd, G)
ti0 = [sp.simplify(L[0, i]) for i in (2, 3)]
curl = sp.simplify(sp.diff(ti0[1], xi) - sp.diff(ti0[0], eta))
ok &= report("B4 integrability of (t,i): d(h(d_t Y)) = 0 forces omega' = 0",
             sp.simplify(curl - sp.diff(om, t)*curl_hdual(rot)) == 0, f"d(...) = {sp.factor(curl)}")
Zans = z1*x_w + z2*y_w + k
ti0z = [sp.simplify(e.subs(Z1, Zans).doit().subs(sp.Derivative(om, t), 0)) for e in ti0]
zsol = sp.solve(sum([conditions(e) for e in ti0z], []), [z1, z2], dict=True)
ok &= report("B4 Z = -2 (c1' x + c2' y) + k(t)", zsol == [{z1: -2*sp.diff(c1, t), z2: -2*sp.diff(c2, t)}], f"{zsol}")
Zsol = Zans.subs(zsol[0])
# B5: remaining (t,t) equation
Xe = [Td, -s*al1 + Zsol, Ya[0], Ya[1]]
L = lie_g(Xe, G)
L = L.subs(sp.Derivative(om, t), 0)
ok &= report("B5 every component except (t,t) now vanishes",
             all(sp.simplify(L[i, j]) == 0 for i in range(4) for j in range(4) if (i, j) != (0, 0)))
condB5 = conditions(L[0, 0])
print("     (t,t) conditions:", condB5)
solB5 = sp.solve(condB5, [c1, c2, om, al1, sp.Derivative(k, t), sp.Derivative(c1, (t, 2)), sp.Derivative(c2, (t, 2))], dict=True)
ok &= report("B5 for a != 0: c1 = c2 = omega = alpha1 = 0, k' = 0",
             len(solB5) == 1 and set(solB5[0].values()) == {0} and len(solB5[0]) == 7, f"{solB5}")
Xfin = [al0, k0, 0, 0]
ok &= report("result: X = alpha0 d_t + k0 d_s, and it is Killing", lie_g(Xfin, G) == sp.zeros(4, 4))
cond0 = [cc.subs(a, 0) for cc in condB5 + condB3]
ok &= report("control: a = 0 (flat space) leaves c1, c2, omega, alpha1, beta free -- extra Killing vectors appear",
             not any(cc.has(om) or cc.has(al1) or cc.has(b1) for cc in cond0 if cc != 0),
             f"remaining: {[cc for cc in cond0 if cc != 0]}")

print()
print("ALL CHECKS AND CONTROLS PASS" if ok else "SOME CHECK FAILED")
