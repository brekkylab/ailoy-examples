# AGENTS.md

Runnable Ailoy agents, one folder per example. Read this before changing anything.

- `<name>/` holds one folder per language (`rust`, `python`, `node`), a `shared/` folder for what the three have in common (skills, prompts, model preparation scripts) and a `README.md`. The three languages do the same thing; a change to one moves the other two with it.
- The Rust example is registered in the root `Cargo.toml` as `[[example]]` and finds its folder from `CARGO_MANIFEST_DIR`, the top of this repository. Each `python/` is a uv project and each `node/` an npm project of its own.
- A new example gets a row in the table in `README.md`.
- Examples are self-contained: a reader runs one with the command in its `README.md` and nothing else set up beyond a model.
- Until the next Ailoy release the examples take Ailoy from `../ailoy` (Cargo `[patch.crates-io]`, uv `path` sources, npm `file:`); `scripts/pin_ailoy.py <version>` points them at a release.

## Before pushing

```bash
cargo fmt --check
cargo clippy --examples -- -D warnings
(cd <name>/python && uv sync --locked && uv run python -m py_compile main.py)
(cd <name>/node && npm ci && node --check main.mjs)
```

No CI runs these yet, so run them yourself. Running an example end to end needs a model and a virtx server, so say whether you ran one when you report a change.

## Comments and commits

- A comment states what the code beside it does now and why, in as few words as that takes.
- Commit titles are `type(scope): summary`, as in `fix(cad): give the agent room for long replies`.
