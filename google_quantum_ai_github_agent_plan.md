# GOOGLE QUANTUM AI — VERIFIABLE QUANTUM CIRCUIT COMPILATION
## Autonomous GitHub-Web-Agent Execution Plan (A–Z)

**Competition:** https://www.kaggle.com/competitions/google-verifiable-quantum-circuit-compilation  
**Host:** Google Quantum AI  
**Status as checked:** 2026-11-19  
**Final deadline:** 2027-01-20, 23:59 UTC  
**Runtime assumption:** **NO local PC, terminal, GPU or manually installed software.** All code changes happen through a web-based AI agent operating on **GitHub**; commands run only on **GitHub-hosted Actions runners**, with **Kaggle Cloud** as a remote fallback when permitted and useful.  
**Primary objective:** Obtain a fully verified, reproducible submission; then beat the reference cost with CPU-first algorithmic optimizations and build a credible research portfolio.  
**Instruction to the agent:** Read this entire document. Execute phase gates in order. Continue autonomously within available permissions, open an issue with exact blockers, and never invent verification results, competition scores, or submissions.

---

## 0. What the competition really is

This is **not** a supervised Kaggle prediction problem. Your deliverable is a compilation of **three specific structured quantum circuits** that preserves the required behavior within verification tolerances while reducing costly resources (qubits, Toffolis and T gates, plus benchmark-specific factors).

Google's open-source **kickmix** library (within Qualtran) describes circuits built from reversible classical logic, phases, and measurement-based uncomputation. This structure makes efficient classical testing possible. **You do not need a quantum computer, a GPU, or LLM fine-tuning** for a first viable attempt. AI coding agents are an intended use case for this event, as explained by Google; still, check the exact competition rules for permitted submissions, sharing, licenses, and prize eligibility.

### The three required tasks

| Task | Domain | What to optimize | Score cost for that task |
|---|---|---|---|
| `invsqrt` | Fusion energy | Reversible approximation to inverse square root for phase computation | `Q * (Toffoli + T/4)` |
| `dqi` | Combinatorial optimization | Reversible Reed–Solomon decoder used by Decoded Quantum Interferometry | `R(epsilon_plus) * Q^2 * T`, where `T` is the Toffoli count |
| `dfthcsos` | Quantum chemistry / FeMoCo | Factorization and parameter-loading ANGLE circuits | `lambda_eff * T * Q` |

Definitions and exact boundary conditions must be taken from the **official verifier and metric code**, not inferred from this summary. In particular, `dqi`'s failure upper confidence bound and `dfthcsos`'s chemistry formulas need exact implementation fidelity.

The competition score is the geometric mean of the three reference-to-candidate cost ratios:

```text
score = (ref_invsqrt / candidate_invsqrt
       * ref_dqi     / candidate_dqi
       * ref_dfthcsos / candidate_dfthcsos) ** (1/3)
```

**Implication:** A valid reference submission is your starting point. An improvement in one task improves the overall score, but **a single invalid or missing task blocks the submission**. Never ship an unverified improvement at the cost of invalidating the portfolio.

### Official calendar (all 23:59 UTC)

| Event | Date | Action |
|---|---|---|
| Competition started | 2026-10-22 | Already open |
| Mid-competition milestone award | **2026-11-20** | Only relevant with eligible public notebook and top public score; do not chase it at the expense of a valid baseline |
| Longest-leader eligibility cutoff | **2027-01-04** | Public notebook/dataset rules apply to this separate prize |
| Entry + team merger deadline | **2027-01-13** | Human owner must accept rules before this date |
| Final submission | **2027-01-20** | Produce and submit final verified ZIP |

There is a $150,000 total prize pool and Kaggle medals/points eligibility. Prize rules and sharing requirements may change; consult the official pages before taking action.

### Absolute rule for AI agents

1. An AI-generated optimization is **only a candidate** until the official task verifier passes it.
2. Never claim quantum equivalence based only on sampling if the competition requires stronger checks.
3. Never alter benchmark verifiers, reference data, or metric implementation to obtain a better score.
4. Never misrepresent a locally estimated metric as an official Kaggle score.
5. Do not assume permission for external models, private sharing, public forks, code reuse, or prize licensing; check and record exact rules.

---

## 1. Workflow contract: web agent + GitHub only

