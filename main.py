"""One Letter: Coffee or Tea — entry for make.fun.

Writes one letter to /output/entry.txt.
The letter A stands for coffee: the fuel of a whole night of bounty hunting.
The rules ask for exactly one letter, A for coffee or B for tea, and nothing else.
"""
import os

LINE = "A"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
