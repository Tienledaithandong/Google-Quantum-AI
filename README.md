# Verifiable quantum circuit compilation

**Status:** repository safeguards only. No verified reference circuit, submission ZIP or Kaggle score yet.

## Run the first check — no local setup

Open a pull request or push to the working branch. In **Actions → CI → scaffold**, inspect the shell syntax checks and Python standard-library tests. They check Git exclusions, tracked file sizes, and refusal of unauthorized or not-yet-audited downloads. No Kaggle account or token is needed. Green means these safeguards passed, not that a circuit passed.

## Before the first benchmark

1. Owner: [prerequisites were acknowledged in #2](https://github.com/Tienledaithandong/Google-Quantum-AI/issues/2), but the live protection checks did not match. Follow [#4](https://github.com/Tienledaithandong/Google-Quantum-AI/issues/4) before enabling any credentialed job.
2. Agent: finish the [source-linked contract](docs/competition_contract.md) and [audit #1](https://github.com/Tienledaithandong/Google-Quantum-AI/issues/1). Both scripts under `scripts/` deliberately exit nonzero pending this work.
3. Only then implement the pinned bootstrap and protected manual benchmark. Reproduce `invsqrt`, `dqi` and `dfthcsos` on hosted Actions, run all official checks on the exact packaged contents, record hashes and request human approval for the first submission. Optimize `invsqrt` only after retaining the verified fallback.

See [agent safeguards](AGENTS.md) and [the execution plan](google_quantum_ai_github_agent_plan.md). `src/` and `configs/` reserve space for audited implementations; `experiments/` and `manifests/` track evidence, not binary artifacts.

**CLI contract check:** On a PR changing the CLI probe (or **Actions → CLI contract → Run workflow** after merge), a clean runner installs the pinned Kaggle client and inspects its help. This does not log in, list competition files, or confirm access.

## Optional laptop upload (already verified ZIP only)

`scripts/submit.py` uploads an existing entry; it does not build circuits or run the official verifier. Use Python 3.11+ from the repository root. Preview offline first:

```sh
python scripts/submit.py submission.zip
```

Before uploading, accept the competition rules, check your remaining quota, and obtain separate approval for the SHA-256 from official verification of the exact ZIP. A matching preview hash alone is not verification. Install the client in your active Python environment (`python -m pip install kaggle==2.2.5`), ensure `kaggle` is on PATH, and authenticate locally per the [Kaggle instructions](https://github.com/Kaggle/kaggle-cli/blob/main/docs/authentication.md). Never put credentials in this repository. Replace `APPROVED_DIGEST` below with the approved 64-character hash:

```sh
python scripts/submit.py submission.zip --approved-sha256 APPROVED_DIGEST --submit
```

Type `SUBMIT` only if ready. Check the competition’s Submissions tab for processing results before retrying an interrupted upload.
