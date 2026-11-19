# Verifiable quantum circuit compilation

**Status:** repository safeguards only. No verified reference circuit, submission ZIP or Kaggle score yet.

## Run the first check — no local setup

Open a pull request or push to the working branch. In **Actions → CI → scaffold**, inspect the shell syntax checks and Python standard-library tests. They check Git exclusions, tracked file sizes, and refusal of unauthorized or not-yet-audited downloads. No Kaggle account or token is needed. Green means these safeguards passed, not that a circuit passed.

## Before the first benchmark

1. Owner: complete [HUMAN_ACTION_REQUIRED #2](https://github.com/Tienledaithandong/Google-Quantum-AI/issues/2) (rules, public-repo sharing constraints, Actions quota and protected benchmark environment). Never paste credentials or competition assets into the issue.
2. Agent: finish the [source-linked contract](docs/competition_contract.md) and [audit #1](https://github.com/Tienledaithandong/Google-Quantum-AI/issues/1). Both scripts under `scripts/` deliberately exit nonzero pending this work.
3. Only then implement the pinned bootstrap and protected manual benchmark. Reproduce `invsqrt`, `dqi` and `dfthcsos` on hosted Actions, run all official checks on the exact packaged contents, record hashes and request human approval for the first submission. Optimize `invsqrt` only after retaining the verified fallback.

See [agent safeguards](AGENTS.md) and [the execution plan](google_quantum_ai_github_agent_plan.md). `src/` and `configs/` reserve space for audited implementations; `experiments/` and `manifests/` track evidence, not binary artifacts.
