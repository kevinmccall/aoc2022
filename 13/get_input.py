#!/usr/bin/python3
import argparse
import subprocess

SESSION = '53616c7465645f5f1b920acdca8730c4430f81a3e9fb42ff96170563b2f43c2abdcec40890760da92d02e87bb3109030'
parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('day', type=int)
parser.add_argument('--year', type=int, default=2020)
args = parser.parse_args()

cmd = 'curl https://adventofcode.com/{}/day/{}/input --cookie "session={}"'.format(
        args.year, args.day, SESSION)
output = subprocess.check_output(cmd, shell=True)
print(output.decode('utf-8'), end='')
