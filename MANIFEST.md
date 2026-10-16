# Provenance of every file in this snapshot

This is a curated snapshot. Its files are copied from private research repositories, which will be made public later.
The SHA-256 of each file lets anyone check, at that point, that these copies are identical to the originals.

| file | source | sha256 |
|---|---|---|
| `_v5core.py` | sumit7194/trivium, `falsification/V5_rank3_vacuum_independent/code/verify.py` at commit ca52cff (byte-identical) | c4e1da47d5ea63f573741ded1c3ea0d8d05aebe93642d4c5a1b94d6085282dcc |
| `_v5e2core.py` | same repo, `.../code/verify_v5e2.py` at ca52cff; only its import line is renamed (`verify` → `_v5core`) | 83da79be9d13c1bd7aeb3e0bbf3e839a4a5ab1816fb2eda773637edcac047dc9 |
| `check_rank3.py` | written for this summary (2026-09-26); imports only the two files above | 44a7fc3d10a6a7bf22170551c83973e4cdee39ab22d82a03f5cda4f33c8c4de3 |
| `check_output.txt` | output of `python check_rank3.py`, regenerated 2026-10-16 | 2d290fe8dc9599f2f5fa42d366db867fa20ed75633365aa035135376ebb71407 |
| `SUMMARY.md` | the one-page summary | 4a55b4de648dba1b26668e412b00ac92305e9bcd0db2d2e59580baa664c36081 |

Environment of the regenerated run: Python 3.14.5, sympy 1.14.0, macOS 26.5 (arm64). Runtime about 4 s.
