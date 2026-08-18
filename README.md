# IL Spy (`il-spy`)

**Category:** reverse engineering · **Difficulty:** medium · **Points:** 275

A .NET assembly holds the key; decompile the IL to recover it.

## Run it

```bash
docker build -t sparflag/il-spy .
# `deca-ai start il-spy` (or the web UI) prints the docker run line with your
# SPARFLAG_SERVER + SPARFLAG_INSTANCE_TOKEN
```

## Recover the flag

The delivery blob is XOR-encrypted then base64-encoded. Discover the challenge key, then invert XOR+base64.

The plaintext flag is never written to disk or served — only the encoded delivery blob
is. When you have it:

```bash
deca-ai submit il-spy 'sparflag{...}'
```

## Hints

- Managed assemblies decompile cleanly.
- Read the key from the decompiled method, then invert XOR+base64.
