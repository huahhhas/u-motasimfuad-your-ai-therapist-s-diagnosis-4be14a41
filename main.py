#!/usr/bin/env python3
# Entry for make.fun bounty u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41
"""Your AI Therapist's Diagnosis.

Deterministic entry: writes exactly one line to /output/entry.txt
and prints that same line, nothing else.
"""

import os

LINE = "Diagnosis: chronic overthinking, presenting as 3 a.m. doomscrolling, 47 open tabs, and asking a chatbot to diagnose the chatbot habit."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
