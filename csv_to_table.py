#!/usr/bin/python3

from sys import stdin
from csv import reader
from simple_table import draw_table

data = list(reader(iter(stdin)))
print(draw_table(data[0], data[1:]))
