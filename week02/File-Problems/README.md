# Problems with files

## Implement the cat command - Print file contents

In Linux, there is a very useful command, called `cat`:

```
$ cat file.txt
This is some file
And cat is printing it's contents
```

Implement a Python script, called `cat.py` that takes one argument - a filename and prints the contents of that file to the console.

### Boilerplate

```python
# cat.py
import sys


def main():
    pass

if __name__ == '__main__':
    main()
```

### Examples

If we have `file.txt` in the same directory with `cat.py`, and `file.txt` is with the following text:

```
Python is an awesome language!
You should try it.
```

This is the result:
```
$ python3.4 cat.py file.txt
Python is an awesome language!
You should try it.
```

## Cat multiple files

Implement a Python script, called `cat2.py` that takes multiple arguments - file names and prints the contents of all files to the console, in the order of the arguments.

__The number of the files that are given as arguments is unknown.__

There should be a newline between every two files that are printed.

### Boilerplate

```python
# cat2.py
import sys


def main():
    pass

if __name__ == '__main__':
    main()
```

### Examples

If we have two files - `file1.txt` and `file2.txt` in the same directory with `cat2.py` and:

__file1.txt:__
```
Python is an awesome language!
You should try it.
```

__file2.txt:__
```
Also, you can use Python at a lot of different places!
```


This is the result:
```
$ python3.4 cat2.py file1.txt file2.txt
Python is an awesome language!
You should try it.

Also, you can use Python at a lot of different places!

## Sum integers from file

Implement a Python script, called `sum_numbers.py` that takes one argument - a `filename` which has integers, separated by `" "`.

The script should print the sum of all integers in that file.

### Examples

If we use the generated file from Problem 3:

```
$ python3.4 sum_numbers.py numbers.txt
47372
```
