# Operating contract

Edit through the GitHub agent. Run tests, builds and benchmarks on GitHub-hosted Actions; never require a personal computer, terminal, GPU or local installation. See the [plan](google_quantum_ai_github_agent_plan.md) for phase gates and [audit](docs/competition_contract.md) for actual evidence.

- Push/PR checks use read-only Git access, no Kaggle secrets or data. Never use `pull_request_target` to execute PR code. Do not expose a credential to unreviewed code.
- Downloads require rules acceptance, protected main, manual dispatch and a restricted, approved environment. Keep tokens out of logs. Never commit competition assets/binaries, cache private data, or publish artifacts before checking permissions.
- Pin and record tool versions. Do not change official verifiers, metrics or reference data. Synthetic tests and estimates are not official results. Verify all three references before optimizing `invsqrt`; retain the best fully verified three-task fallback.
- Record source licenses, revisions, verifier settings and SHA-256 for exact outputs. Require separate human approval of the exact verified ZIP before any submission. Never invent scores or ranks.
