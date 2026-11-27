<p align="center">
  <a href="https://github.com/brekkylab/ailoy">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/brekkylab/ailoy/main/docs/public/img/ailoy-logo-signature-white.svg">
      <img alt="Ailoy" src="https://raw.githubusercontent.com/brekkylab/ailoy/main/docs/public/img/ailoy-logo-signature-black.svg" width="264" style="max-width: 40%;">
    </picture>
  </a>
</p>

<h3 align="center">Examples</h3>

<p align="center">
  <img src="https://cdn.simpleicons.org/rust/000000/ffffff" width="16"/> Rust&nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/python" width="16"/> Python&nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/nodedotjs" width="16"/> Node.js
</p>

<p align="center">
  <a href="https://ailoy.co/docs/"><img src="https://img.shields.io/badge/docs-eng-5a9cae" alt="Documentation"></a>
  <a href="https://discord.gg/27rx3EJy3P"><img src="https://img.shields.io/badge/Discord-7289DA?logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://x.com/brekkylab"><img src="https://img.shields.io/badge/X-000000?logo=x&logoColor=white" alt="X"></a>
</p>

<table align="center">
  <tr>
    <td align="center"><a href="./cad"><img src="https://raw.githubusercontent.com/brekkylab/ailoy/main/docs/images/ailoy-cad.gif" alt="cad"></a><br><sub>cad</sub></td>
    <td align="center"><a href="./sam3"><img src="https://raw.githubusercontent.com/brekkylab/ailoy/main/docs/images/ailoy-sam3-video.gif" alt="sam3"></a><br><sub>sam3</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="./gameplay"><img src="https://raw.githubusercontent.com/brekkylab/ailoy/main/docs/images/ailoy-openttd.gif" alt="gameplay"></a><br><sub>gameplay</sub></td>
    <td align="center"><a href="./laya"><img src="https://raw.githubusercontent.com/brekkylab/ailoy/main/docs/images/ailoy-laya.gif" alt="laya"></a><br><sub>laya</sub></td>
  </tr>
</table>

<p align="center"><sub>These show what each example does, not the screen you see when you run it.</sub></p>

Runnable agent examples built with [Ailoy](https://github.com/brekkylab/ailoy), each in Rust, Python and Node. Every agent works in its own [virtx](https://github.com/brekkylab/virtx) sandbox: the example builds the sandbox's image once, puts its skill and inputs on volumes, and copies the results back when the turn ends.

These are advanced examples, and tutorials are in the Ailoy repository.
[ailoy.co/use-cases](https://ailoy.co/use-cases/) shows these running.

| Example | What the agent does | <img src="https://cdn.simpleicons.org/rust/000000/ffffff" width="14"/> Rust | <img src="https://cdn.simpleicons.org/python" width="14"/> Python | <img src="https://cdn.simpleicons.org/nodedotjs" width="14"/> Node |
| --- | --- | --- | --- | --- |
| [cad](./cad) | Writes CadQuery, renders the model from four sides, looks at the renders and iterates | [rust](./cad/rust) | [python](./cad/python) | [node](./cad/node) |
| [offshore_leaks](./offshore_leaks) | Analyses the ICIJ Offshore Leaks database with SQL and Python that the agent writes itself | [rust](./offshore_leaks/rust) | [python](./offshore_leaks/python) | [node](./offshore_leaks/node) |
| [retail_bench](./retail_bench) | Runs a supermarket simulator, one day per turn | [rust](./retail_bench/rust) | [python](./retail_bench/python) | [node](./retail_bench/node) |
| [gameplay](./gameplay) | Plays OpenTTD (Transport Tycoon Deluxe) while you watch over VNC | [rust](./gameplay/rust) | [python](./gameplay/python) | [node](./gameplay/node) |
| [sam3](./sam3) | Segments images and videos with SAM3 on the guest GPU (ncnn + Vulkan) | [rust](./sam3/rust) | [python](./sam3/python) | [node](./sam3/node) |
| [tts](./tts) | Speaks text in a voice described in words, using Qwen3-TTS | [rust](./tts/rust) | [python](./tts/python) | [node](./tts/node) |
| [laya](./laya) | Answers typed decision questions with a local model on the GPU | [rust](./laya/rust) | [python](./laya/python) | [node](./laya/node) |
| [browser-use](./browser-use) | Waits for what you ask of it, in a window of your own browser | [rust](./browser-use/rust) | [python](./browser-use/python) | [node](./browser-use/node) |

> sam3, tts and laya run ML models and need a GPU: any GPU that supports Vulkan, or Metal on Macs.

## Before you run one

**This repository.** Each example takes Ailoy 0.3.3 and virtx 0.2.1 from crates.io, PyPI and npm, so cloning this repository is all the setup:

```sh
git clone https://github.com/brekkylab/ailoy-examples
```

Python needs 3.11 or later and [uv](https://docs.astral.sh/uv/), Node.js 22 or later.

**A model.** Claude, GPT and Gemini run through their CLIs by default, so an example needs no key if the CLI for its model is installed and logged in. `AILOY_MODEL` picks another model; [Model providers](https://ailoy.co/docs/guides/model-providers/) says how to set one up, with keys in the environment or a `.env` file here.

**virtx** is fetched into virtx's cache on the first run; nothing to install.

## Running

Each example lives in `<name>/`, with one folder per language and, where the three share files (skills, prompts, model preparation scripts), a `shared/` folder. Each example's README says what it needs beyond the above.

Rust, from the top of this repository:

```sh
cargo run --example <name>
```

Python:

```sh
cd <name>/python
uv run main.py
```

Node:

```sh
cd <name>/node
npm install
npm start
```

## License

[Apache-2.0](./LICENSE.md), as Ailoy. `retail_bench/shared/simulator` wraps code under the MIT license; see its `PROVENANCE.md`.
