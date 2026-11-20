# Ailoy examples

Runnable agents built with [Ailoy](https://github.com/brekkylab/ailoy), each in Rust, Python and Node. Every agent works in its own [virtx](https://github.com/brekkylab/virtx) sandbox: the example builds the sandbox's image once, puts its skill and inputs on volumes, and copies the results back when the turn ends.

The smallest example, one turn with no tools and no sandbox, is [`hello`](https://github.com/brekkylab/ailoy/tree/main/examples/hello) in the Ailoy repository. [ailoy.co/examples](https://ailoy.co/examples/) shows these running.

| Example | What the agent does | Rust | Python | Node |
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

**Ailoy, beside this repository.** Until the next Ailoy release, the examples use Ailoy from a checkout next to this one, since they use API that Ailoy 0.3.2 does not have:

```sh
git clone https://github.com/brekkylab/ailoy
git clone https://github.com/brekkylab/ailoy-examples
```

Rust and Python build it on the first run. Node needs the addon built once: `cd ailoy/bindings/node && npm install && npm run build`. Once the release is out, `python3 scripts/pin_ailoy.py <version>` points every example at it and the checkout is no longer needed.

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
