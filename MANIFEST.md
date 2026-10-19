# Provenance of every file in this snapshot

This is a curated snapshot. Its files are copied from private research repositories, which will be made public later.
The SHA-256 of each file lets anyone check, at that point, that these copies are identical to the originals.

| file | source | sha256 |
|---|---|---|
| `_v5core.py` | sumit7194/trivium, `falsification/V5_rank3_vacuum_independent/code/verify.py` at commit ca52cff (byte-identical) | c4e1da47d5ea63f573741ded1c3ea0d8d05aebe93642d4c5a1b94d6085282dcc |
| `_v5e2core.py` | same repo, `.../code/verify_v5e2.py` at ca52cff; only its import line is renamed (`verify` → `_v5core`) | 83da79be9d13c1bd7aeb3e0bbf3e839a4a5ab1816fb2eda773637edcac047dc9 |
| `check_rank3.py` | written for this summary (2026-09-26); imports only the two files above | 44a7fc3d10a6a7bf22170551c83973e4cdee39ab22d82a03f5cda4f33c8c4de3 |
| `check_output.txt` | output of `python check_rank3.py`, regenerated 2026-10-16 | 2d290fe8dc9599f2f5fa42d366db867fa20ed75633365aa035135376ebb71407 |
| `SUMMARY.md` | the one-page summary; step 1 updated 2026-10-19 | 22a0ff44001272afd3160fd9193c2563b90ae26a877bd6c9513be8d3f0ea34a0 |
| `check_killing_direct.py` | written for this snapshot (2026-10-19), with AI assistance (Claude); imports only sympy | 926e403f578baf01eede74d670d44b439720da9628dbbad83b2e239006a4d654 |
| `check_killing_direct_output.txt` | output of `python check_killing_direct.py`, 2026-10-19 | 016746e9a44a6281339d2725d584678360836552713d4234254fa5af88a01471 |

Environment of both runs: Python 3.14.5, sympy 1.14.0, macOS 26.5 (arm64). Runtime about 4 s and 3 s. On 2026-10-19
`check_rank3.py` was rerun and its output matched `check_output.txt` byte for byte.
