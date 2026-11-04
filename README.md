# FLOW: Build AI that uses fewer tokens

A free field guide by **Unnati Tripathi** (@aiwithunnati, Maester Labs).

**Read it live: https://unnati-23.github.io/flow-token-minimising-guide/**

Decide which steps need a model, build a rules-first support-ticket router that calls a small local model only when it has to, and measure what you save.

- **[index.html](index.html)**: the guide as a web page ([live on GitHub Pages](https://unnati-23.github.io/flow-token-minimising-guide/))
- **[FLOW_Token_Minimising_Guide.pdf](FLOW_Token_Minimising_Guide.pdf)**: the original PDF
- **[code/triage.py](code/triage.py)**: the ticket router (rules first, then `qwen2.5:1.5b` via Ollama)
- **[code/test_triage.py](code/test_triage.py)**: four unit tests that mock the model, so they need no Ollama and no tokens

## Run it

```bash
cd code
python3 -m unittest -v
python3 triage.py 'billing ticket #1234'               # -> billing rule
python3 triage.py 'The app closes when I open settings' # model route, or "review fallback" if Ollama is off
```

For the model route, install [Ollama](https://ollama.com/download), start it, and run `ollama pull qwen2.5:1.5b`.

All sources are linked in the guide's Sources section.