The agent must **not** request the user's laptop, local terminal, SSH setup, local Docker, local GPU, or installation of dependencies on a personal machine.

### Execution channels

- **Code editing:** GitHub web editor, Pull Requests, Issues, or authenticated GitHub API through the agent's GitHub integration.
- **CPU compute:** GitHub Actions (`ubuntu-latest`, pinned to a fixed image when reproducibility becomes important).
- **Benchmark/data download:** authenticated GitHub Actions job from Kaggle using **GitHub Actions Secrets** after the owner has accepted competition rules.
- **Heavy or Kaggle-specific evaluation:** optionally Kaggle Notebooks launched remotely by a supported Kaggle API/CLI workflow; these are also remote execution, never local.
- **Results:** GitHub Actions artifacts, Markdown experiment reports, CSV/JSON summaries, and GitHub Releases only when sharing is allowed.
- **Submission:** a verified ZIP uploaded to Kaggle via a separately gated/manual workflow or the website. Do not automatically submit on every commit.

### Human-only prerequisite actions

Ask the repository owner to do these once (the agent cannot assume authorization):

1. **Create a GitHub repository**, preferably private during active development unless rules/strategy call for publication.
2. **Join the Kaggle competition and accept its rules** on Kaggle using the owner's account.
3. **Create an appropriate Kaggle API credential** and add it as an encrypted repository secret, preferably `KAGGLE_API_TOKEN` (current Kaggle CLI supports it). If using legacy credentials instead, follow the official CLI documentation and use secret names such as `KAGGLE_USERNAME` and `KAGGLE_KEY`; never paste their values into chat, issues, logs, or Git.
4. **Enable GitHub Actions** for the repository and confirm the account's available Actions minutes and artifact storage.
5. Review permission settings before allowing any workflow that can submit or publish data.

A web agent with permission to edit code **still may not** have permission to add secrets or click the Kaggle acceptance checkbox. Record these as `HUMAN_ACTION_REQUIRED` and continue noncredentialed work.

### Security boundaries

- Workflow `permissions: contents: read` by default.
- **No secrets on untrusted pull_request events**, especially forks; never use `pull_request_target` to execute untrusted code with secrets.
- Credentialed download/submit workflows: **`workflow_dispatch` only**, owner-approved, on protected main branch.
- Use GitHub environment protection (e.g. `kaggle-submit`) with required reviewers before any final submission.
- Do not print API credentials, authenticated URLs, raw tokens, or secrets in logs.
- Do not send large competition datasets to third-party agent context unless allowed; let runners read them privately instead.
- Audit licenses and provenance for every reused reference circuit and external optimization.

---

## 2. Research and rules audit — REQUIRED FIRST

Agent action: open an Issue named `competition-contract-audit`, and add the following as linked checkboxes:

