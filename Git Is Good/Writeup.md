# Git Is Good

Forensics Medium Rating: 4.13 / 5

[Link](https://ctflearn.com/challenge/104) address here.

## Description

The flag used to be there. But then I redacted it. Good Luck.

https://mega.nz/#!3CwDFZpJ!Jjr55hfJQJ5-jspnyrnVtqBkMHGJrd6Nn_QqM7iXEuc

## Solution

1. Analysis the `flag.txt`, found out the flag has already been modified.
2. Use `git log` to check the commits, find out 3 commits.
3. Use `git log -p -3` to show the last commit, get the flag.

