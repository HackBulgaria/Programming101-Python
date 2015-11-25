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
```

## Sum integers from file

Implement a Python script, called `sum_numbers.py` that takes one argument - a `filename` which has integers, separated by `" "`.

The script should print the sum of all integers in that file.

### Examples

If we use the generated file from Problem 3:

```
$ python3.4 sum_numbers.py numbers.txt
47372
```
## Implement an alternative to du -h command

In linux, if we want to know the size of a directory, we use the `du` command. For example:

```
$ du -hs /home/radorado/code
2,3G  /home/radorado/code
```

* `-h` flag is for "human readable" which means we get the size in gigabytes, not bytes.
* `-s` flag is for silent. We don't want to print every file that we go through.

In a file called `duhs.py`, implement the logic of `du -hs /some/path`, where `/some/path` is obtained as an argument to the file.

Example usage:

```
$ python3.4 duhs.py /home/slavyana/code
/home/slavyana/code size is: 2.3G
```

**THIS IS NOT THE SOLUTION WE WANT:**

```python
from subprocess import call
import sys

path = sys.argv[1]

call(["du", "-s", "-h", path])
```

### Hints

* Check the [`os`](https://docs.python.org/3.4/library/os.html) python module.
* Many of the methods raise errors. In order to deal with an error you can do the following things:

```python
try:
    os.something(path)
except FileNotFoundError as error:
    print(error)
```

When you `except` the error, it wont crash your program.
