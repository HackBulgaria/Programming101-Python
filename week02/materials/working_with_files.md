# Working with Files

Working with files in Python is easy. We are going to do a bunch of problems to illustrate the concept.

But first, some API:

## Reading files

Lets have two files:

* `read.py `- the python script
* `file.txt` - the file we want to read

```python
# read.py


filename = "file.txt"
file = open(filename, "r") # Here, "r" stands for open for reading

# file is a file object
# to get all the content:

content = file.read()
print(content)

# when we are done, we close the file
file.close()
```

If we want to iterate on every line, we can do the following:

```python
for line in file:
    print(line)
```

Each line ends up with a special character, called line break - `\n`.
In order to get each line as an element of a list, you can do the following:

```python
contents = file.read().split("\n")
```

## Writing files

Writing to files is just as easy:

```python
# write.py


filename = "file.txt"
file = open(filename, "w") # Here, "w" stands for open for writing

contents = ["Python is awesome.", "You should check it out!"]

# Here, we are joining each element with a new line
file.write("\n".join(contents))

# when we are done, we close the file
file.close()
```

Now, if we run the following program:

```
$ python3.4 write.py

```

and check what is in `file.txt`:

```
$ cat file.txt
Python is awesome.
You should check it out!
```

We will see our content!

__File arguments:__

When we run our Python scripts with `$ python3.4 script.py`, `script.py` is an argument to the Python program.

We can do the same thing with our Python scripts:

`$ python3.4 cat.py file.txt`

Here for example, `file.txt` is an argument to the `cat.py` script.

The simplest way to get your arguments is the following:

```python
# argv.py
import sys

for arg in sys.argv:
    print(arg)
```

Now, if we run the following command on the shell, we will see the output:

```
$ python3.4 argv.py hello.txt program.py script.py
argv.py
hello.txt
program.py
script.py
```

__IMPORTANT:__ In Python, the first argument is always the file name!

## Using with statement

In Python, there is a very helpful and powerful statement, [called `with`](http://effbot.org/zone/python-with-statement.htm)

You can use it to open files:

```python
with open("x.txt") as f:
    data = f.read()
    do something with data
```

This is a generalization for:

```python
try:
    f = open("x.txt")
    data = f.read()
    do something with data
finally:
    f.close()
```
