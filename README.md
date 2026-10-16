# A rank-3 Killing tensor on Filyukov's vacuum pp-wave

A small, self-contained check of one observation. The vacuum pp-wave of S. A. Filyukov (2017, eq. 33) carries a cubic
integral, the Poisson bracket of its two quadratic ones. That integral is irreducible in the polynomial sense: it is
not built from lower-rank Killing tensors.

- **`SUMMARY.md`:** the one-page statement, the argument, and what the claim is *not*.
- **`check_rank3.py`:** checks every step with sympy. Each check has a control that must fail when something is wrong.

```
pip install -r requirements.txt
python check_rank3.py        # about 4 seconds; expected last line: ALL CHECKS AND CONTROLS PASS
```

`MANIFEST.md` gives each file's provenance and checksum. The work was done with AI assistance (Claude) and has not
yet been reviewed by a professional physicist. Corrections are welcome.

Author: Sumit Pal (independent researcher).
