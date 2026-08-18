#!/usr/bin/env python3
"""IL Spy — real mini-challenge (il-spy)."""
import base64, hashlib, json, os, struct, sys, zlib, wave, io, math, random, re, textwrap
sys.path.insert(0, "/challenge/_shared")
from fetch_material import fetch_material

CHALLENGE_KEY = os.environ.get("CHALLENGE_KEY", 'msil-strings')


def main():
    mat = fetch_material()
    with open("/challenge/flag.enc", "w") as f:
        f.write(mat["delivery_blob"])
    key = CHALLENGE_KEY or "msil-key"
    il = f""".assembly app {{}}
.class public App {{
  .method public static void Main() {{
    ldstr "{key}"
    call void [mscorlib]System.Console::WriteLine(string)
    ret
  }}
}}
"""
    with open("/challenge/app.il", "w") as f:
        f.write(il)
    print("IL Spy: grep ldstr in app.il for key; XOR+base64 flag.enc.")


if __name__ == "__main__":
    main()
