#!/usr/bin/env python3
from sys import argv

MAX_CHAR_SIZE = 100

with open(argv[1], "r") as read:
    text = read.read()

list_of_text_and_lengths = sorted(list(map(lambda line: (line, len(line)), text.splitlines() )), key=lambda index: index[1])

too_long = []

with open(argv[1] + ".edited", "w") as writer:
    for i in list_of_text_and_lengths:
        if i[1] <= MAX_CHAR_SIZE:
            writer.write(i[0] + '\n')
        else:
            too_long.append(i[0])
  
with open(argv[1] + ".long", "w") as writer:
    for i in too_long:
        writer.write(i + '\n')