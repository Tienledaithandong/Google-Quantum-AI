# Competition contract audit · 2026-11-19

[Audit issue #1](https://github.com/Tienledaithandong/Google-Quantum-AI/issues/1) tracks the evidence needed before implementing the baseline. The project plan is a checklist, not a verified specification.

## Confirmed from upstream GitHub documentation

- Qualtran has a [kickmix source distribution](https://github.com/quantumlib/Qualtran/tree/f559b12af459e7e97e6c6c382434431c03b903c9/kickmix). Its [text format specification](https://github.com/quantumlib/Qualtran/blob/f559b12af459e7e97e6c6c382434431c03b903c9/docs/kickmix/kickmix_format.md) describes v2 and a complementary binary format. This revision identifies the documentation inspected, **not** an approved verifier build.
- The [official CLI documentation](https://github.com/Kaggle/kaggle-cli/blob/ad776d4dddb30467523e64d245c795e4c7fbe394/docs/competitions.md) shows `kaggle competitions download <COMPETITION> -p <PATH>`; [authentication documentation](https://github.com/Kaggle/kaggle-cli/blob/ad776d4dddb30467523e64d245c795e4c7fbe394/skills/references/auth.md) supports `KAGGLE_API_TOKEN`. The separate CLI contract workflow checks installed help without enabling downloads.

## UNVERIFIED — requires official competition access/review

| Source | What to establish |
|---|---|
| [Overview](https://www.kaggle.com/competitions/google-verifiable-quantum-circuit-compilation) | Schedule, entry, evaluation and submission limits |
| [Rules](https://www.kaggle.com/competitions/google-verifiable-quantum-circuit-compilation/rules) | Acceptance, licensing, external tools, private processing, publication, award conditions |
| [Data and task READMEs](https://www.kaggle.com/competitions/google-verifiable-quantum-circuit-compilation/data) | File inventory, reference hashes, ZIP/NPZ schemas, exact metric and verifier versions/commands, signatures, limits, seeds, tolerances |
| [Official starter on Code tab](https://www.kaggle.com/competitions/google-verifiable-quantum-circuit-compilation/code) | Locate authoritative example and permitted reuse |
| [Google announcement](https://opensource.googleblog.com/2026/10/announcing-verifiable-quantum-circuit-compilation-competition-on-kaggle.html) and [paper](https://arxiv.org/abs/2610.23832) | Background only; neither replaces the rules or official metric |

The GitHub-only audit has not inspected authenticated assets. No task has passed official verification. After owner confirmation, record exact source/version and evidence per row before promoting any claim. The community READMEs from [nasir26](https://github.com/nasir26/vqcc-kaggle) and [Khanna-Aman](https://github.com/Khanna-Aman/google-quantum-ai-kaggle) were inspected for orientation only; no code, circuit or result was reused.

### Handoff after the owner checklist

Issues #1 and #2 were checked off, but no verifier invocation, asset manifest or runner evidence was attached. Owner acknowledgement of rules and quota is not a test of authenticated access. On 2026-11-19 GitHub reported `main.protected = false`, no active main rules and no visible benchmark environment; [follow-up #4](https://github.com/Tienledaithandong/Google-Quantum-AI/issues/4) blocks any secret use. Do not use a repository-level secret as a fallback.

The no-secret probe uses the [v2.2.5 CLI release](https://github.com/Kaggle/kaggle-cli/releases/tag/v2.2.5) and [upstream dependency pins](https://github.com/Kaggle/kaggle-cli/blob/5da4593737d65353ff35ce402ff2e918c2c780f3/requirements.lock). It runs help only. Once protections are confirmed, start with a reviewed manual inventory on main, not a full download: inspect the official task documentation privately on the runner, record only permitted metadata and hashes, then pin the matching verifier and build the references.
