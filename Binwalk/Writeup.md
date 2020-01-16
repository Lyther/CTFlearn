# Binwalk

Forensics Easy Rating: 4.45 / 5

[Link](https://ctflearn.com/challenge/108) address here.

## Description

Here is a file with another file hidden inside it. Can you extract it?

https://mega.nz/#!qbpUTYiK!-deNdQJxsQS8bTSMxeUOtpEclCI-zpK7tbJiKV0tXYY

## Solution

1. Install `binwalk` according to the hint from title.
2. Use command `binwalk -D 'png image:png' PurpleThing.png` to extract 2 .png files.
3. The flag is in the picture.

