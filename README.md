# tiny-chess-01

A 4 KB chess engine in Python (stdlib only). 0x88 board, alpha-beta with
iterative deepening to a fixed 150,000-node budget, quiescence search,
transposition table, MVV-LVA ordering, formula piece-square tables.
Deterministic: no clock, no randomness — the same position always plays
the same move.

Run: `MAKEFUN_ENV_URL=<env-url> python3 main.py`

Built for the make.fun tiny-chess-01 bounty. Referral: 6t2bz3kn
