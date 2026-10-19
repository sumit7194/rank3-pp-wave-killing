# A rank-3 Killing tensor on Filyukov's vacuum pp-wave

*One-page summary, for a reader's check. Everything below is reproduced by `check_rank3.py` and
`check_killing_direct.py` (sympy only, a few seconds each). It was produced with AI assistance. Updated 2026-10-19:
step 1 now rests on an explicit solution of the Killing equation, added after a reader questioned the jet-count bound.*

## The spacetime (Filyukov 2017, eq. 33)

In coordinates (t, s, ξ, η), with ρ² = ξ² + η² and a ≠ 0:

    ds² = −(4aξ/ρ²) dt² + 2 dt ds + 8ρ² (dξ² + dη²)

With w = (ξ + iη)², the transverse metric is 2|dw|², and −g_tt = 4a Re(w^{−1/2}) = (4a/√2)·√(r + x)/r, where
w = x + iy and r = |w|. This is the Eisenhart lift of the harmonic σ = 0 Smorodinsky–Winternitz potential. It is
the vacuum pp-wave of S. A. Filyukov, *Sci. Tech. Educ.* **1(5)** (2017) 13–20, eq. (33), which also gives one of
its quadratic integrals.

## The observation

With H = ½g^{ab}p_a p_b and K = H − p_t p_s, the two parabolic separation constants are

    Q1 = p_ξ²/16 + 2aξ p_s² − ξ² K
    Q2 = (p_ξ − p_η)²/32 + a(ξ − η) p_s² − ½(ξ − η)² K

Their Poisson bracket is a cubic integral:

    F = −4{Q1, Q2} = (η p_ξ − ξ p_η)(p_ξ² + p_η²)/(32ρ²) + (a p_s²/ρ²)[ξη p_ξ + ½(η² − ξ²) p_η]

**Claim.** F is a rank-3 Killing tensor that is **irreducible in the polynomial sense**: it is not a sum of
symmetrised products of lower-rank Killing tensors. The argument:

1. The Killing vectors are exactly ∂_t and ∂_s. `check_killing_direct.py` solves the Killing equation explicitly
   (part B), and shows that the original 2D system has no integral linear in momenta, time-dependent or not
   (part A). Independently, `check_rank3.py` bounds the Killing algebra by 2 with a second-order jet count at one
   point (at a = 3; t → λt, s → s/λ and ξ → −ξ relate all a ≠ 0). That count is only an upper bound; here it meets
   the two explicit Killing vectors. Flat space gives 10 by the same count, as a control.
2. Rank 3 can only split as 1 + 2 or 1 + 1 + 1, so every reducible rank-3 tensor has a Killing-vector factor.
   It therefore vanishes at p_t = p_s = 0.
3. F does not: its restriction there is (η p_ξ − ξ p_η)(p_ξ² + p_η²)/(32ρ²).

## What it is not

- **Not functionally new.** F² = 4[K(Q1² + Q2²) − a²Q1 p_s⁴], so F adds no new first integral. The same holds for
  the published ultrahyperbolic examples.
- **Not a regular spacetime.** There is a conical excess at ρ = 0, the profile grows like 1/ρ, and it is
  geodesically incomplete.
- **Nothing about rank 4, or about black-hole spacetimes.**

## Why it might interest the reader

Cariglia–Galajinsky 2015 (conclusion) and Fordy–Galajinsky 2019 (introduction) ask for Ricci-flat Lorentzian
spacetimes with irreducible higher-rank Killing tensors. Filyukov 2017's conclusion names a harmonic potential with
a third-order integral as the open problem. Read in the polynomial sense, an example was already in print, one
Poisson bracket away. Read as asking for a *functionally independent* cubic, the question remains open. A search of
three published classification lists found no candidate.

**The questions for the reader:** is this already known? And is the irreducibility argument (steps 1–3) sound?
