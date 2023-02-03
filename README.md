# Advent of Parsing 2022

How to parse the input files for all days

## About

- Basic of reading files on Python
- Eliminate new line character (“\n”)
- Divide days into categories
- Caveat:

    Usually I mean to parse as to get the data from a file into an Python object that is easy to either iterate, analyse or transform thus facilitating solving the problem.
    Different people may think different approaches to represent the data. For instance, a particular data can be store in a list of lists, or into a dictionary.
    There could be more parsing strategies that I’m not seeing.

## How to read a file in Python

```python
# Not recommended
file = open("./example.txt", "r")
data = file.read()
file.close()
```

```python
# Recommended
with open("./example.txt", "r") as file:
    data = file.read()
```

## Warning: be careful with new lines

```bash
$ cat example1.txt
This is line
```

```python
>> with open("./example1.txt", "r") as file:
...     data = file.read()
... 
>>> data
'This is a line\n'
```

## Most of the time use splitlines() is the best solution

```bash
$ cat example2.txt
This is line numero uno
This is line numero dos
This is line numero tres
```

```python
>>> with open("./example2.txt", "r") as file:
...     data = file.read()
... 
>>> data
'This is line numero uno\nThis is line numero dos\nThis is line numero tres\n'
>>> data.splitlines()
['This is line numero uno', 'This is line numero dos', 'This is line numero tres']
```

This even work on single line files:

```bash
$ cat example1.txt
This is line
```

```python
>> with open("./example1.txt", "r") as file:
...     data = file.read()
... 
>>> data
'This is a line\n'
>>> data.splitlines()
['this is a line']
```

## Days organized on parsing categories

| Category | Days |
| ----------- |  ----------- |
| One line of data | 6, 17 |
| Just lines of similar data | 3, 20, 25 |
| Similar lines, but each line needs extra parsing | 2, 9, 18, 20, 4, 14 |
| Blocks of data | 1, 13 |
| Multi dimensional arrays (matrices) | 8, 12, 23, 24 |
| Complex lines | 15, 16, 19 |
| Each line is different | 7, 10, 21, 11 |
| Special cases | 5, 22 |
