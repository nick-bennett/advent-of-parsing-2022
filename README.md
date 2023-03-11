# Advent of Parsing 2022

Browse the beatiful github pages [here](https://papibe.github.io/advent-of-parsing-2022/).

How to parse the input files for the
[Advent of Code 2022](https://adventofcode.com/2022) coding challenge.

## About

If can't parse the input file, you can't solve the problem.

This repository provides general guidelines to parse the input files in Python.
It starts with very simple files, almost trivial, but continue up to input files
that need a complex parsing strategy.

## Topics

- Basic of reading files on Python
- Eliminate new line character (“\n”)
- Divide input files (puzzle days) into categories:

## Caveat

* Usually I mean to parse as to get the data from a file into anPython object
  that is easy to either iterate, analyse or transform thus facilitating solving
  the problem.

* Different people may think different approaches to represent the data. For
  instance, a particular data can be store in a list of lists, or into a
  dictionary. There could be more parsing strategies that I’m not seeing.

* Also, I'm not considering getting the data into objects from custom classes.

[Next: How to read a file in Python](./docs/01.read_file.md)
