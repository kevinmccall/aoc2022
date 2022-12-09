#!/usr/bin/python3
import sys
import argparse
import subprocess
import pathlib
from secret import SESSION

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read input")
    parser.add_argument("day", type=int)
    parser.add_argument("name", type=str)
    parser.add_argument("--year", type=int, default=2022)
    args = parser.parse_args()

    filename = "_".join(args.name.lower().split()) + ".py"
    dest = pathlib.Path(f"./{args.day}/")
    cmd = 'curl https://adventofcode.com/{}/day/{}/input --cookie "session={}"'.format(
        args.year, args.day, SESSION
    )
    output = subprocess.check_output(cmd, shell=True)
    with (dest / "input.txt").open("w", encoding="utf8") as writer:
        print(output.decode("utf-8"), end="", file=writer)
    file = dest / filename
    if not file.exists():
        file.touch()
        with file.open("w", encoding="utf8") as writer:
            writer.write(
                f"""data = None
p1 = 0
p2 = 0
with open("{args.day}/input.txt", "r", encoding="utf8") as reader:
    data = [x.strip() for x in reader.readlines()]

"""
            )
