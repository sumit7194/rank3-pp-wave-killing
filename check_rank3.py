"""Check the claims about a rank-3 Killing tensor on a vacuum pp-wave (Filyukov 2017, eq. 33) -- sympy only.

    python check_rank3.py          (a few minutes)

Coordinates (t, s, xi, eta), rho^2 = xi^2 + eta^2, a != 0:
    ds^2 = -(4 a xi / rho^2) dt^2 + 2 dt ds + 8 rho^2 (dxi^2 + deta^2)
Checks, each with a control that must fail when something is wrong:
  1. Lorentzian signature; Ricci-flat.                 control: a non-harmonic profile is not Ricci-flat
  2. Q1, Q2 (quadratic) and F (cubic) Poisson-commute with H.   control: F with one sign flipped does not
  3. F = -4 {Q1, Q2}, and F^2 = 4[(H - p_t p_s)(Q1^2 + Q2^2) - a^2 Q1 p_s^4].
  4. F restricted to p_t = p_s = 0 is nonzero.
  5. The Killing algebra is exactly span{d_t, d_s}: an upper bound of 2 from a second-order jet count at one point
     (L_X Riem = 0 and L_X grad Riem = 0), plus the two explicit Killing vectors.   control: flat space gives 10
  => F is irreducible in the polynomial sense: every reducible rank-3 tensor has a Killing-vector factor, so it
     vanishes at p_t = p_s = 0, while F does not (claims 4 + 5).
  6. The profile is Filyukov's: in w = (xi + i eta)^2 the transverse metric is 2|dw|^2 and
     -g_tt = 4a Re(w^(-1/2)) = (4a/sqrt 2) sqrt(r + x)/r, with w = x + i y, r = |w|.
Not claimed: functional independence (F is functionally dependent on H, p_t, p_s, Q1, Q2 -- see claim 3).
"""
import sympy as sp
from _v5core import X, N, G, F, metric, christoffel, riemann_up, ricci, poisson, hamiltonian, killing_jet, \
    a, xi, eta, t, s, pt, ps, pxi, peta, rho2

def report(name, ok, detail=""):
    print(f"  {'PASS' if ok else 'FAIL'}  {name}{('   ' + detail) if detail else ''}"); return ok

ok = True
print("1. Signature and vacuum")
ev = [complex(v).real for v in G.subs({a: 3, xi: 2, eta: 1}).evalf().eigenvals(multiple=True)]
ok &= report("signature (1,3)", sum(v < 0 for v in ev) == 1)
ok &= report("Ricci-flat", ricci(riemann_up(christoffel(G))) == sp.zeros(4, 4))
ok &= report("control: non-harmonic profile is NOT Ricci-flat", ricci(riemann_up(christoffel(metric(-4*a*xi**2/rho2)))) != sp.zeros(4, 4))

print("2. Conserved quantities")
H = hamiltonian(G)
K = H - pt*ps
Q1 = pxi**2/16 + 2*a*xi*ps**2 - xi**2*K
Q2 = (pxi - peta)**2/32 + a*(xi - eta)*ps**2 - sp.Rational(1, 2)*(xi - eta)**2*K
for nm, Q in [("Q1", Q1), ("Q2", Q2), ("F", F)]:
    ok &= report(f"{{H, {nm}}} = 0", poisson(H, Q) == 0)
Fbad = (eta*pxi - xi*peta)*(pxi**2 + peta**2)/(32*rho2) - (a*ps**2/rho2)*(xi*eta*pxi + sp.Rational(1, 2)*(eta**2 - xi**2)*peta)
ok &= report("control: F with one sign flipped does NOT commute", poisson(H, Fbad) != 0)

print("3. Bracket origin and algebraic relation")
ok &= report("F = -4 {Q1, Q2}", sp.simplify(F + 4*poisson(Q1, Q2)) == 0)
ok &= report("F^2 = 4[(H - p_t p_s)(Q1^2 + Q2^2) - a^2 Q1 p_s^4]", sp.simplify(F**2 - 4*(K*(Q1**2 + Q2**2) - a**2*Q1*ps**4)) == 0)

print("4. Pure part")
pure = sp.factor(F.subs({pt: 0, ps: 0}))
ok &= report("F at p_t = p_s = 0 is nonzero", pure != 0, f"= {pure}")

print("5. Killing vectors (this step takes the longest)")
import importlib.util, sys
spec = importlib.util.spec_from_file_location("v5e2", __file__.replace("check_rank3.py", "_v5e2core.py"))
v5e2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(v5e2)
point = {a: 3, xi: 2, eta: 1, t: 0, s: 0}
k, M, Gm = v5e2.kernel_2nd(G, point)
ok &= report("upper bound from the second-order jet count = 2", k == 2, f"kernel dim = {k}")
pairs = [(i, j) for i in range(N) for j in range(i + 1, N)]
for idx, nm in [(0, "d_t"), (1, "d_s")]:
    Xup, nab = killing_jet(G, Gm, idx, point)
    vec = sp.Matrix(Xup + [nab[i, j] for (i, j) in pairs])
    ok &= report(f"{nm} is a Killing vector in the kernel", sp.simplify(nab + nab.T) == sp.zeros(4, 4) and sp.simplify(M*vec) == sp.zeros(M.rows, 1))
kflat, _, _ = v5e2.kernel_2nd(metric(sp.Integer(0)), {xi: 2, eta: 1, t: 0, s: 0})
ok &= report("control: flat space gives 10", kflat == 10, f"kernel dim = {kflat}")

print("6. Relation to Filyukov's potential")
w = (xi + sp.I*eta)**2
ok &= report("2|dw|^2 = 8 rho^2 (dxi^2 + deta^2)", sp.simplify(2*sp.Abs(sp.diff(w, xi))**2 - 8*rho2) == 0)
x_, y_ = sp.re(sp.expand(w)), sp.im(sp.expand(w)); r_ = sp.sqrt(x_**2 + y_**2)
for pv in [{xi: sp.Rational(3, 2), eta: sp.Rational(1, 3)}, {xi: sp.Rational(1, 5), eta: -2}]:
    lhs = (4*a*xi/rho2).subs(pv).subs(a, 1); rhs = (4/sp.sqrt(2)*sp.sqrt(r_ + x_)/r_).subs(pv)
    ok &= report(f"-g_tt = (4a/sqrt 2) sqrt(r+x)/r at xi,eta = {tuple(pv.values())}", abs(sp.N(lhs - rhs, 30)) < 1e-25)

print("\nALL CHECKS AND CONTROLS PASS" if ok else "\nSOMETHING FAILED -- see above")
