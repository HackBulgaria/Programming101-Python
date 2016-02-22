# Day 2

## chain

Implement a function that takes two iterables and returns another one that concatenate the two iterables. 


```python
def chain(iterable_one, iterable_two):
    pass
```

### Example

```python
>>> list(chain(range(0, 4), range(4, 8)))
[0, 1, 2, 3, 4, 5, 6, 7]
```

## compress

Implement a function that takes one iterables and one iterable mask. The mask is an collection that contains only ``True`` or ``False``

This function returns only this objects from the first collection that have ``True`` on their position in the mask.


```python
def compress(iterable, mask):
    pass
```

### Example

```python
>>> list(compress(["Ivo", "Rado", "Panda"], [False, False, True]))
["Panda"]
```

## cycle

Implement a function that takes an iterable and returns endless concatenation of it.


```python
def cycle(iterable):
    pass
```

```python
>>> endless = cycle(range(0,10))
for item in endless:
    print(item)
```

## Book Reader
You have some text files. They represent a book. Our book contains chapters. Each chapter starts with ``#`` at the beginning of the line. (Markdown book)

Our book is made of many files. Each file has its number ``001.txt, 002.txt, 003.txt``

Each file may contain one or more chapters.

[Link to the book](Book.zip)

Write a program that displays on the console each chapter. You can only move forwards using the ``space button``.

Try not to load the whole book in the memory. Use generator!

## Book Generator
Make a python program that generates books.

Your program should take the following parameters.

- Chapters count
- Chapter length range (in words)

The words should be with random length and random char. The format of the book should be the same as previous task. Try to place some new lines in the chapters at random positions. The whole book must be in one file.


Try to generate bigger book. Like 1-2G, and try to pass it to the previous program.

## Mouse Beep
Make a generator that returns the current position of your mouse pointer.

Then make a function that checks if your mouse is at the upper left corner of your screen. If it is your computer should make a beep sound.

Ask Google for "How to get mouse cords" and "Python beep sound" 