- [ ] Verify current schedule, deadlines, entry status, and number of daily submissions (if relevant).
- [ ] Read the full [official overview](https://www.kaggle.com/competitions/google-verifiable-quantum-circuit-compilation).
- [ ] Read the [official competition rules](https://www.kaggle.com/competitions/google-verifiable-quantum-circuit-compilation/rules).
- [ ] Read the [official data page](https://www.kaggle.com/competitions/google-verifiable-quantum-circuit-compilation/data).
- [ ] Read the metric implementation and each task's provided README.
- [ ] Inspect source tree of [Qualtran/kickmix](https://github.com/quantumlib/Qualtran/tree/main/kickmix) and [kickmix file format](https://github.com/quantumlib/Qualtran/blob/main/docs/kickmix/kickmix_format.md).
- [ ] Read [Google's official announcement](https://opensource.googleblog.com/2026/10/announcing-verifiable-quantum-circuit-compilation-competition-on-kaggle.html).
- [ ] Read [companion research paper](https://arxiv.org/abs/2610.23832).
- [ ] Identify exact verifier CLI calls, package versions, expected file names, signature arguments, resource limits, random seeds/salts, and acceptable approximations.
- [ ] Record licensing of any reused public notebook, code, or circuit; attribute its source.
- [ ] Confirm public/private notebook requirements for special awards and winning submission obligations.

Write a **source-linked** `docs/competition_contract.md` with only confirmed facts. If unavailable behind login, mark `UNVERIFIED` and ask the owner for authenticated access, not a guess.

### Must inspect starter examples

- Official starter notebook and/or linked starter kit on competition Code tab (for example, search for **Verifiable Circuit Compilation Starter**).
- Public reproductions: https://github.com/nasir26/vqcc-kaggle and https://github.com/Khanna-Aman/google-quantum-ai-kaggle **as examples, not as authority**.
- Never copy unverified competitor code into final submissions; keep a provenance manifest.

---

## 3. Repository structure — agent creates these files

```text
google-quantum-circuit-compiler/
├── README.md
├── AGENTS.md
├── LICENSE                    # only if appropriate for all original code
├── .gitignore
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   ├── benchmark.yml
│   │   └── submit.yml
│   └── ISSUE_TEMPLATE/
│       └── experiment.md
├── docs/
│   ├── competition_contract.md
│   ├── setup_remote.md
│   ├── invsqrt_notes.md
│   ├── dqi_notes.md
│   ├── dfthcsos_notes.md
│   ├── research_log.md
│   └── portfolio_report.md
├── manifests/
│   ├── dependencies.lock
│   ├── source_provenance.json
│   └── artifact_checksums.sha256
├── configs/
│   ├── baseline.yaml
│   ├── invsqrt_search.yaml
│   ├── dqi_search.yaml
│   └── dfthcsos_search.yaml
├── scripts/
│   ├── bootstrap.sh
│   ├── fetch_competition.sh
│   ├── smoke_test.sh
│   ├── run_verifier.sh
│   ├── evaluate.py
│   ├── compare_candidates.py
│   ├── validate_submission.py
│   ├── package_submission.py
│   └── write_report.py
├── src/
│   ├── common/
│   ├── invsqrt/
│   ├── dqi/
│   └── dfthcsos/
├── tests/
│   ├── test_score_formula.py
│   ├── test_submission_layout.py
│   ├── test_candidate_registry.py
│   └── test_reproducibility.py
├── experiments/
│   ├── ledger.csv
│   └── baselines.json
└── outputs/                    # gitignored: generated circuits and zips
```

### `.gitignore` essentials

```gitignore
.env
.kaggle/
*.token
*.key
__pycache__/
.pytest_cache/
.venv/
build/
outputs/
data/
downloads/
artifacts/
*.kmb
*.kmx
*.npz
*.zip
*.so
```

**Do not commit large reference files:** some baseline files are hundreds of MB, above GitHub's per-file Git storage size limit. GitHub Actions artifacts are more suitable, subject to storage quotas. Keep generators, pinning manifests, and SHA-256 checksums in Git instead.

---

## 4. CI/CD: concrete GitHub Actions design

The agent must create real workflows **and validate them with a test run**. If the exact official verifier CLI is not yet known, stop at the prerequisite check and make a clearly failing test/issue; do not invent a successful verification command.

### Workflow A — `.github/workflows/ci.yml`

Runs on push and PR without any Kaggle credentials or competition data:

```yaml
name: CI
on:
  push:
  pull_request:
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install small testing dependencies
        run: python -m pip install --upgrade pip pytest numpy pyyaml
      - name: Static and pure-Python tests
        run: python -m pytest -q tests/
```

The agent must implement meaningful initial tests that pass **without competition secrets**. Later, pin Action versions and Python packages for reproducibility.

### Workflow B — `.github/workflows/benchmark.yml`

Manually dispatched CPU job; fetches competition files only if credentials are available, otherwise can run unit-level mock/synthetic tests. **Only the credentialed workflow on trusted main may access Kaggle secrets.** Use a restricted environment or equivalent access-control policy.

```yaml
name: Benchmark candidate
on:
  workflow_dispatch:
    inputs:
      task:
        description: 'Benchmark task'
        type: choice
        options: [invsqrt, dqi, dfthcsos, all]
        required: true
      mode:
        description: 'smoke or full verification'
        type: choice
        options: [smoke, full]
        required: true
permissions:
  contents: read
concurrency:
  group: benchmark-${{ github.ref }}
  cancel-in-progress: false
jobs:
  benchmark:
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: kaggle-benchmark
    timeout-minutes: 330
    env:
      KAGGLE_API_TOKEN: ${{ secrets.KAGGLE_API_TOKEN }}
      TASK: ${{ inputs.task }}
      MODE: ${{ inputs.mode }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Inspect limits
        run: |
          df -h
          free -h
      - name: Bootstrap
        run: bash scripts/bootstrap.sh
      - name: Download official competition assets
        run: bash scripts/fetch_competition.sh
      - name: Verify candidate
        run: bash scripts/run_verifier.sh "$TASK" "$MODE"
      - name: Generate report
        if: always()
        run: python scripts/write_report.py
      - name: Upload small logs and metrics
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: benchmark-${{ github.run_id }}
          path: |
            outputs/reports/
            outputs/logs/
          retention-days: 14
```

Requirements:

- `bootstrap.sh` MUST install/build `kickmix` and task tooling from **pinned revisions**, not floating random branches.
- `fetch_competition.sh` MUST use the official Kaggle CLI and fail clearly if competition access is missing. A likely command is `kaggle competitions download -c google-verifiable-quantum-circuit-compilation -p downloads/`, but **verify exact CLI options for the installed version**, filenames and extracted paths before implementing download/extraction.
- `run_verifier.sh` MUST call actual task verifiers from the official package; fast smoke and full validation are separate gates.
- Any job approaching GitHub's **6-hour maximum** should break search into bounded chunks and upload a checkpoint, never rely on an unlimited background runner.
- Build caches may speed up later runs, but **do not cache secrets** or restricted data to an accessible public cache.
- Upload summary artifacts only in CI; large binary candidates can be captured in a separately permissioned artifact workflow if quotas permit.

### Workflow C — `.github/workflows/submit.yml`

Create this only **after the first full local-equivalent (GitHub runner) official verification passes**.

Security requirements:

1. Trigger: `workflow_dispatch` from protected `main` only.
2. Environment: `kaggle-submit` requiring human approval.
3. Input: immutable candidate ID or SHA-256 manifest, not an arbitrary shell command or URL.
4. Rebuild/download the exact candidate files using a recorded manifest; validate checksums.
5. `python scripts/validate_submission.py outputs/submission.zip` must pass.
6. Re-run final full official checks or verify a trusted immutable full-verification manifest.
7. Submit via **official Kaggle CLI**, e.g. `kaggle competitions submit -c google-verifiable-quantum-circuit-compilation -f outputs/submission.zip -m 'verified candidate <id>'`, after confirming the installed CLI's syntax and authentication.
8. Store submission ID, UTC timestamp, version, verification evidence, and subsequent leaderboard result in `experiments/ledger.csv` or a PR, **never claim a score until Kaggle reports it**.
9. If submission API is not available for this specific type of competition, deliver the ZIP as a private Actions artifact and document the final manual upload steps; never bypass platform requirements.

Do not implement automatic submission on `push` or `pull_request`.

---

## 5. Exact required submission ZIP layout

The official Kaggle competition requires a **single ZIP archive** with the following top-level structure:

```text
submission.zip
├── invsqrt.kmb          # OR invsqrt.kmx, not both unless rules explicitly permit
├── dqi.kmb              # OR dqi.kmx
└── dfthcsos/
    ├── angle_k_0.kmb     # OR .kmx
    ├── angle_k_1.kmb
    ├── ...
    ├── angle_k_{n-1}.kmb # contiguous indices with no gaps
    └── submission.npz
```

The `submission.npz` contains **exactly those mandatory data structures specified by the official contract**, including keys:

```text
U
W
H2_I
H1_I
Hsym_lower
tree_edges
```

The required dimensions, types, values and chemical invariants must come from `dfthcsos/SCORING_README.md` and the official verifier. An **ANGLE circuit wider than 128 qubits is rejected**. `dfthcsos` counts include the entire block-encoding system, not just the `angle_k_*` component.

Agent task: implement `validate_submission.py` which checks:

- [ ] ZIP can be opened; no path traversal, `../`, absolute paths, duplicates, or suspicious symlinks.
- [ ] Correct top-level files, exactly one supported extension per task.
- [ ] ANGLE circuit sequence begins at zero and is gap-free.
- [ ] `.npz` opens and mandatory keys exist; compare shapes and dtypes to official spec.
- [ ] All paths use correct case and archive-root location.
- [ ] Archive manifest SHA-256 and per-file hashes are recorded.
- [ ] Full verifiers and final official metric were run on the exact candidate contents.

**Do not** write a fake minimal `submission.npz` just to satisfy shape checks. The baseline data must be obtained from the official files or properly derived under the task contract.

---

## 6. Phase 1 — secure, reproduce baseline, submit once

### Goal

Produce a reproducible, **fully valid** baseline submission using only remotely executed code. The priority is the first verified baseline and first legitimate leaderboard entry, not immediate optimization.

### Agent checklist

- [ ] Repository created with files and CI green.
- [ ] Competition contract audit documented.
- [ ] Authentication available only in protected Actions environment.
- [ ] Official competition assets downloaded **inside GitHub runner**, not stored in Git.
- [ ] kickmix/Qualtran built or installed from pinned dependencies on Ubuntu Linux.
- [ ] Reference circuit for `invsqrt` passes the official checker.
- [ ] Reference circuit for `dqi` passes the official checker.
- [ ] Reference chemistry factorization and every ANGLE circuit pass official checks.
- [ ] Full submission ZIP validates and runs the official metric.
- [ ] Reference costs are recorded per task with environment, version, runtime and RAM usage.
- [ ] At least one Kaggle submission accepted; record resulting score.

If Kaggle scoring takes time (competition notes approximately 45 minutes), treat pending status as **PENDING**, not failure or success. Poll only within allowed API/rate limits or inspect the result later.

### Hard gate

**Never proceed to leaderboard-dependent optimization without a valid three-task baseline.** It is fine to investigate theory meanwhile, but don't compare speculative costs to Kaggle scores.

---

## 7. Phase 2 — `invsqrt` research (first optimization target)

### Why start here?

Its cost is comparatively transparent (`Q * (Toffoli + T/4)`), and its mathematical core permits familiar algorithm engineering: fixed-point arithmetic, approximate inverse square root, lookup tables, bitwidth decisions and register reuse. **Simpler is relative; this task is still quantum compilation research.**

### Suggested candidate families (in priority order)

1. **Baseline circuit audit:** identify subroutines, gate counts, qubit lifetime intervals, large arithmetic operations, and error budget.
2. **Range-aware fixed-point arithmetic:** remove unnecessary high/low bits only when rigorous error accounting and the official verifier support it.
3. **Approximation design:** try small lookup-based initial estimates followed by carefully bounded refinement; document numerical error vs circuit cost.
4. **Reversible arithmetic simplification:** propagate constants, simplify multiply/add chains, exploit known bit widths and finite domains.
5. **Ancilla/garbage management:** measure the qubit cost of scratch registers; look for safe uncomputation and reuse without modifying quantum semantics.
6. **Compiler-style local simplification:** search for proven gate identities and cancellation patterns; never assume classical rewrites are valid across phase operations.

### Experiments to implement

For each candidate `INV-XXXX`:

```text
id, git_commit, dependency_revision, algorithmic_change,
claimed_error_bound, verifier_status, verifier_salts,
qubits_Q, toffoli_count, t_gate_count,
ref_cost, candidate_cost, ratio_ref_over_new,
wall_seconds, peak_ram_mb, sha256, notes
```

**Promotion rule:** pass fast tests -> official full verifier -> replicate with independent salts/seeds if relevant -> compute cost -> archive candidate -> optionally update best-known portfolio.

### Do not do

- Truncate the circuit file or delete gates merely because it lowers reported counts.
- Optimize only a short sample set without validating the full domain required by the verifier.
- Break clean-ancilla or phase invariants.
- Swap in a simulator-specific approximation that is not valid under the competition's correctness contract.

---

## 8. Phase 3 — `dqi` research (second target)

This is a reversible **Reed–Solomon decoder** over a finite field. Start by reading the official DQI instructions carefully. It may involve significantly larger circuits, so avoid writing huge textual `.kmx` files into Git.

### Study topics

- Finite fields `GF(2^m)`: basis selection, multiplication, inversion, modulo polynomial arithmetic.
- Syndrome decoding, polynomial operations, and the reference decoder's structure.
- Reversible XOR networks, Toffoli-efficient multipliers, space/time tradeoffs.
- Uncomputation, garbage recycling, register allocation and constant-time control flow.
- Error bound and confidence interval treatment in the exact scoring metric.

### Candidate experiments

- Share common XOR subexpressions in finite-field arithmetic.
- Precompute or synthesize low-cost constant multipliers where allowed.
- Choose alternative multiplication circuits or basis transformations; verify end-to-end behavior.
- Reduce ancilla count if it doesn't increase the Toffoli count excessively; the cost uses `Q^2`, making space particularly important.
- Reduce Toffolis in one helper function at a time and produce unit-level reference tests before the full verifier.

**Critical:** The reported `dqi` error is not simply raw empirical failure rate. Reproduce the official upper-confidence-bound computation and `R(epsilon_plus)` exactly. A superficially small circuit with excessive error may be invalid or worse-scoring.

---

## 9. Phase 4 — `dfthcsos` research (third target)

This task combines **quantum chemistry factorization** and **parameter-loading/ANGLE circuits**. It has the highest integration risk. Early on, preserve the official chemistry baseline to keep a valid portfolio.

### Study topics

- Double factorization / tensor representations and the factorization payload (`U`, `W`, `H2_I`, `H1_I`, `Hsym_lower`).
- Givens rotations and `tree_edges` encoding.
- Table lookup circuits, multiplexed controls and reversible ANGLE synthesis.
- Tradeoffs among `lambda_eff`, Toffoli count and qubits.
- Exact requirements for the **128-qubit ANGLE width cap**.

### Candidate experiments

1. Profile chemistry baseline cost components and identify dominant lookups.
2. Try semantics-preserving ANGLE loader microoptimizations with minimal changes to `submission.npz`.
3. Deduplicate repeated lookup segments or synthesize compact lookup networks, but verify all parameter values.
4. Investigate factorization changes **only after** reproducing the reference chemistry evaluation.
5. Compare global `lambda_eff*T*Q`, not just lower Toffoli counts for one ANGLE circuit.

**Critical:** Treat chemistry arrays and Givens tree as a **coupled contract**. Changing an angle encoding without updating its associated data is likely invalid. The local/official verifier is mandatory.

---

## 10. Candidate registry, benchmarks and promotion

Create `experiments/ledger.csv` with columns:

```csv
candidate_id,task,parent_id,commit_sha,generated_utc,method,source_licenses,compiler_version,metric_version,verified,verification_mode,verification_salts,qubits,toffolis,t_gates,task_cost,reference_cost,improvement_ratio,wall_seconds,peak_ram_mb,archive_sha256,notes
```

### Candidate selection policy

- Each candidate has a deterministic build script and provenance manifest.
- Set a fixed random seed where applicable; record all other randomness (e.g. verifier salts).
- Compute task costs from official metrics, not invented ad hoc scores.
- A newly optimized circuit replaces a baseline **only if the full official verifier passes and cost strictly improves**.
- Keep a `best_valid.json` mapping each task to best verified candidate SHA-256.
- Assemble the final ZIP from the **best verified candidate per task**; chemistry may require selecting a coherent bundle, never mixing incompatible parts.
- All reported “overall score” numbers must be tagged `estimated_local` or `official_kaggle`.
- Save exact official leaderboard results and submission IDs after Kaggle returns them.

### Evidence hierarchy

1. **Authoritative:** Kaggle accepted submission and returned official leaderboard value.
2. **Strong:** Exact official verifier and metric code run on the candidate with reproducible hashes.
3. **Diagnostic:** Custom faster verifier validated against the official verifier.
4. **Weak:** Synthetic tests and hand calculations (useful for development but not final evidence).

---

## 11. Resource and cost constraints — CPU-first, hosted only

- Default to **GitHub-hosted Linux CPU** runners. No GPU training.
- Cap each job at <=330 minutes to leave time for artifact upload; GitHub-hosted execution has a 6-hour ceiling.
- Add job-level CPU/memory/disk preflight checks.
- Split optimization sweeps into deterministic chunks rather than enormous single jobs.
- Use `workflow_dispatch` inputs for task, candidate family, max trials, and seed.
- Enforce per-run cost/time limits and a maximum number of simultaneously active workflows.
- Pin dependency versions and check available storage before downloading extremely large official circuits.
- Do not store binary `.kmb` and `.kmx` in source Git history; use generated artifacts and hashes.
- GitHub Actions artifacts expire and consume storage. Maintain reproducible generation scripts and immutable manifests; for final files keep an approved durable backup where permitted.
- Optional Kaggle Notebook remote compute is acceptable **only if the user explicitly authorizes platform resource use and current rules permit it**.
- If compute quotas or storage block the workflow, stop expensive sweeps, document the blocker, and offer a smaller diagnostic alternative.

---

## 12. Research quality and CV portfolio

Working research title:

**Verified Agentic Optimization of Fault-Tolerant Quantum Circuit Resources Under CPU-Only Constraints**

### Main hypotheses (test, do not assume)

- **H1:** Structured arithmetic simplification reduces inverse-square-root circuit cost while remaining within verifier tolerances.
- **H2:** Shared finite-field subexpressions and ancilla reuse improve DQI cost beyond gate-count-only heuristics.
- **H3:** A verification-guided agent search is more compute-efficient than random candidate search under the same evaluation budget.
- **H4:** Multi-task optimization improves the geometric-mean score better than committing all compute to one task after diminishing returns.

### Required ablations

- Official reference vs each independent optimization.
- Q-only reduction vs Toffoli-only reduction vs combined optimization.
- Local smoke verification vs full official verification (correctness and runtime comparison).
- No-agent manually prescribed rewrite vs agent-generated rewrite vs guided search (if feasible).
- Fixed seed vs multiple seeds / verifier salts.
- Pipeline without candidate caching vs with deduplication and caching.

### Deliverables

- `docs/portfolio_report.md`: abstract, challenge, formal cost, method, verification strategy, experiments, ablation, limitations, reproducibility.
- `README.md`: links, run instructions for GitHub Actions, task costs, comparison table, verified leaderboard rank **only after confirmed**.
- Clearly named figures: cost breakdown, tradeoff frontier, verification funnel, CI pipeline, computational budget.
- `CITATION.cff` and source attributions if appropriate.
- CV bullet templates should stay as placeholders until actual results exist:

```text
Google Quantum AI — Verifiable Quantum Circuit Compilation (Kaggle, 2026–27)
Developed a GitHub Actions-based, CPU-only agentic circuit-optimization pipeline.
Achieved [VERIFIED SCORE] and [VERIFIED RANK], with [X]% cost improvement
on [TASK], validated using Google's official kickmix verifier.
```

Do not imply a medal, research publication, Google affiliation, or original algorithmic discovery without supporting evidence.

---

## 13. Timeline from 2026-11-19 to 2027-01-20

**Week 0 (Nov 19–22):** Audit rules; create repo; establish safe CI; set up authenticated cloud download; document all hidden/manual prerequisites. Ignore the Nov 20 milestone if not already qualified.  
**Week 1 (Nov 23–29):** Fetch assets on Actions; pin kickmix; reproduce task verifiers; generate full reference ZIP; make first valid submission.  
**Week 2 (Nov 30–Dec 6):** Profile `invsqrt`; implement arithmetic and resource accounting; ship 1–3 independently tested candidates.  
**Week 3 (Dec 7–13):** Focus `invsqrt` approximation and reversible register reuse; compare rigorous error vs cost.  
**Week 4 (Dec 14–20):** DQI bottleneck analysis; build finite-field helper-level tests and first verified alternatives.  
**Week 5 (Dec 21–27):** DQI rewrite sweeps and resource tradeoffs; start chemistry baseline cost profiling.  
**Week 6 (Dec 28–Jan 3):** Chemistry ANGLE-loader optimizations; baseline-safe portfolio assembly; review public-notebook requirements for any special prize.  
**Week 7 (Jan 4–10):** Best-of-three portfolio; robustness checks, provenance audit, fresh official re-verification; entry deadline preparation.  
**Week 8 (Jan 11–17):** Human confirms Kaggle entry before Jan 13; final experiments, reproducible build and technical report.  
**Final window (Jan 18–20):** Freeze source + artifacts, approve `submit` workflow, verify ZIP checksums, submit before **Jan 20, 23:59 UTC**, confirm acceptance and final result.

The week boundaries are guidelines, not reason to delay a valid earlier submission. Always maintain a verified fallback.

---

## 14. Agent operating loop (execute continuously, not blindly)

For each small improvement:

```text
1. READ contract + current best candidates + last failed experiment.
2. PROPOSE one concrete algorithmic change and an expected cost mechanism.
3. CREATE an Issue or PR with hypothesis and exact acceptance criteria.
4. IMPLEMENT in a new branch; include deterministic build and unit tests.
5. RUN safe CI using GitHub Actions; fix tests until it passes.
6. RUN credentialed full benchmark only after authorized main-branch merge.
7. VERIFY correctness with the official verifier.
8. MEASURE cost, CPU time, memory, source revision and artifact hash.
9. COMPARE against best verified candidate; promote only if improved.
10. DOCUMENT all results, including failures and invalid candidates.
11. REPEAT until compute quota, deadline or diminishing returns require switching tasks.
```

### Stop conditions

- Invalid/missing competition access: do not try circumvention; document human action needed.
- GitHub Actions secret unavailable: keep working on synthetic non-secret CI and documentation.
- Official verifier cannot be installed: inspect upstream docs/issues and add a specific blocker issue; do not pretend synthetic tests are official.
- Candidate crashes or exceeds RAM/disk/runtime: reduce scale or change representation; do not silently delete gates or mutate verifier.
- Verification fails: candidate is **REJECTED**, keep last verified candidate.
- Rules change: update contract and re-evaluate whether any approach/submission is legal.
- Deadline passed: stop claims of further official submissions and finalize a transparent portfolio.

---

## 15. First exact assignment for the web agent

**Copy the following paragraph into your GitHub-based web agent after giving it access to this document:**

> Operate **exclusively via GitHub**. You may edit the repository and trigger authorized GitHub Actions, but you may not access my local machine. First read `google_quantum_ai_github_agent_plan.md` in full. Create repository structure, `AGENTS.md`, a contract-audit issue, source-linked `docs/competition_contract.md`, safe CI, and the first minimal `bootstrap.sh`/`fetch_competition.sh` stubs. Verify actual official command syntax before implementing verifiers or submissions. Use no credentials on pull-request jobs. If credentials/rule acceptance are needed, open a clearly labeled `HUMAN_ACTION_REQUIRED` issue and continue non-secret tasks. Then reproduce all three reference circuits in hosted Actions, run official validation, produce a ZIP with hashes, and request human approval before the first Kaggle submission. After establishing the baseline, research `invsqrt` optimizations first, always preserving the best fully verified three-task fallback. Never fabricate scores or commit competition data/binaries.

### Acceptance criteria for the FIRST pull request

- [ ] Clear README showing what can run through GitHub Actions without local setup.
- [ ] `AGENTS.md` repeats the no-local, verification, and security contract.
- [ ] Main CI workflow has a real green check on GitHub.
- [ ] Competition contract document links to primary official sources.
- [ ] Repository paths and ignored files created.
- [ ] No API tokens, giant competition files or hard-coded passwords in Git.
- [ ] Clearly stated next-step blocker list for owner, if any.

### Acceptance criteria for a FINISHED competition attempt

- [ ] All three task components correctly packaged.
- [ ] Full official verification logged for the exact final artifact.
- [ ] Final ZIP identified by reproducible SHA-256.
- [ ] Kaggle submission accepted and official result recorded, or clearly documented why submission was impossible.
- [ ] At least one genuine, verified optimization attempt with measured before/after cost.
- [ ] Research report distinguishes validated results, hypotheses, and failures.
- [ ] Repository remains reproducible without a personal computer.

---

## 16. Source links (primary first)

1. Competition overview, metric, deadlines, ZIP layout: https://www.kaggle.com/competitions/google-verifiable-quantum-circuit-compilation
2. Official rules: https://www.kaggle.com/competitions/google-verifiable-quantum-circuit-compilation/rules
3. Official competition data: https://www.kaggle.com/competitions/google-verifiable-quantum-circuit-compilation/data
4. Google Open Source announcement (2026-10-21): https://opensource.googleblog.com/2026/10/announcing-verifiable-quantum-circuit-compilation-competition-on-kaggle.html
5. Google research companion paper: https://arxiv.org/abs/2610.23832
6. Official Qualtran repository: https://github.com/quantumlib/Qualtran
7. Kickmix format spec: https://github.com/quantumlib/Qualtran/blob/main/docs/kickmix/kickmix_format.md
8. Official Kaggle CLI commands: https://github.com/Kaggle/kaggle-cli/blob/main/docs/competitions.md
9. Official Kaggle CLI auth: https://github.com/Kaggle/kaggle-cli/blob/main/skills/references/auth.md
10. GitHub Actions limits: https://docs.github.com/en/actions/reference/limits
11. GitHub Actions workflow security: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
12. Community reproducibility example (not authority): https://github.com/nasir26/vqcc-kaggle

**Final instruction:** Start by making the safest verifiable progress. A GitHub Actions-based green CI and an honest baseline are more valuable than an unverified “optimized” circuit. Keep iterating until the final submission is verified or the deadline ends.
