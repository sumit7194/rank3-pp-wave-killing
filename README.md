# A rank-3 Killing tensor on Filyukov's vacuum pp-wave

A small, self-contained check of one observation. The vacuum pp-wave of S. A. Filyukov (2017, eq. 33) carries a cubic
integral, the Poisson bracket of its two quadratic ones. That integral is irreducible in the polynomial sense: it is
not built from lower-rank Killing tensors.

- **`SUMMARY.md`:** the one-page statement, the argument, and what the claim is *not*.
- **`check_rank3.py`:** checks every step with sympy. Each check has a control that must fail when something is wrong.
- **`check_killing_direct.py`** (added 2026-10-19): solves the Killing equation explicitly, and shows that the
  original 2D system has no integral linear in momenta. This gives step 1 an explicit derivation; the jet count in
  `check_rank3.py` stays as an independent upper bound.

```
pip install -r requirements.txt
python check_rank3.py             # about 4 seconds; expected last line: ALL CHECKS AND CONTROLS PASS
python check_killing_direct.py    # about 3 seconds; same expected last line
```

`MANIFEST.md` gives each file's provenance and checksum. The work was done with AI assistance (Claude). Corrections
are welcome.

## Acknowledgement

Thanks to Prof. Anton Galajinsky (Tomsk Polytechnic University) for reading the summary, and for asking for the
direct proofs that are now in `check_killing_direct.py`.

Author: Sumit Pal (independent researcher).
